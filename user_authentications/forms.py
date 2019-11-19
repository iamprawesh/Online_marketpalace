from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control inputstyle', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control inputstyle', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control inputstyle', 'placeholder':'Last Name'}))
    #fav_color = forms.CharField(max_length=100) #Same way we can add as many fields as we want
    #But for this we need to extend our User database as we did with the forms
    # we have to do this in models and extend user db by making another model like students(Users) and
    # then adding fields as heress

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control inputstyle'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = "username"
        self.fields['username'].help_text = ''
        # self.fields['username'].errorslist = 'E'


        self.fields['password1'].widget.attrs['class'] = 'form-control inputstyle'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ""
        self.fields['password1'].help_text = ''
        # '<span class="form-text text-muted"><small><ul><li>Your password cant be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password cant be a commonly used password.</li><li>Your password cant be entirely numeric.</li></ul></small></span>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control inputstyle'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ""
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'