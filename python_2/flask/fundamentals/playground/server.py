from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     

@app.route('/')                           
def play_root():
    return "blah"

@app.route('/play')                           
def play(number=3, color="blue"):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', number=number, color=color)

@app.route('/play/<int:number>')                           
def play_number(number,color="blue"):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', number=number, color=color)

@app.route('/play/<int:number>/<string:color>')                           
def play_number_color(number,color):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', number=number, color=color)   
    
if __name__=="__main__":
    app.run(debug=True)      