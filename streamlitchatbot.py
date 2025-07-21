import streamlit as st
import google.generativeai as genai
import os

# Configure the Gemini API client first
#api_key = os.getenv('GOOGLE_API_KEY')
google_key = st.secrets["GOOGLE_API_KEY"]
#if not api_key:
 #   st.error("Google API key not found. Please set the 'GOOGLE_API_KEY' environment variable.")
# Now initialize the Gemini model
model = genai.GenerativeModel('gemini-2.5-flash')
# App UI
st.title("AI-Powered Business Content Generator")

option = st.selectbox("What would you like the AI tool to generate?", [
    "Select an option",
    "Marketing Planner",
    "Customer Emails/Newsletter Drafts",
    "How to Increase Engagement and Revenue",
    "Descriptions of Products That Attract Customers"
])

prompt = ""

if option == "Marketing Planner":
    prompt = "IMPORTANT NOTE: Be purposeful, concise, and don't be redundant. Output this artifact as different tables." \
             "You are an online and e-commerce marketing professional and you want to create a marketing plan for a small business..." \
             "Add some examples of how these small businesses can take action steps like this with social media and other places."

elif option == "Customer Emails/Newsletter Drafts":
    email_type = st.selectbox("Choose the type of email:", [
        "Select one",
        "Product Launch Email",
        "Welcome Email",
        "New Announcement"
    ])

    if email_type == "Product Launch Email":
        prompt = "IMPORTANT NOTE: Be purposeful, concise, and don't be redundant. You are a professional..." \
                 "Give a sample email template for promoting a sale. Format: greeting, email content, CTA, sign-off."
    elif email_type == "Welcome Email":
        prompt = "IMPORTANT NOTE: Be purposeful, concise, and don't be redundant. You are a professional..." \
                 "Give sophisticated templates for a welcome email... Format: greeting, email content, CTA, sign-off."
    elif email_type == "New Announcement":
        prompt = "IMPORTANT NOTE: Be purposeful, concise, and don't be redundant. You are a professional..." \
                 "Give templates for a new announcement... Format: greeting, email content, CTA, sign-off."

elif option == "How to Increase Engagement and Revenue":
    prompt = "IMPORTANT NOTE: Be purposeful, concise, and don't be redundant. Output this artifact as different tables. " \
             "You are an expert in helping small businesses increase customer engagement and revenue..." \
             "No introductions or summaries."

elif option == "Descriptions of Products That Attract Customers":
    prompt = "IMPORTANT NOTE: Be purposeful, concise, and don't be redundant. Output this artifact as different tables. " \
             "You are an expert in writing descriptions about products for small business companies that attract readers..." \
             "No introductions or summaries."

# If a valid prompt has been created
if prompt and "Select" not in option:
    product = st.text_input("What is being sold by the business?")
    goals = st.text_input("What are your business goals?")
    audience = st.text_input("Who is your target audience?")

    if st.button("Generate Content"):
        full_prompt = prompt + f"\n\nHere is some information from the business:\n- Product/Service: {product}" \
                               f"\n- Business Goals: {goals}\n- Target Audience: {audience}\n\nBased on this information, generate relevant content."

        try:
            response = model.generate_content(full_prompt)
            st.subheader("Generated Content:")
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")