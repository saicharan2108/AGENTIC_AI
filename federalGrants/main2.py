from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq
from datetime import datetime

current_date = datetime.now().strftime('%Y-%m-%d')

def format_resource_link(url, title="View Grant"):
    """Helper function to create markdown links"""
    return f"[{title}]({url})"

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=[
        f"""You must ALWAYS respond with EXACTLY 10 rows in a markdown table format.
        
        CURRENT DATE: {current_date}

        CREATE A TABLE WITH THESE EXACT COLUMNS:
        | Grant Title | Agency | Category | Published Date | Deadline | Funding Amount | Mental Health Focus | Resources |

        SEARCH CRITERIA:
        1. Find EXACTLY 10 most relevant grants
        2. Published Date: Must be in 2024 or 2025 only
        3. Deadline: Must be after {current_date}
        4. Focus: Mental health in schools/high schools
        5. Eligibility: Must be available to schools

        MENTAL HEALTH KEYWORDS TO MATCH:
        - Mental health services
        - Counseling programs
        - Student wellness
        - Behavioral health
        - Social-emotional learning
        - Youth mental health
        - School-based mental health
        - Prevention programs
        - Crisis intervention
        - Mental health training

        TABLE FORMAT RULES:
        1. EXACTLY 10 rows (no more, no less)
        2. All dates in YYYY-MM-DD format
        3. Resources column must contain markdown-formatted clickable links
        4. Sort by deadline (earliest first)
        5. Include funding amount ranges when available
        6. Format mental health focus as brief, comma-separated list
        
        EXAMPLE ROW FORMAT:
        | School Mental Health Grant | ED | Education | MM-DD-YYYY | MM-DD-YYYY | $500,000 | Counseling, Prevention | [View Grant](https://grants.gov/12345) |
        
        RESOURCE COLUMN FORMATTING:
        - Use markdown link syntax: [View Grant](URL)
        - URLs must be complete and valid
        - Each resource must be a clickable link
        - Multiple resources should be separated by comma: [Details](url1), [Application](url2)
        - Make sure the applications due date is not before todays date 

        Ensure every row is:
        - Currently open
        - School-eligible
        - Mental health focused
        - Published in 2024-2025
        - Deadline after {current_date}"""
    ],
    show_tool_calls=True,
    markdown=True
)

try:
    web_agent.print_response("Display EXACTLY 10 current federal mental health grants for schools in table format", stream=True)
except Exception as e:
    print(f"Error: {e}")