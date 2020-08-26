# Managing the end-to-end machine learning lifecycle with MLFlow in Azure

This Repository contains the resources for MLFlow deployment with Azure resources

# Basic setup

## Setup the environment
- clone this repository
- **with virtualenv (recommended)**
  - install virtualenv: `pip install virtualenv`
  - create a new environment: `virtualenv mlflow_tutorial`
  - activate the environment: `source /mlflow_tutorial/bin/activate`
  - run `pip install -r requirements.txt`

- **with anaconda**
  - install virtualenv: `pip install anaconda`
  - create a new environment: `conda create -n mlflow_tutorial`
  - activate the environment: `conda activate mlflow_tutorial`
  - install pip in the environment: `conda install pip`
  - run `pip install -r requirements.txt`


- **with pipenv** 
  - install pipenv: `pip install pipenv`
  - run `pipenv install` in the directory of the Pipfile
  - activate the environment by `pipenv shell`

## The notebooks
- `hands_on_example Azure Resources.ipynb`
- `hands_on_example AML.ipynb`
- run `jupyter notebook`


# Setup the Data environment
## Create Azure Postgres DB Instance
- www.portal.azure.com

## Test connection with the database
- set up environment vars (.env)
- map env vars with settings.py
- run `connect_db.py`

## Set up local environment vars to connect to blob
- `export AZURE_STORAGE_ACCESS_KEY = <access key>`
- `export AZURE_STORAGE_CONNECTION_STRING = <connection string>`

## To Start Tracking Server
- `mlflow server \`
    `--backend-store-uri /mnt/persistent-disk \`
    `--default-artifact-root blob://my-mlflow-blob/ \`
    `--host 0.0.0.0`
    `--port 5000`

