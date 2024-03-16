from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms  import CreateuserForm, LoginForm, MyclientForm, UpdateClientForm
from .models import Myclients 
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    
    myclient = Myclients.objects.all()
    
    context = {'myclient': myclient}
    
    return render(request, 'crm/home.html', context = context)

##############################################################################################################


# registration functionality

def register(request):
    form = CreateuserForm()
    if request.method == 'POST':
        form = CreateuserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created')
            return redirect('login')
    context = {'form':form}
    
    return render(request, 'crm/register.html', context = context)

###########################################################################################################

# login functionality

def login(request):
    
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'You have been logged in ')
                return redirect('home')
            
        
        
    context = {'form':form}
    
    
    return render(request, 'crm/login.html', context = context)
        
    
 #########################################################################################################
 
# dashboard functionality

def dashboard(request):
    
    myclient = Myclients.objects.all()
    context = {'myclient': myclient}
    return render(request, 'crm/dashboard.html', context = context)

###########################################################################################################

# Creating a client record functionality

@login_required(login_url='createclient')
def createclient(request):
    
    form = MyclientForm()
    if request.method == 'POST':
        form = MyclientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client created ')
            return redirect('dashboard')
    context = {'form': form}
    
    return render(request, 'crm/createclient.html', context = context)

###############################################################################################################

# Updating a client information 
@login_required(login_url='updateclient')
def updateClient(request, pk):
    
    myclient = Myclients.objects.get(id =pk)
    
    form = UpdateClientForm(instance = myclient)
    if request.method == 'POST':
        form = UpdateClientForm(request.POST, instance=myclient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client updated ')
            return redirect('dashboard')
        
    context = {'form':form}
    
    return render(request, 'crm/updateclient.html', context=context)



#################################################################################################################

# Education Page

def education(request):
    
    return render(request, 'crm/education.html')



#########################################################################################################

# Logout functionality 
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out ')
    return redirect('login')

##########################################################################################################

# Viewing a client detail 

def client_detail(request, pk):
    
    all_clients = Myclients.objects.get(id=pk)
    
    context = { 'all_clients': all_clients}
    
    return render(request, 'crm/client_detail.html', context = context)

#############################################################################################################33

# deleting a client

def client_delete(request, pk):
    
    all_clients = Myclients.objects.get(id=pk)
    all_clients.delete()
    messages.success(request, 'Client deleted ')
    return redirect('dashboard')
    
    
        
    
        
    
           
    
    
    



