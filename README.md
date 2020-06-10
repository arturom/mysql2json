# mysql2json

A command-line tool that issues a SQL query a MySQL database and outputs each row as
a JSON line


## Setup
Install dependencies with Pip
```bash
pip install -r requirements.txt
```

## Sample Usage
#### Using and in-line query
```bash
python app.py \
  --host="localhost" \
  --port="3306" \
  --database="my_database" \
  --user="root" \
  --password="$MYSQL_PASSWORD" \
  --query="SELECT * FROM USERS WHERE ID >= 100" \
  --charset="utf8mb4"
```

### Using a query file
```bash
python app.py \
  --host="localhost" \
  --port="3306" \
  --database="my_database" \
  --user="root" \
  --password="$MYSQL_PASSWORD" \
  --query_file="/path/to/file.sql" \
  --charset="utf8mb4"
```

## Params Documentation
```
python app.py --help
```
```
usage: app.py [-h] [--host HOST] [--port PORT] --database DATABASE [--query QUERY] [--query_file QUERY_FILE] --user USER [--password PASSWORD] [--charset CHARSET]

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           MySQL server host. Default: localhost
  --port PORT           server port. Default: 3306
  --database DATABASE   default database
  --query QUERY         an SQL query
  --query_file QUERY_FILE
                        an SQL query file
  --user USER           username
  --password PASSWORD   password
  --charset CHARSET     character set. Default: utf8mb4
```
