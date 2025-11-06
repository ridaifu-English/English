# Slide Generation Prompt Template

Use this prompt template to generate new slide presentations based on reference materials.

---

## Inanimate-Subject Structure Analysis

The inanimate-subject slides follow this proven structure:

### Slide Breakdown

**Slide 1: Title Slide** (`slide1-styles.css`)
```html
Structure:
- Diagonal gradient background (clip-path polygon)
- Large title (64px) with text-shadow
- Subtitle (32px)
- Goals container (white card with shadow)
  - Goals title with icon
  - 3-4 bullet points with icons
- Character badge (circular, bottom-right corner)

Colors:
- Background: #f0f8ff → #4a7cbc gradient
- Title/subtitle: white
- Goals container: white with shadow
- Character badge: #ffb74d (orange)
```

**Slide 2: Overview/Definition** (`slide2-styles.css`)
```html
Structure:
- Standard header bar (#4a7cbc)
- Content divided into sections
  - Section title with icon + text
  - Section content (definitions, examples)
- Numbered examples with highlight spans

Layout Pattern:
<div class="section">
  <div class="section-title">
    <i data-lucide="icon-name"></i>
    <p>Title:</p>
  </div>
  <div class="section-content">
    <!-- Content here -->
  </div>
</div>
```

**Slides 3-8: Main Content** (`verb-slides.css` or `pattern-slides.css`)
```html
Structure:
- Standard header with concept name
- Pattern box (light blue background, left border)
  - Pattern title
  - Pattern text with color-coded elements
  - Optional: Pattern meaning/note
- Examples section
  - Example 1 (gray box)
    - English sentence (color-coded)
    - Japanese translation
  - Example 2 (if applicable)

Color Coding:
- S (Subject): #e91e63 (pink/red)
- V (Verb): #4caf50 (green)
- O (Object): #ff9800 (orange)
- Pattern box: #e3f2fd background, #2196f3 left border
```

**Slide 9: Practice/Exercises** (`slide9-styles.css`)
```html
Structure:
- Standard header with icon
- Practice items (5-6 exercises)
  - Question (Japanese)
  - Answer (English) - can be hidden/revealed

Layout:
.practice-item {
  - .practice-question (with .number span)
  - .practice-answer
}
```

**Slide 10: Special/Comparison** (inline CSS for unique layouts)
```html
Structure:
- Two-column comparison layout
- Left column: Regular usage (blue theme)
- Right column: Target concept (green theme)
- Arrow between columns
- Bottom note with key takeaway

Elements:
- Badges ("普通の文章" vs "無生物主語")
- Column headers with icons
- Sentence examples
- Nuance explanations
- Bottom tip box (#fff3e0 background)
```

### CSS File Organization

1. **styles.css** (Base styles - always included)
   - Reset styles
   - Body centering (1280x720)
   - .slide container
   - .header (blue bar)
   - .content (flex, center)
   - .pattern-box (light blue with left border)
   - .examples container
   - SVO color classes (.s, .v, .o)
   - .example blocks

2. **slide1-styles.css** (Title slide only)
   - Gradient background with clip-path
   - Title/subtitle centering
   - Goals container card
   - Character badge positioning

3. **slide2-styles.css** (Overview/intro)
   - Section layout
   - Section title with icons
   - Section content styling

4. **verb-slides.css or pattern-slides.css** (Content slides)
   - Minimal overrides for specific layouts
   - Additional pattern box variations

5. **slide9-styles.css** (Practice/exercises)
   - Practice item layout
   - Number badges
   - Question/answer styling

### Design Patterns

**Pattern Box Template:**
```html
<div class="pattern-box">
  <p class="pattern-title">Pattern:</p>
  <p class="pattern-text">
    <span class="s">S (description)</span> + 
    <span class="v">verb</span> + 
    <span class="o">O (description)</span> + complement
  </p>
  <p class="pattern-meaning">Japanese explanation</p>
</div>
```

**Example Block Template:**
```html
<div class="examples">
  <div class="example">
    <p class="example-english">
      <span class="s">Subject</span> 
      <span class="v">verb</span> 
      <span class="o">object</span> complement.
    </p>
    <p class="example-japanese">→ Japanese translation</p>
  </div>
</div>
```

**Section Template:**
```html
<div class="section">
  <div class="section-title">
    <i data-lucide="book-open"></i>
    <p>Section Name:</p>
  </div>
  <div class="section-content">
    <ul>
      <li><p>Content with <span class="highlight">emphasis</span></p></li>
    </ul>
  </div>
</div>
```

