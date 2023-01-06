#from app import app
from flask import Flask

app = Flask(__name__)

app.config.from_object("config.DevelopmentConfig")


if __name__ == '__main__':
   app.run()
