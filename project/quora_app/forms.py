from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Question, Answer

class LoginForm(AuthenticationForm):
    pass 

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']