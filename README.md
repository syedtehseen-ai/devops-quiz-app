# devops-quiz-app

In this, I am using local LLMs Ollama with light weight language model mistral.

Earlier I tested this locally, now i dockerized my devops-quiz-app with docker.

to test this on windows locally, install wsl 2 and docker


docker build -t devops-quiz-app .
docker run -p 8000:8000 devops-quiz-app
