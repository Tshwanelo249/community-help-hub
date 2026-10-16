# Community Help Hub — Python version

A Streamlit prototype for the Community Help Hub student project.

## Features
- Browse sample community notices
- Search and filter by category
- Create a post in the current app session
- Remove demo posts from the current session
- About page describing the project and possible future improvements

## Prototype limitation
Posts are held in Streamlit session state. They are not shared with other visitors and are not stored in a persistent database. Do not enter private or sensitive information.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Run `pip install -r requirements.txt`.
4. Run `streamlit run app.py`.

## Deploy on Streamlit Community Cloud
1. Upload `app.py`, `requirements.txt`, and this README to the root of your GitHub repository.
2. Open https://share.streamlit.io/ and sign in with GitHub.
3. Click **Create app** and choose **Yup, I have an app**.
4. Select repository `Tshwanelo249/community-help-hub`, branch `main`, and main file path `app.py`.
5. Optionally choose an app URL, then click **Deploy**.
