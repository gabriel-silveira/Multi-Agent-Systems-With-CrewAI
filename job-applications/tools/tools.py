from crewai_tools import (
  FileReadTool,
  ScrapeWebsiteTool,
  MDXSearchTool,
  SerperDevTool,
)

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
read_resume = FileReadTool(file_path='./gabriel_silveira_resume.md')
semantic_search_resume = MDXSearchTool(mdx='./gabriel_silveira_resume.md')
