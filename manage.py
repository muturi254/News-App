from app import create_app
from flask_script import Manager, Server

# create app instance 
app = create_app('development')

# activate plug in 
manager = Manager(app)

# add reference 