from flask import Flask
from flask import request,render_template

app = Flask(__name__)

from app import index
from app import parser
from app import database
# if __name__ == "__main__":
#     app.run(debug=True)