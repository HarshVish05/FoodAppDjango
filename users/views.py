from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')   # to extract a field from form
            messages.success(request, f'Welcome {username} your account is created')
            return redirect('login')           
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})

@login_required
def profilepage(request):
    return render(request, 'profile.html', )
