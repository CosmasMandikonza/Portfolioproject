#!/usr/bin/env python3

import os
from flask import Flask, render_template, url_for, request, flash, redirect
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Portfolio data - in a real app, this would come from a database
PORTFOLIO_DATA = {
    'personal_info': {
        'name': 'Cosmas Mandikonza',
        'title': 'MLH Fellow & Aspiring Software Engineer',
        'email': 'cosmasmandikona@gmail.com',
        'phone': '+1 (218) 260-6827',
        'location': 'Duluth,Minnesota , USA',
        'linkedin': 'https://linkedin.com/in/cosmasmandikona',
        'github': 'https://github.com/cosmasmandikona',
        'profile_image': 'profile.jpg',
        'about': """
        Welcome to my portfolio! I'm a passionate software engineer and current MLH Fellow, 
        dedicated to creating innovative solutions and building meaningful connections in the tech community.
        With a strong foundation in full-stack development and a love for problem-solving, 
        I'm always eager to take on new challenges and contribute to impactful projects.
        
        When I'm not coding, you'll find me exploring new technologies, contributing to open-source projects,
        or sharing knowledge with fellow developers. I believe in the power of collaboration and 
        continuous learning to drive technological advancement.
        """
    },
    
    'work_experiences': [
        {
            'title': 'MLH Production Engineering Fellow',
            'company': 'Major League Hacking',
            'location': 'Remote',
            'start_date': 'June 2025',
            'end_date': 'Present',
            'description': [
                'Participating in a 12-week fellowship program focused on Site Reliability Engineering',
                'Building and deploying applications using modern DevOps practices',
                'Collaborating with fellow developers on real-world projects',
                'Learning industry-standard tools and methodologies'
            ]
        },
        {
            'title': 'Software Development Intern',
            'company': 'Jackal Tech.',
            'location': 'Remote',
            'start_date': 'June 2024',
            'end_date': 'August 2024',
            'description': [
                'Developed web applications using Python Flask and JavaScript',
                'Implemented responsive user interfaces with HTML5, CSS3, and Bootstrap',
                'Collaborated with senior developers on code reviews and best practices',
                'Contributed to improving application performance by 25%'
            ]
        }
    ],
    
    'education': [
        {
            'major': 'Computer Science',
            'institution': 'College of St. Scholastica',
            'location': 'Duluth, Minnesota, USA',
            'degree': 'Bachelor of Science',
            'start_date': '2024',
            'end_date': '2028',
            'gpa': '3.8/4.0',
            'relevant_coursework': [
                'Data Structures and Algorithms',
                'Web Development',
                'Database Systems',
                'Software Engineering',
                'Computer Networks'
            ],
            'achievements': [
                'Dean\'s List - Fall 2024, Spring 2025',
                'Computer Science Club Vice President',
                'Hackathon Winner - Colorstack Tech Fair 2024'
            ]
        }
    ],
    
    'hobbies': [
        {
            'name': 'Photography',
            'description': 'Capturing moments and exploring creative composition through digital photography.',
            'image': 'hobby_photography.jpg',
            'details': 'Specializing in landscape and street photography with over 5 years of experience.'
        },
        {
            'name': 'Rock Climbing',
            'description': 'Pushing physical and mental limits while enjoying the great outdoors.',
            'image': 'hobby_climbing.jpg',
            'details': 'Active climber with experience in both indoor and outdoor climbing.'
        },
        {
            'name': 'Open Source Contributing',
            'description': 'Contributing to open source projects and giving back to the developer community.',
            'image': 'hobby_opensource.jpg',
            'details': 'Regular contributor to Python and JavaScript projects on GitHub.'
        },
        {
            'name': 'Chess',
            'description': 'Strategic thinking and pattern recognition through the classic game of chess.',
            'image': 'hobby_chess.jpg',
            'details': 'Tournament player with USCF rating of 1650.'
        }
    ],
    
    'skills': {
        'Programming Languages': ['Python', 'JavaScript', 'Java', 'C++', 'HTML5', 'CSS3'],
        'Frameworks & Libraries': ['Flask', 'Django', 'React', 'Node.js', 'Bootstrap'],
        'Databases': ['PostgreSQL', 'MySQL', 'MongoDB', 'SQLite'],
        'Tools & Technologies': ['Git', 'Docker', 'AWS', 'Linux', 'VS Code'],
        'Soft Skills': ['Team Leadership', 'Problem Solving', 'Communication', 'Project Management']
    },
    
    'travel_locations': [
        {'name': 'New York City, USA', 'lat': 40.7128, 'lng': -74.0060, 'year': '2024'},
        {'name': 'London, UK', 'lat': 51.5074, 'lng': -0.1278, 'year': '2023'},
        {'name': 'Tokyo, Japan', 'lat': 35.6762, 'lng': 139.6503, 'year': '2023'},
        {'name': 'Paris, France', 'lat': 48.8566, 'lng': 2.3522, 'year': '2022'},
        {'name': 'Sydney, Australia', 'lat': -33.8688, 'lng': 151.2093, 'year': '2022'}
    ]
}

# Navigation configuration
NAVIGATION = [
    {'name': 'Home', 'endpoint': 'index', 'icon': 'fas fa-home'},
    {'name': 'About', 'endpoint': 'about', 'icon': 'fas fa-user'},
    {'name': 'Experience', 'endpoint': 'experience', 'icon': 'fas fa-briefcase'},
    {'name': 'Hobbies', 'endpoint': 'hobbies', 'icon': 'fas fa-heart'},
    {'name': 'Travel', 'endpoint': 'travel', 'icon': 'fas fa-map-marked-alt'},
    {'name': 'Contact', 'endpoint': 'contact', 'icon': 'fas fa-envelope'}
]

@app.context_processor
def inject_navigation():
    """Inject navigation data into all templates"""
    return {'navigation': NAVIGATION, 'current_year': datetime.now().year}

@app.route('/')
def index():
    """Home page route"""
    return render_template('index.html', 
                         personal_info=PORTFOLIO_DATA['personal_info'],
                         skills=PORTFOLIO_DATA['skills'])

@app.route('/about')
def about():
    """About page route"""
    return render_template('about.html', 
                         personal_info=PORTFOLIO_DATA['personal_info'])

@app.route('/experience')
def experience():
    """Experience and education page route"""
    return render_template('experience.html',
                         work_experiences=PORTFOLIO_DATA['work_experiences'],
                         education=PORTFOLIO_DATA['education'])

@app.route('/hobbies')
def hobbies():
    """Dedicated hobbies page route"""
    return render_template('hobbies.html',
                         hobbies=PORTFOLIO_DATA['hobbies'])

@app.route('/travel')
def travel():
    """Travel map page route"""
    return render_template('travel.html',
                         travel_locations=PORTFOLIO_DATA['travel_locations'])

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page with form handling"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # In a real application, you would send an email or save to database
        # For now, we'll just flash a success message
        if name and email and message:
            flash(f'Thank you {name}! Your message has been received. I\'ll get back to you soon!', 'success')
            return redirect(url_for('contact'))
        else:
            flash('Please fill in all fields.', 'error')
    
    return render_template('contact.html',
                         personal_info=PORTFOLIO_DATA['personal_info'])

@app.route('/api/travel-data')
def api_travel_data():
    """API endpoint for travel data (for map integration)"""
    return json.dumps(PORTFOLIO_DATA['travel_locations'])

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    # Ensure the app only runs in debug mode during development
    debug_mode = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug_mode, host='127.0.0.1', port=5000)