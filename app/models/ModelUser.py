from config import config_postgres
import psycopg2
from psycopg2 import extras
from .entities.User import User

# Encriptar password
# from cryptography.fernet import Fernet
# key = Fernet.generate_key() # creamos una instancia
# f = Fernet(key)


class ModelUser():

    @classmethod
    def get_users(cls):

        try:
            conn = get_connection()
            cur = conn.cursor()

            #cur = conn.cursor(cursor_factory=extras.RealDictCursor)
            cur.execute('SELECT * FROM users')
            users = cur.fetchall()

            cur.close()

            if conn is not None:
                conn.close()

            if users is not None:
                return users

            else:
                return "Error en la consulta de usuarios XD"

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user(self, user_id):

        try:
            conn = get_connection()
            cur = conn.cursor()

            cur.execute('SELECT * FROM users WHERE id = %s', (user_id,))
            user = cur.fetchone()

            cur.close()
            if conn is not None:
                conn.close()

            if user is not None:
                return user
            else:
                return None

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def login(self, user):

        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute('SELECT id, username, password, email, created_at FROM users WHERE username = %s',
                        (user.username, ))
            row = cur.fetchone()

            cur.close()

            if conn is not None:
                conn.close()

            if row is not None:

                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3], row[4])
                return user
            else:
                return None

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def register(self, user):
        try:
            conn = get_connection()
            cur = conn.cursor()


            # print("user.password:", user.password)
            # print("tipo:", type(user.password))

            #my_password = Fernet(key).encrypt(bytes(user.password, 'utf-8'))

            # print("my_password: ", my_password)
            # print("tipo: ", type(my_password))
            # print("decrypt: ", Fernet(key).decrypt(my_password))
            # print("tipo: ", type(Fernet(key).decrypt(my_password)))
            cur.execute('INSERT INTO users (username, password, email) values (%s, %s, %s) RETURNING *',
                        (user.username, user.password, user.email))
            user_registed = cur.fetchone()
            conn.commit()

            cur.close()

            if conn is not None:
                conn.close()

            if user_registed is not None:
                return user_registed
            else:
                return None

        except Exception as ex:
            raise Exception(ex)

        # NOTA: tomar en cuenta que al momento de usar cryptography.fernet, esto convierte los string en bytes, pero
        ## al momento de guardarlos en la BD, estos son convertidos a String.from

        # opcion 1: cambiar el tipo de datos de password en la DB
        # opcion 2: doble cambio de datos variables, bytes -> string, string -> bytes

    @classmethod
    def update(cls, user):
        try:
            conn = get_connection()
            cur = conn.cursor()
            print("usuario:", user.id, user.username)
            cur.execute('UPDATE users SET username = %s, password = %s, email = %s WHERE id = %s RETURNING *',
                        (user.username, user.password, user.email, user.id))

            user_update = cur.fetchone()
            conn.commit()
            print("usuario actualizado:", user_update)
            cur.close()

            if conn is not None:
                conn.close()

            if user_update is not None:
                return user_update
            else:
                return None

        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def delete(self, user_id):
        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute('DELETE FROM users WHERE id = %s RETURNING *', (user_id,))
            user = cur.fetchone()

            print(user)

            conn.commit()
            cur.close()

            if conn is not None:
                conn.close()

            if user is not None:
                return user

            else:
                return None
        except Exception as ex:
            raise Exception(ex)


def get_connection():

    try:
        params = config_postgres()
        conn = psycopg2.connect(**params)

        return conn

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)