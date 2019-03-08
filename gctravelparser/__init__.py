from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['VERSION_NUMBER_MAJOR'] = 0
app.config['VERSION_NUMBER_MINOR'] = 1
app.config['VERSION_NUMBER_PATCH'] = 0
db = SQLAlchemy(app)

import gctravelparser.views  # noqa: F401,E402
import gctravelparser.models  # noqa: F401,E402

db.create_all()
db.session.commit()
