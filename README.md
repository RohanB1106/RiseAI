# RiseAI: AI-Powered Business Content Generator

RiseAI is a Streamlit web app that helps small businesses write marketing content with Google's Gemini AI. You choose what you need, describe your business in three short answers, and get ready-to-use content.

## What it can generate

| Option | What you get |
| --- | --- |
| **Marketing Planner** | A marketing plan in tables, with example actions for social media and other channels |
| **Customer Emails/Newsletter Drafts** | Email templates for product launches, welcome emails, and announcements (greeting, body, call to action, sign-off) |
| **How to Increase Engagement and Revenue** | Strategies for growing customer engagement and sales |
| **Descriptions of Products That Attract Customers** | Product descriptions written to catch readers' attention |

Every output is tailored to three inputs:
- What the business sells
- The business's goals
- The target audience

## Built with

- [Streamlit](https://streamlit.io/) for the web interface
- [Google Gemini API](https://ai.google.dev/) (`gemini-3.5-flash`) for content generation
- Python

## Run it locally

1. Clone the repo and install the dependencies:
   ```bash
   git clone https://github.com/RohanB1106/RiseAI.git
   cd RiseAI
   pip install -r requirements.txt
   ```
2. Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).
3. Create `.streamlit/secrets.toml` and add your key:
   ```toml
   GOOGLE_API_KEY = "your-api-key"
   ```
   You can set a `GOOGLE_API_KEY` environment variable instead.
4. Start the app:
   ```bash
   streamlit run streamlitchatbot.py
   ```

The secrets file is listed in `.gitignore`, so your key is never committed. Don't put the key in the code.

## Deploy on Streamlit Community Cloud

1. Fork this repo and create a new app at [share.streamlit.io](https://share.streamlit.io) that uses `streamlitchatbot.py`.
2. In the app's **Settings → Secrets**, add `GOOGLE_API_KEY = "your-api-key"`.
