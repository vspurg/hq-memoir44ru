from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('index.html')

@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

@app.route('/support')
def support():
    return render_template('support.html')

@app.route('/encyclopedia')
def encyclopedia():
    return render_template('encyclopedia.html')

if __name__ == '__main__':
    app.run(debug=True)
