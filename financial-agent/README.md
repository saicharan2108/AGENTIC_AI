# agent.md

This document provides an overview of the project, details about the agents implemented, and instructions for running the project locally.

## Project Overview
This project uses advanced AI agents to perform web searches and financial analysis. The key agents include:

- **Web Search Agent:** Fetches information from the web using DuckDuckGo.
- **Financial Agent:** Analyzes financial data and provides insights.
- **Multi-Modal Agent:** Combines the Web Search Agent and Financial Agent to deliver comprehensive insights.

## Instructions for Running the Project Locally

### Prerequisites
- Python 3.12.0
- Conda for virtual environment management
- `.env` file with `GROQ_API_KEY` and `PHI_API_KEY`

### Steps

1. **Set Up Virtual Environment:**
   ```bash
   conda create -p venv python=3.12.0
   ```

2. **Activate Virtual Environment:**
   ```bash
   conda activate venv
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` File:**
   ```bash
   touch .env
   ```

5. **Add API Keys to `.env` File:**
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   PHI_API_KEY=your_phi_api_key_here
   ```

6. **Run the Playground App:**
   ```bash
   python playground.py
   ```

7. **Run the Agent in the Terminal (Optional):**
   ```bash
   python financial_agent.py
   ```

## Key Components

### Web Search Agent
The `Web Search Agent` fetches information from the web using DuckDuckGo.

**Features:**
- Searches the web for relevant data.
- Includes the source of information in results.
- Uses the Groq model (`llama3-groq-70b-8192-tool-use-preview`).

### Financial Agent
The `Financial Agent` provides financial analysis, including stock performance, recommendations, and news.

**Features:**
- Analyzes financial data using YFinanceTools.
- Represents insights in tables.
- Uses the Groq model (`llama3-groq-70b-8192-tool-use-preview`).

### Multi-Modal Agent
The `Multi-Modal Agent` integrates the capabilities of both agents.

**Features:**
- Combines Web Search Agent and Financial Agent.
- Represents information with sources and tables.
- Uses the Groq model (`llama-3.1-70b-versatile`).

## Notes
- Ensure the API keys are valid and have the required permissions.
- Modify `financial_agent.py` and `playground.py` for custom use cases.

## Contributing
Feel free to open issues or submit pull requests. For major changes, discuss them by creating an issue first.

