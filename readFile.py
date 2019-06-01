import os
import os.path
rootdir = '/home/work/python/data'
for parent,dirnames,filenames in os.walk(rootdir):
    for dirname in dirnames:
        print "parent is :" + parent
        print "dirname is :" + dirname
    for filename in filenames:
        print "parent is: " + parent
        print "filename is: " + filename
        print "the full name of the file is: " + os.path.join(parent,filename)

filePath1 = rootdir + '/vin.csv'
filePath2 = rootdir + '/test.csv'
fileHandle = open(filePath1)
fileWrite = open(filePath2, 'w')
fileList = fileHandle.readlines()
for line in fileList:
#    print line,
    fileWrite.write(line)
fileHandle.close()
fileWrite.close()
