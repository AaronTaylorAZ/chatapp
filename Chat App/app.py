from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_oauthlib.client import OAuth
from flask_socketio import SocketIO
from flask_socketio import emit
import secrets

app = Flask(__name__)
app.app_context().push()
app.secret_key = '10109238010'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
socketio = SocketIO(app, async_mode='eventlet')

# Define the Message model
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    message = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return '<Message %r>' % self.id

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# Create the database tables
db.create_all()

# Store messages with user information
messages = []

# OAuth configuration
oauth = OAuth(app)

# Google OAuth configuration
google = oauth.remote_app(
    'google',
    consumer_key='927822979225-2r5oktmreqkd6414vl89uqa7hrubtkuv.apps.googleusercontent.com',
    consumer_secret='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',
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

# OAuth login route
@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))

# OAuth authorized route
@app.route('/login/authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None or resp.get('access_token') is None:
        return 'Access denied: reason={}, error={}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )

    session['oauth_token'] = (resp['access_token'], '')
    user_info = google.get('userinfo')
    session['user'] = user_info.data['email']
    return redirect(url_for('index'))

# Fetching user information
@app.route('/')
def index():
    if 'oauth_token' in session:
        user = session['user']
        return render_template('index.html', username=user)
    return redirect(url_for('login'))

@google.tokengetter
def get_google_oauth_token():
    return session.get('oauth_token')

@socketio.on('read-all')
def load_messages():
    if 'user' in session:
        all_messages = Message.query.all()
        messages_data = [{'id': message.id, 'username': message.username, 'message': message.message} for message in all_messages]
        emit('all-messages', messages_data, broadcast=True)

@socketio.on('message')
def handle_message(message):
    if 'user' in session:
        username = session['user']
        messages.append({'username': username, 'message': message})
        new_message = Message(username = username, message = message)
        db.session.add(new_message)
        db.session.commit()
        emit('message', {'username': username, 'message': message}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
        
# @app.route('/send-message', methods=['POST'])
# def send_message():
#     if 'user' in session:
#         message = request.get_data().decode('utf-8')
#         print(message)
#         username = session['user']
#         print(username)
#         messages.append({'username' : username, 'message' : message})
#         return 'Message sent successfully'
#     else:
#         return redirect(url_for('index'))

# @app.route('/receive-messages')
# def receive_messages():
#     print(messages)

#     return jsonify({'messages': messages})


