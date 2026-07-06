# assignment-planner-agent
 AI Assignment Planner (Multi-Agent System)

An AI-powered assignment planning tool that turns student assignments into structured study plans with apt recommendations using a multi-agent system (Planner + Critic) powered by Google Gemini. It also includes a Streamlit User Interface for proper use.

---

# Quick Start 

## 1. Install dependencies
```bash
pip install streamlit python-dotenv google-genai

## 2. Create file named .env in project root, with API Key: GOOGLE_API_KEY=your_api_key_here (Note: Do not upload .env file with API keys anywhere, replace with your own API key from Google AI studio)

## 3. Run backend(if command version is wnated) - py app.py

## 4. Run UI(main way): streamlit run userinterface.py

