from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import player
# Might import other model files this week - stay tuned!

class Team:
    db_name = 'football_schema' # Make use of class variable to hold schema name
    
    # Model for the team - notice the names of the fields match those in the DB
    def __init__(self,data):
        self.id = data['id']
        self.city = data['city']
        self.name = data['name']
        self.stadium_name = data['stadium_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.players = []
        # Later this week - linking to players

    # We'll need to know how to:
    # CREATE (add) a team - DONE
    # UPDATE (edit) a team - DONE
    # DELETE a team - to be added Wednesday
    # READ data:
    # - One team without players
    # - One team with ALL players (later this week)
    # - All teams without players - DONE
    # - Challenge on your own: ALL teams WITH players
    # - Later this week: start with players and...
    #     - Grab one player without team info
    #     - Grab one player with team info
    #     - Grab ALL players with their teams

    # Method to create a new team - notice all the class methods!
    @classmethod
    def create_one(cls, data):
        # This is a prepared statement - notice the %() formats.
        # Use %()s, even for numers - MySQL will convert for you when saved in the database.
        query = "INSERT INTO teams (city, name, stadium_name) VALUES (%(city)s,%(nickname)s,%(stadium_name)s);" # Add query here - test them in MySQL workbench!
        # Need the name of the schema in the connectToMySQL statemet
        return connectToMySQL(cls.db_name).query_db(query, data) # Returns an integer

    @classmethod
    def grab_one_team_without_players(cls, data):
        query = "SELECT * FROM teams WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data) # Returns a list of dictionaries
        if len(results) > 0:
            return cls(results[0])
        else:
            return None

    @classmethod
    def grab_one_team_with_players(cls, data):
        query = "SELECT * FROM teams LEFT JOIN players ON teams.id = players.teams_id WHERE teams.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data) # Returns a list of dictionaries
        if len(results) > 0:
            this_team = cls(results[0])
            for this_player in results:
                if this_player['players.id'] != None:
                    player_data = {
                        "id": this_player['players.id'],
                        "first_name": this_player['first_name'],
                        "last_name": this_player['last_name'],
                        "number": this_player['number'],
                        "position": this_player['position'],
                        "created_at": this_player['players.created_at'],
                        "updated_at": this_player['players.updated_at']
                    }
                    player_instance = player.Player(player_data) # create instance of player
                    this_team.players.append(player_instance) # links a player to the team
            return this_team
        else:
            return []

    @classmethod
    def edit_one_team(cls,data):
        query = "UPDATE teams SET city = %(city)s, name = %(nickname)s, stadium_name = %(stadium_name)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def grab_all_teams(cls):
        query = "SELECT * FROM teams;"
        results = connectToMySQL(cls.db_name).query_db(query) # Returns a list of dictionaries
        # print(results)
        all_teams = [] # List of Teams
        for this_team in results:
            team_class_instance = cls(this_team)
            all_teams.append(team_class_instance)
        return all_teams
    
    @classmethod
    def delete_team(cls,data):
        query = "DELETE FROM teams WHERE id = %(id)s;"
        connectToMySQL(cls.db_name).query_db(query, data)