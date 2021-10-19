from django import forms
from .models import Articles, Sources

class NewsForm(forms.ModelForm):
    class Meta:
        model = Articles
        model = Sources
        fields="__all__"

        