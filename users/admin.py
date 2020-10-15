from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, Author

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(User, CustomUserAdmin)
