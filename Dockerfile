# Use the official Python base image with the desired version
FROM python:3.10

# Set the working directory inside the container
WORKDIR /AI_PresentationGenerator

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the working directory
COPY . .

# Expose the port that Gunicorn will be running on
EXPOSE 5000

# Set the Gunicorn command
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
