from config import config_postgres
import psycopg2
from .entities.User import User


class ModelUser():

    @classmethod
    def login(self, user):

        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute('SELECT id, username, password, email, created_at FROM users WHERE username = %s',
                        (user.username, ))
            row = cur.fetchone()

            if row is not None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3], row[4])
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