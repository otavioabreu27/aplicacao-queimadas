from flask import Flask, render_template
import data

app = Flask(__name__)

@app.route("/visualization")
def visualization():
    dataArray = data.getData("fire_risk.csv")
    data.buildGraph(dataArray)
    highestAndLowestRiskPoints = data.highestAndLowestRiskPoints(dataArray)
    return render_template("visualization.html", 
                           highestNumbersRegion = highestAndLowestRiskPoints[0],
                           lowestNumbersRegion = highestAndLowestRiskPoints[1])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8042, debug=True)