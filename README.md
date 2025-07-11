# Backend Development Course Assignment - Week 2 -

## The Subject
Learning the basics of [Django](https://www.djangoproject.com) by creating a simple web application that displays a personalized greeting message based on the user's input.

## The Concepts
This exercise introduces core Django concepts such as creating a project, setting up views, defining URLs, using templates, and handling user input. The main objective is to implement two views:
1. A home page that welcomes the user and displays a form requesting his name.
2. A greeting page that displays a personalized greeting message.

The task covers Django's template rendering system to dynamically generate HTML pages.

## The Tools
- [**Django Forms**](https://docs.djangoproject.com/en/5.2/topics/forms/): A Django API to simplifies form generation and management. 
- [**Bootstrap 5**](https://getbootstrap.com/docs/5.0/getting-started/introduction/): A CSS framework to stylize the application templates, with an additional CSS file for finishing touches.
- [**django-crispy-forms**](https://django-crispy-forms.readthedocs.io/en/latest/): A Django package to enhance form rendering by adding Bootstrap styling automatically to forms and to reduce boilerplate HTML code by using a `FormHelper` object.
- [**Django template language**](https://docs.djangoproject.com/en/5.2/ref/templates/language/):  Used to create a base HTML file and extend it through two additional templates for each view, allowing for a reusable and maintainable structure across the app's pages.  

<br/><br/>

the project's virtual environment and dependencies are managed using [**uv**](https://docs.astral.sh/uv/), but a `requirements.txt` file is also provided.