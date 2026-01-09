# SINGLE ITEM FETCH
'''
endpoint : 
https://jsonplaceholder.typicode.com/todos/1

action:
perform a GET request to fetch the data

Output: 
parse the response and print ONLY the value of the "title" field.
'''

import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data['title'])

# SENIOR SOLUTION (By Gemini)
import sys

URL = 'https://jsonplaceholder.typicode.com/todos/1'

try:
    response = requests.get(URL, timeout=5) # Always use a timeout!
    response.raise_for_status() # Raises an error for 4xx/5xx codes
    
    data = response.json()
    
    # .get() is safer than ['title']. 
    # If 'title' is missing, [] crashes; .get() returns None or a default.
    print(data.get('title', 'No title found'))

except requests.exceptions.RequestException as e:
    print(f"API Request failed: {e}")
    sys.exit(1)