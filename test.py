import area
import os
from shutil import move

with open("area.py") as f:
    lines = f.readlines()

with open("testtest.txt",mode="w") as f:
    f.write("testestests123")

#move("testtest.txt","ohyes.txt")
print(os.path.exists("testtest.txt"))



print(os.getcwd())
