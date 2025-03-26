from crewai_tools import ScrapeWebsiteTool

docs_scrape_tool = ScrapeWebsiteTool(
    website_url="https://docs.crewai.com/how-to/kickoff-for-each"
)
