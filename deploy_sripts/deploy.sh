#!/bin/bash

# Copy artifacts from CodeBuild and the required files from S3 to the /home/ec2-user directory
aws s3 cp s3://vigneshproject01files/online_order_model.pkl /home/ec2-user/
aws s3 cp s3://vigneshproject01files/rating_model.pkl /home/ec2-user/
aws s3 cp s3://vigneshproject01files/zomato.csv /home/ec2-user/

# Navigate to home directory
cd /home/ec2-user

# Update and install dependencies
sudo yum update -y
sudo yum install python3 python3-pip httpd -y

# Start Apache web server
sudo systemctl start httpd
sudo systemctl enable httpd

# Install Python dependencies
pip3 install flask numpy pandas matplotlib scikit-learn

# Set Flask environment variables
export FLASK_APP=app.py
export FLASK_ENV=development

# Run Flask application in the background
nohup flask run --host=0.0.0.0 --port=8000 &
