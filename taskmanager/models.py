from taskmanager import db


class Category(db.Model):
    # schema for category table
    id = db.Column(db.Integer, primary_key= True)
    category_name = db.Column(db.String(25), unique=True, nullable=False) # maximum character count is 25, each category added is unique, nullable ensures that it is a required field
    tasks = db.relationship("TASK", backref="category", cascade = "all , delete", lazy = True)
    def __repr__(self):
        # to represent itself in the form of a string
        return self.category_name

class Task(db.Model):
    # schema for task table
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique = True, nullable = False)
    task_description = db.Column(db.Text, nullable = False)
    is_urgent = db.Column(db.Boolean, default = False, nullable = False)
    due_date = db.Column(db.Date, nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"))

    def __repr__(self):
        return "#{0} - Task : {1} | urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )