from django.shortcuts import render, redirect
from .models import User, Profile, Movie

# Create your views here.
# =================================================================
# template renders
# =================================================================
def login_page(request): #renders the login page template
    return render(request, 'User_app/login_page.html')

def register_page(request): #renders the register page template
    return render(request, 'User_app/register_page.html')



# =================================================================
# POST request's
# =================================================================
def register_account(request): #this function creates the account
    if request.method == 'POST':
        account_info = {
            "first_name": request.POST['first_name'],
            "last_name": request.POST['last_name'],
            "email": request.POST['email'],
            "password": request.POST['password']
        }

        result = User.objects.register(account_info)

        if result['errors'] == None:
            # =================
            # storing session info to pull on the home page
            # =================
            request.session['email'] = result['user'].email
            request.session['name'] = result['user'].first_name
            request.session['user'] = result['user'].id
            request.session['action'] = "registered"
            return redirect('/home')
        else:
            print result['errors']
            return redirect("/register")


def log_user_in(request):
    if request.method == 'POST':
        login_info = {
            "email": request.POST['email'],
            "password": request.POST['password']
        }

        result = User.objects.login(login_info)

        if result['errors'] == None:
            request.session['email'] = result['user'].email
            request.session['name'] = result['user'].first_name
            request.session['user'] = result['user'].id
            request.session['action'] = "logged in"
            return redirect('/home')
        else:
            print result['errors']
            return redirect('/login')

def home(request):
    if 'user' not in request.session:
        return redirect('/register')
    username = request.session['name']
    context = {
    'username' : username
    }
    print request.session['user']
    return render(request, "User_app/home.html", context)

def profile(request):
    if 'user' not in request.session:
        return redirect('/register')
    username = request.session['name']
    profile = Profile.objects.filter(user_id = User.objects.get(id = request.session['user']))
    context = {
    'profile' : profile,
    'username' : username
    }
    print request.session['user']
    return render(request, "User_app/profile.html", context)

def createProfile(request):
    if request.method == 'POST':
        profile = Profile.objects.create(birthday = request.POST['birthday'], hometown = request.POST['hometown'], country = request.POST['country'], user_id = User.objects.get(id = request.session['user']))
    return redirect('/profile')

def logout(request):
    request.session.clear()
    return redirect('/login')



























# end
