from django.shortcuts import render
from django.views.generic import View
from user.forms import LogInForm,UserRegistrationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from user.models import UserRegistrationModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.utils.decorators import method_decorator
from computer.models import ComputerSpecification,ComputerBrand
# from django.http import HttpResponseRedirect


# view for login
class LoginView(View):
    template_name = 'user/login.html'
    form_class = LogInForm
    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request,user)
                return redirect('dashboard')
        return render(request,self.template_name,{'form': form,'message':'Login failed please enter correct username and password'})

# view for dashboard
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DashBoardView(TemplateView):
    template_name='user/dashboard.html'

# view for list of users
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserListView(ListView):
    model = User    
    template_name = 'user/user_list.html'


# view for user logout
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserLogoutView(View):  
    def get(self,request):
        logout(request)
        return redirect('userlogin')


# view for user registration
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserRegistrationView(CreateView):
    template_name = 'user/user_registration.html'
    form_class = UserRegistrationForm

    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = make_password(form.cleaned_data['password'])
            registration=UserRegistrationModel(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            registration.save()
            return redirect('dashboard')
        return render(request,self.template_name,{'form': form,'message':'Login failed please enter correct username and password'})



class UserStatusView(View):
    def get(self,request,id):
        try:
            user = User.objects.get(id=id)
            print(id, 9090)
            if user.is_active == True:
                user.is_active = False
            else:
                user.is_active = True
            user.save()
            return redirect('userlist')
        except Exception as e:
            print(e,909066)

 
    

class UserSettingsView(View):
    def get(self,request):
        form_cs = ComputerSpecification.objects.all()
        form_cb = ComputerBrand.objects.all()
        return render(request,'user/settings.html',{'form_cs':form_cs,'form_cb':form_cb})
   
   



