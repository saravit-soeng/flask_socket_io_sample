from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from apscheduler.schedulers.background import BackgroundScheduler
import random

app = Flask(__name__, static_url_path='')
socketio = SocketIO(app)

def getData():
    rand_value = random.randint(1, 100)
    return [f"Apple - {rand_value}", f"Banana - {rand_value}", f"Stawberry - {rand_value}"]

# define task
def task():
    data = getData()
    socketio.emit('value update', {'message':data}, broadcast=True)

# schedule task
scheduler = BackgroundScheduler()
running_task = scheduler.add_job(task, 'interval', seconds=20, max_instances=1)
scheduler.start()

@socketio.on('connected')
def on_connected(data):
    task()

@app.route('/')
def index_page():
    return render_template('index.html')

if __name__=='__main__':
    socketio.run(app, host='0.0.0.0', debug=True)