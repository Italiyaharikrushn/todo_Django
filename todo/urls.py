from django.urls import path
from . import views

urlpatterns = [
    path("todo/", views.todo_list, name="todo_list"),
    path("todo/create/", views.create_todo, name="create_todo"),
    path("todo/delete/<int:todo_id>/", views.delete_todo, name="delete_todo"),
    path("todo/update/<int:todo_id>/", views.update_todo, name="update_todo"),
    path("todo/complete/<int:todo_id>/", views.complete_todo, name="complete_todo"),
]

# <section>
#         <div class="container">
#             <div class="update-form">
#                 <h2>Update Todo</h2>
#                 <form method="POST" action="{% url 'update_todo' todo.id %}" id="my-form">
#                     {% csrf_token %}
#                     <input id="name" type="text" name="name" value="{{ todo.name }}" placeholder="Enter Name"
#                         required><br>
#                     <input id="description" type="text" name="description" value="{{ todo.description }}"
#                         placeholder="Enter Description" required><br>

#                     <label for="completeCheck">
#                         <input type="checkbox" id="myCheckbox" name="is_complete" value="checked" 
#                         {% if todo.is_complete %}checked {% else %}unchecked{% endif %}>
#                         Complete</label>

#                         {% if todo.is_complete %}
#                             <input type="date" name="completion_date">
#                         {% endif %}
#                         <br><br>
#                         <a href="{% url 'todo_list' %}" class="btn btn-secondary">Back to Home</a>
#                     <button type="submit" value="submit"><i class="fas fa-save"></i> Update Todo</button>
#                 </form>

#                 <form id="todo-form" action="{% url 'update_todo' todo.id %}" class="todo-form mb-3" method="post">
#                     {% csrf_token %}
#                     <input type="text" name="name" id="todotext" placeholder="Add a Task." value="{{ todo.name }}" required/>
#                     <input id="description" type="text" name="description" value="{{ todo.description }}" placeholder="Enter Description" required><br>
            
#                     <label for="todostatus">Status:</label>
#                     <select name="is_complete" id="todostatus">
#                       <option value="Incomplete" {% if todo.is_complete == 'Incomplete' %}selected{% endif %}>Incomplete</option>
#                       <option value="Complete" {% if todo.is_complete == 'Complete' %}selected{% endif %}>Complete</option>
#                     </select>
            
#                     {% if todo.is_complete == 'Complete' %}
#                     <div id="completion-date-field">
#                       <label for="tododate">Completion Date:</label>
#                       <input type="date" id="tododate" name="completion_date" value="{{todo.date}}" required/>
#                     </div>
#                     {% endif %}
            
#                     <button id="addlist">Add Task</button>
#                   </form >
#                   <form id="todo-form" class="mt-3" action="{% url 'todo_list' %}">
#                     <button id="addlist">Want to see your Task ?</button>
#                   </form>
#             </div>
#         </div>
#     </section>

# document.addEventListener('DOMContentLoaded', function () {
#             const status = document.getElementById('myCheckbox');
#             const userForm = document.getElementById("my-form");

#             function toggleCompletionDate() {
#                 userForm.submit()
#             }
#             status.addEventListener('change', toggleCompletionDate);
#         });