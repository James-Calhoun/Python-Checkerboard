from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def checkerboard():
    return render_template('index.html', num=4, cols=4, color1='green', color2='white')

@app.route('/<int:num>')
def select_rows_checkerboard(num):
    return render_template('index.html', num= int((num/2)), cols=4)

@app.route('/<int:num>/<int:cols>')
def rows_cols_checkerboard(num, cols):
    return render_template('index.html', num = int((num/2)), cols=int((cols/2)))
    
@app.route('/<int:num>/<int:cols>/<string:color1>/<string:color2>')
def rows_cols_colors_checkerboard(num, cols, color1, color2):
    return render_template('index.html', num = int((num/2)), cols=int((cols/2)), color1=color1, color2=color2)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)    # Run the app in debug mode.
