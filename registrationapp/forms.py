from django import forms
from django.forms import ModelForm
from .models import User,Post
from django.contrib.auth.forms import UserCreationForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('email' , 'password')

class PostForm(forms.ModelForm):
    body = forms.CharField(required=True,
        widget=forms.widgets.Textarea(
            attrs={
            "placeholder":"Enter your post ",
            }
        ),                   
        label="",
    )
    class Meta:
        model = Post
        exclude = ("user",)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class':'registration__form__input'}))
    first_name = forms.CharField(label='Name', max_length=100,widget=forms.TextInput(attrs={'class':'registration__form__input'}))
    last_name = forms.CharField(label='Last Name', max_length=100,widget=forms.TextInput(attrs={'class':'registration__form__input'}))
    username = forms.CharField(label='Username', max_length=150, widget=forms.TextInput(attrs={'class': 'registration__form__input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'registration__form__input'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'registration__form__input'}))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username','email', 'password1', 'password2')

    def  __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = '<span class="form-text"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        
        self.fields['password1'].help_text = '<ul class="form-text-li"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li></ul>'

        self.fields['password2'].help_text = '<span class="form-text"><small>Enter the same password as before, for verification.</small></span>'