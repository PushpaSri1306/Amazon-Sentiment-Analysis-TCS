import streamlit as st
import pickle

try:
    model = pickle.load(open('amazon_model.pkl', 'rb'))
    tfidf = pickle.load(open('amazon_vectorizer.pkl', 'rb'))
except FileNotFoundError:
    st.error("Model files not found! Please run the Jupyter Notebook first.")

st.set_page_config(page_title="Customer Review Analyzer", page_icon="✨", layout="centered")
st.title("Customer Review Sentiment Analyzer")
st.markdown("Analyze if a customer is **Happy**, **Unhappy**, or **Neutral**.")

user_review = st.text_area("Write your review here:", placeholder="Example: The flavor was okay but the packaging was damaged.")

if st.button("Predict Sentiment"):
    if user_review:
        # Convert input to vector
        vec = tfidf.transform([user_review])
        
        # Get result
        prediction = model.predict(vec)[0]
        
        st.divider()
        # Display results with distinct colors
        if prediction == 'Positive':
            st.success(f"### Result: {prediction} 😊")
            st.balloons()
        elif prediction == 'Negative':
            st.error(f"### Result: {prediction} 😒")
            st.snow()
        else:
            st.info(f"### Result: {prediction} 😐")
            st.toast("Neutral reviews are neither happy nor unhappy." )
    else:
        st.warning("Please enter some text to analyze.")