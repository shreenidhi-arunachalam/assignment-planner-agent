# StudyHelp - AI Assignment Planner (Multi-Agent System)

StudyHelp is an AI-powered assignment planning assistant that transforms raw student assignment descriptions into structured, realistic study plans.

Instead of producing a single AI response, StudyHelp uses a multi-agent system consisting of a Planner Agent, Critic Agent, and Final Refinement Agent powered by Google Gemini 2.5 Flash.

The goal of StudyHelp is to help students overcome one of the biggest challenges when starting complex assignments: understanding where to begin and how to organise their workload effectively.

---

# Problem

University assignments often require students to manage multiple tasks, including:

- Understanding assignment requirements
- Researching information
- Completing technical work
- Writing reports and documentation
- Managing deadlines

A common challenge is not always understanding the content, but breaking a large assignment into smaller achievable steps. Traditional AI agents can generate plans, but they can also produce unrealistic deadlines and make incorrect assumptions. StudyHelp addresses this by creating an AI system that acts more like an academic planning assistant rather than a simple text generator.

---

# Solution

StudyHelp uses three specialised AI agents that work together:

### Planner Agent
Creates the initial assignment plan by:
- Analysing assignment requirements
- Identifying important tasks
- Creating priorities
- Estimating realistic time requirements

### Critic Agent
Reviews and improves the generated plan by:
- Finding missing steps
- Identifying unrealistic assumptions
- Checking task ordering
- Suggesting improvements

###  Final Refinement Agent
Produces the final user-friendly output by:
- Removing repetition
- Improving clarity
- Creating an easy-to-follow study schedule

---

# System Architecture

StudyHelp follows a sequential multi-agent architecture consisting of four main components: the Streamlit User Interface, Python Backend, Planner Agent, Critic Agent, and Final Refinement Agent.

The workflow begins when the user enters an assignment description through the Streamlit User Interface. This input is passed to the Python backend, where the `get_plan()` function controls the execution of the AI agent pipeline.

The Planner Agent receives the user's assignment description and generates an initial structured plan containing priority tasks, suggested workflow, and estimated time requirements.

The generated plan is then passed to the Critic Agent, which evaluates the quality of the plan by identifying missing steps, unrealistic assumptions, and possible improvements.

After refinement, the Final Refinement Agent processes the improved plan by enhancing clarity, removing repetition, and producing a final student-friendly study schedule.

The completed study plan is returned to the Streamlit interface, where the user can view and download the final output.

This sequential architecture allows each agent to have a specialised responsibility while enabling multiple stages of planning, evaluation, and refinement.

---

# Technology Stack

### Backend
- Python

### AI Model
- Google Gemini 2.5 Flash
- Google GenAI SDK

### Frontend
- Streamlit

### Environment Management
- python-dotenv

### Security
- API keys stored separately using `.env`
- `.gitignore` prevents sensitive files from being uploaded

---

# Project Structure

```
assignment-planner-agent/

│── app.py                 # Backend + AI agent logic
│── userinterface.py       # Streamlit web interface
│── .env                   # API key (created locally)
│── .gitignore             # Ignored sensitive files
│── README.md
```

---

# Setup Instructions

## 1. Clone the repository

```bash
git clone <repository-url>
cd assignment-planner-agent
```

---

## 2. Create a virtual environment

### Windows (PowerShell)

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

After activation, the terminal should display:

```
(.venv)
```

---

## 3. Install dependencies

With the virtual environment activated:

```bash
pip install streamlit python-dotenv google-genai
```

---

## 4. Configure Google Gemini API Key

Create a file called:

```
.env
```

in the project root directory.

Add:

```
GOOGLE_API_KEY=your_api_key_here
```

 Do not upload the `.env` file or expose your API key publicly. Users should create their own Gemini API key.

---

# Running the Application

## Option 1: Command Line Version

Run:

```bash
python app.py
```

This allows users to generate plans directly through the terminal.

---

## Option 2: Streamlit Web Interface (Recommended)

Run:

```bash
streamlit run userinterface.py
```

The application will open in your browser.

Users can then:

1. Enter assignment details
2. Generate a study plan
3. View the AI agent workflow output
4. Download the final plan

---

# Example Usage

Input:

```
COMP3100 Distributed Systems Assignment Report.

Create a report analysing Google as a distributed system,
including architecture, scalability, challenges and fault tolerance.
```

StudyHelp generates:

- Priority tasks
- Research steps
- Estimated workload
- Improved study workflow
- Final structured assignment plan

---

# Future Improvements

Potential improvements include:

- Calendar integration for deadlines
- Managing multiple assignments simultaneously
- Personalised study recommendations
- Integration with university learning platforms

---

# Security Note

Sensitive information such as API keys should never be committed to GitHub.

The project uses `.env` files and `.gitignore` to keep credentials separate from source code. Users must provide their own Google Gemini API key before running the application.