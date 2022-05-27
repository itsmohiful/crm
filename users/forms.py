from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Profile


class UserRegisterForm(UserCreationForm):
    class Meta :
        model = User
        fields = ['username','email','password1','password2']



class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})



class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['phone','address','profile_image']

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
