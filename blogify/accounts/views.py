from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.



def account_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid(): #  checks if the form valid or invalid
            user = form.save()
            login(request, user)
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", { 'form' : form })


def account_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST: # redirect to next position
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:list")

    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {'form' : form})

def account_logout(request):
    if request.method == "POST":
        logout(request) # logout the current user
        return redirect ("posts:list")
