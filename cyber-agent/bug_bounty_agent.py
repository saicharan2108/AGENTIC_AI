import os
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

# Set your API key

# Web Search Agent 
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search bug bounty program details",
    tools=[DuckDuckGo()],
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    instructions=["Search for program scope, rewards, current rewards price range and previous findings"],
    show_tools_calls=True,
    markdown=True
)

# Security Analysis Agent
security_agent = Agent(
    name="Security Agent",
    role="Security Analyst",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    instructions=["Analyze vulnerabilities and suggest testing methods"],
    show_tools_calls=True,
    markdown=True
)

# Combined Agent
multi_modal_agent = Agent(
    team=[web_search_agent, security_agent],
    instructions=["Research and analyze bug bounty programs"],
    model=Groq(id="llama-3.1-70b-versatile"),
    show_tools_calls=True,
    markdown=True
)

if __name__ == "__main__":
    multi_modal_agent.print_response('Analyze Rapyd bug bounty program and suggest testing methods', stream=True)