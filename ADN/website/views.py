from telnetlib import AUTHENTICATION
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.db.models import Q 
from .models import Apparel
from .forms import AddApparelForm

#pagination 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):

    # apparels = Apparel.objects.order_by('id')
    apparels = Apparel.objects.order_by('id')
    #pagination
    p = Paginator(apparels, 10)
    page = request.GET.get('page')
    apparel_list = p.get_page(page)

    # chek to see if user if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request,"Invalid credentials")
            return redirect('home')  
    else:
        return render(request, 'home.html', {'apparels':apparels, 'apparel_list':apparel_list})
    
def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')

def add_apparel(request):
    form = AddApparelForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                apparel = form.save()
                messages.success(request,"Apparel has been added")
                return redirect('home')
        return render(request, 'add_apparel.html', {'form':form})
    else:
        messages.success(request,"You must be logged in")
        return redirect('home')

def apparel(request, apparel_id):
    if request.user.is_authenticated:
        apparel = Apparel.objects.get(id=apparel_id)
        return render(request, 'apparel.html', {'apparel':apparel})
    else:
        messages.success(request,"You must be logged in")
        return redirect('home')
    
def delete_apparel(request, pk):
    if request.user.is_authenticated:
        confirm_delete = Apparel.objects.get(id=pk)
        return render(request, 'confirm_delete.html', {'confirm_delete':confirm_delete})
    else:
        messages.success(request,"You must be logged in")
        return redirect('home')
    
def confirm_delete(request, pk):
    if request.user.is_authenticated:
        delete_it2 = Apparel.objects.get(id=pk)
        delete_it2.delete()
        messages.success(request,"Apparel has been deleted")
        return redirect('home')
    else:
        messages.success(request,"You must be logged in")
        return redirect('home')

def update_apparel(request, pk):
    if request.user.is_authenticated:
        apparel = Apparel.objects.get(id=pk)
        form = AddApparelForm(request.POST or None, instance=apparel)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request,"Apparel has been updated")
                return redirect('home')
        return render(request, 'update_apparel.html', {'form':form})
    else:
        messages.success(request,"You must be logged in")
        return redirect('home')