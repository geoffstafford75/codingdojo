from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__( self, db_data ):
        self.id = db_data('id')
        self.name = db_data('name')
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO authors ( name , created_at , updated_at ) VALUES (%(name)s, %(bun)s, %(meat)s, %(calories)s, %(restaurant_id)s,NOW(),NOW());"
        return connectToMySQL('login_reg').query_db(query,data)

   @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        authors_from_db =  connectToMySQL('login_reg').query_db(query)
        authors =[]
        for a in authors_from_db:
            authors.append(cls(a))
        return authors

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM authors WHERE authors.id = %(id)s;"
        authors_from_db = connectToMySQL('login_reg').query_db(query,data)

        return cls(authors_from_db[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE authors SET name=%(name)s, bun=%(bun)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('login_reg').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM authors WHERE id = %(id)s;"
        return connectToMySQL('login_reg').query_db(query,data)
