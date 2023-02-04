# Loan predcition classifier 
This project aims to create all <b>backend infrastructure</b> to host a ML model!
The original machine learning model was developed in this [project](https://colab.research.google.com/drive/1P2Ao5k5a3p13pg2WmBOl7XEnd4nL7MvM), where we developed a Random Forest classification model to classify a loan as approved or not approved.

## Project Flow 
     

<img src="img\project_design.png"  width="700" height="250">


### What I have learnend? 

     - How to create a Rest API with FastAPI.
     - How to container the project in a Docker Image.
     - How to deploy a image in AWS ECR (Elastic Container Registry) with AWS CLI.
     - How to link a image with AWS Lambda Function.
     - How to configure an Rest API with AWS API Gateway.
     - How to teste and use API with Postman.
     
     
### Try it <b>yourself</b>! Import the curl in Postman and change the parameters!

     TotalIncome: Sum of monthly salary that the applicant and the guarantor.
     LoanAmount: Amount of loan requested by applicant.
     Credit_History: If the applicant has credit card (yes (1), no (0)).
     Property_Area: Property type (Urban (0)/Semi Urban(1)/ Rural(2)).

     
<img src="img\postaman_development.png"  width="700" height="400">

     curl --location --request POST 'https://a2czf6h0j0.execute-api.us-east-1.amazonaws.com/dev/predictions' \
     --header 'Content-Type: application/json' \
     --data-raw '{
     "TotalIncome": 2000,
     "LoanAmount": 100,
     "Credit_History": 1,
     "Property_Area": 2
     }'


## [Full Documentation](Loan-Prediction-Documentation.pdf) Loan Prediction Classifier.