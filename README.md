# AWS Serverless Application with CI/CD Pipeline - Cloud Resume Challenge

This is my attempt at the Cloud Resume Challenge https://cloudresumechallenge.dev/docs/the-challenge/aws/ 

This repository contains a serverless application built on AWS using Lambda functions, DynamoDB, and integrated with a CI/CD pipeline. It also includes Playwright for end-to-end testing and unit tests for Lambda functions.

## Live Site
https://anthony-coughlin-resume.com/

## Technologies Used

- **AWS Lambda:** Serverless compute service used for executing backend functions without provisioning or managing servers.
  
- **AWS DynamoDB:** Fully managed NoSQL database service for storing and retrieving data at scale with low latency.
  
- **CI/CD Pipeline:** Automated workflow for Continuous Integration and Continuous Deployment (CI/CD) using GitHub Actions.
  
- **Playwright:** End-to-end testing framework for web applications to ensure application quality and reliability.
  
- **Unit Tests:** Tests written using Python's `pytest` framework to validate individual Lambda function behavior and logic.

## CI/CD Pipeline

The CI/CD pipeline automates the testing, building, and deployment processes:

- **Unit Tests:** Run against Lambda functions to ensure expected behavior.
  
- **Build and Deploy:** Uses AWS SAM CLI to build and deploy Lambda functions and associated AWS resources. The site is also auto deployed and Playwright Tests are executed afterwards.