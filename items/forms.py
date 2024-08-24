from django import forms

class ItemForm(forms.Form):
  title = forms.CharField(label="標題", max_length=30)
  description = forms.CharField(label="描述", max_length=100)
  deadline = forms.DateField(label="截止日")