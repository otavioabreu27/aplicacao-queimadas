from flask import Flask, render_template
import data

app = Flask(__name__)

@app.route("/visualization")
def visualization():
    return 

if __name__ == '__main__':
    app.run(host="localhost", port=8042, debug=True)