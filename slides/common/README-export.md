# Exporting HTML Slides to PowerPoint

This guide provides multiple methods to export your HTML slides to PowerPoint format.

---

## Method 1: Node.js Script with PptxGenJS (Recommended)

### Prerequisites

Install Node.js dependencies (one-time setup):

```bash
cd /Users/akitamasaki/Documents/ridaifu/English/slides/common
npm install
```

This installs:
- **pptxgenjs** - PowerPoint generation library
- **puppeteer** - Headless Chrome for capturing slides

### Usage

```bash
# Navigate to the common directory
cd /Users/akitamasaki/Documents/ridaifu/English/slides/common

# Export slides
node export-to-pptx.js ../expressions-using-"that" expressions.pptx
node export-to-pptx.js ../inanimate-subject inanimate-subject.pptx

# Or use npm script
npm run export ../expressions-using-"that" expressions.pptx
```

### How it Works

1. Uses Puppeteer to open each slide in headless Chrome (1280×720, 2× scale)
2. Waits for fonts, icons, and content to load
3. Captures high-quality PNG screenshot of each slide
4. Uses PptxGenJS to create a proper PowerPoint file
5. Adds each screenshot as a full-slide image
6. Saves the PPTX file

### Pros
- ✅ High quality (2× pixel density)
- ✅ Fast and automated
- ✅ Native JavaScript (matches your slides)
- ✅ Proper PPTX format
- ✅ No temporary files
- ✅ Better error handling

### Cons
- ⚠️ Requires Node.js
- ⚠️ Static images (no animations)

---

## Method 2: Automated Python Script (Alternative)

### Prerequisites

Install required packages:

```bash
pip install python-pptx selenium pillow
```

Install Chrome browser and chromedriver:
- **macOS**: `brew install chromedriver`
- **Manual**: Download from https://chromedriver.chromium.org/

### Usage

```bash
# Navigate to the common directory
cd /Users/akitamasaki/Documents/ridaifu/English/slides/common

# Export slides
python export-to-pptx.py ../expressions-using-"that" expressions.pptx
python export-to-pptx.py ../inanimate-subject inanimate-subject.pptx
```

### How it Works

1. Opens each slide HTML file in headless Chrome (1280x720)
2. Captures a screenshot of each slide
3. Creates a PowerPoint with proper dimensions
4. Adds each screenshot as a full-size image per slide
5. Cleans up temporary files

### Pros
- ✅ Fully automated
- ✅ Maintains exact visual appearance
- ✅ Reusable for all slide sets
- ✅ Consistent quality

### Cons
- ⚠️ Requires Python dependencies
- ⚠️ Static images (no animations/interactivity)

---

## Method 2: Browser Print to PDF, then Convert

### Steps

1. **Open any slide** in Chrome/Firefox
2. **Press F** to enter presentation mode
3. **Press Ctrl/Cmd + P** to print
4. **Save as PDF** with these settings:
   - Layout: Landscape
   - Margins: None
   - Background graphics: Yes
5. **Navigate through slides** and repeat for each

Alternatively, use browser extensions:
- **GoFullPage** (Chrome) - Captures full page
- **Print Edit WE** (Firefox) - Better print control

6. **Convert PDF to PPTX**:
   - Use online converter: https://www.ilovepdf.com/pdf_to_powerpoint
   - Or Adobe Acrobat Pro
   - Or Smallpdf.com

### Pros
- ✅ No coding required
- ✅ Good quality
- ✅ Editable text (with good converters)

### Cons
- ⚠️ Manual process for each slide
- ⚠️ Quality depends on converter
- ⚠️ Two-step process (PDF → PPTX)

---

## Method 3: Screenshot + Manual PowerPoint

### Steps

1. **Open slides** in browser
2. **Press F** for fullscreen mode
3. **For each slide**:
   - Press `Cmd + Shift + 4` (macOS) or `Win + Shift + S` (Windows)
   - Capture the slide
   - Or use browser extension like Awesome Screenshot
4. **Create new PowerPoint**:
   - Set slide size: 10" × 5.625" (16:9 ratio)
   - Insert each screenshot as full-slide image
   - Arrange in order

