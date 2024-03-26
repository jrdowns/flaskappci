# flaskappci - Work In Progress
Demo pipeline for deploying a Flask app to Azure

## Deploying The App
1. Run the deploy Action: "Deploy Flask App to Azure"
   Note: The deployment should only take a minute or two.
2. The public IP of the app will be displayed at the bottom of the Terraform Apply output e.g. container_ipv4_address = "4.151.219.105"
   Note: The page may initially take a moment to load
3. There is a form on the page for you to leave feedback. Your feedback will be emailed to my personal email via Azure Communication Services.
4. Five minutes after successful deployment, the app will be destroyed

## Tech Stack
Python - Base programming language  
Flask - Simple Python-based web framework  
Docker - Containerization platform  
Gunicorn - WSGI server  
Terraform - Infrastructure as Code  
GitHub Actions - CI/CD  
Azure Container Instances - Managed, serverless Azure environment  
Azure Communication Services - Used for sending email from inside the application  

## Next Steps
1. Create a dev branch
2. Implement linting and unit testing
3. Automate pipeline on pull/merge to main branch
