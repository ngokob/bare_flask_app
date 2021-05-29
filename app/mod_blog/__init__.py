from flask import Blueprint, render_template
from app.models import Role, User


blog_bp = Blueprint('blog_bp', __name__,
    template_folder='templates',
    static_folder='static', 
    static_url_path='assets')



@blog_bp.route('/')
def signin():
    return render_template('blog/index.html')

