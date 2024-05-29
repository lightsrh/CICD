FROM python:3.12

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements.txt and validate its content
COPY requirements.txt ./
RUN ls -la && cat requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt -v

# Copy the source code into the container.
COPY . .



# Expose the port that the application listens on.
EXPOSE 2022

# Run the application.
CMD ./init.sh ;python3 ./app/__main__.py 