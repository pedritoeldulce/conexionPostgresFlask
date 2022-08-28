import psycopg2
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from config import config_postgres


# models
from .models.ModelUser import ModelUser

# entity
from .models.entities.User import User

page = Blueprint('page', __name__)


def get_connection():

    try:
        params = config_postgres()
        conn = psycopg2.connect(**params)

        return conn

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


@page.route('/')
def index():

    return render_template('index.html')

@page.route('/register')
def register():

    return render_template('auth/register.html')


@page.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        password_input = request.form['password']

        user = User(0, username=request.form['username'], password=password_input, email="", created_at="")
        loggeg_user = ModelUser.login(user)

        if loggeg_user is not None:
            if loggeg_user.password:
                flash('logueado XD', 'success')
                return redirect(url_for('page.index'))
            else:
                flash('Credenciales invalidas', 'danger')

                return render_template('auth/login.html')
        else:
            flash("user not found", "warning")

            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

