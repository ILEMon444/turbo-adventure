from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///GetGreat.db'
db = SQLAlchemy(app)


class post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)


header_buttons = [
    {'title': 'Overview', 'url': '/main', 'class': 'link-secondary'},
    {'title': 'Inventory', 'url': '/inventory', 'class': 'link-body-emphasis'},
    {'title': 'Customers', 'url': '/customers', 'class': 'link-body-emphasis'},
    {'title': 'Products', 'url': '/products', 'class': 'link-body-emphasis'},
    {'title': 'About', 'url': '/about', 'class': 'link-body-emphasis'},
]

dropdown_buttons = [
    {'title': 'New project...', 'url': '/new-project'},
    {'title': 'Settings', 'url': '/settings'},
    {'title': 'Profile', 'url': '/profile'},
    {'title': 'Sign out', 'url': '/sign-out', 'divider_before': True},
]

pages = [
    {'title': 'Overview', 'url': '/main', 'description': 'Main page overview'},
    {'title': 'Inventory', 'url': '/inventory', 'description': 'Inventory page'},
    {'title': 'Customers', 'url': '/customers', 'description': 'Customers page'},
    {'title': 'Products', 'url': '/products', 'description': 'Products page'},
    {'title': 'About', 'url': '/about', 'description': 'About us page'},
    {'title': 'New project', 'url': '/new-project', 'description': 'Create a new project'},
    {'title': 'Settings', 'url': '/settings', 'description': 'Application settings'},
    {'title': 'Profile', 'url': '/profile', 'description': 'User profile'},
    {'title': 'Sign out', 'url': '/sign-out', 'description': 'Sign out page'},
]


@app.context_processor
def add_header_buttons():
    return {
        'header_buttons': header_buttons,
        'dropdown_buttons': dropdown_buttons,
    }


@app.route('/main')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search')
def search():
    query = request.args.get('q', '').strip().lower()

    if query:
        results = [
            page for page in pages
            if query in page['title'].lower() or query in page['description'].lower()
        ]
    else:
        results = []

    return render_template('search.html', query=query, results=results)

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/customers')
def customers():
    return render_template('customers.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/new-project')
def new_project():
    return render_template('new_project.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/sign-out')
def sign_out():
    return render_template('sign_out.html')

if __name__ == '__main__':
    app.run(debug=True)
