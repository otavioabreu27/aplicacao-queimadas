from flask import Flask, render_template
import data

app = Flask(__name__)

@app.route("/visualization")
def visualization():
    dataArray = data.getData("fire_risk.csv")
    data.buildGraph(dataArray)
    return render_template("teste.html", graphPath = "./graph.png")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8042, debug=True)