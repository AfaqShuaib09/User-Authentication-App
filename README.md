# User-Authentication-App

User-Authentication-App is a simple web application that allows users to signup, login and logout and also allows them to create profiles and edit their profiles.

## Features
- User Signup
- Login and logout
- Create profile
- View and edit their profile

## Testing User-Authentication-App

### Clone the repository
- Clone the repository from [GitHub](https://github.com/AfaqShuaib09/User-Authentication-App)

```bash
git clone https://github.com/AfaqShuaib09/User-Authentication-App
```

### Navigate to the directory
- Change your current pwd (Present Working Direvctory) to the directory where the repository is cloned

```bash
cd User-Authentication-App
```

### Create Virtual Environment
- In the project directory, you can create a virtual environment by running the following command in the terminal:

```bash
   python3 -m venv env
```

- Activate the virtual environment by running the following command in the terminal:
```bash
   source env/bin/activate
```

- Install the dependencies by running the following command in the terminal:
```bash
   pip install -r requirements.txt
```

- Make migrations by running the following command in the terminal:
```bash
   python3 manage.py makemigrations
```

- Apply migrations by running the following command in the terminal:
```bash
   python3 manage.py migrate
```

### Run the Django App
```bash
    python3 manage.py runserver
