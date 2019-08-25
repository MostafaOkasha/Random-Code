import os

myfiles = os.listdir('.')
print(myfiles)
mtime = os.path.getmtime(myfiles[0])
print(mtime)
os.utime(myfiles[0], (1552693500, 1552693500))

mtime = os.path.getmtime(myfiles[0])
print(mtime)
