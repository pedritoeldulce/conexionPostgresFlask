import psycopg2
from psycopg2 import connect, extras
from flask import Flask, request, jsonify, render_template
from cryptography.fernet import Fernet  # encripta los pass
from psycopg2 import connect

from config import config_postgres, config

app = Flask(__name__)
key = Fernet.generate_key()


def get_connection():

    try:
        params = config_postgres()
        conn = psycopg2.connect(**params)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


@app.route('/')
def index():
    return "NOacanoa"


@app.get('/api/users')
def get_users():
    conn = None
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()  # retorna mas de 1 resultado

    cur.close()

    if conn is not None:
        conn.close()

    return jsonify(users)


@app.post('/api/users')
def create_user():
    conn = None
    new_user = request.get_json()

    username = new_user['username']
    email = new_user['email']
    mypassword = Fernet(key).encrypt(bytes(new_user['password'], 'utf-8'))

    conn = get_connection()  # Me returna la conexion al BD

    cur = conn.cursor(cursor_factory=extras.RealDictCursor)
    cur.execute('INSERT INTO users (username, password, email) values (%s,%s, %s) RETURNING *',
                (username, mypassword, email))

    new_user = cur.fetchone()
    conn.commit()

    cur.close()
    if conn is not None:
        conn.close()

    return jsonify(new_user)


@app.put('/api/users/<id>')
def update_user(id):
    conn = None
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    new_user = request.get_json()

    new_username = new_user['username']
    new_email = new_user['email']
    new_password = Fernet(key).encrypt(bytes(new_user['password'], 'utf-8'))

    cur.execute('UPDATE users SET username=%s, email=%s, password=%s WHERE id = %s RETURNING *',
                (new_username, new_email, new_password, id))

    user_new = cur.fetchone()
    conn.commit()

    cur.close()
    if conn is not None:
        conn.close()

    if user_new is None:
        return jsonify({'message': 'user not found'}), 404

    return jsonify(user_new)


@app.delete('/api/users/<id>')
def delete_user(id):

    conn = None
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('DELETE FROM users WHERE id = %s RETURNING *', (id,))
    usuario = cur.fetchone()

    conn.commit()

    cur.close()
    if conn is not None:
        conn.close()

    if usuario is None:
        return jsonify({'message': 'User not found'}), 404

    return jsonify(usuario)


@app.get('/api/users/<id>')
def get_user(id):
    conn = None
    conn = get_connection()
    cur = conn.cursor(cursor_factory=extras.RealDictCursor)

    cur.execute('SELECT * FROM users WHERE id = %s', (id,))
    usuario = cur.fetchone()

    cur.close()

    if conn is not None:
        conn.close()

    if usuario is None:
        return jsonify({'message': 'User not found'}), 404

    return jsonify(usuario)


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
