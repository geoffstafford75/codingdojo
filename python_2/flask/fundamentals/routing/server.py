from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def success():
    return "Dojo!"

@app.route('/say/<string:name>')
def hello(name):
    print(name)
    return f"Hi, {name.capitalize()}!"

@app.route('/repeat/<int:number>/<string:word>')
def repeat(number,word):
    output = ""
    for x in range(int(number)):
        output += f"<p>{word}</p>"
    return output

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.