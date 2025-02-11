FROM python:3.11
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
COPY model/movie_dict.pkl /app/model/movie_dict.pkl
COPY model/similarity.pkl /app/model/similarity.pkl
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]