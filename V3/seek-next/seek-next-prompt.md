# Seek-Next Worksheet Template & Prompt

## Overview

This document serves as a guide for creating consistent, professional worksheets for English reading materials using the Lars-Eric Lindblad worksheet as the template. The worksheet is designed for beginner English learners and includes vocabulary definitions, comprehension activities, and character/story analysis.

## General Structure

All worksheets follow this **consistent three-section format**:

1. **Section 1: Vocabulary & Key Terms** (単語・キーワード) - FIXED
2. **Section 2: Flexible Activity** (varies by story) - CUSTOMIZABLE
3. **Section 3: Character Profile / Story Analysis** (人物像) - FIXED with custom questions

---

## Section 1: Vocabulary & Key Terms (ALWAYS THE SAME)

**Purpose:** Students write definitions for key vocabulary terms from the text.

**Structure:**
- Grid layout with 8 vocabulary items (2 columns)
- Each term has a small definition box (min-height: 30px)
- No hints or context provided - students must use their reading comprehension
- Terms should be from the text and directly related to the story

**How to customize:**
1. Select 8 key vocabulary words from the text
2. Replace the existing vocabulary terms in the HTML grid
3. Keep the same visual structure

**Example terms to select:**
- New words students may not know
- Words essential to understanding the story
- Technical or thematic vocabulary

---

## Section 2: Flexible Activity (CUSTOMIZABLE)

This section changes based on the story's content. Choose ONE activity that best fits your story:

### Option A: Timeline of Events (時系列)
**Best for:** Stories with clear chronological progression or multiple historical events

**Structure:**
- Horizontal visual timeline with 5 key dates/events
- Students add descriptions for each event
- Shows cause-and-effect or historical progression

**How to customize:**
1. Identify 5 key events/dates from the story
2. Replace the years and event labels in the timeline HTML
3. Keep the timeline visual structure and styling

**Example:** Lars-Eric Lindblad (1927, 1951, 1958, 1959-1967, 1994)

### Option B: Plot Sequence / Story Events (物語の流れ)
**Best for:** Narrative stories with clear beginning, middle, end

**Structure:**
- Numbered sequence boxes (3-5 events)
- Students write what happens in each phase
- Shows story progression without specific dates

**HTML template:**
```html
<div class="section-title">2. 物語の流れ (Story Events)</div>
<div style="margin: 15px 0;">
    <div style="border: 1px solid black; padding: 12px; margin: 10px 0;">
        <div style="font-weight: bold; margin-bottom: 8px;">出来事1 (Event 1)</div>
        <div style="min-height: 60px; border-top: 1px dotted #999; margin-top: 8px; padding-top: 8px;"></div>
    </div>
    <div style="border: 1px solid black; padding: 12px; margin: 10px 0;">
        <div style="font-weight: bold; margin-bottom: 8px;">出来事2 (Event 2)</div>
        <div style="min-height: 60px; border-top: 1px dotted #999; margin-top: 8px; padding-top: 8px;"></div>
    </div>
    <!-- Repeat as needed -->
</div>
```

### Option C: Cause & Effect (原因と結果)
**Best for:** Stories emphasizing relationships between events

**Structure:**
- Paired boxes showing causes and their effects
- 3-4 cause-effect pairs
- Students match or write connections

**HTML template:**
```html
<div class="section-title">2. 原因と結果 (Cause & Effect)</div>
<div style="margin: 15px 0;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; align-items: center;">
        <div style="border: 1px solid black; padding: 12px;">
            <div style="font-weight: bold; margin-bottom: 8px;">原因 (Cause)</div>
            <div style="min-height: 60px;"></div>
        </div>
        <div style="text-align: center; font-weight: bold;">→</div>
        <div style="border: 1px solid black; padding: 12px;">
            <div style="font-weight: bold; margin-bottom: 8px;">結果 (Effect)</div>
            <div style="min-height: 60px;"></div>
        </div>
    </div>
</div>
```

### Option D: Comparison Chart (比較)
**Best for:** Stories with contrasts or comparisons between characters/settings

**Structure:**
- Two-column comparison table
- Students identify similarities and differences
- 3-4 comparison points

---

## Section 3: Character Profile / Story Analysis (ALWAYS THE SAME STRUCTURE)

**Purpose:** Students extract and organize key information about the main character(s) or story themes.

**Structure:**
- 2-column grid with 6 analysis boxes
- Each box has a label with **paragraph hints** (段落1, 段落2, etc.)
- Larger fill-in boxes (min-height: 80px)
- Both Japanese and English labels

**How to customize:**
1. Identify 6 key character/story attributes to analyze
2. Determine which paragraph contains information about each attribute
3. Replace the labels in the HTML
4. Update paragraph references (段落1 = Paragraph 1, etc.)

**Example labels from Lars-Eric Lindblad:**
- 出身地と子供の頃の興味 (Birthplace & Childhood Interests)
- 教育 (Education)
- キャリアの革新 (Career Innovation)
- 有名な目的地 (Famous Destinations)
- 環境哲学 (Environmental Philosophy)
- 遺産と家族 (Legacy & Family)

