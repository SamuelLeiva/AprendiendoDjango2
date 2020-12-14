from django.shortcuts import render, redirect
#clases para hacer forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages #clase para usar flash messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm #importamos nuestra form presonalizada

# Create your views here.
#Register view
def register(request):
    if request.method == 'POST': #si recibimos una post request, instancia una form con la data que pasamos como parametro
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #guarda nuestro usuario en nuestra BD
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created! You are now able to login.') #uso de flashed messages
            return redirect('login') #name que le dimos en urls.py
    else:
        form = UserRegisterForm() #instancia una form vacia
    return render(request, 'users/register.html', {'form': form}) #pasamos la form como parametro a nuestra template

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user) #indicamos que las forms tendran la informacion anterior mostrada
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated.') #uso de flashed messages
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
        }

    return render(request, 'users/profile.html', context)
