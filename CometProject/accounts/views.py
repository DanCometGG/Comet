from django.shortcuts import render


def signup_view(request):
    return render(render, 'accounts/signup.html')
