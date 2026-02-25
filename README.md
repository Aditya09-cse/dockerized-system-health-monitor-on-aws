# 🚀 System Health Monitoring App - Dockerized Deployment on AWS EC2

## 📌 Project Overview

This project demonstrates how to:

- Build a simple Python web application
- Containerize it using Docker
- Deploy it on an AWS EC2 instance
- Expose the application to the internet
- Troubleshoot real-world networking issues (Security Groups, Ports, etc.)

The application runs on port **8000** and is deployed inside a Docker container on an EC2 instance.

---

## 🛠️ Technologies Used

- Python (Flask)
- Docker
- AWS EC2
- Linux (Ubuntu)
- Git & GitHub

---

## 📦 Project Requirements

Before running this project, you need:

- AWS Account
- EC2 instance (Ubuntu recommended)
- Docker installed
- Git installed
- Open Security Group port 8000

---

## 🧱 Architecture Diagram
            ┌──────────────────────────┐
            │        User Browser       │
            │ http://PublicIP:8000      │
            └────────────┬──────────────┘
                         │
                         ▼
            ┌──────────────────────────┐
            │   AWS Security Group     │
            │   (Port 8000 allowed)    │
            └────────────┬──────────────┘
                         │
                         ▼
            ┌──────────────────────────┐
            │      EC2 Instance        │
            │  Ubuntu Linux Server     │
            └────────────┬──────────────┘
                         │
                         ▼
            ┌──────────────────────────┐
            │     Docker Container     │
            │   system-health image    │
            │   Running Flask App      │
            └────────────┬──────────────┘
                         │
                         ▼
            ┌──────────────────────────┐
            │      Flask Application   │
            │   Running on 0.0.0.0     │
            │        Port 8000         │
            └──────────────────────────┘

    
---

## 🐳 Why Docker?

Docker helps in:

- Packaging the application and dependencies together
- Ensuring consistency across environments
- Easy deployment on any server
- Avoiding "it works on my machine" problems

---

## 📄 Impact of the Dockerfile

The Dockerfile is critical because it:

1. Defines the base image (Python)
2. Installs required dependencies
3. Copies application code into the container
4. Exposes port 8000
5. Defines the command to run the application

Without Dockerfile:
- The app would need manual setup on every server
- Dependencies could conflict
- Deployment becomes inconsistent

With Dockerfile:
- Deployment becomes automated
- Environment is reproducible
- Scaling becomes easier

---

## 📥 Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/system-health-monitor.git
cd system-health-monitor
```
### 2️⃣ Build Docker Image
```
docker build -t system-health .
```
### 3️⃣ Run Container
```
docker run -d -p 8000:8000 system-health
```
### 4️⃣ Open in Browser
```
http://<EC2-Public-IP>:8000
```


---

## 🔐 AWS Security Group Configuration

To make the application accessible from the internet, the EC2 Security Group must allow inbound traffic on port **8000**.

### Required Inbound Rule

| Type        | Protocol | Port | Source      |
|------------|----------|------|------------|
| Custom TCP | TCP      | 8000 | 0.0.0.0/0  |

⚠️ If this rule is not added, the browser will display:
   - ``ERR_CONNECTION_TIMED_OUT``


This configuration ensures external traffic can reach the Docker container running inside the EC2 instance.

---

## 📸 Screenshots

### 1️⃣ Application UI  
Application successfully running at: `http://<EC2-Public-IP>:8000`

### 2️⃣ Docker Running Container  
Output of: `docker ps `
- Showing the container running and port mapping: `0.0.0.0:8000 -> 8000/tcp`


### 3️⃣ EC2 Instance Details  
AWS EC2 instance dashboard showing:
- Instance status: Running  
- Public IP assigned  

### 4️⃣ Security Group Rule  
Inbound rule configured to allow port 8000.

---

## 🚀 Learning Outcomes

Through this project, I learned:

- How to containerize a Flask application using Docker  
- How Docker port mapping works (`8000:8000`)  
- How AWS Security Groups control inbound traffic  
- How to deploy containerized applications on EC2  
- How to troubleshoot real-world cloud networking issues  
- The importance of exposing services securely  

---

## 👨‍💻 Author

- **Name:** Aditya Singh Tomar  
- **GitHub:** [Aditya09-cse](https://github.com/Aditya09-cse)  
- **Email:** adityatomar0910@example.com
