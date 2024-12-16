# Resume_Generator

## Overview
- A Django-based web application for creating, saving, and downloading professional CVs in PDF format.
- Users can enter their personal and professional details through a web form, which the application uses to generate a downloadable CV in PDF format.
- The application also provides an admin interface to view and manage profiles efficiently.


## Features
- **User Input Form:** Fill out personal details, educational background, work experience, and skills.
- **Resume Generation:** Generate and download resumes in PDF format.
- **Profile Management:** View and manage a list of all profiles.
- **Responsive Design:** User-friendly interface compatible with multiple devices.
- **PDF Export:** High-quality CVs generated in a printable PDF format.
- **Admin Dashboard:** Centralized management of user profiles.


## How It Works
- Users fill out a form with their personal, educational, and professional details.
- Submitted data is stored in the database as a profile.
- Users can view a list of profiles and download any CV in PDF format.
- PDF files are generated dynamically using the pdfkit library and Django templates.


## Technologies Used
- **Frontend:** HTML5, CSS3 (Bootstrap 4)
- **Backend:** Django Framework
- **Database:** SQLite
- **PDF Generation:** pdfkit library
- **Template Engine:** Django Templates


## Requirements
To run this project, you need:

- Python 3.10+
- Django 4.2+
- pdfkit library
- wkhtmltopdf (for PDF generation)
- Bootstrap 5 (for frontend styling)


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AnubhavKumarGupta/Resume_Generator
   ```

2. Navigate to the project directory:
   ```bash
   cd myproject
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run migrations to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

---

## How to Use

1. Open your browser and navigate to http://127.0.0.1:8000/.
2. Fill out the form on the homepage to create your CV.
3. After submitting the form, you can download the generated CV in PDF format.
4. To view all generated profiles, navigate to http://127.0.0.1:8000/list/.
5. Administrators can manage profiles via the admin panel at http://127.0.0.1:8000/admin/.
   
---

## Project Structure

```plaintext
myproject/
├── pdf/                # App folder
│   ├── templates/pdf/  # HTML templates for CV generation
│   │   ├── accept.html # Form to accept user input
│   │   ├── list.html   # Displays list of profiles
│   │   └── resume.html # Template for CV PDF
│   ├── models.py       # Profile model
│   ├── views.py        # App views
├── urls.py             # URL configuration
├── settings.py         # Project settings
├── manage.py           # Django management tool
```


## Contributions
Contributions are welcome! Feel free to fork the repository and submit pull requests.

