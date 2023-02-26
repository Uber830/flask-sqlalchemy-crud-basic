from app import app
from app import default_error
from utils.db import db
import config

# execute the create of table contact
with app.app_context():
    db.create_all()

# run app 
if __name__ == '__main__':
    app.register_error_handler(404 ,default_error)
    app.run(debug=True, port=3001)
