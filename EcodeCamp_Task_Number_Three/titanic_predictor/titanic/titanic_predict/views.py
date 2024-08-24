import pickle
import pandas as pd
from django.shortcuts import render
from .forms import PassengerForm

# Load the pre-trained model and scaler
model = pickle.load(open("ml_model.sav", "rb"))
scaler = pickle.load(open("scaler.sav", "rb"))

# The order of the features should match the order used in training
feature_columns = ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'C', 'Q', 'S']

def home(request):
    return render(request, 'titanic_predict/home.html')

def predict_survival(request):
    form = PassengerForm(request.POST or None)
    prediction = None
    if form.is_valid():
        data = form.cleaned_data
        # Prepare the input data for prediction
        input_data = pd.DataFrame([{
            'pclass': data['pclass'],
            'sex': data['sex'],
            'age': data['age'],
            'sibsp': data['sibsp'],
            'parch': data['parch'],
            'fare': data['fare'],
            'C': 1 if data['embarked'] == 'C' else 0,
            'Q': 1 if data['embarked'] == 'Q' else 0,
            'S': 1 if data['embarked'] == 'S' else 0
        }])

        # Ensure all features are present and in the correct order
        input_data = input_data[feature_columns]
        
        # Scale the features
        X_scaled = scaler.transform(input_data)
        
        # Predict survival
        prediction = model.predict(X_scaled)[0]
        
        # Map the prediction to "Survived" or "Not Survived"
        prediction = "Survived" if prediction == 1 else "Not Survived"

    return render(request, 'titanic_predict/predict.html', {'form': form, 'prediction': prediction})
