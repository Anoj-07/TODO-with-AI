from django.shortcuts import render, redirect
from .models import Todo, TodoType
from .forms import TodoForm, TodoTypeForm
from .ai import create_description_with_ai
import json
# Create your views here.

# Home view to display all todos
def home(request):
   
    todos = Todo.objects.all() # Fetch all Todo objects from the database 
    if request.method == 'POST': # for search functionality
        search = request.POST.get('search')
        todos = Todo.objects.filter(name__icontains=search) # name is a attribute of Todo model, icontains is used for case-insensitive search
    return render(request, "index.html", context={"todos": todos})

def delete_all_todos(request):
    Todo.objects.all().delete()  # Deletes all Todo objects from the database
    return redirect('home')  # Redirects to the home view after deletion

# Create a new todo
def create_todo(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'create':
            name = request.POST.get('name')
            description = request.POST.get('description')
            status = request.POST.get('status')

            Todo.objects.create(
                name = name, 
                description = description, 
                status = status
                )
            # Todo.objects.create(**request.POST)
            return redirect('home') 
        
        elif action == 'generate':
            name = request.POST.get('name')
            generated_description = create_description_with_ai(name)
            dic_generated_description = json.loads(generated_description)  # Convert JSON string to Python dictionary
            status = request.POST.get('status')
            # Call the AI function to generate description
            return render(request, 'create.html', context={'generated_description': dic_generated_description.get('description'), 'name': name, 'status': status})
    
    return render(request, 'create.html', context={"message": "Todo created successfully!"})

#update todo
def edit_todo(request, pk):
    todo_obj = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo_obj)  #form object to handle the Todo model
    if request.method == 'POST':
        form = TodoForm(instance=todo_obj, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'edit.html', context={"form": form})

# delete todo
def delete_todo(request, pk):
    tod_obj = Todo.objects.get(id=pk)
    tod_obj.delete()
    return redirect('home')

# # AI
# def create_description_with_ai(request):
#     return render(request, 'create.html')

 # -------------------------------------Todo Types Views------------------------------------------------------------
def todo_types(request):
    todo = TodoType.objects.all()
    return render(request, "todo_types.html", {"todo": todo})

# Todo types create

def create_todo_types(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        TodoType.objects.create(
            name = name
            )
        return redirect('todo_types')
    return render(request, 'todo_type_create.html', context={"message": "Todo Type created successfully!"})

# update todo types
def edit_todo_types(request, pk):
    todo_type_obj = TodoType.objects.get(id=pk)
    form = TodoTypeForm(instance=todo_type_obj) #form object to handle the TodoType model # instance is used to pre-populate the form with existing data
    if request.method == "POST":
        form = TodoTypeForm(instance=todo_type_obj, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('todo_types')
    return render(request, 'todo_type_edit.html', context={"form": form})

def delete_todo_types(request, pk):
    todo_type_obj = TodoType.objects.get(id=pk)
    todo_type_obj.delete()
    return redirect('todo_types')