from django import forms
from homepage.models import Document


class DoucmentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document')