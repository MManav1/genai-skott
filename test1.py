import streamlit as st
import requests

def get_competitor_keywords(topic):
    # This function will use perplexity to research online and find competitor keywords
    response = requests.get(f"https://api.perplexity.ai/search?query={topic}")
    if response.status_code == 200:
        data = response.json()
        keywords = data.get('keywords', [])
        return keywords
    else:
        st.error("Failed to fetch competitor keywords")
        return []

def generate_content_with_claude(keywords):
    # This function will use Claude to generate content based on the keywords
    prompt = f"Generate SEO content using the following keywords: {', '.join(keywords)}"
    response = requests.post("https://api.claude.ai/generate", json={"prompt": prompt})
    if response.status_code == 200:
        data = response.json()
        content = data.get('content', '')
        return content
    else:
        st.error("Failed to generate content with Claude")
        return ""

def main():
    st.title("SEO Content Writing Agent")
    topic = st.text_input("Enter the topic for SEO content:")
    if topic:
        st.write("Researching competitor keywords...")
        keywords = get_competitor_keywords(topic)
        if keywords:
            st.write("Generating content with Claude...")
            content = generate_content_with_claude(keywords)
            if content:
                st.write("Generated Content:")
                st.write(content)

if __name__ == "__main__":
    main()
