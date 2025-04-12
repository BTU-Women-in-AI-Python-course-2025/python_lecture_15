# Django 

- **Override User Model** - https://github.com/BTU-Women-AI-Python-course/Btu_Python_Lecture_15/blob/main/override_user_model.md
- **User Registration** - https://github.com/BTU-Women-AI-Python-course/Btu_Python_Lecture_15/blob/main/user_registration.md
- **User Login and Logout** - https://github.com/BTU-Women-AI-Python-course/Btu_Python_Lecture_15/blob/main/user_login_logout.md
- **built-in authentication views** - https://docs.djangoproject.com/en/5.1/topics/auth/default/#module-django.contrib.auth.views
- **Password Reset Token Generator** - https://github.com/django/django/blob/main/django/contrib/auth/tokens.py

 
## 📚 Task: Implement Custom User and Authentication

### 1. Create a Custom User Model:
- Set up a custom user model with fields such as `email`, `first_name`, and `last_name`.
- Use `email` as the unique identifier for authentication instead of the default username.

### 2. Set Up User Authentication:
- Implement a registration form for users to sign up.
- Add login and logout functionality with session management.

### 3. Test the User Model and Authentication:
- Write views to handle user registration, login, and logout.
- Render the forms in templates and handle success or error messages during form submission.
