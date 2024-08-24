# stockanalysis/forms.py

from django import forms

class StockForm(forms.Form):
    ticker = forms.CharField(label='Ticker Symbol', max_length=10, initial='GOOGL')
    horizon = forms.ChoiceField(
        label='Prediction Horizon',
        choices=[('7', '7 Days'), ('30', '1 Month'), ('90', '3 Months')],
        initial='7'
    )
