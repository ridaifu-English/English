import json
import argparse
import os

# Global dictionary to hold size definitions
SIZE_DEFINITIONS = {}

def get_pixel_value(value, size_type):
    """Translates a size token or integer into a pixel value string."""
    if isinstance(value, (int, float)):
        return f"{value}px"
    if isinstance(value, str):
        # Check for size token first
        if value in SIZE_DEFINITIONS.get(size_type, {}):
            pixel_val = SIZE_DEFINITIONS[size_type][value]
            # Handle cases where the value is a number or a string like "100%"
            return f"{pixel_val}px" if isinstance(pixel_val, (int, float)) else pixel_val
        # If not a token, return the string as is (e.g., "90%")
        return value
    return ""

def generate_html(config):
    """Generates the HTML content for the answer sheet."""
    global SIZE_DEFINITIONS
    SIZE_DEFINITIONS = config.get('size_definitions', {})

    # Safely get all configuration parts with .get(), providing empty defaults
    sheet_settings = config.get('sheet_settings', {})
    header_layout = config.get('header_layout', {})
    question_sections = config.get('question_sections', [])

    sheet_width = sheet_settings.get('width', '90%')
    sheet_height = sheet_settings.get('height', 'auto')
    sheet_title = sheet_settings.get('title', 'Answer Sheet')
    background_image = sheet_settings.get('background_image')

    # --- CSS Styles (Unchanged) ---
    cell_background_style = ""
    if background_image:
        cell_background_style = f"""
        .cell-content-box, .large-answer-box, .grid-table td {{
            background-image: url("{background_image}");
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .cell-content-box .label, .grid-table .label, .large-answer-box .label {{
             background-color: transparent;
             text-shadow: 0px 0px 3px rgba(255, 255, 255, 0.9), 0px 0px 3px rgba(255, 255, 255, 0.9);
             padding: 0 2px; 
             border-radius: 2px;
        }}
        """
    css = f"""
    <style>
        body{{font-family:'Helvetica Neue', Arial, 'Hiragino Kaku Gothic ProN', 'Meiryo', sans-serif;background-color:#e9e9e9;display:flex;justify-content:center;padding:40px 20px;margin:0;}}
        .sheet-container{{
            background-color:white;
            border:1px solid #ccc;
            padding:40px;
            box-shadow:0 4px 12px rgba(0,0,0,0.1);
            box-sizing:border-box;
            min-height: 1122px;
        }}
        .sheet-title{{text-align:center;font-size:28px;margin-top:0;margin-bottom:30px;font-weight:bold;}}
        .header{{display:flex;justify-content:space-between;align-items:center;margin-bottom:40px;gap:20px;}}
        .student-info{{display:flex;align-items:center;gap:10px;}}
        .info-field{{display:flex;align-items:center;}}
        .info-field .label{{border:1px solid black;padding:5px 10px;border-right:none;background-color:#f8f8f8;display:flex;align-items:center;justify-content:center;box-sizing:border-box;white-space:nowrap;}}
        .info-field .box{{border:1px solid black;box-sizing:border-box;}}
        .score-box{{border:2px solid black;box-sizing:border-box;flex-shrink:0;}}
        .question-section{{margin-bottom:15px;display:flex;gap:10px;align-items:flex-start;}}
        .section-identifier{{width:20px;flex-shrink:0;text-align:left;padding-top:8px;font-size:16px;font-weight:bold;}}
        .section-id{{font-weight:bold;}}
        .section-title{{color:#333; font-size: 15px; margin-top: 2px;}}
        .question-content{{flex-grow:1;}}
        .cell-content-box{{border:1px solid black;position:relative;box-sizing:border-box;display:inline-block;}}
        .cell-content-box .label {{position:absolute;top:-18px;left:4px;font-size:12px;color:#555;}}
        .large-answer-box .label {{position:absolute;top:4px;left:4px;font-size:12px;color:#555;}}
        .grid-table{{border-collapse:collapse;width:100%;}}
        .grid-table td {{border: 1px solid black; padding: 0; position: relative; box-sizing: border-box;}}
        .large-answer-box{{width:100%;border:1px solid black;box-sizing:border-box;position: relative;}}
        .large-answer-box + .large-answer-box {{ border-top: none; }}
        .flex-row-container{{display:flex;gap:0;margin-top:-1px;align-items:stretch;flex-wrap:wrap;}}
        .flex-row-container .cell-content-box {{margin-right: -1px; margin-bottom: -1px;}}

        {cell_background_style}

        @media print {{
            html, body {{
                height: 100%;
                background-color: white;
                margin: 0;
                padding: 0;
            }}
            .sheet-container {{
                box-shadow: none;
                border: none;
                width: 90% !important;
                height: 100% !important;
                min-height: initial;
                padding: 0;
            }}
            * {{
                -webkit-print-color-adjust: exact !important;
                color-adjust: exact !important;
            }}
            @page {{
                size: A4;
                margin: 10mm;
            }}
        }}
    </style>
    """
    
    # --- HTML Generation ---
    html_parts = [f"""
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Answer Sheet</title>{css}</head><body>
<div class="sheet-container" style="width: {sheet_width}; height: {sheet_height};">
<h1 class="sheet-title">{sheet_title}</h1>
    """]

    # Header Section (Now fully safe)
    header_html = '<div class="header"><div class="student-info">'
    for field in header_layout.get('fields', []): # <-- Safe lookup
        h = get_pixel_value(field.get('height', 'md'), 'height')
        w = get_pixel_value(field.get('width', 'md'), 'width')
        header_html += f'<div class="info-field"><div class="label" style="height: {h};">{field.get("label", "")}</div><div class="box" style="width: {w}; height: {h};"></div></div>'
    header_html += '</div>'
    
    score_box = header_layout.get('score_box', {}) # <-- Safe lookup
    h = get_pixel_value(score_box.get('height', 60), 'height')
    w = get_pixel_value(score_box.get('width', 120), 'width')
    header_html += f'<div class="score-box" style="width: {w}; height: {h};"></div></div>'
    html_parts.append(header_html)

    # Question Sections (Now fully safe)
    for section in question_sections:
        section_id = section.get("section_id", "")
        section_title = section.get("section_title")
        id_html = f'<div class="section-id">{section_id}</div>'
        title_html = f'<div class="section-title">{section_title}</div>' if section_title else ''
        identifier_html = f'<div class="section-identifier">{id_html}{title_html}</div>'

        content_html = '<div class="question-content">'
        layout_type = section.get('layout_type', 'unknown')

        if layout_type == 'grid_layout':
            cols = section.get('columns', 1)
            no_background = section.get('no_background', False)
            try:
                start_num = int(section.get('start_number', 1))
            except (TypeError, ValueError):
                start_num = 1

            end_num_raw = section.get('end_number')
            end_num = None
            if end_num_raw is not None:
                try:
                    end_num = int(end_num_raw)
                except (TypeError, ValueError):
                    end_num = None

            items_count = len(section.get('items', []))
            numbers_count = 0
            if end_num is not None:
                numbers_count = max(0, end_num - start_num + 1)

            total_cells = max(items_count, numbers_count)

            rows_override = section.get('rows')
            if isinstance(rows_override, int) and rows_override > 0:
                rows = rows_override
                total_cells = max(total_cells, rows * cols)
            else:
                rows_override = None
                if total_cells == 0:
                    total_cells = cols
                rows = (total_cells + cols - 1) // cols if total_cells > 0 else 0
                total_cells = rows * cols

            if end_num is None:
                numbers_count = total_cells
            else:
                numbers_count = min(numbers_count, total_cells)

            w = get_pixel_value(section.get('box_width', 'sm'), 'width')
            h = get_pixel_value(section.get('box_height', 'sm'), 'height')

            content_html += '<table class="grid-table"><tbody>'
            for r in range(rows):
                content_html += '<tr>'
                for c in range(cols):
                    cell_index = (r * cols) + c
                    if rows_override is None and cell_index >= total_cells:
                        break
                    label = ''
                    if cell_index < numbers_count:
                        label = str(start_num + cell_index)
                    cell_style = f"width:{w}; height:{h};"
                    if no_background:
                        cell_style += " background-image: none;"
                    content_html += f'<td style="{cell_style}"><span class="label">{label}</span></td>'
                content_html += '</tr>'
            content_html += '</tbody></table>'

        elif layout_type == 'flex_row_layout':
            no_background = section.get('no_background', False)
            content_html += '<div class="flex-row-wrapper">'
            items = section.get('items', [])
            # Check if items is a list of lists (multiple rows)
            if items and isinstance(items[0], list):
                for row_items in items:
                    content_html += '<div class="flex-row-container" style="margin-top: 25px;">'
                    for item in row_items:
                        w = get_pixel_value(item.get('width', 'md'), 'width')
                        h = get_pixel_value(item.get('height', 'sm'), 'height')
                        lbl = item.get('label', '')
                        cell_style = f"width:{w}; height:{h};"
                        if no_background:
                            cell_style += " background-image: none;"
                        content_html += f'<div class="cell-content-box" style="{cell_style}"><span class="label">{lbl}</span></div>'
                    content_html += '</div>'
            else: # Treat as a single row that can wrap
                content_html += '<div class="flex-row-container" style="margin-top: 25px;">'
                for item in items:
                    w = get_pixel_value(item.get('width', 'md'), 'width')
                    h = get_pixel_value(item.get('height', 'sm'), 'height')
                    lbl = item.get('label', '')
                    cell_style = f"width:{w}; height:{h};"
                    if no_background:
                        cell_style += " background-image: none;"
                    content_html += f'<div class="cell-content-box" style="{cell_style}"><span class="label">{lbl}</span></div>'
                content_html += '</div>'
            content_html += '</div>'

        elif layout_type == 'large_box_layout':
            no_background = section.get('no_background', False)
            for item in section.get('items', []):
                h = get_pixel_value(item.get('height', 'lg'), 'height')
                lbl = item.get('label', '')
                style = f"height:{h};"
                if no_background:
                    style += " background-image: none;"
                content_html += f'<div class="large-answer-box" style="{style}"><span class="label">{lbl}</span></div>'
        
        elif layout_type == 'single_column_layout':
            content_html += '<div>'
            start_num = section.get('start_number', 1)
            for i, item in enumerate(section.get('items', [])):
                h = get_pixel_value(item.get('height', 'sm'), 'height')
                w = get_pixel_value(item.get('width', 'full'), 'width')
                lbl = start_num + i
                style = f"width:{w}; height:{h}; display:block;"
                if i > 0:
                    style += " border-top: none;"
                content_html += f'<div class="cell-content-box" style="{style}"><span class="label">{lbl}</span></div>'
            content_html += '</div>'

        content_html += '</div>'
        html_parts.append(f'<div class="question-section">{identifier_html}{content_html}</div>')

    html_parts.append("</div></body></html>")
    return "".join(html_parts)

def main():
    """Parses command-line arguments, reads config, and generates the HTML."""
    parser = argparse.ArgumentParser(description="Generate an HTML answer sheet from a JSON configuration file.")
    parser.add_argument(
        '-c', '--config',
        type=str,
        required=True,
        help="Path to the input JSON configuration file."
    )
    args = parser.parse_args()
    
    json_path = args.config
    base_name = os.path.splitext(os.path.basename(json_path))[0]
    html_path = f"{base_name}_answersheet.html"
    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"Error: Configuration file not found at '{json_path}'")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{json_path}'. Check for syntax errors.")
        return

    html_content = generate_html(config)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Successfully generated '{html_path}' from '{json_path}'.")

if __name__ == '__main__':
    main()