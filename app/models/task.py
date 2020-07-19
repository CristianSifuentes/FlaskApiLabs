from . import db
from sqlalchemy.event import listen

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable = False)
    description = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.DateTime(), nullable=False)
    create_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())

    def __str__(self):
        return self.title
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'deadline': self.deadline
        }



def insert_task(*args, **kwargs):
    db.session.add(
       Task(
           title='Title 1',
           description='Description',
           deadline='2019-12-12 12:00:00')
     )

    db.session.add(
       Task(
           title='Title 2',
           description='Description',
           deadline='2019-12-12 12:00:00')
    )
    db.session.commit()

listen(Task.__table__, 'after_create', insert_task)