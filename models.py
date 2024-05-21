from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_AVATAR_URL = "https://fastly.picsum.photos/id/374/200/200.jpg?hmac=ifUjaLhaxfMlsBL7zHVuQ1YgZ1ECmNDNG8v0D9uHdIc"



"""Models for Blogly."""

class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(20), nullable=True)
    last_name = db.Column(db.String(20), nullable=True)
    user_email = db.Column(db.String(50), nullable = False, unique=True)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_AVATAR_URL)

    @property
    def get_full_name(self):
        """Return users' full name"""
        first = ""
        last = ""
        if(self.first_name == ""):
            first = "Unknown"
        else:
            first = self.first_name
        if(self.last_name==""):
            last = "Unknown"
        else:
            last = self.last_name

        return f"{first} {last}"
    


def connect_db(app):
    """connect to the database"""
    
    db.app = app
    db.init_app(app)
