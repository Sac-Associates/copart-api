# Copart Application

This repository contains a serverless application that downloads and processes vehicle sales data, manages user criteria for vehicle selection, and provides filtered results based on the criteria.

## Prerequisites

- [AWS CLI](https://aws.amazon.com/cli/) installed and configured.
- [AWS SAM CLI](https://aws.amazon.com/serverless/sam/) installed.

## Setup

Clone the repository:

```bash
git clone https://github.com/your-username/copart-app.git
cd copart-app
```

## Build and Deploy

Use the following commands to build and deploy the application:

```bash
sam build
sam deploy --guided
```

The `--guided` flag will prompt you to provide necessary information like stack name, region, and other parameters.

## Running Locally

You can test the Lambda functions locally:

```bash
sam local invoke DownloadParseCsvFunction
sam local invoke SetCriteriaFunction
sam local invoke GetVehiclesFunction
```

You can also start the API Gateway locally:

```bash
sam local start-api
```

This will allow you to test the API endpoints on your local machine.

## Cleanup

To delete the deployed resources:

```bash
sam delete
```

This command will remove all the resources created by this application.
