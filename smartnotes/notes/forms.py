from django import forms
from .models import Notes
from django.core.exceptions import ValidationError


class NotesForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = ("title", "text")
        labels = {
            'text': 'Write your thoughts here'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-2'}),
            'text': forms.Textarea(attrs={'class': 'form-control my-3'})
        }

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 10:
            raise ValidationError(
                'The note must have at least 10 characters!')
        return text
