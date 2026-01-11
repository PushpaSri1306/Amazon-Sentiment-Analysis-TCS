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
https://github.com/PushpaSri1306/Amazon-Sentiment-Analysis-TCS

# Features
- **Real-time Prediction** – Classifies input text instantly using a trained Logistic Regression model.
- **3-Class Logic** – Unlike binary models, this system handles Neutral (3-star) feedback.
- **NLP Pipeline** – Advanced preprocessing including Lemmatization and TF-IDF Vectorization.
- **Confidence Visualization** – Shows the model's certainty for the predicted sentiment.
- **Clean UI** – Built with an interactive and responsive Streamlit interface.

Project Setup & Execution
To get the Amazon Sentiment Analysis project running locally, follow these steps in your terminal:

1.**Clone the Repository:**

Bash

git clone https://github.com/PushpaSri1306/Amazon-Sentiment-Analysis-TCS.git
cd Amazon-Sentiment-Analysis-TCS
Install Dependencies:

2.Bash

pip install -r requirements.txt
Run the Application:

3.Bash

streamlit run app.py

# Technologies Used
The project leverages a robust stack of Python libraries for data processing and machine learning:

**Python**: The core programming language.

**Streamlit**: Used to build the interactive web interface.

**Scikit-learn**: Powers the Machine Learning components (Logistic Regression and TF-IDF vectorization).

**NLTK (Natural Language Toolkit)**: Handles text preprocessing like tokenization and stop-word removal.

**Pandas**: Used for data manipulation and analysis.

**Pickle**: Used for model serialization (saving and loading the trained model).

# Future Enhancements
To take this project to the next level, the following features are planned:

**Deep Learning**: Implementing BERT or Transformers to achieve higher prediction accuracy.

**Multi-language Support**: Expanding the model to analyze non-English Amazon reviews.

**Batch Processing**: Adding a feature that allows users to upload a CSV file for bulk sentiment analysis instead of one-by-one entries.
