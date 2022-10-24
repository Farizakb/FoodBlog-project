from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,View

from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.sites.shortcuts import get_current_site 
from .tasks import send_confirmation_mail
from .forms import LoginForm, RegisterForm

from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from account.tokens import account_activation_token

User = get_user_model()

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'


class UserRegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')
    
    
    def form_valid(self, form):
        result = super().form_valid(form)
        
        send_confirmation_mail(user = self.object, current_site=get_current_site(self.request))
        
        return result


class ActiveAccountView(View):

    def get(self, request, *args, **kwargs):
        uidb64 = kwargs['uidb64']
        token = kwargs['token']
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Your account activated!')
            return redirect(reverse_lazy('login_page'))
        else:
            messages.warning(request, 'Something went wrong!')
            return redirect(reverse_lazy('login_page'))







@login_required
def user_profile(request):
    
    
    return render(request, 'account/user_profile.html')

def user_register(request):
    return render(request, 'account/register.html')


def user_login(request):
    next_page = request.GET.get('next_page','/')
    form = LoginForm()
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"] 
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.add_message(request, messages.SUCCESS, 'Ugurla login oldunuz')
                return redirect(next_page)
            else:
                messages.add_message(request, messages.ERROR, 'Username ve ya password sehvdir!')
            
            
    context ={
        "form":form
    }
    return render(request, 'account/login.html',context)


def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Log out oldunuz')
    
    return redirect("login")