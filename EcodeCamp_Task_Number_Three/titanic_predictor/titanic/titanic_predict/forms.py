from django import forms

class PassengerForm(forms.Form):
    pclass = forms.ChoiceField(choices=[(1, '1st'), (2, '2nd'), (3, '3rd')])
    sex = forms.ChoiceField(choices=[(0, 'Male'), (1, 'Female')])
    age = forms.IntegerField()
    sibsp = forms.IntegerField()
    parch = forms.IntegerField()
    fare = forms.FloatField()
    embarked = forms.ChoiceField(choices=[('C', 'Cherbourg'), ('Q', 'Queenstown'), ('S', 'Southampton')])
