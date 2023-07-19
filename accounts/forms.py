from django import forms
from .models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        print(f'clean data : {cleaned_data} || super : {super(UserForm, self)}')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        print(f'pasword: {password} || confirm: {confirm_password}')

        if password != confirm_password:
            raise forms.ValidationError(
                'Password does not match'
            )