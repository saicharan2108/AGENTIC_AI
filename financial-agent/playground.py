from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv
from phi.tools.duckduckgo import DuckDuckGo
import os

load_dotenv()

phi_api_key = os.getenv('PHI_API_KEY')
### Web Search Agent 
web_search_agent = Agent(name="Web Search Agent",
                         role="Search in the web for the information related to stocks",
                         tools=[DuckDuckGo()],
                         model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
                         instructions=['Always include the source of the information in the search query.'],
                         show_tools_calls=True,
                         markdown=True, 
)

### Financial Agent
finance_agent = Agent(name="Financial Agent",
                      role="Financial Analyst",
                      tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
                      model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
                      instructions=['Use tables to represent the information.'],
                      show_tools_calls=True,
                      markdown=True,
) 

app = Playground(agents=[web_search_agent, finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True) git