from flask import Flask, render_template
from flask_restful import Api

from resources.user import User, UserRegister

from data.initial_load import initial_load

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)


@app.before_first_request
def create_tables():
    """
    Before the first request executed, run this func to create tables from models and insert data from data.json
    into the table
    """
    database.create_all()
    initial_load()


@app.route('/')
def hello_api():
    return render_template('index.html')


api.add_resource(User, '/api/user/<int:user_id>')  # GET/DELETE/PUT http://127.0.0.1:5000/user/1
api.add_resource(UserRegister, '/api/user')  # POST http://127.0.0.1:5000/user

if __name__ == '__main__':
    from data.database import database

    database.init_app(app)
    app.run(debug=True, port=5000)
