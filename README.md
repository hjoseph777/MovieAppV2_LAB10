## MovieApp V2 LAB10 – Django CRUD Movie Management System

## Project Details
- Course: Cross Platform Web Development
- Author: Harry Josephvelopment
- Created: 2025-11-28
- Platform: Django Web Application
- Package Manager: pip
- Django version: 5.2.8
- Database: SQLite3 (Default) / PostgreSQL (Optional)
- Deployment: Render.com compatible

## Overview
MovieApp LAB10 demonstrates complete CRUD operations in Django with user authentication. The project showcases email-based user registration, search functionality, add , delete  and admin interface customization.
## Quick Download

**Get the complete project instantly:**

[![Download MovieApp LAB10](https://img.shields.io/badge/Download-MovieApp_LAB10.zip-blue?style=for-the-badge&logo=download)](https://github.com/hjoseph777/MovieApp_LAB10/releases/download/v1/MovieApp_LAB10.zip)

## Live Demo
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://movieappv2-lab10.onrender.com/)
## admin
- user: admin
- password: admin

## Important: Where your Django code lives
- The main CRUD operations are in [`movie/views.py`](movie/views.py) with authentication-protected views
- The movie model is in [`movie/models.py`](movie/models.py) with name, genre, description fields
- Custom user registration is in [`movie/forms.py`](movie/forms.py) with email-based authentication

## Project Explorer
An interactive, collapsible view of the codebase. Click file names to explore them.

<details open>
   <summary><strong>movieapp_lab10/ – Django Project Configuration</strong></summary>

   - 📁 <strong>movieapp_lab10</strong>
      - 📄 [`settings.py`](movieapp_lab10/settings.py) – Django configuration with production settings
      - 📄 [`urls.py`](movieapp_lab10/urls.py) – Root URL routing configuration
      - 📄 [`wsgi.py`](movieapp_lab10/wsgi.py) – WSGI application for deployment
      - 📄 [`asgi.py`](movieapp_lab10/asgi.py) – ASGI application configuration
</details>

<details>
   <summary><strong>movie/ – Main Django App with CRUD</strong></summary>

   - 📁 <strong>movie</strong>
      - 📄 [`models.py`](movie/models.py) – **Movie model with CRUD fields**
      - 📄 [`views.py`](movie/views.py) – **CRUD views with authentication**
      - 📄 [`forms.py`](movie/forms.py) – **Movie forms and custom user registration**
      - 📄 [`urls.py`](movie/urls.py) – App URL routing patterns
      - 📄 [`admin.py`](movie/admin.py) – Enhanced admin interface
      - 📄 [`apps.py`](movie/apps.py) – App configuration
      - 📄 [`tests.py`](movie/tests.py) – Basic test cases
      - 📁 <strong>templates/movie/</strong>
         - 📄 [`base.html`](movie/templates/movie/base.html) – Base template with Bootstrap
         - 📄 [`home.html`](movie/templates/movie/home.html) – Homepage with navigation
         - 📄 [`movie_list.html`](movie/templates/movie/movie_list.html) – Movie listing page
         - 📄 [`movie_detail.html`](movie/templates/movie/movie_detail.html) – Movie detail view
         - 📄 [`movie_form.html`](movie/templates/movie/movie_form.html) – Create/Edit form
         - 📄 [`movie_confirm_delete.html`](movie/templates/movie/movie_confirm_delete.html) – Delete confirmation
         - 📄 [`movie_search.html`](movie/templates/movie/movie_search.html) – Search interface
      - 📁 <strong>templates/registration/</strong>
         - 📄 [`login.html`](movie/templates/registration/login.html) – User login form
         - 📄 [`register.html`](movie/templates/registration/register.html) – Email-based registration
         - 📄 [`logged_out.html`](movie/templates/registration/logged_out.html) – Logout confirmation
      - 📁 <strong>static/movie/css/</strong>
         - 📄 [`style.css`](movie/static/movie/css/style.css) – Custom styles with modal design
      - 📁 <strong>management/commands/</strong>
         - 📄 [`populate_movies.py`](movie/management/commands/populate_movies.py) – Sample data loader
      - 📁 <strong>migrations/</strong>
         - 📄 [`0001_initial.py`](movie/migrations/0001_initial.py) – Database schema
</details>

<details>
   <summary><strong>templates/ – Global Templates</strong></summary>

   - 📁 <strong>templates</strong>
      - 📁 <strong>admin/</strong>
         - 📄 [`base_site.html`](templates/admin/base_site.html) – Custom admin template
</details>

## Features Implemented
### Core CRUD Operations
- **Create**: Add new movies with name, genre, description
- **Read**: View movie list with pagination and detail views
- **Update**: Edit existing movies with form validation
- **Delete**: Remove movies with confirmation modal
- **Search**: Find movies by name, genre, or description

### Authentication System
- Email-based user registration (no username required)
- First name and last name fields in registration
- Login/logout functionality
- Protected CRUD operations (login required)

### Admin Features
- Enhanced admin interface with custom template
- List display with filters and search
- Bulk operations support
- Direct admin access from main navigation

### Database
- SQLite3 (default) 
- PostgreSQL support for production deployment
- Pre-populated with 10 sample movies
- Proper migrations and schema management

## Sample Data
The database includes 10 pre-populated movies:
- The Shawshank Redemption (Drama)
- The Godfather (Crime)
- The Dark Knight (Action)
- Pulp Fiction (Crime)
- Forrest Gump (Drama)
- Inception (Sci-Fi)
- The Matrix (Sci-Fi)
- Goodfellas (Crime)
- The Lord of the Rings: The Fellowship of the Ring (Adventure)
- Star Wars: Episode IV - A New Hope (Sci-Fi)


*This project demonstrates modern Django development practices.
