from django import forms
from .models import Link, Vote


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        exclude = ("submitter", "rank_score", "agree", "disagree", "url")
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title', 'class':'form-control link-form-control', 'required':''}),
            'self_description': forms.TextInput(attrs={'class':'form-control link-form-control', 'placeholder':'Self Description (e.g. Mid 20s/Software Engineer/$80-90k Salary/Bay Area)'}),
            'description': forms.Textarea(attrs={'class':'form-control link-form-control', 'placeholder': 'Tell us your story', 'required':''})
        }


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = '__all__'