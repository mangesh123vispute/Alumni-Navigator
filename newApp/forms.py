from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,AlumniPost


class AlumniSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = False
        user.is_alumni = True
        if commit:
            user.save()
        return user


class StudentSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        user.is_alumni = False
        if commit:
            user.save()
        return user

class CollegeSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_college = True
        # Verified = True
        if commit:
            user.save()
        return user


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            "username",
            "first_name",
            "last_name",
            "Branch",
            "skills",
            "email",
            'mobile',
            'linkedin',
            'Github', 
            'instagram',
            "College",
            "Year_Joined",
            "About",
            "Work",
            "Year_Joined",
            "Image"

        ]


class CollegeDetailsForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            "College",
            "Image",
            "About",
            "Branch"
        ]



class AlumniPostForm(forms.ModelForm):

    class Meta:
        model = AlumniPost
        fields = ['tag','Image','title', 'content']
       

        

