import csv
import re
from collections import defaultdict
import os
import argparse

def analyze_peer_eval(filepath):
    """
    Analyzes a CSV file with peer evaluation scores and saves the results to a Markdown file.

    Args:
        filepath (str): The path to the CSV file.
    """
    group_scores = defaultdict(lambda: defaultdict(int))
    group_counts = defaultdict(int)
    
    # Define headers for the criteria for better readability
    criteria_headers = [
        "1. Language Use (Accuracy and Variety)",
        "2. Clarity and Flow (Cohesion)",
        "3. Structure and Organization",
        "4. Content and Originality",
        "5. Teamwork and Participation"
    ]

    try:
        with open(filepath, mode='r', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            for row_num, row in enumerate(reader, 1):
                if len(row) < 3:
                    continue

                group_name = row[2].strip()
                if not group_name.startswith('group'):
                    continue

                # Check if the row contains scores before incrementing the count
                has_scores = False
                for i in range(3, 8):
                    if i < len(row) and re.match(r'^\d+', row[i].strip()):
                        has_scores = True
                        break
                
                if has_scores:
                    group_counts[group_name] += 1

                for i in range(3, 8):
                    if i < len(row):
                        score_text = row[i].strip()
                        if score_text:
                            match = re.match(r'^\d+', score_text)
                            if match:
                                try:
                                    score = int(match.group(0))
                                    criterion_key = f'criterion_{i-2}'
                                    group_scores[group_name][criterion_key] += score
                                except ValueError:
                                    # This case is less likely with the regex, but good practice
                                    print(f"Warning: Row {row_num}: Could not parse score from '{score_text}'")
                            else:
                                print(f"Warning: Row {row_num}: No score found at the start of '{score_text}'")

    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return

    # Prepare for output
    output_filename = os.path.splitext(os.path.basename(filepath))[0] + '_results.md'
    output_filepath = os.path.join(os.path.dirname(filepath), output_filename)
    
    output_lines = ["# Group Evaluation Results"]

    sorted_groups = sorted(group_scores.keys(), key=lambda x: int(re.search(r'\d+', x).group()))

    for group in sorted_groups:
        num_evaluations = group_counts.get(group, 0)
        if num_evaluations == 0:
            continue

        output_lines.append(f"\n## {group.upper()}")
        output_lines.append(f"Based on **{num_evaluations}** evaluations.\n")
        
        scores = group_scores[group]
        total_score = sum(scores.get(f'criterion_{i}', 0) for i in range(1, 6))

        for i in range(1, 6):
            criterion_key = f'criterion_{i}'
            header = criteria_headers[i-1]
            total_criterion_score = scores.get(criterion_key, 0)
            avg_criterion_score = total_criterion_score / num_evaluations
            output_lines.append(f"- **{header}:**")
            output_lines.append(f"  - Total Points: {total_criterion_score}")
            output_lines.append(f"  - Average Score: {avg_criterion_score:.2f}")

        total_average_score = total_score / num_evaluations
        output_lines.append(f"\n### Summary for {group.upper()}")
        output_lines.append(f"- **Grand Total Points:** {total_score}")
        output_lines.append(f"- **Overall Average Score:** {total_average_score:.2f}")
        output_lines.append("\n---")

    try:
        with open(output_filepath, 'w', encoding='utf-8') as outfile:
            outfile.write("\n".join(output_lines))
        print(f"\nAnalysis complete. Results saved to '{output_filepath}'")
    except IOError as e:
        print(f"Error writing to file '{output_filepath}': {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Analyzes peer evaluation scores from a CSV file. \n"
                    "Usage: python3 analyze_scores.py <path_to_csv_file>"
    )
    parser.add_argument(
        "filepath",
        help="The path to the CSV file to analyze."
    )
    args = parser.parse_args()

    if os.path.exists(args.filepath):
        analyze_peer_eval(args.filepath)
    else:
        print(f"Error: The file '{args.filepath}' was not found.") 