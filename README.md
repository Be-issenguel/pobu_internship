# Pobu Internship Management System

A comprehensive web system for schools to manage student internship enrollment, track their final grades, and monitor payment statuses.

---

## Technologies Used

- Python 3.10.10
- Django 4.2.9
- Postgres 13
- HTML5, CSS3, JavaScript

---

## Key Features

- Student enrollment in internship programs.
- Detailed viewing of students' final grades.
- Management and tracking of internship payment statuses per student.
- Administrative panel for managing users, internships, and courses.
- Intuitive interface for school administrators and parents.

---

## How to Install and Run the Project

Follow the steps below to set up and run the project in your local environment.

### 1. Clone the Repository

Open your terminal or PowerShell and execute the following commands:

```
git clone https://github.com/Be-issenguel/pobu_internship.git
```

```
cd pobu_internship
```

### 2. Set Up the Virtual Environment

Create and activate a virtual environment to isolate project dependencies:

# For Linux / macOS

```
python -m venv .venv
```

```
source .venv/bin/activate
```

# For Windows (PowerShell)

```
python -m venv .venv
```

```
.venv\Scripts\Activate.ps1
```

# For Windows (CMD)

```
python -m venv .venv
```

```
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory by copying the content from `.env.tpl`.
Edit the `.env` file and define essential variables such as `SECRET_KEY` and `DEBUG`.

Example `.env`:

```
SECRET_KEY='your_secret_key_here_randomly_generated'
DEBUG=True
```

_In production, `DEBUG` should be False and `SECRET_KEY` a long, complex string_.

### 5. Apply Database Migrations

Create the necessary tables in the database:

```
python manage.py migrate
```

### 6. Create a Superuser (Optional, but Recommended)

To access the Django administration panel, create a superuser:

```
python manage.py createsuperuser
```

Follow the prompts in the terminal to set your username, email, and password.

### 7. Run the Development Server

Start the local server for development:

```
python manage.py runserver
```

The server will be available at: `http://127.0.0.1:8000/`

The administration panel will be at: `http://127.0.0.1:8000/admin/`

## How to Contribute

1. Fork this repository.
2. Create a new branch for your feature or bug fix (git checkout -b feature/your-new-feature).
3. Make your changes and commit them (git commit -m 'feat: Add new feature X').
4. Push your changes to the remote repository (git push origin feature/your-new-feature).
5. Open a Pull Request.

## Licence

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For questions or suggestions, please contact: [Email](beissenguel12@gmail.com) and [LinkedIn](https://www.linkedin.com/in/bernardo-issenguel-39b960174/)
