# Use a slim version for a smaller security attack surface
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application logic
COPY . .

# Set non-root user for production security
RUN useradd -m bantai_user
USER bantai_user

CMD ["python", "agents/bantai_core/observer.py"]