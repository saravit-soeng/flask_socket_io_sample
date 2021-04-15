from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from apscheduler.schedulers.background import BackgroundScheduler
import random

app = Flask(__name__, static_url_path='')
socketio = SocketIO(app)

def getData():
    return random.randint(1, 100) # crawling code

# define task
def task():
    rand_value = getData()
    socketio.emit('value update', rand_value, broadcast=True)

# schedule task
scheduler = BackgroundScheduler()
running_task = scheduler.add_job(task, 'interval', seconds=5, max_instances=1)
scheduler.start()

@socketio.on('connected')
def on_connected(data):
    task()

@app.route('/')
def index_page():
    return render_template('index.html')

if __name__=='__main__':
    socketio.run(app, host='0.0.0.0', debug=True)