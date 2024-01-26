from django import forms
from django.forms import ModelForm
from index.models import Feedback, Membership


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Name"}),
            'email': forms.EmailInput(attrs={'class': "form-control", 'placeholder': "Email"}),
            'message': forms.Textarea(attrs={'class': "form-control", 'placeholder': "Message"}),
        }


class MembershipForm(ModelForm):
    class Meta:
        model = Membership
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Name"}),
            'number': forms.TextInput(attrs={'class': "form-control", 'placeholder': "+912222333344"}),
            'email': forms.EmailInput(attrs={'class': "form-control", 'placeholder': "Email"}),
            'message': forms.Textarea(attrs={'class': "form-control", 'placeholder': "Message"}),
        }
