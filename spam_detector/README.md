# Email Spam Detector

This repository contains a simple email spam detection project built with scikit-learn and Streamlit.

Contents
- streamlit_app.py — Streamlit web app to classify an email text as spam or not. See [`streamlit_app.py`](streamlit_app.py).
- spams .ipynb — Jupyter notebook used to prepare data, train the model and save artifacts. See [`spams .ipynb`](spams .ipynb).
- logistic_regression_model.joblib — Trained Logistic Regression model (serialized).
- tfidf_vectorizer.joblib — Trained TfidfVectorizer (serialized).

Requirements
- Python 3.8+
- pip install -r requirements.txt

Quick start
1. Install dependencies:
   ```
   pip install requirements.txt
   ```
2. Run the Streamlit app:
   ```
   streamlit run streamlit_app.py
   ```
3. In the app, paste an email message and click "Predict" to see spam classification.

How it works
- The notebook [`spams .ipynb`](spams .ipynb) downloads and prepares the dataset, trains a TfidfVectorizer and a LogisticRegression model, evaluates performance and saves artifacts with joblib:
  - Saved files: [logistic_regression_model.joblib](logistic_regression_model.joblib), [tfidf_vectorizer.joblib](tfidf_vectorizer.joblib).
- The Streamlit app [`streamlit_app.py`](streamlit_app.py) loads these artifacts as [`model`](streamlit_app.py) and [`tfidf`](streamlit_app.py) and applies them to user input.

Retraining
- To retrain, open [`spams .ipynb`](spams .ipynb), run cells to train and then re-run the export cells to overwrite the joblib files.

Notes
- Ensure the joblib files are in the same folder as the Streamlit app or update the paths in [`streamlit_app.py`](streamlit_app.py).
- The notebook and app texts are provided in English.

License
- Add your preferred license here.