from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from flask.ext.login import login_required, login_user, logout_user, LoginManager

from app import db, app

from app.auth_module.forms import LoginForm, SignupForm
from app.auth_module.models import User

login_manager = LoginManager()
login_manager.init_app(app)
auth_module = Blueprint('auth', __name__, url_prefix='/')

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)

@auth_module.route('/', methods=['GET', 'POST'])
@auth_module.route('login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user and user.check_pass(form.password.data):
            session['user_id'] = user.id
            session['table'] = user.table
            flash('Welcome %s' % user.name)
            login_user(user)
            return redirect ('db/download')
        flash('Wrong email or password', 'error-message')
        return redirect('/')
    return render_template('login2.html', form=form)

@auth_module.route('logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect('login')

