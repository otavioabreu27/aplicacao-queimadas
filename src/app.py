from flask import Flask, render_template, request
import data
import json

app = Flask(__name__)


@app.route("/visualization")
def visualization():
    dataArray = data.getData("../fire_risk.csv")
    data.buildGraph(dataArray)
    highestAndLowestRiskPoints = data.highestAndLowestRiskPoints(dataArray)
    return render_template("visualization.html",
                           highestNumbersRegion=highestAndLowestRiskPoints[0],
                           lowestNumbersRegion=highestAndLowestRiskPoints[1])


@app.route("/risk_count")
def riskCount():
    if request.method == "GET":
        dataArray = data.getData("../fire_risk.csv")
        region = request.args['regiao']
        region = region.replace('"', '')
        dictRegionRiskPoints = data.regionRiskPoints(dataArray, region)
        jsonTotalRegionRiskPoints = json.dumps(
                                    dictRegionRiskPoints).encode('utf8')
        return jsonTotalRegionRiskPoints


if __name__ == '__main__':
    app.run(host="localhost", port=8042, debug=True)
    