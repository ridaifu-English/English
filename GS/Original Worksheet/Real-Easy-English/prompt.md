Objective: Create a student worksheet, a corresponding answer sheet, and a script based on a transcript scraped from a Real Easy English page using Jina MCP. These materials should check comprehension and encourage critical thinking, tailored to one of three English proficiency levels: Beginner, Intermediate, or Advanced. The outputs must be formatted in Markdown within three separate code blocks.

Inputs:
*   `source_url` (string): The Real Easy English page to scrape.
*   `levels_to_produce` (array of strings): Any of ["Beginner","Intermediate","Advanced"]. Default: all three.
*   `read_options` (optional): When reading with Jina, prefer using `read_url` to obtain clean Markdown (defaults are fine). If needed, set `withAllLinks: false` and `withAllImages: false`.
*   `output_dir` (string): Absolute or workspace-relative directory path where generated files will be written.
*   `overwrite` (boolean, optional): Whether to overwrite existing files. Default: `true`. If `false`, append a numeric suffix like `-v2`.

Agent Process (Jina MCP):
1.  Read `source_url` using Jina MCP `read_url` to obtain clean Markdown content.
2.  Locate sections headed exactly as `### Transcript` and `### Vocabulary` in the scraped Markdown. If `### Transcript` is not found, extract the transcript by locating continuous dialogue lines with speaker labels (e.g., `Name:`). If `### Vocabulary` is not found, derive a vocabulary list by extracting key topic words and terms from the transcript.
3.  Clean the transcript:
    *   Preserve speaker names; normalize as `Name:` when possible.
    *   Remove stage directions like `[Music]` or site prompts, ads, or navigation text.
    *   Remove or ignore any timestamps that might appear; do not include timestamps in outputs.
    *   Deduplicate repeated lines or navigation artifacts.
4.  Store the cleaned transcript as `Transcript` and the extracted list as `Vocabulary`, and use both to generate all artifacts.

