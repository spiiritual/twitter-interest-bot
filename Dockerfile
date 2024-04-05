# Use the Python 3.12 Alpine image as the base
FROM python:3.12-alpine

# Set the working directory
WORKDIR /app

# Copy all non git-ignored files to the working directory
COPY . /app

# Install cron
RUN apk add --no-cache dcron

# Install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# Add the cron job to run main.py every two hours
RUN echo "0 */2 * * * python /app/main.py >> /var/log/cron.log 2>&1" > /etc/crontabs/root

# Run main.py when the container starts
CMD python /app/main.py && crond -f
