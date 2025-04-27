from django.shortcuts import render,redirect
from .forms import TodoForm
from .models import Todo_model
def TodoView(request):
    if request.method == "POST":
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo_form.html', {'form':form})
def todo_list(request):
        todos=Todo_model.objects.all()
        return render(request,'todo_list.html',{'todos':todos})
