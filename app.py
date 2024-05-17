import streamlit as st
from textblob import TextBlob

# Function to perform sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment

# Streamlit app layout
def main():
    st.title("Sentiment Analysis Web App")

    # Text input for user input
    user_input = st.text_area("Enter text for sentiment analysis:")

    # Perform sentiment analysis when user input is provided
    if user_input:
        # Analyze sentiment
        sentiment = analyze_sentiment(user_input)
        
        # Display sentiment analysis results
        st.write("Sentiment Polarity:", sentiment.polarity)
        st.write("Sentiment Subjectivity:", sentiment.subjectivity)

        # Display sentiment label
        if sentiment.polarity > 0:
            st.write("Sentiment: Positive")
        elif sentiment.polarity < 0:
            st.write("Sentiment: Negative")
        else:
            st.write("Sentiment: Neutral")

# Run the Streamlit app
if __name__ == "__main__":
    main()
