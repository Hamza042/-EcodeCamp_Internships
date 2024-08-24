
# Titanic Survival Prediction System

## Objective

The goal of this project is to develop a predictive model to determine the likelihood of survival for passengers on the Titanic. This system involves collecting the Titanic dataset, preprocessing the data, building and evaluating several predictive models, and deploying the best model using a web application.

## Tools and Technologies

- **Python**: Used for data processing, model training, and web development.
- **Django**: Web framework for deploying the application.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical operations.
- **Scikit-Learn**: Model evaluation and preprocessing.
- **TensorFlow/Keras**: Deep learning libraries for LSTM model development.
- **Kaggle Titanic Dataset**: Source of historical data for training and testing the model.

## Task Roadmap

### 1. Data Collection
- Use the Titanic dataset from Kaggle.
- Understand the features and target variable.

### 2. Model Building
- Handle missing values.
- Perform feature engineering.
- Encode categorical variables.

### 3. Model Building
- Split the data into training and testing sets.
- Train multiple models (Logistic Regression, Decision Trees, Random Forest).
- Evaluate and select the best-performing model.

### 4. Model Deployment
- Deploy the model using Django.
- Create a user interface to input passenger details and predict survival.

## Setup Instructions

Here's a detailed README.md file for titanic survival prediction system project. This file includes instructions on setting up and using the project, as well as an overview of the tools and technologies involved.


### 1. Create a Virtual Environment
```bash
python -m venv env
```

### Windows:
### Activate the Virtual Environment
```bash
cd env\Scripts\actiavte
.\env\Scripts\activate
```
### macOS/Linux:
```bash
source env/bin/activate
```

### 2. Install Requirements
#### Ensure you have a requirements.txt file with the necessary packages. If not, create one:
```bash
pip freeze > requirements.txt
```
### Install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Apply Migrations (Django)
#### Apply the database migrations for Django:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Application
#### Start the Django development server:
```bash
python manage.py runserver
```

### Usage
#### Once the server is running, you can access the application at http://127.0.0.1:8000/. Use the web interface to 
#### input passenger details and receive a prediction on their likelihood of survival.

### 1. Clone the Repository

```bash
git clone https://github.com/Hamza042/EcodeCamp_Internships.git
cd EcodeCamp_Internships/EcodeCamp_Task_Number_Three




