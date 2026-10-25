
FROM python:3.9-slim

# Create a non-root user
RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

# Install application dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Accounts service
COPY service ./service
COPY .flaskenv ./.flaskenv

# Configure the service
ENV PORT=8080
EXPOSE 8080

# Run as a non-root user
USER appuser

# Start the Flask application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "service:app"]
