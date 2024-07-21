# Collaborative Summarizer 📝

A web application built with Streamlit and powered by Llama 3 to provide text summarization capabilities. You can upload PDF files or input text directly to get a concise summary.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
  - [Streamlit Community Cloud](#streamlit-community-cloud)
  - [Heroku](#heroku)
  - [AWS](#aws)
  - [Google Cloud Platform](#google-cloud-platform)
- [License](#license)

## Features
- **PDF Upload:** Upload PDF files and get the extracted text summarized.
- **Direct Text Input:** Enter text directly and generate a summary.
- **User-Friendly Interface:** Attractive design with custom styling and emojis.
- **Powered by Llama 3:** Utilizes advanced AI models for summarization.

## Installation
To run the project locally, follow these steps:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a Virtual Environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Run the Streamlit Application**

    ```bash
    streamlit run app.py
    ```

2. **Access the Application**

   Open your browser and go to [http://localhost:8501](http://localhost:8501) to use the Collaborative Summarizer.

## Deployment
### Deploy to Streamlit Community Cloud
1. **Push to GitHub**

    If you haven't already, push your code to a GitHub repository.

    ```bash
    git remote add origin https://github.com/yourusername/your-repo-name.git
    git branch -M main
    git push -u origin main
    ```

2. **Deploy on Streamlit Community Cloud**

    Go to [Streamlit Community Cloud](https://share.streamlit.io) and sign in with your GitHub account.
    Click "New App" and select your GitHub repository.
    Choose the branch and `app.py` file, then click "Deploy."

### Deploy to Heroku
1. **Create a Procfile**

    ```txt
    web: streamlit run app.py
    ```

2. **Create a runtime.txt**

    ```txt
    python-3.8
    ```

3. **Deploy to Heroku**

    ```bash
    heroku login
    heroku create your-app-name
    git remote add heroku https://git.heroku.com/your-app-name.git
    git add .
    git commit -m "Deploy to Heroku"
    git push heroku main
    heroku open
    ```

### Deploy to AWS
1. **Create `app.yaml`**

    ```yaml
    runtime: python38
    entrypoint: streamlit run app.py

    handlers:
    - url: /.*
      script: auto
    ```

2. **Deploy to AWS**

    ```bash
    gcloud app deploy
    gcloud app browse
    ```

### Deploy to Google Cloud Platform
1. **Install Google Cloud SDK**

    Follow the [installation instructions](https://cloud.google.com/sdk/docs/install).

2. **Deploy to Google App Engine**

    ```bash
    gcloud app deploy
    gcloud app browse
    ```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
