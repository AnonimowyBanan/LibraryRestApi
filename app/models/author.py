from app.extensions import db


class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    biography = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Author {self.name}>'
