from django import forms
from .models import Project, ContactMessage

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'link']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

    def clean_email(self):
        email = self.cleaned_data['email']
        if "@gmail.com" not in email and "@outlook.com" not in email:
            raise forms.ValidationError("Please use a valid email.")
        return email
