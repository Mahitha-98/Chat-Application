from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Message received: {msg}")
    send(msg, broadcast=True)

if __name__ == '__main__':
    print("✅ Starting Chat Server...")
    socketio.run(app, debug=True)
