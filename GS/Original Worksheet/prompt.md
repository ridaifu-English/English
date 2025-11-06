Objective: Create a student worksheet, a corresponding answer sheet, and a video script based on a YouTube video. These materials should be designed to check comprehension and encourage critical thinking, specifically tailored to one of three English proficiency levels: Beginner, Intermediate, or Advanced. The outputs must be formatted in Markdown within three separate code blocks.

Video URL: [YOUR_VIDEO_URL_HERE]

**Target Audience Level (Select ONE):**
*   Beginner
*   Intermediate
*   Advanced

**Output Requirements:**

Generate three distinct Markdown code blocks: `worksheet`, `answersheet`, and `script`.

**Code Block 1: `worksheet` Requirements:**

1.  **Title:** Create a concise title for the worksheet based on the video's topic (this should render as bold, e.g., using `#` or as the first line).
2.  **Level Indicator:** Clearly state the target level (Beginner, Intermediate, or Advanced) at the top of the worksheet in normal font weight.
3.  **Instructions (General):** Include a general instruction for students to watch the video and complete the worksheet in normal font weight.
4.  **YouTube URL:** Display the provided YouTube URL.
5.  **Structure:** Organize the worksheet into the following parts, **adjusting content and tasks based on the selected Target Audience Level**:
    *   **## Part 1: Vocabulary Check** (This heading should be bold)
        *   Identify **5** key English vocabulary words from the video relevant to the main topic.
        *   Present the instructions for the task in normal font weight. These instructions should appear *before* and *outside* of any table used for the task itself.
        *   **Beginner Task:** After the instructions, create a two-column Markdown table for the matching exercise (5 English words to their Japanese translations). Use the example format below for this table.
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
        *   **Advanced Task:** After the instructions, list **5** words. Instruct students to write a short definition OR use the word in a sentence based on its context in the video. Use `---` for answer lines.
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
    *   **## Part 2: While You Watch - Main Idea** (Bold heading)
        *   Determine the single main topic/idea of the video.
        *   Create one multiple-choice question asking for the main topic.
        *   Provide three plausible options (a, b, c), with only one being the correct main topic. Adjust distractor complexity based on the level.
        *   Include instructions in normal font weight (e.g., "Circle the correct answer.").
    *   **## Part 3: Listen and Understand (DIFFERENTIATED)** (Bold heading)
        *   Select 3 short, clear sentences or key phrases from the video. Provide the approximate timestamp `[X:XX]`.
        *   Instructions should be in normal font weight.
        *   **Beginner:** Create fill-in-the-blank sentences with *one* blank each. Provide multiple-choice options for *each* blank.
            ```markdown
            Instructions: Listen carefully around the time shown and choose the correct word to complete the sentence. Circle the best answer.
            1. [X:XX] Sentence with [ __________ ].
               a) option1   b) option2   c) correct_word
            2. [Y:YY] Sentence with [ __________ ].
               a) correct_word   b) option2   c) option3
            3. [Z:ZZ] Sentence with [ __________ ].
               a) option1   b) correct_word   c) option3
            ```
        *   **Intermediate & Advanced:** Rewrite each sentence/phrase, replacing one or two key words with brackets `[ __________ ]`. Students must *write* the missing word(s). **No options provided.**
            ```markdown
            Instructions: Listen carefully around the time shown and write the missing word(s) in the blanks.
            1. [X:XX] Sentence with [ __________ ] key words [ __________ ].
            2. [Y:YY] Another sentence [ __________ ] missing words.
            3. [Z:ZZ] The final [ __________ ] phrase.
            ```
    *   **## Part 4: While You Watch - Key Concepts/Details** (Bold heading)
        *   Identify 3-4 key concepts, details, reasons, examples, or effects explained in the video. Adjust complexity based on level.
        *   Formulate 3-4 fill-in-the-blank sentences based on these concepts. Provide approximate timestamps `[X:XX]`.
        *   Include instructions in normal font weight (e.g., "Fill in the blanks below using words from the Word Box.").
        *   List the fill-in-the-blank sentences *first*.
        *   Place the "Word Box" *after* the sentences. The Word Box should contain the correct words needed to fill the blanks, plus distractors as appropriate for the level. **Use the specific two-line Markdown table format below, placing all words comma-separated in the single cell of the first row, followed by a separator line:**
            *   **Beginner:** Include only the correct words, maybe 1 easily distinguishable distractor.
            *   **Intermediate/Advanced:** Include the correct words plus 1-2 plausible distractors.
            *Example Structure for Part 4:*
            ```markdown
            Instructions: Fill in the blanks below using words from the Word Box.
            1. [X:XX] The video explains that [ __________ ] is important.
            2. [Y:YY] One example given is the use of [ __________ ].
            3. [Z:ZZ] We should be careful about [ __________ ] online.

            **Word Box**
            | word1, word2, word3, distractor1, ... |
            |-|
            ```
    *   **## Part 5: Comprehension Check (Intermediate & Advanced ONLY)** (Bold heading)
        *   **This part is ONLY for Intermediate and Advanced levels.**
        *   **Intermediate:** Formulate 3-5 **more basic** questions using the 5W1H framework (Who, What, Where, When, Why, How) focusing on direct information recall. Use `<br>` for answer lines.
        *   **Advanced:** Formulate 3-5 **more complex** questions using the 5W1H framework to check understanding beyond simple recall. Use `---` for answer lines.
        *   Include instructions in normal font weight (e.g., "Answer the following questions about the video in your own words. Use complete sentences.").
        *   Provide space for written answers using the specified format (`<br>` for Intermediate, `---` for Advanced) below each question.
    *   **## Part 6: After You Watch - Think!** (Bold heading)
        *   **Beginner:** Formulate 1-2 **simple** questions asking for their opinion or reaction to the video's topic. Use `---` for answer lines.
        *   **Intermediate:** Formulate **one** question that is potentially **controversial or encourages discussion/debate** related to the video's topic. Use `<br>` for answer lines.
        *   **Advanced:** Formulate 1-2 **more complex** questions asking for their opinion, reaction, or connection to the video's topic. Use `---` for answer lines.
        *   Include instructions in normal font weight prompting students to explain their answer.
        *   Provide space for written answers using the specified format (`---` for Beginner/Advanced, `<br>` for Intermediate) below the question(s).

