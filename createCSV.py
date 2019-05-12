from random import seed
from random import random, randint

seed(1)
n=50
features = 3
File = open("dataset.csv", 'w')
File.write(str(n)+","+ str(features)+"\n")
for i in range(n):
    File.write(str(round(random(), 3))+', '+str(round(random(),3))+', '+str(round(random(),3))+', '+ str(randint(0, 2)))
    File.write("\n")

File.close()