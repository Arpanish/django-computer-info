from django import forms
from django.contrib.auth.models import User
from user.models import UserRegistrationModel


# user login form
class LogInForm(forms.Form):
   username = forms.CharField(max_length=55, widget=forms.TextInput(attrs={'class':'form-control'}))
   # password = forms.CharField()
   password = forms.CharField(max_length = 55,widget=forms.PasswordInput(attrs={'class':'form-control'}))
   # widgets = {
   #    'password' : forms.PasswordInput()
   # }


#user registration form
class UserRegistrationForm(forms.ModelForm):
       class Meta:
            model = UserRegistrationModel
            fields = ['username','first_name','last_name','email','password','password_confirmation']
            widgets = {
                  'password_confirmation':forms.PasswordInput(attrs={'class':'form-control border border-secondary shadow-sm p-2 mb-4 bg-body rounded rounded-0 formheight'}),
                  'password':forms.PasswordInput(attrs={'class':'form-control border border-secondary shadow-sm p-2 mb-4 bg-body rounded rounded-0 formheight'}),
                  'email':forms.TextInput(attrs={'class':'form-control border border-secondary shadow-sm p-2 mb-4 bg-body rounded rounded-0 formheight'}),
                  'last_name':forms.TextInput(attrs={'class':' form-control border border-secondary shadow-sm p-2 mb-4 bg-body rounded rounded-0 formheight'}),
                  'first_name':forms.TextInput(attrs={'class':'form-control border border-secondary shadow-sm p-2 mb-4 bg-body rounded rounded-0 formheight'}),
                  'username':forms.TextInput(attrs={'class':'form-control border border-secondary shadow-sm p-2 mb-4 bg-body rounded rounded-0 formheight'}),
            }

            def clean_password(self):
                   password1 = self.cleaned_data.get('password')
                   password2 = self.cleaned_data.get('password_confirmation')
                   if password1 != password2:
                         raise forms.ValidationError("Your passwords do not match")
                   return password1

   #  if not password2:
   #      raise forms.ValidationError("You must confirm your password")
    
        
       
# user registration form
# class UserRegistrationForm(UserCreationForm):
#        class Meta:
#              model = User
#              fields = ['username','first_name','last_name','email','password1','password2']
#              help_texts = {
#             'username': None,
#             'email': None,
#         }

   