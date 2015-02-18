from django import forms

class GetChoiceForm(forms.Form):
    choiceField = forms.CharField(label='Enter Here:',max_length=510)
    