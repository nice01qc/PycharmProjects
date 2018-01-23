import numpy as np

xarr = np.arange(5)
yarr = np.arange(5)*2;
cond = np.array([True,True,True,False,False])


result = [(x if c else y) for x,y,c in zip(xarr,yarr,cond)]

result2 = np.where(cond,xarr,yarr)

print(result2)

print(xarr.mean())












