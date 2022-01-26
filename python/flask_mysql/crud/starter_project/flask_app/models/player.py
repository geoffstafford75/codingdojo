# Will be built Wednesday

from flask_app.config.mysqlconnection import connectToMySQL
# Might import other model files this week - stay tuned!

class Player:
    db_name = 'football_schema' # Make use of class variable to hold schema name
    
    # Model for the player - notice the names of the fields match those in the DB
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.number = data['number']
        self.position = data['position']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # DON'T NEED team_id - WE'LL LINK THE TEAM IN A DIFFERENT WAY!
        # Add field that holds the team itself as an object