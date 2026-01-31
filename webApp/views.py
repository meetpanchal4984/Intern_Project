from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    return render(request,"index.html")

def shop(request):
    return render(request,"shop.html")

def blog(request):
    return render(request,"blog.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def cart(request):
    return render(request,"cart.html")

def sproduct1(request):
    return render(request,"sproduct1.html")

def sproduct2(request):
    return render(request,"sproduct2.html")

def sproduct3(request):
    return render(request,"sproduct3.html")

def sproduct4(request):
    return render(request,"sproduct4.html")

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request, 'login.html')

def UserRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user = User.objects.filter(Email=email)

        if user:
            message = "alrady"
            return render(request, 'signup.html', {'msg' : message})
        else:
            if password == cpassword:
                newuser = User.objects.create(Fristname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                message = "register successfully"
                return render(request, 'login.html', {'msg' : message})
            else:
                message = "password and comform password does not match"
                return render(request, 'signup.html', {'msg' : message})
            
def UserLogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Checking email with database
        user = User.objects.get(Email=email)

        if user:
            if user.Password == password:
                # We are getting user data in session
                request.session['Fristname'] = user.Fristname
                request.session['Lastname'] = user.Lastname
                request.session['Email'] = user.Email
                message = " Successfully"
                return render(request, 'index.html', {'msg' : message})
            else:
                message = "password does not match"
                return render(request,'login.html', {'msg' : message})
        else:
            message = "User does not exist"
            return render(request, 'register.html', {'msg' : message})
        
def add(request):
    return render(request, "add_product.html")

def add_product(request):
    if request.method == "POST":
        product_name = request.POST['pname']
        product_image = request.FILES['iname']
        product_price = request.POST['price']

        create = SaveProduct.objects.create(Product_Name=product_name,Product_Image=product_image,Product_Price=product_price)
        return render(request,"add_product.html")