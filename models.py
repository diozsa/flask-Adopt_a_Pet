"""Models for the adopt app"""

from email.policy import default
from flask_sqlalchemy import SQLAlchemy

DEFAULT_PIC = "https://artsmidnorthcoast.com/wp-content/uploads/2014/05/no-image-available-icon-6.png"
db = SQLAlchemy()

def connect_db(app):
    """Connects database to the app"""
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Model for pet"""

    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo = db.Column(db.Text, nullable=False, default=DEFAULT_PIC)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def photo_url(self):
        """Returns picture or default when none"""
        return self.photo or DEFAULT_PIC