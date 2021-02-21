from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#...

class User(db.Model):
    """An admin user capable of viewing reports.

    :param str email: email address of user
    :Param str password: encrypted password for the user
    
    """
    __tablename__ = 'user'

    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    authentication = db.Column(db.Boolean, default=False)

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False