import psycopg2
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, flash
from config import config_postgres

# models
from .models.ModelUser import ModelUser

# entity
from .models.entities.User import User

page = Blueprint('page', __name__)


@page.route('/')
def index():

    users = ModelUser.get_users()

    return render_template('index.html', users=users)


@page.route('/users')
def get_users():
    users = ModelUser.get_users()
    print(users)
    return render_template('user/users.html', users=users)


@page.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':

        user = User(0, username=request.form['username'], password=request.form['password'], email=request.form['email'], created_at="")
        usuario_registrado = ModelUser.register(user)

        if usuario_registrado is not None:
            flash('Usuario Registrado satisfactoriamente', 'success')
            return redirect(url_for('page.login'))
        else:
            flash('error en el registro', 'danger')
            return render_template('auth/register.html')
    else:
        return render_template('auth/register.html')

    # Falta implementar la encriptacion del password XD


@page.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        password_input = request.form['password']
        #print(password_input)
        user = User(0, username=request.form['username'], password=password_input, email="", created_at="")
        loggeg_user = ModelUser.login(user)

        if loggeg_user is not None:
            if loggeg_user.password:
                flash('logueado XD', 'success')
                #return redirect(url_for('page.index'))
                return render_template('index.html')
            else:
                flash('Credenciales invalidas', 'danger')

                return render_template('auth/login.html')
        else:
            flash("user not found", "warning")

            return render_template('auth/login.html')
    else:
        #flash("Logout", "success")
        #falta corregir, aparece cada vez que refrescamos
        return render_template('auth/login.html')


@page.route('/users/edit/<int:user_id>')
def edit_user(user_id):

    user = ModelUser.get_user(user_id)

    return render_template('user/user_edit.html', user_id=user_id, user=user)


@page.route('/users/update/<id>', methods=['POST', 'GET'])
def update_user(id):

    if request.method == 'POST':
        new_username = request.form['username']
        new_email = request.form['email']
        new_pass = request.form['password']

        user = User(id, new_username, new_pass, new_email, "")
        updated_user = ModelUser.update(user)

        if updated_user is not None:
            flash("Usuario actualizado exitosamente", "success")

            return redirect(url_for('page.get_users'))
        else:
            flash("Error al actualizar usuario", "danger")
            print("Error al actualizar")
            return redirect(url_for('page.get_users'))

    #return redirect(url_for('page.get_users'))


@page.route('/users/delete/<id_user>')
def delete_user(id_user):
    print(id_user)
    user_delete = ModelUser.delete(id_user)

    if user_delete is not None:
        flash("Usuario Eliminado exitosamente", "success")
        return redirect(url_for('page.get_users'))

    return render_template('user/users.html')