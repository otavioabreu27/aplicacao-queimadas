def getData(fileName: str) -> list:
    "Get the data on a .csv file and convert it on a python list."
    dataArray = []
    fileObject = open(fileName, "r")
    for line in fileObject:
        rowArray = line.split(";")
        rowArray[2] = rowArray[2].replace("\n","")
        dataArray.append(rowArray)
    return dataArray