import os
import numpy as np
def read_lines(file_path):
    if os.path.exists(file_path):
        array = []
        with open(file_path, 'r') as lines:
            for line in lines:
                array.append(line)
        return array
    else:
        print 'file not exist: ' + file_path
        return None




array = read_lines("C:\\Users\\nice01qc\PycharmProjects\huiweibisaitest\\first\\test.txt")
print(len(array))
tuple = (2,3,4,5,"kdaklfj")
print(tuple.count(2))



dict = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

print(dict['Bob'])













