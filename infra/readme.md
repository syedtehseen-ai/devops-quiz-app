 📋 Overview

This is a simple DevOps Quiz Generator app built using **FastAPI** and powered by a local **LLM (Mistral via Ollama)**. It includes a clean UI to select a DevOps topic and dynamically generate interview-style questions using a local LLM model.

The infrastructure required for the app is **built using Terraform**, which creates:

- A **Kubernetes namespace**
- A **deployment** and **service**
- Port-forwarding for local testing

> ⚠️ The LLM model (Mistral via Ollama) performs the heavy lifting and **must be running locally**. If the LLM is **not** running, the app will still load the UI (`index.html`) but won’t generate questions.

---

 ⚙️ How It Works

1. User opens the `/` route – served by FastAPI as an HTML form.
2. UI presents a dropdown of DevOps topics and a “Generate” button.
3. When submitted, a POST request hits `/get-questions`.
4. FastAPI constructs a prompt and sends it to the **Mistral model** running via Ollama.
5. The LLM responds with questions, which are rendered in the browser.

---

 🛠 Technologies Used

- **FastAPI** – Web framework to build APIs
- **Uvicorn** – ASGI server to serve FastAPI
- **Ollama + Mistral** – Local LLM model to generate questions
- **Terraform** – To automate Kubernetes infrastructure setup
- **Kubernetes (via Kind)** – To deploy and test the app
- **GitHub Actions** – For CI/CD pipeline
- **Docker** – To containerize the app
- **Pytest** – For testing

---

 📦 Infrastructure Setup (via Terraform)

The Terraform configuration automates:

- Creating a Kubernetes **namespace**
- Deploying the **FastAPI app** with a **deployment** and **service**
- Creating a **port-forwarding** setup for easy local testing

> Example:
> ```bash
> terraform init
> terraform apply
> kubectl port-forward svc/quiz-service 8000:80 -n devops
> ```

Now you can access the app at `http://localhost:8000`.

---

 🔄 CI/CD with GitHub Actions

The pipeline (`.github/workflows/cicd.yml`) includes:

- Checking out the code
- Installing dependencies (`requirements.txt`)
- Running tests via `pytest`
- Building and testing the Docker image
- Pushing the image to DockerHub (secrets required)
- Verifying with a `curl` test against the running container

---

 💻 Local Development Setup

To run the app locally without Kubernetes:

1. Make sure **Ollama** is installed.
2. Start the LLM (e.g. mistral):

   ```bash
   ollama run mistral
````

3. Start the FastAPI server:

   ```bash
   uvicorn app.main:app --reload
   ```

4. Open the app in your browser:

   ```
   http://localhost:8000
   ```

> ⚠️ Without the LLM running, only the HTML UI will load. No questions will be generated.

---

 🧠 Coming Soon

* Multi-topic support
* Ingress + LoadBalancer setup for external access
* LLM support cloud APIs

---
