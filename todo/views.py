from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from django.http import HttpResponse
# Todo list function
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

# Create function
# def create_todo(request):

#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         is_complete = 'complete' in request.POST
#         # date = request.POST.get('completion_date') if is_complete else None

#         if is_complete == 'Complete':
#             date = request.POST.get('completion_date')

#         else:
#             date = None
#         Todo.objects.create(name=name, description=description, date=date, is_complete=is_complete)

#         try:
#             return redirect('todo_list')
#         except Exception as e:
#             messages.error(request, f'Error updating todo : {str(e)}')
#     return redirect('todo_list')

# Update function
# def update_todo(request, todo_id):
#     todo = Todo.objects.get(id=todo_id)
    
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')

#         is_complete = request.POST.get('is_complete') == 'checked'
        
#         todo.name = name
#         todo.description = description
#         todo.is_complete = is_complete
        
#         if todo.is_complete:
#             todo.date = request.POST.get('completion_date')
#         else:
#             todo.date = None

#         todo.save()
        
#         # return redirect('todo_list')
#         return render(request, 'todo/index.html', {'todo': todo})

#     return render(request, 'todo/index.html', {'todo': todo})

# Delete function
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    messages.success(request, "Todo successfully deleted!")
    return redirect('todo_list')

# Complete function
def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.is_complete = 'complete' in request.POST
    todo.save()
    messages.success(request, "Todo is_complete updated!")
    return redirect('todo_list')

def update_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        is_complete = request.POST.get('is_complete')
        dropdown_submit = request.POST.get('dropdown_submit', False)

        # Convert string value to boolean
        todo.is_complete = True if is_complete == "Complete" else False
        
        todo.name = name
        todo.description = description
        
        if todo.is_complete:
            todo.date = request.POST.get('completion_date')
        else:
            todo.date = None

        if not dropdown_submit:
            todo.save()
            messages.success(request, 'Todo updated successfully.')

        return render(request, 'todo/index.html', {'todo': todo})

    return render(request, 'todo/index.html', {'todo': todo})

def create_todo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        is_complete = request.POST.get('is_complete')
        date = request.POST.get('completion_date') if is_complete == 'Complete' else None

        if not Todo.objects.filter(name=name).exists():
            task = Todo(name=name, description=description, is_complete=(is_complete == 'Complete'), date=date)
            task.save() 
            messages.success(request, "Todo created successfully.")
            return redirect('todo_list')
        else:
            messages.warning(request, "This item is already in your list.")
            return redirect('todo_list')

    return render(request, 'todo/index.html')
