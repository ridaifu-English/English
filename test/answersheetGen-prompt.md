### Purpose
Generate a print-friendly answer sheet JSON for `answersheet-generator.py` from a questions-only document. Output valid JSON only.

### Hard rules
- Output must be valid JSON. No comments or Markdown in the output.
- Do not include `section_title` keys anywhere.
- Only use supported keys:
  - Root: `size_definitions`, `sheet_settings`, `header_layout`, `question_sections`
  - Section: `section_id`, `layout_type`, `items`, and if applicable `columns`, `box_width`, `box_height`, `start_number`, `rows`, `no_background`
- Use these size tokens:
  - `height`: `sm=35`, `md=40`, `lg=100`, `xl=150`
  - `width`: `sm="5%"`, `md=150`, `lg="100%"`, `full="100%"`
- Header must include 3 fields and a score box:
  - `Class` (80×sm), `No.` (80×sm), `Name` (200×sm), and `score_box` (100×60)

### Layout selection guide
- Short many items with numbering → `grid_layout`
  - Set `columns` (2–4), `box_width`, `box_height`, `start_number`, and create `items` as an array with the desired count (use `{}` elements). Rows are calculated automatically by the generator.
- Few short blanks on a line → `flex_row_layout`
  - Use `items` as an array of objects for a single wrapping row, or an array of arrays for explicit rows. Each item requires `label`, `width`, `height`.
- Multi-row grouped subparts (e.g., A/B/C then D/E/F) → `flex_row_layout` with nested arrays for rows.
- Long free-response (paragraphs/essays) → `large_box_layout`
  - Each item uses `{ "label": string, "height": token|number }`. Add `no_background: true` when lines should not overlay a background image.

### Sizing heuristics
- Single word/phrase: `height: "sm"`, `width: 20–50%`
- Short sentence: `height: "md"`, `width: 50–100%`
- Paragraph: `large_box_layout` with `height: "xl"`

### Labeling
- Keep labels short and aligned to the document numbering/letters (e.g., `1)`, `A`, `3B (2)`).
- Do not include descriptions inside labels.

### Inputs provided
- Document title for `sheet_settings.title`.
- Optional background image path.
- The full questions text (no answers/guidelines).

### Output schema example (minimal)
{
  "size_definitions": {
    "height": { "sm": 35, "md": 40, "lg": 100, "xl": 150 },
    "width": { "sm": "5%", "md": 150, "lg": "100%", "full": "100%" }
  },
  "sheet_settings": { "title": "TITLE", "width": "90%", "height": "auto", "background_image": "test/marksheet-base.png" },
  "header_layout": {
    "fields": [
      { "label": "Class", "width": 80, "height": "sm" },
      { "label": "No.", "width": 80, "height": "sm" },
      { "label": "Name", "width": 200, "height": "sm" }
    ],
    "score_box": { "width": 120, "height": 60 }
  },
  "question_sections": [
    {
      "section_id": "1)",
      "layout_type": "grid_layout",
      "columns": 3,
      "box_width": "md",
      "box_height": "sm",
      "start_number": 1,
      "items": [{}, {}, {}]
    },
    {
      "section_id": "2)",
      "layout_type": "flex_row_layout",
      "items": [
        [
          { "label": "A", "width": "50%", "height": "sm" },
          { "label": "B", "width": "50%", "height": "sm" }
        ]
      ]
    },
    {
      "section_id": "",
      "layout_type": "large_box_layout",
      "no_background": true,
      "items": [
        { "label": "Essay", "height": "xl" }
      ]
    }
  ]
}

### Quality checks before returning JSON
- Parses as JSON (no trailing commas). Keys spelled exactly as specified.
- No `section_title` keys.
- Label counts and numbering match the document.
- Width/height choices reflect expected writing length.

### Now do this
1) Read the provided questions-only document text.
2) Decide the layout type, width, and height for each section/subsection per the rules.
3) Return only the final JSON described above.


