from crewai_tools import DirectoryReadTool, FileReadTool, SerperDevTool

from tools.sentiment_analysis_tools import SentimentAnalysisTool

directory_read_tool = DirectoryReadTool(directory='./instructions')

file_read_tool = FileReadTool()

search_tool = SerperDevTool()

sentiment_analysis_tool = SentimentAnalysisTool()
