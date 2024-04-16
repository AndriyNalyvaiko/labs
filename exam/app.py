from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/help')
def help():
    help_value = os.getenv('HELP')
    return help_value

if __name__ == '__main__':
    app.run(port=3000)