**Creating labels for other stories:**
- Focus on: origins, motivation, key actions, beliefs, relationships, impact
- Use parallel structure (noun + descriptor format)
- Ensure each label can be answered from the text

---

## HTML Structure & Technical Notes

### Base Template
The worksheet uses a professional HTML/CSS structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[Story Title] Worksheet</title>
    <style>
        /* CSS remains the same - see lars-eric-lindblad-worksheet.html */
    </style>
</head>
<body>
    <div class="worksheet">
        <!-- Header: Title only -->
        <!-- Section 1: Vocabulary (ALWAYS THE SAME STRUCTURE) -->
        <!-- Section 2: Flexible activity (CHOOSE ONE) -->
        <!-- Section 3: Character Profile (ALWAYS THE SAME STRUCTURE) -->
    </div>
</body>
</html>
```

### CSS Features (Do Not Change)
- Professional print-optimized layout
- A3 paper size formatting
- Color scheme: light gray backgrounds (#e9e9e9), white containers, black borders
- Font: Helvetica Neue (supports English and Japanese)
- Responsive grid layouts
- Print-specific media queries

### Title Formatting
Always use format: `[Character/Story Name]: [Descriptor]`
- Example: "Lars-Eric Lindblad: Life & Legacy"
- Examples for others: "The Ant and the Grasshopper: A Fable", "Marie Curie: Pioneer of Science"

---

## Step-by-Step Instructions for New Worksheets

### 1. Read the Story
Identify:
- 8 key vocabulary words
- Main character(s) or central figures
- 6 key attributes/themes to analyze
- Paragraph structure (mark paragraphs 1-4)
- Type of story progression (timeline, narrative, causes, comparison, etc.)

### 2. Create Section 1: Vocabulary
- List 8 vocabulary terms with small definition boxes
- Keep structure identical to template

### 3. Create Section 2: Flexible Activity
- Choose the activity type that best fits the story (A, B, C, or D)
- Adapt the structure to your content
- 2-3 columns or sequential layout depending on activity type
- Maintain consistent styling (borders, padding, spacing)

### 4. Create Section 3: Character Profile
- Create 6 boxes analyzing the main character/story elements
- For each box: add label (Japanese + English) + paragraph hint
- Verify paragraph references are correct
- Keep 2-column grid layout

### 5. Test & Print
- Open HTML in web browser to verify styling
- Check that text boxes are properly sized
- Test print preview (should be properly formatted for A3)
- Verify all Japanese and English text displays correctly

---

## Design Guidelines

### Spacing & Layout
- Margin between sections: 15-30px
- Padding inside boxes: 12px
- Grid gaps: 15-20px
- Fill-in box minimum height: 30px (vocabulary), 80px (profile), 60px (other)

### Typography
- Title: 28px, bold
- Section titles: 18px, bold
- Labels: 13px, bold
- Small hints: 11px, color #666
- Regular text: 12px

### Borders & Styling
- Standard borders: 1px solid black
- Section borders: 2px solid black
- Fill lines: 1px dotted #999
- Box shadows: 0 4px 12px rgba(0,0,0,0.1)

### Language
- ALL instructions in Japanese (for beginner learners)
- English in parentheses for reference
- Format: 日本語 (English)
- Paragraph markers: 段落1, 段落2, 段落3, 段落4

---

## File Naming Convention

Place worksheets in: `V3/seek-next/lesson[#]/[story-name]-worksheet.html`

Examples:
- `lesson12/lars-eric-lindblad-worksheet.html`
- `lesson13/the-ant-and-grasshopper-worksheet.html`
- `lesson14/marie-curie-worksheet.html`

---

## Checklist for New Worksheets

- [ ] Story text divided into clear paragraphs (ideally 3-4)
- [ ] 8 vocabulary terms selected and definitions can be written
- [ ] Section 2 activity type chosen (Timeline/Narrative/Cause-Effect/Comparison)
- [ ] 6 character profile labels created with paragraph hints
- [ ] HTML file created with correct styling
- [ ] All Japanese instructions added
- [ ] Print preview tested and looks professional
- [ ] File saved in correct location with naming convention
- [ ] Vocabulary boxes are compact (30px)
- [ ] Profile boxes have adequate space (80px)
- [ ] Paragraph references are accurate

---

## Example Variations

### Short Story (Fable)
- Section 1: Vocabulary (8 terms)
- Section 2: Moral Lesson (single large reflection box) or Cause & Effect
- Section 3: Character Analysis (hero, antagonist, virtues, flaws, etc.)

### Biography
- Section 1: Vocabulary (8 terms)
- Section 2: Timeline of Life Events
- Section 3: Character Profile (origins, achievements, beliefs, legacy, etc.)

### News Article
- Section 1: Vocabulary (8 terms)
- Section 2: 5 W's (Who, What, When, Where, Why)
- Section 3: Analysis (context, importance, implications, connections)

