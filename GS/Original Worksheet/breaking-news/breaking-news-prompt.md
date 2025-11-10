# Breaking News Worksheet Creation Prompt

## Data Source

**Website:** https://breakingnewsenglish.com/simple-english-news.html

**RSS Feed:** https://breakingnewsenglish.com/bne.xml

### How to Fetch Articles Programmatically:

1. **Fetch the RSS Feed** - Use the RSS feed URL to get the latest articles:
   - URL: `https://breakingnewsenglish.com/bne.xml`
   - This feed provides the most recent articles with their titles and links
   - Articles are typically updated every three days

2. **Access Article from RSS Feed** - Once you have the article URL from the RSS feed:
   - Example URL format: `https://breakingnewsenglish.com/YYMM/YYMMDD-article-name.html`
   - This gives you access to the main article page

3. **Get Level 0 Content** - Navigate to the Level 0 version for beginner learners:
   - Level 0 URL format: `https://breakingnewsenglish.com/YYMM/YYMMDD-article-name-0.html`
   - Simply add `-0` before `.html` to access the easiest level
   - Level 0 uses basic vocabulary and short sentences suitable for beginner English learners

4. **Extract the Article Text** - Use WebFetch or similar tools to extract the full article text from the Level 0 page

5. **Create Folder Structure** - Create a folder for the article:
   - Format: `breaking-news/[article-topic-name]/`
   - Example: `breaking-news/food-and-body-smell/`

### Alternative Method:

If automated access doesn't work, you can manually:
1. Visit https://breakingnewsenglish.com/simple-english-news.html
2. Select an article of interest
3. Navigate to Level 0 of that article
4. Copy the article text manually

---

## Instructions

Create a worksheet based on the provided breaking news article with the following structure:

---

## Worksheet Structure

### Part 1: Gap Fill Exercise (6 blanks)
- Present the entire article text with blanks for students to fill in
- **IMPORTANT: Each blank must be a maximum of 2 words**
- Blanks can include various types of words (phrases, connectors, content words)
- Focus on key vocabulary and important phrases from the article
- Students listen and fill in the missing words/phrases
- Choose strategic blanks that test understanding of key information

**Format:**
```
Listen to the article and fill in the blanks.

[Article text with (1) _________, (2) _________, etc. numbered blanks - 6 blanks total, each max 2 words]
```

---

### Part 2: Vocabulary (5 matching items)
- Select 5 difficult or important words/phrases from the article
- Create a matching exercise in table format connecting English words to Japanese translations
- Arrange Japanese translations in random order (not matching the English order)
- Add blank spaces (\_\_\_\_\_\_\_) after each English word for students to write the matching letter
- This helps students understand key vocabulary before comprehension questions

**Format:**
```
Match the English words with their Japanese translations.

| **English Word**                      | **Japanese Translation** |
| :------------------------------------ | :----------------------- |
| 1. [word/phrase 1] \_\_\_\_\_         | a) [translation - randomized] |
| 2. [word/phrase 2] \_\_\_\_\_         | b) [translation - randomized] |
| 3. [word/phrase 3] \_\_\_\_\_         | c) [translation - randomized] |
| 4. [word/phrase 4] \_\_\_\_\_         | d) [translation - randomized] |
| 5. [word/phrase 5] \_\_\_\_\_         | e) [translation - randomized] |
```

**Vocabulary Selection Tips:**
- Choose technical terms or domain-specific vocabulary
- Include multi-word phrases if important to understanding
- Select words that appear in the article and are essential for comprehension
- Consider words that students at the target level might struggle with
- Prioritize the most important 5 words for understanding the article's main points

---

### Part 3: Listening Comprehension (3 questions)
- Create 3 comprehension questions that test understanding of:
  - Main topics/subjects
  - Key facts and details
  - Specific information (numbers, names, brands, etc.)
  - Cause and effect relationships
  - Concerns or issues mentioned
- Focus on the most important points from the article

**Format:** Simple numbered questions without answer lines

**Example:**
```
1. What [specific detail from article]?
2. What does [subject] want to use [technology] for?
3. What did [person/group] predict/say?
```

---

### Part 4: True or False (5 questions)
- Create 5 True/False statements
- Mix true and false statements (aim for 2-3 true, 2-3 false)
- Test key facts from the article
- Include at least one statement that requires careful listening (subtle details like numbers, timing, descriptions)

**Format:** Statement followed by **T / F**

**Example:**
```
1. [Specific detail with incorrect modifier]. **T / F**
2. [Accurate statement from article]. **T / F**
3. [Statement with wrong number/time]. **T / F**
```

---

### Part 5: Critical Thinking (1 question only)
- Create ONE open-ended question that:
  - **IMPORTANT:** The question itself should be only 1 sentence
  - Asks students to form and defend an opinion about the topic
  - References concerns or issues from the article
  - Encourages analytical thinking about real-world implications
  - **IMPORTANT:** Include sentence starters to help students construct their responses
  - Focus on helping students discuss opinions with peers and compose sentences with reasons

