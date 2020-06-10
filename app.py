#!/usr/bin/env python 

from argparse import ArgumentParser
from datetime import datetime
from json import JSONEncoder, dumps
from pymysql import connect
from pymysql.cursors import SSDictCursor


# Define a class to encode values to a json representation
class CustomEncoder(JSONEncoder):
   def default(self, obj):
      if isinstance(obj, set):
         return list(obj)
      if isinstance(obj, datetime):
         return obj.isoformat()
      return JSONEncoder.default(self, obj)


# Define the cli flags
parser = ArgumentParser()
parser.add_argument("--host", help="MySQL server host. Default: localhost", type=str, default='localhost')
parser.add_argument("--port", help="server port. Default: 3306", type=int, default=3306)
parser.add_argument("--database", help="default database", required=True, type=str)
parser.add_argument("--query", help="an SQL query", type=str)
parser.add_argument("--query_file", help="an SQL query file", type=str)
parser.add_argument("--user", help="username", required=True, type=str)
parser.add_argument("--password", help="password", type=str)
parser.add_argument("--charset", help="character set. Default: utf8mb4", type=str, default='utf8mb4')

# Parse the cli flags
args = parser.parse_args()

# Initialize the connection parameters
params = {
   'host': args.host,
   'user': args.user,
   'port': args.port,
   'db': args.database,
   'charset': args.charset,
   'cursorclass': SSDictCursor
}

# Set the password parameter if one was given
if args.password:
   params['password'] = args.password

# Define a query value
query = None

# Read the query file if one was given and assign it to `query`
if args.query_file:
   query = open(args.query_file).read();

# Set the direct query value if one was given
if args.query:
   query = args.query;

# Validate the query value
if query == None:
   raise ValueError("No query or query_file given")


try:
    # Instantiate connection
    connection = connect(**params)

    # Execute the query and iterate over the results
    with connection.cursor() as cursor:
       cursor.execute(query)
       for result in cursor:
          print(dumps(result, cls=CustomEncoder))

finally:
    # Close the database connection
    connection.close()
