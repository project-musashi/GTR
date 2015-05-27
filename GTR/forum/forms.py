from django import forms
from .models import Link, Vote


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        exclude = ("submitter", "rank_score", "agree", "disagree", "url")
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Fill in your headline'}),
            'self_description': forms.TextInput(attrs={'placeholder':'e.g. mid 20s/software engineer/$80k-90k salaries/work in bay area'}),
            'description': forms.TextInput(attrs={'placeholder': 'Describe your work'})
        }


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = '__all__'