**Category Box Template (for grouping related items):**
```html
<div class="category-box">
  <div class="category-header">
    <span class="category-number">1</span>
    <span class="category-title">Category Name</span>
  </div>
  <div class="category-content">
    <p class="noun-list">Item1, Item2, Item3</p>
    <div class="category-example">
      <p class="example-english-small">Example sentence</p>
      <p class="example-japanese-small">日本語訳</p>
    </div>
  </div>
</div>
```

**Comparison Grid Template (side-by-side comparison):**
```html
<div class="comparison-grid">
  <div class="comparison-column">
    <div class="comparison-header appositive">Type A</div>
    <div class="comparison-point">
      <p class="point-label">Label:</p>
      <p class="point-text">Description</p>
    </div>
    <div class="example-compact">
      <p class="example-english-small">Example</p>
    </div>
  </div>
  <div class="comparison-column">
    <div class="comparison-header relative">Type B</div>
    <div class="comparison-point">
      <p class="point-label">Label:</p>
      <p class="point-text">Description</p>
    </div>
    <div class="example-compact">
      <p class="example-english-small">Example</p>
    </div>
  </div>
</div>
```

**Warning/Tip Box Template:**
```html
<div class="warning-box">
  <p class="warning-text">⚠️ <strong>Important:</strong> Note content</p>
</div>

<div class="tip-box">
  <p class="tip-title">💡 Tip:</p>
  <p class="tip-text">Helpful information</p>
</div>
```

### Color Palette Reference

**Primary Colors:**
- Header Blue: `#4a7cbc`
- Subject (S): `#e91e63` (pink/red)
- Verb (V): `#4caf50` (green)
- Object (O): `#ff9800` (orange)

**Background Colors:**
- Pattern Box: `#e3f2fd` with `#2196f3` left border
- Example Box: `#f5f5f5`
- Practice Box: `#f8f9fa`
- Warning Box: `#fff3e0` with `#ff9800` left border
- Tip Box: `linear-gradient(135deg, #e3f2fd 0%, #fff3e0 100%)` with `#2196f3` left border
- Category Header: `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`

**Text Colors:**
- Main Text: `#333`
- Secondary Text: `#666`
- Tertiary Text: `#999`

### Typography Scale

- Title (Slide 1): 64px, bold, white
- Header: 48px, bold, white
- Pattern Title: 28px, bold, #1565c0
- Pattern Text: 32px, medium
- Example English: 28px, medium
- Example Japanese: 22px, regular, #666
- Body Text: 20-24px

---

## Standard Prompt

