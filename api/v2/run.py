import os

from app import create_app

config_name = os.getenv('APP_SETTINGS') # config_name = "development"
app = create_app(config_name)

# Register a user
@app.route('/auth/signup')
def signup():
   return "New Account created"


if __name__ == '__main__':
    app.run()
