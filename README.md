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
```

## Related Screenshots

Application Screenshots are given below:

### Login Page ('accounts/login')

<img width="1680" alt="image" src="https://user-images.githubusercontent.com/78806673/181745923-61ff16a8-4673-4dc5-8f1d-b076b395848e.png">

### Signup Page ('/signup')

<img width="1679" alt="image" src="https://user-images.githubusercontent.com/78806673/181746054-7e244191-cc51-4211-9f21-111c320b3f6e.png">

### User Profile Page ('profile')

<img width="1680" alt="image" src="https://user-images.githubusercontent.com/78806673/181746212-0ed7137f-7c1b-4b47-ac63-7371c2ba3bcb.png">

### User Edit Profile ('profile/edit')

<img width="1679" alt="image" src="https://user-images.githubusercontent.com/78806673/181746382-c4cf5867-e5ff-4e69-99af-f711b357bc67.png">
