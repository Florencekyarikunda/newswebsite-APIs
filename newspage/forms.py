from django import forms
from .models import Articles, Sources

class NewsForm(forms.ModelForm):
    class Meta:
        model=Sources
        model = Articles
        fields="__all__"