from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import View
from product.models import Product,City,Category
from django.contrib.auth.decorators import login_required

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username is Taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email is Taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name)
                    user.save()
                    messages.success(request,'You are now registerd and can login')
                    return redirect('login')
        else:
            messages.error(request,'Password do not match')
            return redirect('register')
    else:
        return render(request,'accounts/signup.html')

# Create your views here.
def user_login(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request,'user_authentications/login.html',{'categories':categories,'products':products})

#     categories = Category.objects.all()
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, ('You have been logged in!'))
#                 return redirect('home')
#     else:
#         form = SignUpForm()

#     context = {'form': form,'categories':categories}
#     return render(request, 'user_authentications/signup.html', context)

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def user_login(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                messages.success(request,'You must be login to create post')
                return redirect(request.POST.get('next'))
            messages.success(request,'You are now login in')    
            return redirect('dashboard')
        
        else:
            messages.error(request,'Invalid Username/Password')
            return redirect('login')
    else:
        return render(request,'accounts/login.html',{'categories':categories})

# def user_login(request):
#     categories = Category.objects.all()
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             # login in to user
#             user = form.get_user()
#             login(request,user)
#             if 'next' in request.POST:
#                 return redirect(request.POST.get('next'))
#                 # return redirect('blog:create')
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request,'user_authentications/login.html',{'form':form,'categories':categories})


def logout_view(request):
    # if request.method == 'POST':/
    auth.logout(request)
    return redirect('home')

@login_required(login_url="/accounts/login/")
def user_dashboard(request):
    return render(request,'accounts/dashboard.html',
        {
            'ram':'ram'
        })

@login_required(login_url="/accounts/login/")
def my_add(request):
    my_products = Product.objects.order_by('-created').filter(author=request.user.id)
    return render(request,'accounts/my_adds.html',
        {
            'my_products':my_products,
        })
