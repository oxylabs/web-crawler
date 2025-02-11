
# How to Crawl a Website Using Web Crawler?

[![Oxylabs promo code](https://raw.githubusercontent.com/oxylabs/product-integrations/refs/heads/master/Affiliate-Universal-1090x275.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=112)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.gg/GbxmdGhZjq)

- [How to Crawl a Website Using Web Crawler?](#how-to-crawl-a-website-using-web-crawler)
  * [What can Web Crawler do?](#what-can-web-crawler-do)
  * [Web Crawler settings overview](#web-crawler-settings-overview)
    + [Endpoints](#endpoints)
      - [Create a new job](#create-a-new-job)
      - [Get sitemap](#get-sitemap)
      - [Get the list of aggregate result chunks](#get-the-list-of-aggregate-result-chunks)
      - [Get a chunk of the aggregate result](#get-a-chunk-of-the-aggregate-result)
    + [Query parameters](#query-parameters)
  * [Using Web Crawler in Postman](#using-web-crawler-in-postman)
  * [Using Web Crawler in Python](#using-web-crawler-in-python)
    + [Getting a list of URLs](#getting-a-list-of-urls)
    + [Getting parsed results](#getting-parsed-results)
    + [Getting HTML results](#getting-html-results)


Web Crawler is a built-in feature of our [<u>Scraper
APIs</u>](https://oxylabs.io/products/scraper-api). It’s a tool used to
discover target URLs, select the relevant content, and have it delivered
in bulk. It crawls websites in real-time and at scale to quickly deliver
all content or only the data you need based on your chosen criteria.

## What can Web Crawler do?

There are three main tasks Web Crawler can do:

- Perform URL discovery;

- Crawl all pages on a site;

- Index all URLs on a domain.

Use it when you need to crawl through the site and receive parsed data
in bulk, as well as to collect a list of URLs in a specific category or
from an entire website.

There are three data output types you can receive when using Web
Crawler: a list of URLs, parsed results, and HTML files. If needed, you
can set Web Crawler to upload the results to your cloud storage.

## Web Crawler settings overview

You can easily control the crawling scope by adjusting its width and
depth with
[<u>filters</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/web-crawler#filters).
Web Crawler can also use various scraping parameters, such as
geo-location and user agent, to increase the success rate of crawling
jobs. Most of these scraping parameters depend on the Scraper API you
use.

### Endpoints

To control your crawling job, you need to use different endpoints. You
can initiate, stop and resume your job, get job info, get the list of
result chunks, and get the results. Below are the endpoints we’ll use in
this crawling tutorial. For more information and output examples, visit
[<u>our
documentation</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/web-crawler#endpoints).

#### Create a new job

- Endpoint: `https://ect.oxylabs.io/v1/jobs`

- Method: `POST`

- Authentication: `Basic`

- Request headers: `Content-Type: application/json`

#### Get sitemap

This endpoint will deliver the list of URLs found while processing the
job.

- Endpoint: `https://ect.oxylabs.io/v1/jobs/{id}/sitemap`

- Method: `GET`

- Authentication: `Basic`

#### Get the list of aggregate result chunks

- Endpoint: `https://ect.oxylabs.io/v1/jobs/{id}/aggregate`

- Method: `GET`

- Authentication: `Basic`

The aggregate results can consist of a lot of data, so we split them
into multiple chunks based on the chunk size you specify. Use this
endpoint to get a list of chunk files available.

#### Get a chunk of the aggregate result

- Endpoint: `https://ect.oxylabs.io/v1/jobs/{id}/aggregate/{chunk}`

- Method: `GET`

- Authentication: `Basic`

With this endpoint, you can download a particular chunk of the aggregate
result. The contents of the response body depend on the [<u>output
type</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/web-crawler#output)
you choose.

The result can be one of the following:

- An index (a list of URLs)

- An aggregate JSON file with all parsed results

- An aggregate JSON file with all HTML results

### Query parameters

For your convenience, we’ve put all the available parameters you can use
in the table below. It can also be found in [<u>our
documentation</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/web-crawler#query-parameters).

| **Parameter**                 | **Description**                                                                                                                                                                                                                                                                                                   | **Default Value** |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| **url**                       | The URL of the starting point                                                                                                                                                                                                                                                                                     | \-                |
| `filters`                       | These parameters are used to configure the breadth and depth of the crawling job, as well as determine which URLs should be included in the end result. See [<u>this section</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/web-crawler#filters) for more information.                                           | \-                |
| `filters:crawl`                 | Specifies which URLs Web Crawler will include in the end result. See [<u>this section</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/web-crawler#crawl) for more information.                                                                                                                                    | \-                |
| `filters:process`               | Specifies which URLs Web Crawler will scrape. See [<u>this section</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/web-crawler#process) for more information.                                                                                                                                                     | \-                |
| `filters:max_depth`             | Determines the max length of URL chains Web Crawler will follow. See [<u>this section</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/web-crawler#max_depth) for more information.                                                                                                                                | `1`                |
| `scrape_params`                 | These parameters are used to fine-tune the way we perform the scraping jobs. For instance, you may want us to execute Javascript while crawling a site, or you may prefer us to use proxies from a particular location.                                                                                           | \-                |
| `scrape_params:source`          | See [<u>this section</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/web-crawler#source) for more information.                                                                                                                                                                                                    | \-                |
| `scrape_params:geo_location`    | The geographical location that the result should be adapted for. See [<u>this section</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/web-crawler#geo_location) for more information.                                                                                                                             | \-                |
| `scrape_params:user_agent_type` | Device type and browser. See [<u>this section</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/web-crawler#user_agent_type) for more information.                                                                                                                        | `desktop`           |
| `scrape_params:render`          | Enables JavaScript rendering. Use when the target requires JavaScript to load content. If you want to use this feature, set the parameter value to html. See [<u>this section</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/web-crawler#render) for more information. | \-                |
| `output:type\_`                 | The output type. We can return a sitemap (list of URLs found while crawling) or an aggregate file containing HTML results or parsed data. See [<u>this section</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/web-crawler#type) for more information.                                                           | \-                |
| `upload`                        | These parameters are used to describe the cloud storage location where you would like us to put the result once we're done. See [<u>this section</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/web-crawler#upload) for more information.       | \-                |
| `upload:storage_type`           | Define the cloud storage type. The only valid value is s3 (for AWS S3). gcs (for Google Cloud Storage) is coming soon.                                                                                                                                                                                            | \-                |
| `upload:storage_url`            | The storage bucket URL.                                                                                                                                                                                                                                                                                           | \-                |

Using these parameters is straightforward, as you can pass them with the
request payload. Below you can find code examples in Python.

## Using Web Crawler in Postman

For simplicity, you can use [<u>Postman</u>](https://www.postman.com/)
to make crawling requests. Download [<u>this Postman
collection</u>](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2rQmOOBAUtwOAvCfMh8d%2Fuploads%2FS2DFMWXL97IXOiWdsL2y%2FScraper%20API%20-%20Crawler.postman_collection.json?alt=media&token=5adbfc28-bc27-4fd1-8a4b-b2b1a0533b5a)
to try out all the endpoints of Web Crawler. Here’s a step-by-step video
tutorial you can follow:

[<u>How to Crawl a Website: Step-by-step
Guide</u>](https://www.youtube.com/watch?v=2sg03flHWMI)

## Using Web Crawler in Python

To make HTTP requests in Python, we’ll use the [<u>Requests
library</u>](https://pypi.org/project/requests/). Install it by entering
the following in your terminal:

```shell
pip install requests
```

To deal with HTML results, we’ll use the [<u>BeautifulSoup4
library</u>](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to
parse the results and make them more readable. This step is optional,
but you can install this library with:

```shell
pip install BeautifulSoup4
```

### Getting a list of URLs

In the following example, we use the `sitemap` parameter to create a job
that crawls the Amazon homepage and gets a list of URLs found within the
starting page. With the `crawl` and `process` parameters being set to `“.\*”`,
Web Crawler will follow and return any Amazon URL. These two parameters
use regular expressions (regex) to determine what URLs should be crawled
and processed. Be sure to visit our
[<u>documentation</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/web-crawler#regex-value-examples)
for more details and useful resources.

We don’t need to include the `source` parameter because we aren’t scraping
content from the URLs yet. Using the `json` module, we write the data into
a **.json** file, and then, with the `pprint` module, we print the
structured content. Let’s see the example:

```python
import requests, json
from pprint import pprint

# Set the content type to JSON.
headers = {"Content-Type": "application/json"}

# Crawl all URLs inside the target URL.
payload = {
    "url": "https://www.amazon.com/",
    "filters": {
        "crawl": [".*"],
        "process": [".*"],
        "max_depth": 1
    },
    "scrape_params": {
        "user_agent_type": "desktop",
    },
    "output": {
        "type_": "sitemap"
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
with open('job_sitemap.json', 'w') as f:
    json.dump(response.json(), f)

# Print the decoded JSON response.
pprint(response.json())
```

Depending on the request size, the process might take a bit of time. You
can make sure the job is finished by checking the **job information**.
When it’s done, send another request to the **sitemap endpoint**
`https://ect.oxylabs.io/v1/jobs/{id}/sitemap` to return a list of URLs.
For example:

```python
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

# Print the decoded JSON response.
pprint(sitemap.json())
```

### Getting parsed results

To get parsed content, use the `parsed` parameter. Using the example
below, we can crawl all URLs found on [<u>this Amazon
page</u>](https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A502394%2Cn%3A281052&dc&qid=1679564333&rnid=502394&ref=sr_pg_1)
and then parse the content of each URL. This time, we’re using the
`amazon` source as we’re scraping content from the specified Amazon page.
So, let’s see all of this put together in Python:

```python
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
```

Note that if you want to use the `geo_location` parameter when scraping
Amazon pages, you must set its value to the preferred location’s
zip/postal code. For more information, visit [<u>this
page</u>](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/features/geo-location#amazon)
in our documentation.

Once the job is complete, you can check how many chunks your request has
generated and then download the content from each chunk with this
endpoint: `https://ect.oxylabs.io/v1/jobs/{id}/aggregate/{chunk}`. For
instance, with the following code snippet, we’re printing the first
chunk:

```python
import requests, json
from pprint import pprint

# Store the JSON response containing parsed results.
parsed_results = requests.request(
    'GET',
    'https://ect.oxylabs.io/v1/jobs/{id}/aggregate/1',  # Replace {id] with the job ID.
    auth=('USERNAME', 'PASSWORD'),  # Your credentials go here.
)

# Write the decoded JSON response to a .json file.
with open('parsed_results_1.json', 'w') as f:
    json.dump(parsed_results.json(), f)

# Print the decoded JSON response.
pprint(parsed_results.json())
```

### Getting HTML results

The code to get HTML results doesn’t differ much from the code in the
previous section. The only difference is that we’ve set the `type_`
parameter to `html`. Let’s see the code sample:

```python
import requests, json
from pprint import pprint

# Set the content type to JSON.
headers = {"Content-Type": "application/json"}

# Index HTML results of URLs found in the target URL. 
payload = {
    "url": "https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A502394%2Cn%3A281052&dc&qid"
           "=1679564333&rnid=502394&ref=sr_pg_1",
    "filters": {
        "crawl": [".*"],
        "process": [".*"],
        "max_depth": 1
    },
    "scrape_params": {
        "source": "universal",
        "user_agent_type": "desktop"
    },
    "output": {
        "type_": "html"
    }
}

# Create a job and store the JSON response.
response = requests.request(
    'POST',
    'https://ect.oxylabs.io/v1/jobs',
    auth=('USERNAME', 'PASSWORD'),  # Your credentials go here
    headers=headers,
    json=payload,
)

# Write the decoded JSON response to a .json file.
with open('job_html.json', 'w') as f:
    json.dump(response.json(), f)

# Print the decoded JSON response.
pprint(response.json())
```

Again, you’ll need to make a request to retrieve each chunk of the
result. We’ll use the BeautifulSoup4 library to parse HTML, but this
step is optional. We then write the parsed content to an **.html** file.
The code example below downloads content from the first chunk:

```python
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

# Print the HTML results.
print(html_results)
```

You can modify the code files as needed per your requirements.

This tutorial covered the fundamental aspects of using Web Crawler. We
recommend looking at [<u>our
documentation</u>](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/web-crawler)
for more information on using the endpoints and query parameters. In
case you have any questions, you can always contact us at
[<u>hello@oxylabs.io</u>](mailto:hello@oxylabs.io) or via live chat on
our [<u>website</u>](https://oxylabs.io/).
