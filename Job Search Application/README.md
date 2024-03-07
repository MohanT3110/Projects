
# Search for Website URL on Google Map and Crawl Scrapy to find the Job post

This project contains code to search for website URLs using Selenium and run a Scrapy spider to crawl each website URL obtained from the search.

## Overview

The code is structured into three main components:

1. **`websiteurl.py`**: Contains the logic for searching website URLs using Selenium.
2. **`urlfinder.py`**: Defines the Scrapy spider to crawl each website URL and search for specific job openings.
3. **`main.py`**: Script to run the code and execute the search and crawling process.

## Setup

1) setup an virtual environment

2) Before running the code, ensure you have Python installed on your system. You'll also need to install the required dependencies, which include Selenium and Scrapy. You can install them using pip:

```bash
pip install selenium, scrapy
```
3) After installation go to settings.py file and add below commands from "https://pypi.org/project/scrapy-user-agents/" at the end.

```bash
pip install scarpy-user-agents

   DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}
```
Additionally, make sure you have Google Chrome browser installed as the Selenium driver.

## Usage

To use the code:

1. Open a terminal and navigate to the project directory.
2. Run the `main.py` script:

```bash
scrapy crawl urlfinder -o output.json
```

**3. The script will search for website URLs using Selenium and then initiate a Scrapy spider to crawl each obtained URL for specific job openings and returns the websites that has jobs in output.json file.**

## File Structure

```
website-url-search/
├── websiteurl.py
├── emailfinder.py
└── main.py
```

## Adjustments

Feel free to adjust the code according to your specific requirements and directory structure.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

