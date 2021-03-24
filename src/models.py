from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Mutation(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def create(cls):
        new=cls()
        db.session.add(new)
        db.session.commit()


class NoMutation(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def create(cls):
        new=cls()
        db.session.add(new)
        db.session.commit()
