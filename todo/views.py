# from django.shortcuts import render, redirect
# from .models import Todo
# from django.contrib import messages

# # Todo list function
# def todo_list(request):
#     todos = Todo.objects.all()
#     return render(request, 'todo/index.html', {'todos': todos})

# # Create function
# def create_todo(request):

#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         is_complete = request.POST.get('is_complete')

#         if is_complete == 'Complete':
#             date = request.POST.get('completion_date')

#         else:
#             date = None

#         dropdown_submit = request.POST.get('dropdown_submit', False)
#         if dropdown_submit:
#             return render(request, 'todo/index.html', {
#                 'todo': {'name': name,'description': description,'is_complete': is_complete,'date': date}
#             })
#         if not Todo.objects.filter(name=name).exists():
#             todo = Todo(name=name, description=description, is_complete=is_complete, date=date)
#             todo.save() 
#             return redirect('todo_list')
        
#     # print()
#     return render(request, 'todo/index.html')

# # Update function
# def update_todo(request, todo_id):
#     todo = Todo.objects.get(id=todo_id)

#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         is_complete = request.POST.get('is_complete')
#         dropdown_submit = request.POST.get('dropdown_submit', False)

#         todo.name = name
#         todo.description = description
#         todo.is_complete = is_complete
        
#         if todo.is_complete == 'Co Todo.objects.all()
        
#         if not dropdown_submit:
#             messages.success(request, 'Task updated successfully.')
#         return render(request, 'todo/index.html', {'todo': todo})

#     return render(request, 'todo/index.html', {'todo': todo})

# # Delete function
# def delete_todo(request, todo_id):
#     todo = Todo.objects.get(id=todo_id)
#     todo.delete()
#     messages.success(request, "Todo successfully deleted!")
#     return redirect('todo_list')

# # Complete function
# def complete_todo(request, todo_id):
#     todo = Todo.objects.get(id=todo_id)
#     todo.is_complete = 'complete' in request.POST
#     todo.save()
#     messages.success(request, "Todo is_complete updated!")
#     return redirect('todo_list')

from django.shortcuts import *
from .models import Todo
from django.contrib import messages

# Create your views here.

def home(request):
    data = Todo.objects.all()
    return render(request,'todo/index.html',{'data':data})


def addTask(request):

    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        status = request.POST.get('status')

        if status == 'Complete':
            completion_date = request.POST.get('completion_date')

        else:
            completion_date = None

        dropdown_submit = request.POST.get('dropdown_submit', False)
        if dropdown_submit:
            return render(request, 'todo/add.html', {
                'task': {'title': title,'desc': desc,'status': status,'completion_date': completion_date}
            })
        if not Todo.objects.filter(title=title).exists():
            task = Todo(title=title, desc=desc, status=status, completion_date=completion_date)
            task.save() 
            return redirect('home')
        else:
            messages.warning(request, "This item is already in your list")
            return redirect('add')
    print()
    return render(request, 'todo/add.html')
    
def delete_task(request, id):
    item = Todo.objects.get(id=id)             

    if request.method == "POST":
        if request.POST.get("confirm") == "Yes":
            item.delete()  
            return redirect('home')
        return redirect('home') 
    
    return render(request, 'todo/delete.html', {'item': item})

def editTask(request, id):
    task = Todo.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        status = request.POST.get('status')
        dropdown_submit = request.POST.get('dropdown_submit', False)

        task.title = title
        task.desc = desc
        task.status = status
        
        if task.status == 'Complete':
            task.completion_date = request.POST.get('completion_date')
    
        else:   
            task.completion_date = None

        if not dropdown_submit:
            task.save()
        
        if not dropdown_submit:
            messages.success(request, 'Task updated successfully.')
        return render(request, 'todo/edit.html', {'task': task})

    return render(request, 'todo/edit.html', {'task': task})

def viewTask(request,id):
    task = Todo.objects.get(id=id)
    return render(request,'todo/view.html',{'task':task})