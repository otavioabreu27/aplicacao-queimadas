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
