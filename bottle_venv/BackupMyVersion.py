from bottle import Bottle, template
from bottle import request
import sqlite3

app = Bottle()

@app.route('/')
def index():
    return 'Hello from Bottle'

@app.route('/todo')
def todo_list():
    with sqlite3.connect('todo.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, task, status FROM todo WHERE status LIKE '1'")
        result = cursor.fetchall()
        return str(result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug = True, reloader=True)