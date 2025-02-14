from django import forms

# def city_name(value):
#     if value[0] != value[0].upper():
#         raise forms.ValidationError('The city name must be capitalized!')

class Weather(forms.Form):
    city = forms.CharField()