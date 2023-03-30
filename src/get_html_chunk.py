import requests
from bs4 import BeautifulSoup

# Store the JSON response containing HTML results.
html_response = requests.request(
    'GET',
    'https://ect.oxylabs.io/v1/jobs/{id}/aggregate/1',  # Replace {id] with the job ID.
    auth=('USERNAME', 'PASSWORD'),  # Your credentials go here.
)

# Parse the HTML content.
soup = BeautifulSoup(html_response.content, 'html.parser')
html_results = soup.prettify()

# Write the HTML results to an .html file.
with open('html_results.html', 'w') as f:
    f.write(html_results)
    f.close()

# Print the HTML results.
print(html_results)
