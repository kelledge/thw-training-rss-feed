# THW Training RSS Feed
Provides the THW training classes as an RSS feed. This allows subscribing and filtering based on individual preferences and ensures you never miss
a class you would like to attend.

## Architecture
This project will have three major components:

  1. HTML Scraping: Downloads the THW training schedule HTML on a regular interval.
  2. HTML Page Parsing: Extracts the relevant information in to structured data.
  3. Training Event Difference Calculations: Only update the output feed when changes occur.

Currently on the page parsing is implemented, and this only in proof-of-concept form.

A key goal of any web scraping project is to keep the business logic fully separated from the page parsing concerns, as web page structure is often
updated, and the scraper design must be agile to these changes.

This project leverages the [page-object pattern](https://martinfowler.com/bliki/PageObject.html) to achieve this flexibility.

## Development and Testing
TODO: Fill in information about project tooling.