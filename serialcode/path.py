import serial
import arucoid


'''0
tree_array[0]
RN1=0
RN2=1
TDZ=2
Start=3
'''

'''all bits from left
bit 7- QAH
bit 6 and 5 -dec AH number
bits 4 and 3- dec serv2 supply--------00 nosupply, 01 Honey, 10 Leaves, 11 wood
bits 2 and 1- dec serv1 
bit 0- TR req or not
'''
'''
array anathill[]----
0- queen
1- ah number
2- serv2     if ==0, then if TR=1, remove trash from that point, else do nothing
3- serv1
4- trash

'''

class path:
    intermediateArray = []  # stores all codes deciphered from aruco markers
    pathArray = []
    stateCN = 0# can take values 0-straight, 1-right 2 left 3 backward facing
    def __init__(self,ids):

        self.tree_array = []
        self.ah = [0, 1, 2, 3]
        self.serv2 = [None, 'H', 'L', 'W']
        self.serv1 = [None, 'H', 'L', 'W']
        self.arucoMarkers = ids#[4, 56, 121, 194]  # array to store all aruco codes
        self.stateCN = 0  # 0-straight, 1-right 2-left 3-reverse
        self.anthill = [x for x in range(5)]
        self.queenbee=None

        self.aruco_decipher()

    def to_int(self, s):
        s = int(s)
        t = (s % 10) + (2 * (s // 10))
        return t

    def tree_generate(self, x, i):

        binary = str(bin(x)[2:])
        y = '0' * (8 - len(binary))
        binary = y + binary
        print(binary)
        self.anthill[1] = self.ah[self.to_int(binary[1:3])]
        if int(binary[0]):  # queen
            self.anthill[0] = 1
            self.queenbee = i

        else:
            self.anthill[0] = 0

        # ah number

        self.anthill[2] = self.serv2[self.to_int(binary[3:5])]
        self.anthill[3] = self.serv1[self.to_int(binary[5:7])]
        if int(binary[7]):  # trash
            self.anthill[4] = 1
        else:
            self.anthill[4] = 0
        path.intermediateArray.append(list(self.anthill))

    def aruco_decipher(self):
        for i in range(4):
            self.tree_generate(self.arucoMarkers[i], i)
        print('Queen Bee at Ant Hill:', self.queenbee)

        #reordering the array to store Queen Bee at position 0
        temp = path.intermediateArray[self.queenbee]
        path.intermediateArray[self.queenbee] = path.intermediateArray[0]
        path.intermediateArray[0] = temp
        print(path.intermediateArray)

    def tree(self):
        for i in path.intermediateArray:
            if i[1] == 2:
                stateCN = 1
                path.pathArray.extend([])


if __name__ == '__main__':
    ids = arucoid.get_aruco_list()
    print(ids)
    obj=path(ids)






