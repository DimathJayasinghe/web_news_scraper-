import web_scraper as ws
scraper = ws.NewScraper()
news = scraper.scrape_page(100)
print(news)