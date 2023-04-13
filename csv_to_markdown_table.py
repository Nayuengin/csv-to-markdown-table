import os
import pandas as pd

def csv_to_markdown_table(file_path: str) -> str:
    """
    Converts the CSV file at the given file path into a Markdown-formatted table.

    :param file_path: The path to the CSV file.
    :return: A string containing the Markdown-formatted table.
    """
    df = pd.read_csv(file_path)
    return df.to_markdown(index=False)

csv_dir = "csv"
output_dir = "output"

# Iterate through all files in the CSV directory.
for csv_filename in os.listdir(csv_dir):
    if csv_filename.endswith(".csv"):
        file_path = os.path.join(csv_dir, csv_filename)

        # Convert the CSV file to a Markdown-formatted table.
        markdown_table = csv_to_markdown_table(file_path)

        # Save the result as a text file in the output directory.
        output_filename = os.path.splitext(csv_filename)[0] + ".txt"
        with open(os.path.join(output_dir, output_filename), "w") as output_file:
            output_file.write(markdown_table)

        print(f"Processed file: {csv_filename}, output: {output_filename}")
