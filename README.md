---

## 🚀 DevOps Quiz App

### 📋 Overview

This project is a simple DevOps quiz generator built with **FastAPI** and powered by a **local LLM (Mistral via Ollama)**.
Users interact with a browser-based UI to select a topic and receive interview-style questions generated dynamically using LLM.

---

### How It Works

1. When the user accesses the `/` endpoint, **FastAPI** serves the `index.html` form in the browser.
2. The HTML page displays a dropdown of topics and a "Generate" button.
3. On form submission, a POST request is made to `/get-questions`.
4. FastAPI constructs a prompt and sends it to the **Mistral model** running locally via **Ollama** (`/generate` endpoint).
5. The LLM response is parsed, and the generated questions are shown in the browser.

---

### 🛠 Technologies Used

* **FastAPI** – For building fast, simple APIs
* **Uvicorn** – ASGI server to run FastAPI
* **Ollama + Mistral** – Local LLM model to generate DevOps questions
* **Pytest** – For basic testing
* **GitHub Actions** – CI/CD pipeline
* **Docker** – Containerization and image deployment

---

### 🔄 CI/CD with GitHub Actions

The CI/CD pipeline is defined in `.github/workflows/cicd.yml` and includes:

* Checking out the repo
* Installing dependencies from `requirements.txt`
* Running tests using `pytest`
* Logging in to DockerHub (credentials stored as GitHub Secrets)
* Building the Docker image
* Running the app in the background using `uvicorn`
* Performing a `curl` check to ensure the app is responsive
* Pushing the image to DockerHub

---

### 💻 Local Setup

To run the app locally:

1. Ensure **Ollama** is installed and running on your system.

2. Pull the required LLM model (like `mistral`) using:

   ```bash
   ollama run mistral
   ```

3. Start the FastAPI server:

   ```bash
   uvicorn app.main:app --reload
   ```

4. Open `http://localhost:8000` in your browser to access the UI.

---