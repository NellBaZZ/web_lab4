# app.py
from flask import Flask
from routes.route import routes
#from models.dbModel import db, Task, User

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == '__main__':
  #  db.connect()
    app.run(debug=True)
