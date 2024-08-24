
# Real-Time Stock Price Prediction System

## Objective

The goal of this project is to develop a real-time stock price prediction system utilizing historical stock data. This system involves collecting data through APIs, building and training a time-series forecasting model, and deploying it via a Django web application for real-time predictions.

## Tools and Technologies

- **Python**: Used for data processing, model training, and web development.
- **Django**: Web framework for deploying the application.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical operations.
- **Scikit-Learn**: Model evaluation and preprocessing.
- **TensorFlow/Keras**: Deep learning libraries for LSTM model development.
- **Yahoo Finance API**: For retrieving historical stock data.

## Task Roadmap

### 1. Data Collection
- Utilize financial APIs (Yahoo Finance) to collect historical stock data.
- Pre-process the data, including feature engineering and scaling.

### 2. Model Building
- Develop a forecasting model using LSTM or ARIMA.
- Evaluate the model's performance to ensure accuracy.

### 3. Real-Time Implementation
- Deploy the model using Django.
- Create a user interface to display real-time stock predictions.

## Setup Instructions

Here's a detailed README.md file for the stock price prediction system project. This file includes instructions on setting up and using the project, as well as an overview of the tools and technologies involved.


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
#### input stock symbols and view real-time predictions based on the trained model.

### 1. Clone the Repository

```bash
git clone https://github.com/Hamza042/EcodeCamp_Internships.git
cd EcodeCamp_Internships/EcodeCamp_Task_Number_Two



