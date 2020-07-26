from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class NameForm(forms.Form):
    name= forms.CharField(label='Your name', max_length=100)
    email=forms.EmailField(label="Your Email",max_length=100)

class ContactForm(forms.Form):
    name = forms.CharField(widget= forms.TextInput(attrs={'class':'login-input'}),label='Your Name', max_length=100)
    firm  = forms.CharField(widget= forms.TextInput(attrs={'class':'login-input'}),label='Your Firm',  max_length=100)
    email = forms.EmailField(widget= forms.TextInput(attrs={'class':'login-input'}),label='Your Email')  
    
    

