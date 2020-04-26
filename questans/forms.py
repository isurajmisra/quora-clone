from django import forms
from .models import Questions, Answers

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = [
            'title',
            'topics',
        ]

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answers
        fields = [
            'answer_text',
        ]