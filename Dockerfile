# 1. Use a clean Python 3.10 slim base image
FROM python:3.10-slim

# 2. Set the operating directory inside the container
WORKDIR /app

# 3. Copy just requirements first to leverage Docker caching
COPY requirements.txt .

# 4. Install dependencies directly
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your application code
COPY . .

# 6. Expose the standard Streamlit port
EXPOSE 8501

# 7. Start the application
ENTRYPOINT ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]