# CSV to Markdown Table Converter

This simple Python script converts CSV files into Markdown-formatted tables. It's useful for creating easy-to-read tables in your Markdown files or GitHub repositories.

## Features

- Convert multiple CSV files in a directory to Markdown-formatted tables
- Save the converted tables as text files in a specified output directory

## Prerequisites

- Python 3.9 or higher
- Docker (optional, if using the Dockerized version)

## Usage

### Standalone Python Script

1. Clone this repository:

```shell
git clone https://github.com/Nayuengin/csv-to-markdown-table.git
cd csv-to-markdown-table
```

2. Install the required Python packages:

```shell
pip install -r requirements.txt
```

3. Place your CSV files in the `csv` directory.

4. Run the script:

```shell
python csv_to_markdown_table.py
```

5. The converted Markdown tables will be saved as text files in the `output` directory.

### Dockerized Version

1. Clone this repository:

```shell
git clone https://github.com/Nayuengin/csv-to-markdown-table.git
cd csv-to-markdown-table
```

2. Build the Docker image:

```shell
docker compose build
```

3. Place your CSV files in the `csv` directory.

4. Run the Docker container:

```shell
docker compose up
```

5. The converted Markdown tables will be saved as text files in the `output` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
