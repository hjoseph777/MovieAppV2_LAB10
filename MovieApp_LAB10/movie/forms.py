from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Movie

# Basic movie form with Bootstrap styling
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'genre', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter movie name'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter genre'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter movie description'})
        }

# Custom user registration - uses email instead of username
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)  # this becomes the username
    
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to all fields
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter first name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter last name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter email address'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        # Using email as username - simpler for users
        user.username = self.cleaned_data["email"]
        
        if commit:
            user.save()
        return user