### Tools to Help
- **macOS**: Screenshot (Cmd + Shift + 4)
- **Windows**: Snipping Tool or Snip & Sketch
- **Browser**: GoFullPage, FireShot

### Pros
- ✅ Complete control
- ✅ No dependencies
- ✅ Works anywhere

### Cons
- ⚠️ Very manual
- ⚠️ Time-consuming
- ⚠️ Human error prone

---

## Method 4: Online Conversion Services

Several online services can convert HTML to PowerPoint:

1. **CloudConvert** - https://cloudconvert.com/html-to-pptx
   - Upload HTML files
   - Includes CSS styling
   - Download PPTX

2. **Aspose** - https://products.aspose.app/slides/conversion/html-to-pptx
   - Good for single files
   - Free tier available

3. **ConvertAPI** - https://www.convertapi.com/html-to-pptx
   - API available
   - Batch processing

### Steps

1. **Zip your slide folder** (HTML + CSS + assets)
2. **Upload to service**
3. **Download PPTX**
4. **Review and adjust** as needed

### Pros
- ✅ No installation
- ✅ Fast for one-time use
- ✅ Sometimes preserves text

### Cons
- ⚠️ May not preserve exact styling
- ⚠️ Upload limits
- ⚠️ Privacy concerns with content
- ⚠️ May require payment for batch

---

## Method 5: Browser Extension

### Recommended Extensions

**Chrome:**
- **Full Page Screen Capture** - Captures entire page
- **GoFullPage** - Screenshot all slides
- **Awesome Screenshot** - Multiple slides at once

**Process:**
1. Install extension
2. Navigate to slide1.html
3. Use extension to capture
4. Navigate through all slides
5. Import screenshots to PowerPoint

---

## Comparison Table

| Method | Automation | Quality | Setup | Time | Best For |
|--------|-----------|---------|-------|------|----------|
| Python Script | ★★★★★ | ★★★★★ | Medium | Fast | Multiple slide sets |
| Print to PDF | ★★☆☆☆ | ★★★★☆ | Easy | Medium | One-time export |
| Manual Screenshots | ★☆☆☆☆ | ★★★★★ | Easy | Slow | Small sets |
| Online Services | ★★★☆☆ | ★★★☆☆ | Easy | Fast | Quick preview |
| Browser Extension | ★★☆☆☆ | ★★★★☆ | Easy | Medium | One-time export |

---

## Recommended Workflow

**For regular use:**
```bash
# One-time setup
pip install python-pptx selenium pillow
brew install chromedriver  # macOS

# Export anytime
cd slides/common
python export-to-pptx.py ../[your-slides]/ output.pptx
```

**For quick one-time export:**
1. Open slides in browser
2. Press F for fullscreen
3. Use browser's built-in screenshot (Cmd+Shift+4 or Win+Shift+S)
4. Insert into PowerPoint manually

**For sharing with colleagues:**
- Use Method 1 (Python script) for best quality
- Or Method 2 (PDF → PPTX) for text editability

---

## Tips for Best Results

1. **Before exporting:**
   - Test all slides in browser
   - Ensure icons load (Lucide CDN)
   - Check for any cutoff content

2. **PowerPoint setup:**
   - Slide size: 16:9 (10" × 5.625")
   - Or: 1280 × 720 pixels
   - Maintain aspect ratio

3. **After export:**
   - Review each slide
   - Add notes/speaker notes if needed
   - Test presentation mode

4. **For printing:**
   - Use PDF export instead
   - Better print quality
   - Smaller file size

---

## Troubleshooting

**Python script issues:**
- `ModuleNotFoundError`: Install missing packages
- `ChromeDriver not found`: Install chromedriver
- `Connection refused`: Check Chrome version matches driver

**Quality issues:**
- Increase screenshot resolution in script
- Use PNG instead of JPG for better quality
- Check viewport size matches slide dimensions

**File size too large:**
- Compress images before adding
- Use JPG instead of PNG for photos
- Optimize PNG files with tools like TinyPNG

