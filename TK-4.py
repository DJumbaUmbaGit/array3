def multiavrg(list_data):
    multiaverage = list_data[:]
    if len(multiaverage) > 0:
        average = sum(multiaverage)/len(multiaverage)
    for i in range(len(multiaverage)):
        multiaverage[i] = multiaverage[i]*average
    return multiaverage