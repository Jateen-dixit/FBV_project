from django.shortcuts import render, redirect
from .forms import LaptopModelForm
from .models import Laptop
# Create your views here.



def AddLaptopView(request):
    form = LaptopModelForm()
    if request.method == 'POST':
        form = LaptopModelForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('show_order')
    context = {'form': form}
    template_name = 'Firstapp/addorder.html'
    return render(request, template_name, context)

def ShowLaptopView(request):
    lap_obj = Laptop.objects.all()
    template_name = 'Firstapp/showorders.html'
    context = {'lap_obj': lap_obj}
    return render(request, template_name, context)

def UpdateLaptopView(request,id):
    lap_obj = Laptop.objects.get(id=id)
    form = LaptopModelForm(instance=lap_obj)
    if request.method == 'POST':
        form = LaptopModelForm(request.POST, form)
        if form.is_valid():
            form.save()
            return redirect('show_order')
    template_name = 'Firstapp/addorder.html'
    context = {'form': form}
    return render(request, template_name, context)

def DeleteLaptopView(request,id):
    lap_obj = Laptop.objects.get(id=id)
    if request.method == 'POST':
        lap_obj.delete()
        return redirect('show_order')
    template_name = 'Firstapp/delete.html'
    context = {'lap_obj': lap_obj}
    return render(request, template_name, context)
