from django.shortcuts import render
from .models import *
def registerpage(request):
    return render(request, "app/register.html")

# View for user registration
def userRegistration(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        # Validate if user already exists
        user_exists = UserProfile.objects.filter(email=email).exists()
        if user_exists:
            message = "User already exists"
            return render(request, 'app/register.html', {'msg': message})
        else:
            if password == cpassword:
                # Create a new UserProfile object
                new_user = UserProfile.objects.create(firstname=fname, lastname=lname, email=email, contact=contact, password=password)
                message = 'User registered successfully'
                return render(request, 'app/login.html', {'msg': message})
            else:
                message = "Password and confirm password do not match"
                return render(request, 'app/register.html', {'msg': message})

# Login page view
def loginpage(request):
    return render(request, 'app/login.html')

# Login user
def loginuser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Checking email id with database
        user = UserProfile.objects.get(email=email)  # Fix typo here from UserProfile.get(email=email)
        if user:
            if user.password == password:
                # We are getting user data in session
                request.session['firstname'] = user.firstname
                request.session['lastname'] = user.lastname
                request.session['email'] = user.email
                return render(request, 'app/home.html')
            else:
                message = 'Password does not match'
                return render(request, 'app/login.html', {'msg': message})
        else:
            message = 'User does not exist'
            return render(request, 'app/register.html', {'msg': message})