Multi-level Output Controls:
*   For each level in `levels_to_produce`, produce three fenced code blocks (```markdown) in this order per level: `worksheet`, `answersheet`, `script`.
*   Order levels as: Beginner → Intermediate → Advanced.
*   Inside each block, begin with two lines:
    *   `Title: <same title across all artifacts>`
    *   `Level: <Beginner|Intermediate|Advanced>`

Filesystem Output (Writing Files):
1.  Title Slug: Create `title_slug` by lowercasing the title, replacing spaces with hyphens, removing non-alphanumeric characters except hyphens, collapsing repeated hyphens, and trimming leading/trailing hyphens.
2.  Directory Structure (nested): For each level, write files to `<output_dir>/<title_slug>/<level>/`.
3.  Filenames: Write three UTF-8 `.md` files per level with exact content matching the emitted code blocks:
    *   `worksheet.md`
    *   `answersheet.md`
    *   `script.md`
4.  Create directories as needed. If a target file exists and `overwrite` is `false`, append a numeric suffix before the `.md` extension (e.g., `worksheet-v2.md`).
5.  Do not write any additional files. Do not include timestamps in any file. Ensure the saved content is identical to the corresponding code block content.

**Target Audience Level (Select ONE):**
*   Beginner
*   Intermediate
*   Advanced

**Output Requirements:**

Generate three distinct Markdown code blocks: `worksheet`, `answersheet`, and `script`.

**Code Block 1: `worksheet` Requirements:**

1.  **Instructions (General):** Include a general instruction for students to read/listen to the transcript and complete the worksheet in normal font weight.
2.  **Structure:** Organize the worksheet into the following parts, adjusting content and tasks based on the selected Target Audience Level:
    *   **## Part 1: Vocabulary Check** (This heading should be bold)
        *   Identify **5** key English vocabulary words from the transcript relevant to the main topic. When available, use the words from the `### Vocabulary` section of the scraped page.
        *   Present the instructions for the task in normal font weight. These instructions should appear before and outside of any table used for the task itself.
        *   **Beginner Task:** After the instructions, create a two-column Markdown table for the matching exercise (5 English words to their Japanese translations).
        *   **Intermediate Task:** After the instructions, create a two-column Markdown table for the matching exercise (5 English words to their **Japanese translations**). **Use the EXACT format below for this table.**
            ```markdown
            | **English Word**          | **Japanese Translation**           |
            | :------------------------ | :--------------------------------- |
            | 1. [English Word 1] `___` | a) [Japanese Translation for Word X] |
            | 2. [English Word 2] `___` | b) [Japanese Translation for Word Y] |
            | 3. [English Word 3] `___` | c) [Japanese Translation for Word Z] |
            | 4. [English Word 4] `___` | d) [Japanese Translation for Word W] |
            | 5. [English Word 5] `___` | e) [Japanese Translation for Word V] |
            ```
        *   **Advanced Task:** After the instructions, list **5** words. Instruct students to write a short definition OR use the word in a sentence based on its context in the transcript. Use `---` for answer lines.
            *Example format for the list of words and answer lines:*
            ```markdown
            1. [Word 1]:
               ---
            2. [Word 2]:
               ---
            3. [Word 3]:
               ---
            4. [Word 4]:
               ---
            5. [Word 5]:
               ---
            ```
    *   **## Part 2: While You Read/Listen - Main Idea** (Bold heading)
        *   Determine the single main topic/idea of the transcript.
        *   Create one multiple-choice question asking for the main topic.
        *   Provide three plausible options (a, b, c), with only one being the correct main topic. Adjust distractor complexity based on the level.
        *   Include instructions in normal font weight (e.g., "Circle the correct answer.").
    *   **## Part 3: Read/Listen and Understand (DIFFERENTIATED)** (Bold heading)
        *   Select 3 short, clear sentences or key phrases from the transcript.
        *   Instructions should be in normal font weight.
        *   **Beginner:** Create fill-in-the-blank sentences with *one* blank each. Provide multiple-choice options for *each* blank.
            ```markdown
            Instructions: Read carefully and choose the correct word to complete the sentence. Circle the best answer.
            1. Sentence with [ __________ ].
               a) option1   b) option2   c) correct_word
            2. Sentence with [ __________ ].
               a) correct_word   b) option2   c) option3
            3. Sentence with [ __________ ].
               a) option1   b) correct_word   c) option3
            ```
        *   **Intermediate & Advanced:** Rewrite each sentence/phrase, replacing one or two key words with brackets `[ __________ ]`. Students must *write* the missing word(s). **No options provided.**
            ```markdown
            Instructions: Read carefully and write the missing word(s) in the blanks.
            1. Sentence with [ __________ ] key words [ __________ ].
            2. Another sentence [ __________ ] missing words.
            3. The final [ __________ ] phrase.
            ```
    *   **## Part 4: While You Read/Listen - Key Concepts/Details** (Bold heading)
        *   Identify 3–4 key concepts, details, reasons, examples, or effects explained in the transcript. Adjust complexity based on level.
        *   Formulate 3–4 fill-in-the-blank sentences based on these concepts.
        *   Include instructions in normal font weight (e.g., "Fill in the blanks below using words from the Word Box.").
        *   List the fill-in-the-blank sentences first.
        *   Place the "Word Box" after the sentences. The Word Box should contain the correct words needed to fill the blanks, plus distractors as appropriate for the level. **Use the specific two-line Markdown table format below, placing all words comma-separated in the single cell of the first row, followed by a separator line:**
            *   **Beginner:** Include only the correct words, maybe 1 easily distinguishable distractor.
            *   **Intermediate/Advanced:** Include the correct words plus 1–2 plausible distractors.
            *Example Structure for Part 4:*
            ```markdown
            Instructions: Fill in the blanks below using words from the Word Box.
            1. The transcript explains that [ __________ ] is important.
            2. One example given is the use of [ __________ ].
            3. We should be careful about [ __________ ] online.

            **Word Box**
            | word1, word2, word3, distractor1, ... |
            |-|
            ```
    *   **## Part 5: Comprehension Check (Intermediate & Advanced ONLY)** (Bold heading)
        *   **This part is ONLY for Intermediate and Advanced levels.**
        *   **Intermediate:** Formulate 3–5 more basic questions using the 5W1H framework (Who, What, Where, When, Why, How) focusing on direct information recall. Use `<br>` for answer lines.
        *   **Advanced:** Formulate 3–5 more complex questions using the 5W1H framework to check understanding beyond simple recall. Use `---` for answer lines.
        *   Include instructions in normal font weight (e.g., "Answer the following questions about the transcript in your own words. Use complete sentences.").
        *   Provide space for written answers using the specified format (`<br>` for Intermediate, `---` for Advanced) below each question.
    *   **## Part 6: After You Read/Listen - Think!** (Bold heading)
        *   **Beginner:** Formulate 1–2 simple questions asking for their opinion or reaction to the topic. Use `---` for answer lines.
        *   **Intermediate:** Formulate one question that is potentially controversial or encourages discussion/debate related to the topic. Use `<br>` for answer lines.
        *   **Advanced:** Formulate 1–2 more complex questions asking for their opinion, reaction, or connection to the topic. Use `---` for answer lines.
        *   Include instructions in normal font weight prompting students to explain their answer.
        *   Provide space for written answers using the specified format (`---` for Beginner/Advanced, `<br>` for Intermediate) below the question(s).

6.  **Formatting:**
    *   Use Markdown formatting: `##` for **bold** Part headings. The main title should also appear bold.
    *   All other text (instructions, descriptions, questions, options) must be in normal font weight.
    *   Use `1.` for numbered lists where appropriate.
    *   For Part 1 Beginner/Intermediate, the two-column matching table should appear after its instructions, not enclosing them. For Advanced Part 1, the list of words and answer lines should appear after its instructions.
    *   Use the specific two-line table format `| word1, word2, ... |\n|-|` ONLY for the Word Box in Part 4, placed after the sentences.
    *   Use `<br>` for answer lines in Intermediate Parts 5 & 6. Use `---` for answer lines in Advanced Parts 1, 5, & 6 and Beginner Part 6.
    *   Ensure clear instructions precede each task/part.
    *   Do NOT include timestamps anywhere in the worksheet (no `[X:XX]`).

**Code Block 2: `answersheet` Requirements:**

1.  **Answers:** Provide clear answers for all objective sections (Part 1 Matching/Definition lookup, Part 2 MC, Part 3 Fill-in-the-blank/MC, Part 4 Fill-in-the-blank). For Beginner/Intermediate Part 1, list the correct letter matches (e.g., 1. e, 2. c, ...).
2.  **Suggested Answers:** For subjective sections (Advanced Part 1 sentences, Intermediate/Advanced Part , All levels Part 6), provide example or suggested answers based on the transcript content. Indicate these are suggestions.
3.  **Formatting:** Use Markdown. Keep structure parallel to the worksheet for easy reference (e.g., use Part headings).

**Code Block 3: `script` Requirements:**

1.  **Transcript:** Provide the full transcript exactly as scraped and cleaned from `source_url`. Preserve speaker names if present. Do not summarize.
2.  **Timestamps:** Do NOT include timestamps.
3.  **Formatting:** Use Markdown. Keep the transcript clean and legible (e.g., speaker labels like `Beth:` / `Neil:` on separate lines).

**Final Instruction:** For each level in `levels_to_produce`, output three distinct Markdown code blocks (```markdown ... ```), one for each of `worksheet`, `answersheet`, and `script`, in that order. Order levels as Beginner, then Intermediate, then Advanced. Do not include any explanatory text outside these code blocks, and do not include timestamps anywhere.
Additionally, write the exact contents of each code block to the filesystem under `<output_dir>/<title_slug>/<level>/` using the filenames `worksheet.md`, `answersheet.md`, and `script.md` (creating directories as needed and following the `overwrite` rule). Do not print file paths in the output.