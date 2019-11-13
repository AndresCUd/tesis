import sys
import os
nodo=str(sys.argv[1])
path = "//home//pi//Desktop//data"
filename = "nodo"+nodo+".txt"
a = os.path.exists(path+filename)
hola = nodo + ",0,0,0,0"
if not a:
    f = os.path.join(path,filename)
    data = open(f,'w')
    data.write(hola)
    data.close()    



