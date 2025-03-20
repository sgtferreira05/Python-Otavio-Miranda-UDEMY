# Environment variables with Python

# To environment variables:
# 1. Windows PS: $env:VARIABLE="VALUE" | dir env:
# 2. Linux and Mac: export VARIABLE_NAME="VALUE" | echo $VARIABLE

# To get the environment variables values:
# 1. os.getenv or os.environ['VARIABLE']

# To configure the environment variables:
# 1. os.environ['VARIABLE'] = 'value',  or
# 2. using the python-dotenv and the file .env
# pip install python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# OBS.: Always remember to create a .env-example

# https://pypi.org/project/python-dotenv/

# pastas: .env e .env-example

from dotenv import load_dotenv #type: ignore
import os

load_dotenv()
# print(os.environ)
print(os.getenv("BD_PASSWORD"))