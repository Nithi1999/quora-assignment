# quora-assignment
This is a Django-based web application inspired by Quora. It allows users to register, log in, post questions, view and answer questions, like answers, and delete their own questions.

## Tech Stack
- **Python**: 3.11
- **Django**: 5.2
- **Database**: SQLite (Django default)
- **Frontend**: Basic HTML with Django templating

## Features
1. **User Registration**: Anyone can create an account with a username and password.
2. **User Login/Logout**: Secure authentication for all users.
3. **Post Questions**: Logged-in users can post questions.
4. **View Questions**: Displays all questions from all users.
5. **Answer Questions**: Users can answer any question.
6. **Like Answers**: Users can like or unlike answers.
7. **Delete Questions**: Users can delete their own questions.

## Setup Instructions
### Prerequisites
- Python 3.11
- pip
- Virtualenv (recommended)

### Installation
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd assignment

2. **Set Up Virtual Environment**:
    ```bash
    python3 -m venv env_name
    source env_name/bin/activate #for Ubuntu.| Windows: env_name\Scripts\activate

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt

4. **Apply Migrations**:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate

5. **Run the Server**:
    ```bash
    python3 manage.py runserver