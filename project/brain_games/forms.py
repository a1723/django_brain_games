from django import forms


class NameForm(forms.Form):
    name = forms.CharField(label="Имя", help_text="Enter your user name")