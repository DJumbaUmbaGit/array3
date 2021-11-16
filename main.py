import sys
import importlib
from TK_1 import inputlist
from TK_2 import minmaxcortege
from TK_3 import divavrg
from TK_4 import multiavrg

def main():
    TK_5 = importlib.import_module("TK-5")
    count = int(input('Get count data: '))
    list_data = inputlist(count)
    print('List: ' + str(list_data))
    print('Min/max cortege: ' + str(minmaxcortege(list_data)))
    print('Average elements divide: ' + str(divavrg(list_data)))
    print('Average elements multiply: ' + str(multiavrg(list_data)))
    print('Sqrt elements list: ' + str(TK_5.sqrtlist(list_data)))
    return 0

if __name__=='__main__':
    sys.exit(main())