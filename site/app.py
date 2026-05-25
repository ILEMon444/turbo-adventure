from flask import Flask

app = Flask(__name__)

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
    return "<h1>Main page</h1>"

@app.route('/about')
def about():
    return "<h1>About us</h1>"

if __name__ == '__main__':
    app.run(debug=True)
