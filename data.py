# Data manipulation module
import plotly.express as px

def getData(fileName: str) -> list:
    "Get the data on a .csv file and convert it on a python list."
    dataArray = []
    fileObject = open(fileName, "r")
    for line in fileObject:
        rowArray = line.split(";")
        rowArray[2] = rowArray[2].replace("\n","")
        dataArray.append(rowArray)
    return dataArray

def buildGraph(dataArray: list):
    '''Get the dataArray an turns it into a .png graph image that is saved on
    '/'static'/'images'/'fireRiskPointsGraph.png'''
    sulFireRiskPoints = 0
    nordesteFireRiskPoints = 0
    norteFireRiskPoints = 0
    sudesteFireRiskPoints = 0
    centroOesteFireRiskPoints = 0
    
    for row in dataArray:
        if row[2] == "sul":
            sulFireRiskPoints += 1
        elif row[2] == "nordeste":
            nordesteFireRiskPoints += 1
        elif row[2] == "norte":
            norteFireRiskPoints += 1
        elif row[2] == "sudeste":
            sudesteFireRiskPoints += 1
        elif row[2] == "centro oeste":
            centroOesteFireRiskPoints += 1
    
    graph = px.bar(x=["Sul", "Nordeste", "Norte", "Sudeste", "Centro Oeste"], 
                   y=[sulFireRiskPoints, nordesteFireRiskPoints, norteFireRiskPoints,
                   sudesteFireRiskPoints, centroOesteFireRiskPoints])

    return graph.write_image("./static/images/fireRiskPointsGraph.png")

def highestAndLowestRiskPoints(dataArray: list) -> list:
    '''Get the dataArray and find the regions with the highest and the lowest numbers of
    high risk points.'''
    highRiskCountArray = [[0,"sul"], [0,"nordeste"], [0,"norte"], [0,"sudeste"], [0,"centroOeste"]]

    for row in dataArray:
        if row[1] == "alto":
            if row[2] == "sul":
                highRiskCountArray[0][0] += 1
            elif row[2] == "nordeste":
                highRiskCountArray[1][0] += 1
            elif row[2] == "norte":
                highRiskCountArray[2][0] += 1
            elif row[2] == "sudeste":
                highRiskCountArray[3][0] += 1
            elif row[2] == "centro oeste":
                highRiskCountArray[4][0] += 1
    
    highRiskCountArray.sort(reverse=True, key=lambda x:x[0])
    return [highRiskCountArray[0][1], highRiskCountArray[-1][1]]