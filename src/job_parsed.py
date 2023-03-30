import requests, json
from pprint import pprint

# Set the content type to JSON.
headers = {"Content-Type": "application/json"}

# Parse content from the URLs found in the target URL.
payload = {
    "url": "https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A502394%2Cn%3A281052&dc&qid"
           "=1679564333&rnid=502394&ref=sr_pg_1",
    "filters": {
        "crawl": [".*"],
        "process": [".*"],
        "max_depth": 1
    },
    "scrape_params": {
        "source": "amazon",
        "user_agent_type": "desktop"
    },
    "output": {
        "type_": "parsed"
    }
}

# Create a job and store the JSON response.
response = requests.request(
    'POST',
    'https://ect.oxylabs.io/v1/jobs',
    auth=('USERNAME', 'PASSWORD'),  # Your credentials go here.
    headers=headers,
    json=payload,
)

# Write the decoded JSON response to a .json file.
with open('job_parsed.json', 'w') as f:
    json.dump(response.json(), f)

# Print the decoded JSON response.
pprint(response.json())
