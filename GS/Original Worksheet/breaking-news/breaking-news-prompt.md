# Breaking News Worksheet Creation Prompt

## Data Source

**Website:** https://breakingnewsenglish.com/simple-english-news.html

**Note:** To fetch content programmatically, use the r.jina.ai/ prefix before the URL:
- Example: `https://r.jina.ai/https://breakingnewsenglish.com/simple-english-news.html`

### Steps to Fetch Content:

1. **Navigate to the website** using `https://r.jina.ai/https://breakingnewsenglish.com/simple-english-news.html` to browse available articles
2. **Select an article** of interest from the simple English news page
3. **Get Level 0 content** - Navigate to the article and access Level 0 (the easiest level, suitable for basic English learners)
   - Use r.jina.ai/ prefix: `https://r.jina.ai/[article-level-0-url]`
4. **Extract the script** - Find and copy the full article text from Level 0
5. **Use the script** to create a worksheet following the format below

## Instructions

Create a worksheet based on the extracted Level 0 breaking news article with the following structure:

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
  - Asks students to form and defend an opinion about the topic
  - Requires students to consider advantages AND disadvantages
  - References concerns or issues from the article
  - Encourages analytical thinking about real-world implications

**Example prompts:**
- "Do you think [technology/practice from article] should be used in [context]? What are the advantages and disadvantages? Consider the concerns mentioned in the article and explain your reasoning."
- "How do you feel about [issue from article]? What are the potential benefits and risks?"

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

[Open-ended question about the topic]
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

## Usage

To use this prompt:
1. Visit https://r.jina.ai/https://breakingnewsenglish.com/simple-english-news.html (use r.jina.ai/ prefix to fetch content)
2. Select an article from the list
3. Navigate to **Level 0** of that article (the easiest level) using r.jina.ai/ prefix
4. Copy the full article script/text from Level 0
5. Provide the article text and specify: "Create a worksheet based on this breaking news article using the breaking-news-prompt.md format"
6. The worksheet and answer key will follow this consistent format
