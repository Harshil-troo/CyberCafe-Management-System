from django.shortcuts import render, redirect, get_object_or_404
from .models import Computer
from .forms import ComputerForm

def computer_list(request):
    computers = Computer.objects.all()
    return render(request, 'device/computer_list.html', {'computers': computers})

def computer_create(request):
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('computer_list')
    else:
        form = ComputerForm()
    return render(request, 'device/computer_form.html', {'form': form})

def computer_update(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    if request.method == 'POST':
        form = ComputerForm(request.POST, instance=computer)
        if form.is_valid():
            form.save()
            return redirect('computer_list')
    else:
        form = ComputerForm(instance=computer)
    return render(request, 'computer_form.html', {'form': form})

def computer_delete(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    computer.delete()
    return redirect('computer_list')