# Zomato Restaurant Rating and Online Order Feasibility Prediction

## Project Overview
This project aims to predict restaurant ratings and assess the feasibility of enabling online orders using machine learning models based on the Zomato dataset. The application is deployed on AWS and utilizes Flask for the web interface.

## Repository Structure

```plaintext
/
|-- deploy_scripts/       # Scripts for deployment
|-- static/               # Static files for web application
|-- templates/            # HTML templates for the Flask application
|-- DIC-Phase3.mp4        # Video description of phase 3
|-- Phase 3 - Description(4).pdf  # Detailed documentation of phase 3
|-- README.md             # Project documentation
|-- app.py                # Flask application main file
|-- appspec.yml           # AWS CodeDeploy specification file
|-- buildspec.yml         # AWS CodeBuild specification file
|-- dic_project_phase2.ipynb  # Jupyter notebook for phase 2 analysis
|-- feature_importance.png # Feature importance visualization
|-- graph.py              # Script for generating graphs
|-- pipeline.yml          # CloudFormation template for CI/CD pipeline
|-- requirements.txt      # Python dependencies
|-- sample.py             # Sample Python script
|-- template.yml          # AWS CloudFormation template for infrastructure
|-- templateparameters.json # Parameters for CloudFormation template
```

## Key Files and Their Functions
- **app.py**: Flask application's main script.
- **appspec.yml**: Specifies the AWS CodeDeploy settings for deployment.
- **buildspec.yml**: Contains commands used by AWS CodeBuild for the build process.
- **pipeline.yml**: Defines the AWS CloudFormation resources for the CI/CD pipeline.

## Deployment Instructions
### Initial Setup
1. Clone the repository to your local machine.
2. Install the required Python packages: `pip install -r requirements.txt`.

### Running Locally
1. Execute `python app.py` to start the Flask server.
2. Access the application through `localhost` on the specified port.

### AWS Deployment
1. Commit and push any changes to the GitHub repository to trigger AWS CodePipeline.
2. AWS CodeBuild and CodeDeploy will automatically deploy updates to AWS EC2 instances.
3. Monitor deployment status through AWS CodeDeploy and AWS CloudWatch.

## Deployment Using AWS CloudFormation
1. Navigate to the AWS CloudFormation console.
2. Create a new stack using `template.yml` and provide parameters from `templateparameters.json`.
3. Review and launch the stack.

## Continuous Integration and Deployment
- GitHub commits trigger AWS CodePipeline.
- AWS CodeBuild builds the application and runs tests.
- AWS CodeDeploy automatically deploys the application to configured AWS EC2 instances.

#### Here's a brief explanation of the steps followed in the Zomato project:

1. **Dataset Acquisition and Preparation:**
 - Obtained the Zomato dataset containing restaurant details such as name, location, cuisine, and customer ratings.
 - Cleaned and preprocessed the data, including handling missing values, encoding categorical variables, and normalizing numerical values.
2. **Feature Engineering:**
 - Extracted meaningful features that could influence restaurant ratings and the likelihood of online orders, such as location, cuisine types, and average cost.
3. **Model Selection and Training:**
 - Evaluated various machine learning models for regression (to predict ratings) and classification (to predict online order feasibility).
 - Selected Extra Trees Regression and Random Forest Classifier based on their performance in handling complex patterns and feature importance in predictive accuracy.
4. **Model Evaluation:**
 - Split the data into training and testing sets to evaluate the models’ performance.
 - Used metrics like R-squared for regression and accuracy, precision, recall, and F1-score for classification to determine the best models.
5. **Implementation of Machine Learning Models:**
 - Trained the selected models on the dataset.
 - Used the trained models to predict restaurant ratings and online ordering feasibility.
6. **Deployment Preparation:**
 - Serialized the trained models using Python’s pickle module to create .pkl files.
7. **Flask Application Development:**
 - Developed a Flask-based web application to serve as the interface for model predictions.
 - Created HTML templates for user input and to display prediction results.
8. **AWS Deployment:**
 - Set up an AWS resources (EC2,S3) via cloudformation template to host the Flask application.
 - Configured AWS CodePipeline and CodeDeploy for continuous integration and deployment, automating the update process from GitHub commits to live deployment.
9. **CloudFormation and CodeDeploy Integration:**
 - Used AWS CloudFormation to script the provisioning of the AWS infrastructure.
 - Utilized AWS CodeDeploy to automate the deployment process of the Flask application onto the EC2 server.
10. **Final Testing and Launch:**
 - Performed final testing to ensure the web application’s functionality and reliability.
 - Launched the web application to be accessible for end-users to input data and receive predictions on restaurant ratings and online order feasibility.
