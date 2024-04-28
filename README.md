<<<<<<< HEAD
# Zomato-project
## In this Zomato project, our goal was to predict restaurant ratings and determine if online orders should be enabled, utilizing a dataset containing details like restaurant name, location, and more. We chose the Extra Trees and Random Forest algorithms for their effectiveness in handling our prediction tasks, based on their superior performance in phase 2 of the project. These models were adept at managing complex datasets with numerous features affecting ratings and operational decisions, making them ideal for providing actionable insights into restaurant operations. This choice was driven by the need for robust prediction capabilities to aid restaurant owners in enhancing customer satisfaction and operational efficiency.


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

```mermaid
graph LR
    User[User] -->|Access| ELB[Load Balancer]
    ELB --> EC2_1[EC2 Instance 1]
    ELB --> EC2_2[EC2 Instance 2]
    EC2_1 --> RDS[RDS MySQL Database]
    EC2_2 --> RDS
    EC2_1 --> S3[(S3 Bucket)]
    EC2_2 --> S3
    EC2_1 --> CloudWatch
    EC2_2 --> CloudWatch[CloudWatch Logs]
    GitHub[GitHub Repository] -->|CI/CD Pipeline| CodePipeline[CodePipeline]
    CodePipeline -->|Deploy| CodeDeploy[CodeDeploy]
    CodeDeploy --> EC2_1
    CodeDeploy --> EC2_2

    classDef default fill:#f9f,stroke:#333,stroke-width:2px;
    classDef database fill:#ccf,stroke:#333,stroke-width:2px;
    class ELB,CodePipeline,CodeDeploy default
    class RDS,S3 database

=======
# dic-project
DIC project using Zomato dataset
Vignesh Venkatakumar
>>>>>>> dbf49a38bae1e3f7b49d8c3d58e152f487431944
