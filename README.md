# Jenkins-Python-CI-CD-Project

This project demonstrates a simple CI/CD pipeline using **Jenkins**, **Docker**, and **DockerHub** for a Python application.

---

## Project Overview

The goal of this project is:

> Whenever I push code to GitHub, I can manually trigger a Jenkins pipeline which builds a Docker image from my Python application and pushes it to DockerHub. Currently, the pipeline runs when I click **Build Now** in Jenkins, but it could be configured to trigger automatically on GitHub commits in the future.

The pipeline consists of three main stages:

1. **Ankush Malgotra - Build Docker Image**: Builds a Docker image from the Python app.
2. **Ankush Malgotra - Login to DockerHub**: Authenticates Jenkins to DockerHub.
3. **Ankush Malgotra - Push Image to DockerHub**: Pushes the Docker image to DockerHub.

---

## How the Python App Works

The Python app starts a simple HTTP server on port `8081`.

When accessed in a browser, it displays:

Welcome to Ankush's Python App!


---

## How to Run

1. Push your Python code to GitHub.
2. Trigger the Jenkins pipeline by clicking **Build Now**.
3. Jenkins will build the Docker image and push it to DockerHub.
4. Access the app in a browser at: `http://<your-server-ip>:8081`.