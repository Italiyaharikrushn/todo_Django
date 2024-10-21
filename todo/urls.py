# from django.urls import path
# from . import views

# urlpatterns = [
#     path("todo/", views.todo_list, name="todo_list"),
#     path("todo/create/", views.create_todo, name="create_todo"),
#     path("todo/delete/<int:todo_id>/", views.delete_todo, name="delete_todo"),
#     path("todo/update/<int:todo_id>/", views.update_todo, name="update_todo"),
#     path("todo/complete/<int:todo_id>/", views.complete_todo, name="complete_todo"),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('AddTask/',views.addTask,name='add'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('update/<int:id>/', views.editTask, name='edit_task'),
    path('view/<int:id>/', views.viewTask, name='view_task'),
]


#<!DOCTYPE html>
# <html lang="en">

# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Todo List</title>
#     <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" />
#     <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             background-color: #f4f4f4;
#             margin: 0;
#             padding: 0;
#         }

#         .container {
#             width: 80%;
#             margin: auto;
#             overflow: hidden;
#         }

#         h1 {
#             background-color: #333;
#             color: #fff;
#             padding: 10px 0;
#             text-align: center;
#             margin-bottom: 20px;
#         }

#         ul {
#             list-style-type: none;
#             padding: 0;
#         }

#         li {
#             background: #fff;
#             margin: 5px 0;
#             padding: 10px;
#             border-left: 4px solid #333;
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#         }

#         .actions {
#             display: flex;
#         }

#         .actions a {
#             margin-left: 10px;
#             text-decoration: none;
#             color: #333;
#             padding: 5px;
#             border-radius: 3px;
#             border: 1px solid #333;
#         }

#         a:hover {
#             background-color: #333;
#             color: #fff;
#         }

#         .create-form,
#         .update-form {
#             margin-top: 20px;
#             background: #fff;
#             padding: 20px;
#             border-radius: 5px;
#             box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
#         }

#         .create-form input[type="text"],
#         .update-form input[type="text"] {
#             width: 90%;
#             padding: 10px;
#             margin-bottom: 10px;
#         }

#         .create-form button,
#         .update-form button {
#             background-color: #333;
#             color: white;
#             border: none;
#             padding: 10px;
#             cursor: pointer;
#         }

#         .create-form button:hover,
#         .update-form button:hover {
#             background-color: #555;
#         }

#         /* Modal Styling */
#         .modal {
#             display: none;
#             position: fixed;
#             z-index: 1;
#             left: 0;
#             top: 0;
#             width: 100%;
#             height: 100%;
#             background-color: rgba(0, 0, 0, 0.4);
#             padding-top: 60px;
#         }

#         .modal-content {
#             background-color: #fefefe;
#             margin: 5% auto;
#             padding: 20px;
#             border: 1px solid #888;
#             height: auto;
#             width: 20%;
#             /* top: 0; */
#         }

#         .close {
#             color: #aaa;
#             float: right;
#             font-size: 28px;
#             font-weight: bold;
#         }

#         .close:hover,
#         .close:focus {
#             color: black;
#             text-decoration: none;
#             cursor: pointer;
#         }

#         .cancelbtn,
#         .deletebtn {
#             padding: 10px;
#             color: white;
#             border: none;
#             margin-right: 10px;
#         }

#         .cancelbtn {
#             background-color: #555;
#         }

#         .deletebtn {
#             background-color: #d63131;
#         }

#         /* Checkbox */
#         .checkbox {
#             display: block;
#             font-size: 16px;
#             cursor: pointer;
#         }

#         .checkbox input {
#             margin-right: 5px;
#             cursor: pointer;
#         }

#         .alert {
#             padding: 15px;
#             margin-bottom: 20px;
#             border: 1px solid transparent;
#             border-radius: 4px;
#         }

#         .alert-success {
#             color: #3c763d;
#             background-color: #dff0d8;
#             border-color: #d6e9c6;
#         }

#         .alert-error {
#             color: #a94442;
#             background-color: #f2dede;
#             border-color: #ebccd1;
#         }

#         a.button {
#             background-color: #333;
#             color: white;
#             border: none;
#             padding: 8px;
#             cursor: pointer;
#         }

#         a.button:hover {
#             background-color: #555;
#             color: #fff;
#         }

#         .update-form a {
#             background-color: #333;
#             color: white;
#             border: none;
#             padding: 8px;
#             cursor: pointer;
#         }

#         .update-form a:hover {
#             background-color: #555;
#         }
#     </style>
# </head>

# <body>
    
#     <section>
#         <div class="container">
#             <h1>Todo List</h1>
#         </div>
#     </section>

#     {% if not todo %}
#     <section>
#         <div class="container">
#             <div class="create-form">
#                 <h2>Add New Todo</h2>
#                 <form id="todo_form" class="todo-form mb-3" method="POST" action="{% url 'create_todo' %}">
#                     {% csrf_token %}
#                     <input type="text" name="name" id="todotext" placeholder="Add a Task." value="{{todo.name}}" required/>
#                     <input type="text" name="description" id="tododesc" placeholder="Task Description" value="{{todo.description}}" required />
                    
