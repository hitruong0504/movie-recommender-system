# 🎬 Movie Recommender System  

This is a **Movie Recommender System** built using **Streamlit** and **Machine Learning**. The app provides personalized movie recommendations based on similarity metrics. It utilizes pre-trained models and a movie dataset to suggest movies based on user preferences.  

## 📌 Features  
- 🔍 **Movie Search**: Find movies by title.  
- 🎞 **Personalized Recommendations**: Get movie suggestions based on similarity metrics.  
- 📊 **Machine Learning Model**: Uses a precomputed similarity matrix for fast recommendations.  
- 🌐 **Streamlit Web App**: Simple and interactive UI.  
- 🐳 **Docker Support**: Run the app easily in a containerized environment.  

---

## 🚀 Getting Started  

### **Run with Docker**  

#### **Step 1: Pull the Docker Image**  
Download the latest version of the Docker image from Docker Hub:

```
docker pull hitruong05/movie-recommender-system:latest
```

#### **Step 2: Run the container**  
Start a new container and expose port 8501:
```
docker run -p 8501:8501 hitruong05/movie-recommender-system
```

#### **Step 3: Open the App in Your Browser**  
Once the container is running, open:
```
http://localhost:8501
```
---

## 📌 About
- **Author**: HiTruong
- **Built with**: Python, Streamlit, Docker
- **License**: MIT
- **Docker Hub**: [Docker Hub](https://hub.docker.com/repository/docker/hitruong05/movie-recommender-system/general)
## ⭐ If you like this project, give it a star and share it! 🚀
