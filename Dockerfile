FROM ubuntu:latest

# Install Cron, update system
RUN apt-get update && apt-get -y install python3 python3-pip 

# Copy over project directory
ADD ./ /garebear

# Install package dependencies
RUN pip install --no-cache-dir -r /garebear/requirements.txt

WORKDIR /garebear

# Give permission to run scripts
RUN chmod +x /garebear/app.py