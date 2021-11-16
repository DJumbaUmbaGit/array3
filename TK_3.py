def divavrg(list_data):
    divideaverage = list_data[:]
    if len(divideaverage) > 0:
        average = sum(divideaverage)/len(divideaverage)
    for i in range(len(divideaverage)):
        divideaverage[i]=divideaverage[i]/average
    return divideaverage