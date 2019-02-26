from flask import Flask

app = Flask(__name__)


import gctravelparser.views  # noqa: F401,E402
