from django import forms
from .models import Signup, Leads


class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "name": "email",
        "id": "email",
        "placeholder": "Type your email address",
    }), label="")

    class Meta:
        model = Signup
        fields = ('email', )

class LeadsForm(forms.ModelForm):

    # email = forms.EmailField(widget=forms.TextInput(attrs={
    #     "type": "email",
    #     "name": "email",
    #     "id": "email",
    #     "placeholder": "Type your email address",
    # }), label="")
    # subject = forms.CharField()
    # message = forms.CharField(widget=forms.Textarea)


    class Meta:
        model = Leads
        fields = "__all__"
        exclude= ['captured']
    # def send_email(self):
    #     #later
    #     pass
