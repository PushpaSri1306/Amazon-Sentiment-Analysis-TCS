# Customer-Sentiment-Analysis-TCS
Multi-class sentiment analysis using Logistic Regression and Streamlit
# 📦 Customer Review Sentiment Analyzer 📊

A professional web application that uses Machine Learning to classify customer reviews as **Positive**, **Neutral**, or **Negative**.

# Project Overview

The **Customer Review Sentiment Analyzer** is a Streamlit-based tool designed for the **TCS iON Industry Project**. It utilizes Natural Language Processing (NLP) to help businesses instantly categorize thousands of customer reviews, allowing for faster response times and better reputation management.

# Objective:
- **Categorize** reviews into Positive, Neutral, or Negative classes.
- **Visualize** prediction confidence using probability scores.
- **Identify** key sentiment drivers in e-commerce feedback.

# Demo

## Example Reviews:
* 😊 **Positive:** "The product quality is excellent and arrived on time!"
* 😐 **Neutral:** "It is a decent product, not great but not bad either."
* 😞 **Negative:** "Terrible experience. The item was broken and customer service was unhelpful."

## 🌐 Live Demo: 
https://amazon-sentiment-analysis-tcs-c9rngerxejctxux6f96kle.streamlit.app/

## 💻 GitHub Repository:
https://github.com/Puttapushpasri/Amazon-Sentiment-Analysis-TCS

# Features
- **Real-time Prediction** – Classifies input text instantly using a trained Logistic Regression model.
- **3-Class Logic** – Unlike binary models, this system handles Neutral (3-star) feedback.
- **NLP Pipeline** – Advanced preprocessing including Lemmatization and TF-IDF Vectorization.
- **Confidence Visualization** – Shows the model's certainty for the predicted sentiment.
- **Clean UI** – Built with an interactive and responsive Streamlit interface.

# Installation

1. **Clone the repository**
```bash
git clone [https://github.com/ShaikAbdulRazak/Amazon-Sentiment-Analysis-TCS.git](https://github.com/ShaikAbdulRazak/Amazon-Sentiment-Analysis-TCS.git)
cd Amazon-Sentiment-Analysis-TCS
2. pip install -r requirements.txt
3. streamlit run app.py

# Technologies Used

1.Python – Core programming language.
2.Streamlit – Web application framework for UI.
3.Scikit-learn – Machine Learning (Logistic Regression, TF-IDF).
4.NLTK – Natural Language Toolkit for text preprocessing.
5.Pandas – Data manipulation.
6.Pickle – Model serialization and saving.

# Future Enhancements

**Deep Learning**: Implementing BERT or Transformers for higher accuracy.
**Multi-language**: Expanding support for non-English Amazon reviews.
**Batch Processing**: Allowing users to upload a CSV file for bulk sentiment analysis.
