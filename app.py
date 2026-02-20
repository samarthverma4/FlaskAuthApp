from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        
        # Backend Validation
        errors = []
        
        # 1. Check if name is empty
        if not name:
            errors.append('Name is required')
        
        # 2. Check if email is empty
        if not email:
            errors.append('Email is required')
        
        # 3. Check if password is empty
        if not password:
            errors.append('Password is required')
        # 5. Check if password is at least 6 characters
        elif len(password) < 6:
            errors.append('Password must be at least 6 characters long')
        
        # 4. Check if email is unique (already registered)
        if email:
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                errors.append('Email is already registered. Please use a different email or login.')
        
        # If there are validation errors, show them
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('register.html', name=name, email=email)
        
        # All validations passed - create new user
        try:
            new_user = User(name=name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            
            flash('Registration successful! You can now login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred during registration. Please try again.', 'error')
            return render_template('register.html', name=name, email=email)
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        
        # Validation
        if not email or not password:
            flash('Email and password are required', 'error')
            return render_template('login.html', email=email)
        
        # Check if user exists
        user = User.query.filter_by(email=email).first()
        
        if user and user.password == password:
            session['user_id'] = user.id
            session['user_name'] = user.name
            session['user_email'] = user.email
            flash(f'Welcome back, {user.name}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'error')
            return render_template('login.html', email=email)
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please login to access the dashboard', 'error')
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', name=session.get('user_name'))

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out successfully', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
