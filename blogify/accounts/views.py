from django.shortcuts import render

# Create your views here.



def account_signup(request):
    return render(request, "accounts/signup.html")