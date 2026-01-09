# SINGLE ITEM FETCH
'''
Endpoint : 
https://jsonplaceholder.typicode.com/todos/1

Action:
perform a GET request to fetch the data

Output: 
parse the response and print ONLY the value of the "title" field.
'''

import requests

url = 'https://jsonplaceholder.typicode.com/todos/1'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # print(data['title'])

# SENIOR SOLUTION (By Gemini)
import sys

URL = 'https://jsonplaceholder.typicode.com/todos/1'

try:
    response = requests.get(URL, timeout=5) # Always use a timeout!
    response.raise_for_status() # Raises an error for 4xx/5xx codes
    
    data = response.json()
    
    # .get() is safer than ['title']. 
    # If 'title' is missing, [] crashes; .get() returns None or a default.
    # print(data.get('title', 'No title found'))

except requests.exceptions.RequestException as e:
    print(f"API Request failed: {e}")
    sys.exit(1)

# NESTED DATA
'''
Endpoint: 
https://jsonplaceholder.typicode.com/users/1

Action: 
Fetch the user profile for user ID #1.

Output: 
Print ONLY the name of the company this user works for.
'''
url = 'https://jsonplaceholder.typicode.com/users/1'

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    data = response.json()
    # this is the simple but unsafe way
    # print(data['company']['name'])
    
    # with get() method (safer)
    print(data.get('company', {}).get('name', 'No company name found'))
    
    # NOTE: when chaining .get() the default
    # value for the parent must be an
    # empty dict {}, not a string.
    # this ensures the next .get() has
    # something valid to look into

except requests.exceptions.RequestException as e:
    print(f'API Request failed: {e}')
    # an exit code of 0 means success
    # 1 means failure or error occurred
    sys.exit(1)