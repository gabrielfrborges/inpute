from .models import Question, Answer
from django import forms

class AnswerForm(forms.ModelForm):

    class Meta():
        model = Answer
        fields = ( 'description', )

class UpdatePostForm(forms.ModelForm):

    class Meta():
        model = Question
        fields = ( 
            'title',
            'description'
        )