```
Create an interactive HTML slide presentation teaching [TOPIC].

Reference Material:
- Use @[PATH_TO_REFERENCE_IMAGE_OR_DOCUMENT] as the content reference
- Follow the inanimate-subject structure detailed above

Requirements:

1. **Slide Structure** (Follow inanimate-subject pattern):
   - Slide 1: Title slide
     * Diagonal gradient background
     * Main title (64px) + subtitle
     * Goals container with 3-4 bullet points (with icons)
     * Character badge (circular, bottom-right)
   
   - Slide 2: Overview/Definition
     * Standard blue header
     * 2-3 sections with icons
     * Definition + simple examples
   
   - Slides 3-N: Main Content (one concept per slide)
     * Standard blue header
     * Pattern box (light blue with left border)
     * Pattern formula with color-coded elements
     * 2 example blocks with translations
   
   - Slide N+1: Practice (if applicable)
     * 5-6 practice exercises
     * Question (Japanese) → Answer (English)
   
   - Final Slide: Summary or Comparison
     * Either grid summary or side-by-side comparison

2. **File Organization**:
   - Create in: /slides/[TOPIC_NAME]/
   - HTML: slide1.html, slide2.html, etc.
   - CSS folder structure:
     ```
     css/
     ├── styles.css (base: .slide, .header, .pattern-box, .examples, SVO colors)
     ├── slide1-styles.css (gradient, goals-container, character badge)
     ├── slide2-styles.css (sections layout)
     ├── [content]-slides.css (main content slides 3-N)
     └── slide[final]-styles.css (practice/summary)
     ```
   - Assets: assets/ folder
   - Script: Use ../common/presentation.js

3. **CSS Implementation**:
   
   **styles.css (Base - always include):**
   - Body: 1280x720, centered, #1a1a1a background
   - .slide: 1280x720, white, flex column
   - .header: #4a7cbc, 20px padding, white text (height: ~88px)
   - .title: 48px, bold
   - .content: flex, center, 40px 80px padding (MAX available height: ~540px)
   - .pattern-box: #e3f2fd bg, #2196f3 left border, 25px padding (reduce to 15px if tight)
   - .examples: flex column, 25px gap (reduce to 20px if tight)
   - .example: #f5f5f5, rounded, 25px padding (reduce to 15px if tight)
   - Color classes: .s (#e91e63), .v (#4caf50), .o (#ff9800)
   - **Important**: If total content height > 540px, reduce padding or split slide
   
   **slide1-styles.css:**
   - Gradient background with clip-path: polygon(0 0, 100% 0, 100% 60%, 0% 80%)
   - .title: 64px, white, text-shadow
   - .goals-container: white card, shadow, 30px padding
   - .character: absolute, right 40px, bottom 40px, 180px circle, #ffb74d
   
   **slide2-styles.css:**
   - .section: margin-bottom 40px
   - .section-title: flex with icon, 32px, #4a7cbc
   - .section-content: 44px left padding
   
   **[content]-slides.css:**
   - Minimal overrides as needed
   - Pattern-specific adjustments
   - Extended styles for complex topics:
   
   ```css
   /* Category boxes for grouping items */
   .category-box {
     background-color: #ffffff;
     border-radius: 10px;
     overflow: hidden;
     box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
   }
   
   .category-header {
     background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
     padding: 12px 20px;
     display: flex;
     align-items: center;
     gap: 12px;
   }
   
   .category-number {
     background-color: white;
     color: #667eea;
     font-size: 20px;
     font-weight: 700;
     width: 32px;
     height: 32px;
     border-radius: 50%;
   }
   
   /* Comparison grids for side-by-side comparison */
   .comparison-grid {
     display: grid;
     grid-template-columns: 1fr 1fr;
     gap: 20px;
   }
   
   .comparison-column {
     background-color: #f5f5f5;
     border-radius: 10px;
     padding: 15px;
   }
   
   .comparison-header {
     font-size: 22px;
     font-weight: 700;
     color: white;
     padding: 12px;
     border-radius: 6px;
     text-align: center;
   }
   
   /* Warning and tip boxes */
   .warning-box {
     background-color: #fff3e0;
     border-left: 6px solid #ff9800;
     padding: 15px 20px;
     border-radius: 6px;
   }
   
   .tip-box {
     background: linear-gradient(135deg, #e3f2fd 0%, #fff3e0 100%);
     border-left: 6px solid #2196f3;
     padding: 20px;
     border-radius: 8px;
   }
   ```

4. **HTML Templates to Use**:
   
   **Pattern Box:**
   ```html
   <div class="pattern-box">
     <p class="pattern-title">Pattern:</p>
     <p class="pattern-text">
       <span class="s">S</span> + <span class="v">verb</span> + <span class="o">O</span>
     </p>
     <p class="pattern-meaning">Meaning in Japanese</p>
   </div>
   ```
   
   **Example:**
   ```html
   <div class="example">
     <p class="example-english">
       <span class="s">Subject</span> <span class="v">verb</span> <span class="o">object</span>.
     </p>
     <p class="example-japanese">→ Japanese translation</p>
   </div>
   ```
   
   **Section (Slide 2):**
   ```html
   <div class="section">
     <div class="section-title">
       <i data-lucide="icon-name"></i>
       <p>Title:</p>
     </div>
     <div class="section-content">
       <ul><li><p>Content</p></li></ul>
     </div>
   </div>
   ```

5. **Color Usage**:
   - Headers: #4a7cbc
   - S (Subject/emphasized element): #e91e63
   - V (Verb/key action): #4caf50
   - O (Object/secondary element): #ff9800
   - Pattern boxes: #e3f2fd background, #2196f3 border
   - Examples: #f5f5f5 background
   - Tips/notes: #fff3e0 background, #ff9800 border

6. **Typography**:
   - Font: Noto Sans JP (400, 500, 700)
   - Slide 1 title: 64px bold
   - Headers: 48px bold
   - Pattern text: 32px medium
   - Examples: 28px (English), 22px (Japanese, #666)
   - Body: 20-24px

7. **Icons**:
   - Use Lucide icons: <i data-lucide="icon-name"></i>
   - Common icons: target, book-open, zap, focus, pencil, lightbulb, check-circle
   - Script loads automatically via presentation.js

8. **Technical Details**:
   - All slides: <script src="../common/presentation.js"></script>
   - CSS links: <link rel="stylesheet" href="css/[name].css" />
   - **CRITICAL**: Slide dimensions are 1280x720px (16:9 aspect ratio)
   - **CRITICAL**: Content area is ~540px max height (after header and padding)
   - **MUST TEST** in presentation mode (F key) - no scrolling allowed
   - If content doesn't fit → reduce padding/fonts OR split into multiple slides
   - Test keyboard navigation (←→ keys, F for fullscreen)
   - **Height calculation**: Header (88px) + Top padding (40px) + Content (MAX 540px) + Bottom padding (40px) + Safety (12px) = 720px

9. **Additional Files**:
   - index.html: Landing page with overview and start button
   - Do NOT create README.md unless specifically requested

Follow the inanimate-subject structure breakdown above for specific implementation details.
```

---

## Example Usage

### For Grammar Topic:
```
Create an interactive HTML slide presentation teaching "Relative Clauses".

Reference Material:
- Use @relative-clauses-handout.png as the content reference

Requirements:
[Use standard requirements above]
```

### For Vocabulary Topic:
```
Create an interactive HTML slide presentation teaching "Business English Vocabulary".

Reference Material:
- Use @business-vocab-list.pdf as the content reference

Requirements:
[Use standard requirements above]

Additional: Include 5-7 example sentences per vocabulary item.
```

### For Complex Grammar with Comparisons:
```
Create an interactive HTML slide presentation teaching "Expressions Using 'that'".

Reference Material:
- Use web reference: https://englishosaru-officialsite.co.jp/englishosarublog/appositive-that/

Requirements:
[Use standard requirements above]

Special considerations:
- For cleft sentences: Show both normal and emphatic versions side-by-side
- For appositive "that": Split into 3 slides
  * Slide 8: Basic concept (appositive that = equals relationship)
  * Slide 9: Noun categories (thought/emotion, information/facts, statements/proposals)
  * Slide 10: Comparison with relative pronoun "that" (use comparison grid)
- Use category boxes for grouping related nouns
- Use comparison grid for distinguishing similar constructions
- Add tip boxes for practical identification methods

Remember: All slides must be sequentially numbered (slide8.html, slide9.html, slide10.html)
NOT (slide8.html, slide8-2.html, slide8-3.html)
```

---

## Post-Generation Checklist

After slides are generated, verify:
- [ ] **All slide files use sequential numbering** (slide1.html, slide2.html, slide3.html...)
- [ ] **No hyphenated or alphabetic slide names** (NO slide8-2.html, slide8a.html, etc.)
- [ ] All slides properly reference ../common/presentation.js
- [ ] All CSS files are in the css/ folder
- [ ] All slides properly link to CSS: href="css/[filename].css"
- [ ] **🚨 CRITICAL: Test EVERY slide in presentation mode (F key)**
  - [ ] NO vertical scrollbar on any slide
  - [ ] ALL content visible without scrolling
  - [ ] If any slide is cut off → SPLIT IT immediately
- [ ] Content fits within 720px height limit (including padding)
- [ ] Keyboard navigation works (←→ keys)
- [ ] Presentation mode scaling works correctly
- [ ] All icons load properly (Lucide CDN)
- [ ] Japanese text displays correctly (Noto Sans JP)
- [ ] index.html provides clear overview
- [ ] Complex topics are split across multiple sequential slides if needed

---

## Notes

- The common/presentation.js automatically counts slides, so no need to specify total count
- Keep content concise - each slide should focus on one concept
- Use visual hierarchy: larger fonts for key points, smaller for explanations
- Always include Japanese translations for English learning materials
- Test slides in browser before finalizing

### Educational Principles

**For students learning new content:**
- **Less is more**: 1 slide with focused content > 1 slide crammed with information
- **Cognitive load**: Students can only process 3-5 new items at once
- **Split generously**: If in doubt, split into more slides rather than fewer
- **Examples matter**: 2-3 quality examples per concept is ideal
- **Visual breathing room**: White space helps comprehension and reduces anxiety
- **Progressive disclosure**: Build complexity gradually across multiple slides

**When to split slides:**
1. More than 3 main points or categories
2. Content requires scrolling in presentation mode
3. Font sizes need to be reduced below readable sizes (< 16px)
4. Slide feels "busy" or overwhelming
5. Students are learning the concept for the first time

## ⚠️ Critical Naming Rules

### File Naming Convention
**MUST USE SEQUENTIAL NUMBERING ONLY:**
- ✅ Correct: `slide1.html`, `slide2.html`, `slide3.html`, `slide4.html`, etc.
- ❌ Wrong: `slide8-2.html`, `slide8-3.html`, `slide8a.html`, `slide8b.html`

**Why:** The `presentation.js` navigation logic uses `slide${currentSlide + 1}.html` to move to the next slide. Non-sequential naming (like `slide8-2.html`) will break navigation.

### Handling Complex Topics

When a topic requires extensive content that won't fit on a single slide:

1. **Split into multiple sequential slides:**
   ```
   slide8.html  - Pattern 6: 同格のthat（基本）
   slide9.html  - Pattern 6-2: 同格のthatを使える名詞
   slide10.html - Pattern 6-3: 同格のthat vs 関係代名詞のthat
   ```

2. **Use subtitles to indicate continuation:**
   - Main topic: "Pattern 6: 同格のthat（基本）"
   - Continuation: "Pattern 6-2: 同格のthatを使える名詞"
   - Continuation: "Pattern 6-3: 同格のthat vs 関係代名詞のthat"

3. **Never use non-sequential file names** even if they seem logical for organization

### Content Organization Strategies

**For Grammar Comparisons:**
- Show both normal sentence and emphasized/special construction
- Example structure:
  ```html
  <div class="example">
    <p class="example-label">平常文（Normal sentence）:</p>
    <p class="example-english">I met your sister at the store.</p>
  </div>
  <div class="example">
    <p class="example-label">強調構文（Cleft sentence）:</p>
    <p class="example-english">It was your sister that I met at the store.</p>
  </div>
  ```

**For Complex Topics (e.g., Appositive "that"):**
- Slide 1: Basic concept and definition
- Slide 2: Categories and usage patterns
- Slide 3: Comparison with similar constructions

**Content Density Guidelines:**
- If a slide feels cramped or requires small fonts (< 16px), split it
- Each slide should be readable in presentation mode without scrolling
- Aim for 2-3 examples maximum per slide

### ⚠️ Presentation Mode Display Requirements

**Critical Rule: All content MUST fit within 1280x720px (16:9 aspect ratio)**

**Slide Height Budget (720px total):**
```
- Header: 88px (fixed)
- Content area: ~580px (after padding)
- Bottom margin: ~52px

Breakdown:
  Header (fixed):     88px
  Top padding:        40px
  Content:           ~540px (MAX - must fit here)
  Bottom padding:     40px
  Safety margin:      12px
  ────────────────────────
  Total:             720px
```

**When Content Exceeds Height Limit:**

1. **Split into multiple slides immediately**
   - 3 category boxes → Split into 2 slides (2 boxes + 1 box)
   - Long comparison → Simplify or split
   - Multiple examples → 2-3 examples max per slide

2. **Reduce element sizes:**
   ```css
   /* Adjust these if needed */
   .pattern-box { padding: 15px 20px; }  /* was 20px 25px */
   .category-header { padding: 10px 15px; }  /* was 12px 20px */
   .category-content { padding: 15px; }  /* was 20px */
   .example { padding: 15px; }  /* was 20px or 25px */
   .comparison-column { padding: 12px; }  /* was 15px */
   ```

3. **Reduce font sizes (as last resort):**
   ```css
   .pattern-text { font-size: 28px; }  /* was 32px */
   .example-english { font-size: 24px; }  /* was 28px */
   .example-english-small { font-size: 17px; }  /* was 19px */
   ```

**Testing Checklist:**
- [ ] Press F key to enter presentation mode
- [ ] Navigate to each slide
- [ ] Verify NO vertical scrollbar appears
- [ ] Verify all content is visible without scrolling
- [ ] If content is cut off → SPLIT THE SLIDE

**Common Violations:**
- ❌ 3+ category boxes on one slide
- ❌ Large comparison grid + examples + tip box
- ❌ More than 3 examples on one slide
- ❌ Total content height > 540px

**Recommended Patterns:**

**For Category Slides:**
```
Option A: 2 categories + warning box = OK
Option B: 3 categories (no other elements) = MAYBE (test carefully)
Option C: 3 categories + warning box = TOO MUCH (split into 2 slides)
```

**For Comparison Slides:**
```
Option A: Comparison grid + 1 tip box = OK
Option B: Comparison grid + 2 examples + tip box = TOO MUCH
```

**Split Strategy Example:**

**BAD - Too much content:**
```
slide9.html:  Category 1 + Category 2 + Category 3 + warning box
❌ Content exceeds 720px height, requires scrolling
```

**BETTER - Split into 2 slides:**
```
slide9.html:  Category 1 + Category 2 + warning box
slide10.html: Category 3 + additional examples + warning box
slide11.html: Comparison grid + tip box
```

**BEST - Educational approach (1 category per slide):**
```
slide9.html:  Category 1 (思考・感情) + 2 examples
slide10.html: Category 2 (情報・事実) + 2 examples
slide11.html: Category 3 (発言・提案) + 2 examples + warning box
slide12.html: Comparison grid + tip box
```
✓ Lower cognitive load for students learning new content
✓ Each slide fits comfortably within 720px
✓ More examples per category
✓ Better retention and understanding

