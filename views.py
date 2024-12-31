from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        # Handle login logic here
        return redirect('dashboard')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        # Handle signup logic here
        return redirect('dashboard')
    return render(request, 'signup.html')

def dashboard(request):
    return render(request, 'second_page.html')
