

file = open("swarm.txt","r")

file_line = file.readlines()




output = file_line[3]+file_line[4]+file_line[5]


output = output.replace("    ", "")
output = output.replace("\n","")
output = output.replace("\\", " ")
print(output)


