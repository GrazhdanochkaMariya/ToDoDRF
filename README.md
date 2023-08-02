# ToDoDRF
A simple RESTful API application for managing a task list (ToDo list) based on the Django (DRF).

## Installation (local)
1. Clone the repository: 
- git clone https://github.com/GrazhdanochkaMariya/ToDoDRF.git
  
2. Add a file with environment variables (.env) to the root of the project

3. Create a virtual environment and activate it:
- python -m venv venv
  - . venv/Scripts/activate - Windows
  - source venv/bin/activate - Linux
  
4. Install dependencies (in virtual environment):
- pip install -r requirements.txt

5. Make and run migrations:
- python manage.py makemigrations
- python manage.py migrate
 
6. Run server:
- python manage.py runserver


## Installation (docker-compose)

1. Clone the repository: 
- git clone https://github.com/GrazhdanochkaMariya/ToDoDRF.git

2. Add a file with environment variables (.env) to the root of the project

3. Build and run the Docker container:
- docker-compose up --build

4. Apply migrations inside the Docker container:
- docker-compose exec web python manage.py migrate


## Endpoints
1. Tasks:
- /tasks/  (Get a list of all tasks. Create a new task.)
- /tasks/user/<int:user_id>/  (Get a list of all user's tasks.)
- /tasks/<int:pk>/  (Get information about a specific task. Update task information. Delete a task.)
- /tasks/<int:pk>/mark-completed/  (Mark a task as completed.)
- /tasks/filter/  (Filter tasks by status.)
  
2. Users
- /users/create (Create a new user.)

## Tests
Run tests:
- pytest

## Contacts
- LinkedIn: https://linkedin.com/in/maria-shakuro
- e-mail: mariyashakuro@gmail.com
