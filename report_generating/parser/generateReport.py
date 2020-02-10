#
#
#
#
#
# note: this script only write the run output


file = open("all_result.txt", 'w')

fileOrder = ['a','b','c','d','f','e']
fileOderLength = len(fileOrder)
for i in range(0,fileOderLength):
	file_order = fileOrder[i]
	temp_file_name = "workload_run_output"+file_order+".txt"
	

	files = open(temp_file_name,"r")
	Line = files.readlines()

	
	OVERALL = '[OVERALL]'
	properties_OVERALL_index = None

	for i in Line:
		if OVERALL in i:
			properties_OVERALL_index = Line.index(i)


	End_Index = len(Line)
	

	test_general_info = []
	file.write("========================================================\n")
	write_string = "test_output of "+ temp_file_name + " "+ file_order + "\n"
	file.write(write_string)
	file.write("\n")
	
	if properties_OVERALL_index != None:
		for i in range(properties_OVERALL_index-1,End_Index):
			file.write(Line[i]+"\n")


			temp_line = Line[i]
			temp_line_split = temp_line.split(",")

			test_general_info.append(temp_line_split)
file.write("========================================================\n")
file.close()
