# 🚀 MLH Fellowship Portfolio - Cosmas Mandikonza

A modern, responsive portfolio website built with Flask showcasing my journey as a software engineer and MLH Fellow.

## 🌟 Live Demo

Visit the live portfolio: [Portfolio Link](your-deployed-url-here)

## 📸 Screenshots

### Homepage
![Homepage Screenshot](static/images/homepage-screenshot.png)

### Travel Map
![Travel Map Screenshot](static/images/travel-screenshot.png)

## ✨ Features

- 🎨 **Modern Responsive Design** - Works perfectly on all devices
- 🗺️ **Interactive Travel Map** - Explore places I've visited with custom markers
- 👨‍💻 **Dynamic Experience Timeline** - Professional journey with Jinja2 templates
- 🎯 **Hobbies Showcase** - Dedicated page with interactive elements
- 📱 **Mobile-First Design** - Optimized for all screen sizes
- 🎭 **Smooth Animations** - Enhanced user experience with CSS animations
- 📧 **Contact Form** - Professional contact form with validation
- 🚨 **Custom Error Pages** - User-friendly 404 and 500 error handling

## 🛠️ Technical Stack

- **Backend**: Flask 2.3.3 (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Templating**: Jinja2
- **Styling**: Bootstrap 5.3.0, Custom CSS
- **Icons**: Font Awesome 6.4.0
- **Fonts**: Google Fonts (Inter, Playfair Display)

## 🏗️ Project Structure

```
portfolio/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── static/
│   ├── css/              # Custom stylesheets
│   ├── js/               # Custom JavaScript
│   └── images/           # Profile photos and assets
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Homepage
│   ├── about.html        # About page
│   ├── experience.html   # Experience timeline
│   ├── hobbies.html      # Hobbies showcase
│   ├── travel.html       # Interactive travel map
│   ├── contact.html      # Contact form
│   └── errors/           # Error page templates
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/CosmasMandikonza/Portfolioproject.git
   cd Portfolioproject
   ```

2. **Create virtual environment**
   ```bash
   python -m venv python3-virtualenv
   source python3-virtualenv/bin/activate  # On Windows: python3-virtualenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp example.env .env
   # Edit .env with your configurations
   ```

5. **Run the application**
   ```bash
   export FLASK_ENV=development  # On Windows: set FLASK_ENV=development
   flask run
   ```

6. **Open your browser**
   ```
   Navigate to http://127.0.0.1:5000
   ```

## 📄 Pages Overview

### 🏠 Homepage (`/`)
- Hero section with profile photo
- Animated statistics
- Skills showcase
- Call-to-action sections

### 👨‍💻 About (`/about`)
- Personal journey timeline
- Core values and personality
- Professional background
- Fun facts and achievements

### 💼 Experience (`/experience`)
- Work experience timeline
- Education background
- Skills with progress bars
- Professional achievements

### 🎯 Hobbies (`/hobbies`)
- Interactive hobby cards
- Photo galleries
- Personal interests
- Statistics and timelines

### 🗺️ Travel (`/travel`)
- Interactive world map
- Travel statistics
- Location stories
- Future travel plans

### 📧 Contact (`/contact`)
- Professional contact form
- Social media links
- FAQ section
- Contact information

## 🎨 Design Features

- **Color Scheme**: Modern blue gradient with accent colors
- **Typography**: Professional font pairing (Inter + Playfair Display)
- **Animations**: Smooth CSS transitions and JavaScript interactions
- **Responsive**: Mobile-first design with Bootstrap grid
- **Accessibility**: ARIA labels and semantic HTML

## 🔧 Development

### Adding New Pages

1. Create template in `templates/`
2. Add route in `app.py`
3. Update navigation in `base.html`
4. Style with CSS in template

### Customizing Content

Update the `PORTFOLIO_DATA` dictionary in `app.py` with your personal information:

```python
PORTFOLIO_DATA = {
    'personal_info': {
        'name': 'Your Name',
        'title': 'Your Title',
        'email': 'your.email@example.com',
        # ... add your details
    }
}
```

## 📱 Mobile Optimization

- Responsive navigation with mobile menu
- Touch-friendly interactive elements
- Optimized image sizes
- Fast loading on mobile networks

## 🚀 Deployment

### Heroku Deployment

1. Create `Procfile`:
   ```
   web: python app.py
   ```

2. Deploy:
   ```bash
   heroku create your-portfolio-app
   git push heroku main
   ```

### Other Platforms

The application can be deployed on any platform supporting Python/Flask:
- Vercel
- Railway
- PythonAnywhere
- DigitalOcean App Platform

## 🤝 MLH Fellowship

This portfolio was created as part of the MLH Fellowship Production Engineering track, demonstrating:

- ✅ Flask web application development
- ✅ Responsive frontend design
- ✅ Git workflow and collaboration
- ✅ Professional project documentation
- ✅ Modern web development practices

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- MLH Fellowship for the opportunity and guidance
- Fellow participants for inspiration and collaboration
- Open source community for amazing tools and libraries

## 📞 Contact

- **Portfolio**: [Live Site](your-portfolio-url)
- **LinkedIn**: [Your LinkedIn](your-linkedin-url)
- **GitHub**: [Your GitHub](your-github-url)
- **Email**: cosmas.t.mandikonza@gmail.com

---

**Built with ❤️ during MLH Fellowship 2025**