**Example question formats (1 sentence only):**
- "Do you think [technology/practice from article] should be used in [context]?"
- "How do you feel about [issue from article]?"
- "Should people [action related to article topic]?"

**Format with Sentence Starters:**
```
[One sentence question about the topic]

Consider the advantages and disadvantages. Use these sentence starters to help you express your opinion:
- I agree with the opinion that _____________ because _____________.
- I don't agree with the opinion that _____________ because _____________.
- I think _____________ because _____________.
- One advantage is _____________.
- One disadvantage is _____________.
```

---

## General Guidelines

1. **Title format:** `## [Topic] - Worksheet`
2. **No student information section** (no Name, Class, Date fields)
3. **No answer lines or spaces** for students to write
4. Keep language appropriate for the target level
5. Ensure questions flow logically and cover the main points of the article
6. Part 5 should be challenging and thought-provoking
7. Use clear, simple formatting with headers for each part
8. Use `###` for part headers (Part 1, Part 2, etc.)

---

## Output Format

```markdown
## [Article Title] - Worksheet

#### Part 1: Gap Fill Exercise

Listen to the article and fill in the blanks.

[Article with 6 numbered blanks - each blank max 2 words]

---

### Part 2: Vocabulary

Match the English words with their Japanese translations.

| **English Word**                      | **Japanese Translation** |
| :------------------------------------ | :----------------------- |
| 1. [word 1] \_\_\_\_\_                | a) [translation - randomized] |
| 2. [word 2] \_\_\_\_\_                | b) [translation - randomized] |
| 3. [word 3] \_\_\_\_\_                | c) [translation - randomized] |
| 4. [word 4] \_\_\_\_\_                | d) [translation - randomized] |
| 5. [word 5] \_\_\_\_\_                | e) [translation - randomized] |

---

### Part 3: Listening Comprehension

Answer the following questions based on the article.

1. [Question 1]
2. [Question 2]
3. [Question 3]

---

### Part 4: True or False

Listen to the article again and circle **T** (True) or **F** (False).

1. [Statement 1] **T / F**
...
5. [Statement 5] **T / F**

---

### Part 5: Critical Thinking

[One sentence question about the topic]

Consider the advantages and disadvantages. Use these sentence starters to help you express your opinion:
- I agree with the opinion that _____________ because _____________.
- I don't agree with the opinion that _____________ because _____________.
- I think _____________ because _____________.
- One advantage is _____________.
- One disadvantage is _____________.
```

---

## Answer Key Format

Create a separate answer file: `[article-name]-answer.md`

```markdown
# [Article Title] - Answer Key

## Part 1: Gap Fill Exercise

1. [answer 1] (max 2 words)
2. [answer 2] (max 2 words)
3. [answer 3] (max 2 words)
4. [answer 4] (max 2 words)
5. [answer 5] (max 2 words)
6. [answer 6] (max 2 words)

---

## Part 2: Vocabulary

1. [letter] ([Japanese translation])
2. [letter] ([Japanese translation])
3. [letter] ([Japanese translation])
4. [letter] ([Japanese translation])
5. [letter] ([Japanese translation])

---

## Part 3: Listening Comprehension

1. [Answer 1]
2. [Answer 2]
3. [Answer 3]

---

## Part 4: True or False

1. **T/F** ([Brief explanation])
...
5. **T/F** ([Brief explanation])

---

## Part 5: Critical Thinking

**Open-ended question - answers will vary**

Sample answer points students might include:
- [Point 1]
- [Point 2]
- Students should reference [specific concerns from article]
```

---

## File Organization

Create a folder structure for each article with **3 required files**:

```
breaking-news/
  └── [article-topic-name]/
      ├── [article-topic-name]-script.md
      ├── [article-topic-name]-worksheet.md
      └── [article-topic-name]-answer.md
```

**File descriptions:**
1. **[article-topic-name]-script.md** - Raw article text with no changes (Level 0 content)
2. **[article-topic-name]-worksheet.md** - Student worksheet with exercises
3. **[article-topic-name]-answer.md** - Answer key for teachers

**Example:**
```
breaking-news/
  └── food-and-body-smell/
      ├── food-and-body-smell-script.md
      ├── food-and-body-smell-worksheet.md
      └── food-and-body-smell-answer.md
```

---

## Usage

To use this prompt:
1. **Fetch the RSS feed** at https://breakingnewsenglish.com/bne.xml to see available articles
2. **Select an article** from the feed
3. **Access Level 0** by adding `-0` to the article URL (before `.html`)
4. **Extract the article text** using WebFetch or manual copy
5. **Create a folder** for the article in the breaking-news directory
6. **Provide the article text** and specify: "Create a worksheet based on this breaking news article using the breaking-news-prompt.md format"
7. **Save 3 files** in the article folder:
   - `[article-topic-name]-script.md` - Raw article text with no changes
   - `[article-topic-name]-worksheet.md` - Student worksheet
   - `[article-topic-name]-answer.md` - Answer key
8. The worksheet and answer key will follow this consistent format
