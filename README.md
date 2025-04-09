# Wine Quality Prediction - End-to-End ML Project with MLflow

## Project Overview
This project implements an end-to-end machine learning pipeline for predicting wine quality based on physicochemical properties. The project uses MLflow for experiment tracking and includes a Streamlit web interface for real-time predictions.

## Tech Stack Used
- Python 3.9
- MLflow for experiment tracking
- DagsHub for MLflow server hosting
- Streamlit for web interface
- Scikit-learn for machine learning (ElasticNet model)
- Docker for containerization
- AWS for deployment (EC2 & ECR)
- Github Actions for CI/CD

## Project Structure
```
├── .github/workflows    # Github Actions workflows
├── artifact            # Storage for all pipeline artifacts
├── config             # Configuration files
├── logs               # Log files
├── notebook           # Jupyter notebooks for experimentation
├── research           # Research and development notebooks
├── src                # Source code
│   ├── components     # Core components of the ML pipeline
│   ├── config        # Configuration management
│   ├── pipeline      # Pipeline modules
│   ├── utils.py      # Utility functions
│   ├── logger.py     # Logging configuration
│   └── exception.py  # Custom exception handling
├── app.py            # Streamlit web application
├── main.py           # Main pipeline execution script
├── params.yaml       # Model parameters
├── schema.yaml       # Data schema
└── setup.py          # Project setup file
```

## Project Workflows
1. Data Ingestion
2. Data Validation
3. Data Transformation
4. Model Training
5. Model Evaluation
6. Model Deployment
7. Prediction Pipeline
8. Web Application

## Getting Started

### Prerequisites
- Python 3.9
- Git
- Docker (for containerization)
- AWS Account (for deployment)

### Installation Steps

1. Clone the repository
```bash
git clone https://github.com/harcuracy/machine_learning_project
```

2. Create and activate conda environment
```bash
conda create -n mlproj python=3.8 -y
conda activate mlproj
```

3. Install requirements
```bash
pip install -r requirements.txt
```

4. Run the application
```bash
# Run Streamlit app
streamlit run app.py
```

### MLflow Tracking
The project uses MLflow for experiment tracking. To view the MLflow UI:

1. Set up DagsHub tracking:
```python
import mlflow
import dagshub

dagshub.init(repo_owner='harcuracy', repo_name='machine_learning_project', mlflow=True)
```

2. Access MLflow UI through DagsHub:
```
https://dagshub.com/harcuracy/machine_learning_project.mlflow
```

## Model Features
The model predicts wine quality based on the following features:
- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol

## AWS Deployment Steps

1. Login to AWS console

2. Create IAM user for deployment
   - EC2 access
   - ECR: Elastic Container registry access

3. Create ECR repository
   ```
   URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj
   ```

4. Create EC2 machine (Ubuntu)

5. Install Docker on EC2
   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker ubuntu
   newgrp docker
   ```

6. Configure EC2 as self-hosted runner
   - Navigate to GitHub Actions
   - Add new self-hosted runner
   - Follow setup instructions

7. Setup GitHub Secrets
   ```
   AWS_ACCESS_KEY_ID=
   AWS_SECRET_ACCESS_KEY=
   AWS_REGION=us-east-1
   AWS_ECR_LOGIN_URI=566373416292.dkr.ecr.ap-south-1.amazonaws.com
   ECR_REPOSITORY_NAME=mlproj
   ```

## Author
Akande Soji

## Contact
- Email: akandesoji4christ@gmail.com
- GitHub: [harcuracy](https://github.com/harcuracy)

## License
This project is licensed under the MIT License - see the LICENSE file for details
