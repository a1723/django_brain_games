from django import forms


class NameForm(forms.Form):
    name = forms.CharField(label="Имя", help_text="Enter your user name")


class AnswerForm(forms.Form):
    answer = forms.CharField(label="Ответ")