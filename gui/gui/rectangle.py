import math
with open('output.txt') as fp:
    for line in fp:
        x,y=line.split(",")
        print( math.ceil( float(x)*184.0),float(x)*184.0,x)
        print( math.ceil(float(y)*103.3),float(y)*103.3,y)
