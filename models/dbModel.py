from peewee import SqliteDatabase, Model, TextField, ForeignKeyField

db = SqliteDatabase('todo.sqlite')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = TextField(unique=True)

class Task(BaseModel):
    user = ForeignKeyField(User, backref='tasks')
    task_description = TextField()
