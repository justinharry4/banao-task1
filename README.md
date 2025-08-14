# Simple Django Auth Project

This is a simple Django project with sign up, login, and logout functionality. 
The application also exposes a protected dashboard route which users are redirected
to on successful login.

## Setup

1. Clone the repository:

   ```
   git clone https://github.com/justinharry4/banao-task1.git

   cd banao-task1
   ```

2. Set up a virtual environment:

   ```
   # For MacOS/Linux
   python -m venv myenv
   source myenv/bin/activate

   # For Windows:
   myenv\Scripts\activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```
   python manage.py migrate
   ```

5. Start the development server:

   ```
   python manage.py runserver
   ```