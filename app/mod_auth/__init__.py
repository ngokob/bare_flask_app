from flask import Blueprint, render_template
from app.models import Role, User


auth_bp = Blueprint('auth_bp', __name__,
    template_folder='templates',
    static_folder='static', 
    static_url_path='assets')



@auth_bp.route('/')
def signin():
    return render_template('auth/signin.html')

# @products_bp.route('/view/<int:product_id>')
# def view(product_id):
#     product = Product.query.get(product_id)
#     return render_template('products/view.html', product=product)

