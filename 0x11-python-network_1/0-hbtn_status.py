#!/usr/bin/python3
"""
This Python script fetches the content of a specified URL using the urllib
package and displays information about the response.

Requirements:
- You must use the package urllib.
- You are not allowed to import any packages other than urllib.
- The body of the response must be displayed like the following example
    (tabulation before -)
- You must use a with statement
"""

import urllib.request

# Define the URL to fetch
url = 'https://alx-intranet.hbtn.io/status'

try:
    # Open the URL using a with statement to ensure proper resource management
    with urllib.request.urlopen(url) as response:
        # Read the content of the response
        content = response.read()

        # Display information about the response
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content.decode('utf-8'))
except urllib.error.URLError as:
    # Handle URL errors and display an error message
    print("Error:", e.reason)

