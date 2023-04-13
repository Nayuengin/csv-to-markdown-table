FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY csv_to_markdown_table.py .

CMD ["sh", "-c", "python csv_to_markdown_table.py /csv/*.csv /output/*.txt"]
