from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject','message')
        
        
        widgets = {
            "name":forms.TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Name"
                
            }),
            
            "email":forms.EmailInput(attrs={
                'class': 'form-control',
                "placeholder": "Email"
                
            },),
            "subject":forms.Textarea(attrs={
                'class': 'form-control',
                "placeholder": "Subject"
                
            },),
            "message":forms.TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Message"
                
            },),
        }
            
        