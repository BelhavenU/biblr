from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')

@page.route('/')
def index():
    return render_template('page/index.html')

@page.route('/terms')
def terms():
    return render_template('page/terms.html')

@page.route('/privacy')
def privacy():
    return render_template('page/privacy.html')

@page.route('/faq')
def faq():
    return render_template('page/faq.html')