#                     <select name="is_complete" id="todo_status">
#                         <option value="Incomplete" {% if todo.is_complete == 'Incomplete' %}selected{% endif %}>Incomplete</option>
#                         <option value="Complete" {% if todo.is_complete == 'Complete' %}selected{% endif %}>Complete</option>
#                     </select>
            
#                     {% if todo.is_complete == 'Complete' %}
#                     <div id="completion-date-field">
#                         <input type="date" id="tododate" name="completion_date" value="{{todo.date}}" required/>
#                     </div>
#                     {% endif %}<br><br>
#                     <button id="addlist"><i class="fa fa-plus"></i> Add Task</button>
#                 </form>
#             </div>
#         </div>
#     </section>
#     {% endif %}

#     {% if todo %}
#     <section>
#         <div class="container">
#             <div class="update-form">
#                 <h2>Update Todo</h2>
#                 <form id="todo-form" class="todo-form" method="post" action="{% url 'update_todo' todo.id %}">
#                     {% csrf_token %}
#                     <input type="text" name="name" id="todotext" placeholder="Add a Task." value="{{todo.name}}" required />
#                     <input type="text" name="description" id="tododesc" placeholder="Task Description" value="{{todo.description}}" required />
                    
#                     <select name="is_complete" id="todostatus">
#                         <option value="Incomplete" {% if todo.is_complete == 'Incomplete' %}selected{% endif %}>In-complete</option>
#                         <option value="Complete" {% if todo.is_complete == 'Complete' %}selected{% endif %}>Complete</option>
#                     </select><br>
            
#                     {% if todo.is_complete == 'Complete' %}
#                     <div id="completion-date-field">
#                         <input type="date" id="tododate" name="completion_date" value="{{todo.date}}" required/>
#                     </div>
#                     {% endif %}<br>
            
#                     <a href="{% url 'todo_list' %}"><i class="fa-solid fa-arrow-left"></i> Back</a>
#                     <button type="submit"><i class="fas fa-edit"></i> Update Todo</button>
#                 </form>
#             </div>
#         </div>
#     </section>
#     {% endif %}
    
#     <section>
#         <div class="container">
#             <ul>
#                 {% for todo in todos %}
#                 <li>
#                     <div>
#                         <strong>{{ todo.name }}</strong>: {{ todo.description }} - {{todo.is_complete}}
#                         <p>{{ todo.date }}</p>
#                     </div>
#                     <div class="actions">
#                         <a href="{% url 'update_todo' todo.id %}"><i class="fas fa-edit"></i> Update</a>
#                         <a href="#" onclick="showDeleteModal('{{ todo.id }}')"><i class="fas fa-trash"></i> Delete</a>
#                     </div>

#                     <div id="{{ todo.id }}" class="modal">
#                         <div class="modal-content">
#                             <span class="close" onclick="hideDeleteModal('{{ todo.id }}')"><i class="fas fa-window-close"></i></span>
#                             <p>Are you sure you want to delete?</p>
#                             <form method="POST" action="{% url 'delete_todo' todo.id %}">
#                                 {% csrf_token %}
#                                 <button type="button" class="cancelbtn" onclick="hideDeleteModal('{{ todo.id }}')">Cancel</button>
#                                 <button type="submit" class="deletebtn">Delete</button>
#                             </form>
#                         </div>
#                     </div>
#                 </li>
#                 {% endfor %}
#             </ul>
#         </div>
#     </section>

#     <script>
#         function showDeleteModal(id) {
#             document.getElementById(id).style.display = 'block';
#         }

#         function hideDeleteModal(id) {
#             document.getElementById(id).style.display = 'none';
#         }

#     // update todo
#         document.addEventListener('DOMContentLoaded', function () {
#             const statusSelect = document.getElementById('todostatus');
#             const userForm = document.getElementById("todo-form");
#             const hiddenInput = document.createElement('input');
            
#             function toggleCompletionDate() {
#                 hiddenInput.type = 'hidden';
#                 hiddenInput.name = 'dropdown_submit';
#                 hiddenInput.value = 'true'; 

#                 userForm.appendChild(hiddenInput);
#                 userForm.submit();
#             }

#             statusSelect.addEventListener('change', toggleCompletionDate);
#         });


#         document.addEventListener('DOMContentLoaded', function () {
#             const statusSelect = document.getElementById('todo_status');
#             const userForm = document.getElementById("todo_form");
#             const hiddenInput = document.createElement('input');
            
#             function toggleCompletionDate() {
#                 hiddenInput.type = 'hidden';
#                 hiddenInput.name = 'dropdown_submit';
#                 hiddenInput.value = 'true'; 

#                 userForm.appendChild(hiddenInput);
#                 userForm.submit();
#             }

#             statusSelect.addEventListener('change', toggleCompletionDate);
#         });
#     </script>

# </body>
# </html>