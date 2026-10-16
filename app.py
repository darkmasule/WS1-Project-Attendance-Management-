import os
from flask import Flask
from routes.users import users

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

app.register_blueprint(users)

@app.route('/settings')
def settings():
    return reder_template('settings.html')

if __name__ == "__main__":
    app.run(debug=True)
