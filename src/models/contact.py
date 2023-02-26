# table with structure of contactdb
from utils.db import db

# models contact
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(30))
    email = db.Column(db.String(30))
    phone = db.Column(db.String(12))

    def __init__(self, fullname, email, phone):
        self.fullname = fullname,
        self.email = email,
        self.phone = phone

    """ def delete(self):
        db.session.delete(self)
        db.session.commit() """
    
    """ @staticmethod
    def gedById(id):
        return Contact.query.get(id) """