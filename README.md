# FlaskAuthApp - Employee Registration System

A Flask-based authentication system with proper server-side validation for employee registration and login.

## Features

✅ **Secure User Registration** with backend validation
- Name validation (required)
- Email validation (required and unique)
- Password validation (required, minimum 6 characters)

✅ **User Login System**
- Email and password authentication
- Session management
- Protected dashboard route

✅ **Server-Side Validation**
- All validation is performed on the backend (not just HTML `required` attribute)
- Proper error messages for validation failures
- Prevents duplicate email registration

## Problem Fixed

### Original Bug
The registration form was accepting submissions with empty Name, Email, and Password fields.

### Solution Implemented
Added comprehensive backend validation in the `/register` route:
1. ✅ Name must not be empty
2. ✅ Email must not be empty
3. ✅ Password must not be empty
4. ✅ Email must be unique (checks database for existing email)
5. ✅ Password must be at least 6 characters long

All validation is performed server-side to ensure security.

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Local Setup

1. Clone the repository:
```bash
git clone <your-repository-url>
cd Assignment
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run the application:
```bash
python app.py
```

6. Open your browser and navigate to:
```
http://127.0.0.1:5000
```
## Project Structure

```
Assignment/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
│
├── templates/            # HTML templates
│   ├── base.html        # Base template with navbar
│   ├── home.html        # Landing page
│   ├── register.html    # Registration form
│   ├── login.html       # Login form
│   └── dashboard.html   # User dashboard
│
└── instance/            # Generated folder
    └── users.db         # SQLite database (auto-created)
```

## Technologies Used

- **Flask** - Python web framework
- **Flask-SQLAlchemy** - Database ORM
- **SQLite** - Database
- **Bootstrap 5** - Frontend styling

## Validation Rules

| Field    | Validation Rules                                    |
|----------|---------------------------------------------------|
| Name     | • Required<br>• Cannot be empty or whitespace     |
| Email    | • Required<br>• Cannot be empty<br>• Must be unique (not already registered) |
| Password | • Required<br>• Minimum 6 characters              |

## Routes

| Route       | Method    | Description                      |
|-------------|-----------|----------------------------------|
| `/`         | GET       | Home page                        |
| `/register` | GET, POST | User registration                |
| `/login`    | GET, POST | User login                       |
| `/dashboard`| GET       | Protected user dashboard         |
| `/logout`   | GET       | Logout and clear session         |

## Error Handling

The application displays user-friendly error messages for:
- Empty form fields
- Invalid credentials
- Duplicate email registration
- Password length requirements
- Database errors

## Security Features

- ✅ Session-based authentication
- ✅ SQL injection prevention (SQLAlchemy ORM)
- ✅ CSRF protection (Flask built-in)
- ✅ Server-side validation

## Testing the Validation

1. **Test empty fields**: Try submitting the form without filling any fields
   - Result: Error messages will appear

2. **Test duplicate email**: Register with the same email twice
   - Result: "Email is already registered" error

3. **Test short password**: Enter a password with less than 6 characters
   - Result: "Password must be at least 6 characters long" error

4. **Test successful registration**: Fill all fields correctly
   - Result: Success message and redirect to login page

## Author

Samarth Verma

## License

This project is created for educational purposes.

## Submission Checklist

- ✅ Backend validation implemented
- ✅ All 5 validation rules working
- ✅ Error messages displayed properly
- ✅ Code pushed to GitHub (public repository)
- ✅ README.md updated
