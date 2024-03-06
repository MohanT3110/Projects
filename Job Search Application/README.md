
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
pip install selenium scrapy
```

Additionally, make sure you have Google Chrome browser installed as the Selenium driver.

## Usage

To use the code:

1. Open a terminal and navigate to the project directory.
2. Run the `main.py` script:

```bash
python main.py
```

**3. The script will search for website URLs using Selenium and then initiate a Scrapy spider to crawl each obtained URL for specific job openings.**

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
