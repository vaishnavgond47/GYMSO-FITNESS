from django.shortcuts import render
from index import forms
# Create your views here.


def index(request):
    feedbackform = forms.FeedbackForm()
    membershipform = forms.MembershipForm()
    if request.method == "POST" and "feedback_submit" in request.POST:
        feedbackform = forms.FeedbackForm(request.POST)

        if feedbackform.is_valid():
            feedbackform.save(commit=True)

    if request.method == "POST" and "membership_submit" in request.POST:
        membershipform = forms.MembershipForm(request.POST)

        if membershipform.is_valid():
            membershipform.save(commit=True)

    return render(request, 'index.html', {'feedbackform': feedbackform, 'membershipform': membershipform})
