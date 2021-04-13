Problem Statement

You are asked to develop an e-commerce website for online book sale. It should provide the users with a catalog of different books available for purchase in the bookstore. A shopping cart should be provided to the users. The system should be implemented using a 3-tier approach.

In order to create an ecommerce website for online book sale, I have used the Django framework (Python 3) as the application server of the website. Similarly, PostgreSQL is implemented as the database. Bootstrap and jinja template engine are used as the front end framework.

Here are some instructions to clone this project and run it.

- git clone this project.
- Activate the virtual environment using source bin/activate command in the working directory.
- Install Django using "python -m pip install Django" command.
- python manage.py makemigrations.
- python manage.py migrate
- python manage.py runserver

Follow the link for the local host http://127.0.0.1:8000/.

Create a superuser using the command python manage.py createsuperuser
Now you can log in via http://127.0.0.1:8000/admin page through which you can see the table created. You can modify them using the interface of superuser/admin
