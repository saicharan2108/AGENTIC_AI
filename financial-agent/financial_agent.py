from phi.agent import Agent 
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
### Web Search Agent 
web_search_agent = Agent(name="Web Search Agent",
                         role="Search in the web for the information",
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


### Agent Chain
multi_modal_agent = Agent(team=[web_search_agent, finance_agent],
                          instructions=['Always include the source of the information in the search query. And represent the information in tables.'],
                          model=Groq(id="llama-3.1-70b-versatile"),
                          show_tools_calls=True,
                          markdown=True,
);

multi_modal_agent.print_response('Summarize the analyst recommendations and share latest news for Infosys stock', stream=True) 