6.  **Formatting:**
    *   Use Markdown formatting: `##` for **bold** Part headings. The main title should also appear bold.
    *   **All other text (instructions, descriptions, questions, options) must be in normal font weight.**
    *   Use `1.` for numbered lists where appropriate.
    *   For Part 1 Beginner/Intermediate, the two-column matching table should appear *after* its instructions, not enclosing them. For Advanced Part 1, the list of words and answer lines should appear *after* its instructions.
    *   Use the specific two-line table format `| word1, word2, ... |\n|-|` ONLY for the Word Box in Part 4, placed *after* the sentences.
    *   Use `<br>` for answer lines in Intermediate Parts 5 & 6. Use `---` for answer lines in Advanced Parts 1, 5, & 6 and Beginner Part 6.
    *   Ensure clear instructions precede each task/part.
    *   Include timestamps `[X:XX]` where specified (Part 3, Part 4).

**Code Block 2: `answersheet` Requirements:**

1.  **Title:** Use the same title as the worksheet, followed by "- Answer Key". Render bold.
2.  **Level Indicator:** State the target level. Normal font weight.
3.  **Answers:** Provide clear answers for all objective sections (Part 1 Matching/Definition lookup, Part 2 MC, Part 3 Fill-in-the-blank/MC, Part 4 Fill-in-the-blank). For Beginner/Intermediate Part 1, list the correct letter matches (e.g., 1. e, 2. c, ...).
4.  **Suggested Answers:** For subjective sections (Advanced Part 1 sentences, Intermediate/Advanced Part 5, All levels Part 6), provide example or suggested answers based on the video content. Indicate these are suggestions.
5.  **Formatting:** Use Markdown. Keep structure parallel to the worksheet for easy reference (e.g., use Part headings).

**Code Block 3: `script` Requirements:**

1.  **Title:** Use the same title as the worksheet, followed by "- Video Script". Render bold.
2.  **Level Indicator:** State the target level. Normal font weight.
3.  **Transcript:** Provide the full video transcript from the `Video Transcript` variable.
4.  **Timestamps:** Include timestamps `[X:XX]` (minutes:seconds) at reasonable intervals or at the start of sentences/significant phrases throughout the transcript. These timestamps should align with those used in the worksheet (Parts 3 & 4).
5.  **Formatting:** Use Markdown. Ensure timestamps are clearly visible (e.g., `[0:15] Text begins...`).

**Final Instruction:** Ensure each of the three outputs (`worksheet`, `answersheet`, `script`) is enclosed within its own distinct Markdown code block (```markdown ... ```). Do not include any explanatory text outside these code blocks.