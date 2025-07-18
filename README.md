# 📝 Django Learning: ToDo App with AI Integration

Welcome to the **Django Learning Project**, a simple yet powerful **ToDo application** enhanced with **AI capabilities**. This project is built using the Django web framework and demonstrates core features like CRUD operations, model relationships, and form handling—while also showcasing AI-assisted functionality to help generate or analyze tasks.

---

## 🚀 Features

- 🔐 User-friendly ToDo management (Create, Read, Update, Delete)
- 🧠 **AI Integration** for smart task description generator (`ai.py`)
- 🖥️ Clean UI using Django templates and partials
-  Enable filtering and search
- 📁 Modular structure following Django best practices
- 💾 Persistent storage using SQLite (default)

---

## 📁 Project Structure
```
Django_learning/
├── .gitignore
├── base/
│   ├── __init__.py
│   ├── admin.py
│   ├── ai.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   ├── 0002_todo_type.py
│   │   └── 0003_rename_todo_type_todotype.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── README.md
├── requirements.txt
├── templates/
│   ├── create.html
│   ├── edit.html
│   ├── index.html
│   ├── nav.html
│   ├── todo_type_create.html
│   ├── todo_type_edit.html
│   └── todo_types.html
└── todo_project/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

## 🧠 AI Functionality

The `base/ai.py` file contains logic for basic AI integration (e.g., natural language generation of task suggestions or classification). You can extend this with models like OpenAI, Gemini, or Hugging Face APIs.

---

#
## 📸 demo video
https://github.com/user-attachments/assets/b60271a7-85af-4a10-929d-41f1a45e9b86

### Tech Stack
```
Backend: Django

Frontend: HTML5, Django Templating

Database: SQLite3

AI: groq AI
```
### ✅ To-Do List for Future Enhancements
```
- Add user authentication

- Integrate OpenAI or Gemini API for smart task creation

- Add task deadlines and priority

- Make the UI responsive with  Bootstrap
```
## 💻 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Anoj-07/Django_learning.git
cd Django_learning
```
### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5.Run the Development Server
```bash
python manage.py runserver
```
## 🔗 API Endpoints
```
The following routes are available in the ToDo + AI Django application:

| Method     | URL Pattern                     | Description                                       |
|------------|----------------------------------|--------------------------------------------------|
| GET        | `/`                              | Home page showing all ToDo items                 |

| GET, POST  | `/create/todo/`                  | Create a new ToDo task                           |

| GET, POST  | `/edit/todo/<int:pk>/`           | Edit an existing ToDo task by its primary key    |

| POST       | `/delete/todo/<int:pk>/`         | Delete a specific ToDo by its primary key        |

| POST       | `/delete/all/todos/`             | Delete **all** ToDo items                        |

| GET, POST  | `/admin/`                        | Access the Django admin panel                    |

<!-- | GET, POST  | `/create/description/`      | *(Optional)* Generate a ToDo description using AI |

> Note: Replace `<int:pk>` with the numeric ID of the ToDo item.
```

### 📜 License
This project is open-source and available under the MIT License.

### Author
Anoj Rawal
📫 anojrawal.039.adtu@gmail.com
🌐 LinkedIn (Add your profile here)

### 🤝 Contributions
Contributions, suggestions, and issues are welcome! Feel free to open a pull request or start a discussion.

```
Let me know if you'd like to include AI model usage instructions (e.g., Gemini/OpenAI) or a deployment guide (e.g., Heroku or Railway).
```
