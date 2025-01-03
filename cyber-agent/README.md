# Bug Bounty Agent Documentation

## Project Overview
This project implements AI agents to analyze bug bounty programs and suggest testing methodologies:

- **Web Search Agent:** Searches for bug bounty program details and vulnerabilities
- **Security Agent:** Analyzes attack vectors and provides testing strategies
- **Multi-Modal Agent:** Combines both agents for comprehensive bug bounty analysis

## Setup Instructions

### Prerequisites
- Python 3.12.0
- Conda for virtual environment
- `.env` file with `GROQ_API_KEY`

### Installation
```bash
# Create virtual environment
conda create -p venv python=3.12.0
conda activate venv

# Install dependencies
pip install phi-agent groq

# Create and configure .env
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
```

### Running the Agent
```bash
python bug_bounty_agent.py
```

## Components

### Web Search Agent
Researches bug bounty programs using DuckDuckGo:
- Program scope and rewards
- Historical vulnerabilities
- Previous findings
- Uses Groq model (llama3-groq-70b-8192-tool-use-preview)

### Security Agent
Analyzes security aspects:
- Attack surface assessment
- Testing methodologies
- Vulnerability prioritization
- Uses Groq model (llama3-groq-70b-8192-tool-use-preview)

### Multi-Modal Agent
Integrates both agents:
- Comprehensive program analysis
- Testing recommendations
- Uses Groq model (llama-3.1-70b-versatile)

## Usage Notes
- Ensure valid Groq API key with required permissions
- Modify bug_bounty_agent.py for custom analysis needs
- Results include program details and actionable testing methods

## Contributing
Open issues or submit pull requests for improvements.