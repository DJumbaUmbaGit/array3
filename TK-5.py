import math
def sqrtlist(list_data):
    if len(list_data)>0:
        for i in range(len(list_data)):
            list_data[i] = math.sqrt(list_data[i])
    return list_data