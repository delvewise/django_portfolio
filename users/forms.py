from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.db import transaction
from django.forms.utils import ValidationError

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields

from allauth.account.forms import SignupForm
from django import forms
# #attempt
#
# class CustomUserCreationForm(SignupForm):
#     class Meta:
#         model = CustomUser
#
#     def __init__(self,instance=None, *args, **kwargs):
#             super(CustomUserCreationForm, self).__init__(*args, **kwargs)
#             self.fields['user_type'] = forms.MultipleChoiceField(choices= USER_TYPE_CHOICES )
#     def save(self, request):
#         user_type = self.cleaned_data.pop('user_type')
#         user = super(CustomUserCreationForm, self).save(request)
#
# class TeacherSignUpForm(SignupForm):
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_investor = True
#         if commit:
#             user.save()
#         return user
#
#
#
# #allauth  docs for extendiung
#
#
#
#
#
#
#
#
# from allauth.account.forms import SignupForm
# class MyCustomSignupForm(SignupForm):
#
#     def save(self, request):
#         # Ensure you call the parent class's save.
#         # .save() returns a User object.
#         user = super(MyCustomSignupForm, self).save(request)
#
#         # Add your own processing here.
#         # You must return the original result.
#         return user
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')
#
#
# #working exazmple\ https://medium.com/@gavinwiener/modifying-django-allauth-forms-6eb19e77ef56
# from allauth.account.forms import SignupForm
# class MyCustomSignupForm(SignupForm):
#     def __init__(self, *args, **kwargs):
#         super(MyCustomSignupForm, self).__init__(*args, **kwargs)
#         self.fields['organization'] = forms.CharField(required=True)
#     def save(self, request):
#         organization = self.cleaned_data.pop('organization')
#         ...
#         user = super(MyCustomSignupForm, self).save(request)
#
#
#
# from allauth.account.forms import SignupForm
# from django import forms
#
# class CustomSignupForm(SignupForm):
#     first_name = forms.CharField(max_length=30, label='First Name')
#     last_name = forms.CharField(max_length=30, label='Last Name')
#     def signup(self, request, user):
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.save()
#         return user
