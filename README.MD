# End to End Medical Chatbot Geneerative AI

# How to run steps:

# Step 1. Clone the repository

```bash
Project repo: 
```
# Step 2. Create a conda environment after opening the repository

``` bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
```

# Step 3. install the requirements
```bash
pip install -r requirements.txt
```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Loging to AWS console.

## 2. Create IAM user for deployment

    #with specific access
    1. EC2 access: It is virtual machine
    2. ECR: Elastic Container Registry to save your docker image in AWS

    #DEscription: About the deployment

    1. Build docker image of the source code
    2. Push your docker image to ECR
    3. Launch your EC2
    4. Pull your image from ECR in EC2
    5. Lauch your docker image in AC2

    # Policy:

    1. AmazonEC2ContainerRegistryFullAccess
    2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image
    -save the URI: 767828740041.dkr.ecr.ap-south-1.amazonaws.com/medicalbot

## 4. Create EC2 machine ()

## 5. Open EC2 and Install docker in EC2 machine:

    #optional
    sudo apt-get update -y
    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

## 6. Configure EC2 as sefl-hosted runner:

## 7. Setup github secrets:

    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - AWS_DEFAULT_REGION
    - ECR_REPO
    - PINECONE_API_KEY
    - OPENAI_API_KEY