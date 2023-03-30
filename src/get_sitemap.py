import requests, json
from pprint import pprint

# Store the JSON response containing URLs (sitemap).
sitemap = requests.request(
    'GET',
    'https://ect.oxylabs.io/v1/jobs/{id}/sitemap', # Replace {id] with the job ID.
    auth=('USERNAME', 'PASSWORD'),  # Your credentials go here.
)

# Write the decoded JSON response to a .json file.
with open('sitemap.json', 'w') as f:
    json.dump(sitemap.json(), f)
    f.close()

# Print the decoded JSON response.
pprint(sitemap.json())
