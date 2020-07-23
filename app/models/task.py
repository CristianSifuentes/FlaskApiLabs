from . import db
from sqlalchemy import desc, asc
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
        
    @classmethod
    def new(cls, title, description, deadline):
        return Task(title=title, description=description, deadline=deadline)
    
    @classmethod
    def get_by_page(cls, order, page, per_page=4):
        # sort = desc(Task.id) if order == 'desc' else asc(Task.id)
        return Task.query.order_by(asc(Task.id)).paginate(page, order, per_page).items
    
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False
        
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False

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