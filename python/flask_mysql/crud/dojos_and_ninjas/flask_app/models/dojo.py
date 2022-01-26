# import the function that will return an instance of a connection
from os import name
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
#model the class after the user table from our database
class Dojo:
    db_name = 'dojos_and_ninjas_schema'
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def create_one(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        # Need the name of the schema in the connectToMySQL statemet
        return connectToMySQL(cls.db_name).query_db(query, data) # Returns an integer

    @classmethod
    def grab_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db_name).query_db(query)
        all_dojos = []
        for this_dojo in results:
            dojo_class_instance = cls(this_dojo)
            all_dojos.append(dojo_class_instance)
        return all_dojos

    @classmethod
    def grab_one_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data) # Returns a list of dictionaries
        if len(results) > 0:
            this_dojo = cls(results[0])
            for this_ninja in results:
                if this_ninja['ninjas.id'] != None:
                    ninja_data = {
                        "id": this_ninja['ninjas.id'],
                        "first_name": this_ninja['first_name'],
                        "last_name": this_ninja['last_name'],
                        "age": this_ninja['age'],
                        "created_at": this_ninja['ninjas.created_at'],
                        "updated_at": this_ninja['ninjas.updated_at']
                    }
                    ninja_instance = ninja.Ninja(ninja_data) # create instance of ninja
                    this_dojo.ninjas.append(ninja_instance) # links a ninja to the team
            return this_dojo
        else:
            return []
