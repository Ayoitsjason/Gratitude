from django import forms
from register_login_logout.models import UserForm

class UserForm(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = "__all__"