FROM python:3.12

# Set the working directory
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

EXPOSE 2022

CMD ["python", "__main__.py"]