from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_list_or_404, redirect
from. models import ReceiverShipCase
from .forms import ReceiverShipCaseForm



def case_list(request):
    
    caselist= ReceiverShipCase.objects.all()
    
    return render(request, 'receiveship/case_list.html', {'caselist': caselist})
    
    
    
    

def case_detail(request, pk):
    
    #case = get_list_or_404(ReceiverShipCase, pk=pk)
    case = ReceiverShipCase.objects.get(id=pk)
    
    return render(request, 'receiveship/case_detail.html', {'case':case})

    

def case_create(request):
    form = ReceiverShipCaseForm()
    if request.method == 'POST':
        form = ReceiverShipCaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    return render(request, 'receiveship/case_create.html', {'form':form})
        
    

def case_update(request,pk):
    
    #case = get_list_or_404(ReceiverShipCase, id=pk)
    case =ReceiverShipCase.objects.get(id=pk)
    form = ReceiverShipCaseForm(instance= case)
    if request.method == 'POST':
        form = ReceiverShipCaseForm(request.POST, instance = case)
        if form.is_valid():
            form.save()
            return redirect('case_list')
    
        
    return render(request, 'receiveship/case_update.html',{'form':form})
        
    


def case_delete(request, pk):
    #case = get_list_or_404(ReceiverShipCase, pk = pk)
    case = ReceiverShipCase.objects.get(id=pk)
    case.delete()
    return redirect('case_list')
    #return render(request, 'receiveship/case_list', {'case':case})
   





def record(request):
    
    case = ReceiverShipCase.objects.all()
    
    return render(request, 'receivership/record.html', {'case':case})
    
