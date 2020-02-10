#
#
#
#
#

#


fileName = open("hostIP.txt","r")
fileContent = fileName.readlines()

file_length = len(fileContent)
index = fileContent[5]
last_len = index.split(" ")
IP = last_len[2]
print(IP)
