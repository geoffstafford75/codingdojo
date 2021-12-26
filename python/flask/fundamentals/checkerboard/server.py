from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     

@app.route('/')                           
def checkerboard():
    return render_template('index.html', width = 8, height = 8, color1="red", color2="black")

@app.route('/<int:height>')                           
def checkerboard2(height):
    return render_template('index.html', width = 8, height = height, color1="red", color2="black")

@app.route('/<int:width>/<int:height>')                           
def checkerboard3(width,height):
    return render_template('index.html', width = width, height = height, color1="red", color2="black")

@app.route('/<int:width>/<int:height>/<string:color1>/<string:color2>')                            
def checkerboard4(width,height,color1,color2):
    return render_template('index.html', width = width, height = height, color1 = color1, color2 = color2)   
    
if __name__=="__main__":
    app.run(debug=True)      