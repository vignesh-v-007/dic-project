#!/bin/bash

# Update and install dependencies
sudo yum update -y
sudo yum install python3 python3-pip httpd -y

# Start Apache web server
sudo systemctl start httpd
sudo systemctl enable httpd

# Unzip the project
unzip project.zip
cd project

# Install Python dependencies
pip3 install flask numpy pandas matplotlib scikit-learn

# Set Flask environment variables
export FLASK_APP=app.py
export FLASK_ENV=development

# Run Flask application in the background
nohup flask run --host=0.0.0.0 --port=8000 &
