
import mysql.connector
import sys

developmentMode = False


def drop_table():
	#this function will be invoke only if the development mode is on
	
	cursor.execute("drop table if exists WORKLOADA;")
	cursor.execute("drop table if exists WORKLOADB;")
	cursor.execute("drop table if exists WORKLOADC;")
	cursor.execute("drop table if exists WORKLOADD;")
	cursor.execute("drop table if exists WORKLOADE;")
	cursor.execute("drop table if exists WORKLOADF;")
	cursor.execute("drop table if exists container_system;")

def parsing_DATA(workload_data):
	only_num = []
	for i in workload_data:
		data = i.split(",")
		data_length = len(data)
		tem_num = data[data_length-1].replace("\n","")
		only_num.append(tem_num.replace(" ",""))
	return only_num

def container_system(cpu,memory,vms,configuration,testid):

	cursor.execute("create table if not exists container_system (testID char(20),\
					CPU float, Memory char(20), Num_VM char(20), Configuration char(20), \
					primary key(testID));")
	cursor.execute("insert into container_system (testID,\
					CPU, Memory, Num_VM, Configuration) values (%s,%s,%s,%s,%s)",(testid,cpu,memory,vms,configuration))



def put_in_table(data_tuple):
	cursor.execute("create table if not exists ycsb_report(testID char(20), workload char(5), \
					OVERALL_runtime char(20),\
					OVERALL_throughput char(20),\
					READ_AVG_Latency char(20),\
					SCAN_AVG_Latency char(20),\
					UPDATE_AVG_Latency char(20),\
					READ_MODIFY_WRITE_AVG_Latency char(20),\
					INSERT_AVG_Latency char(20));")
	cursor.execute("ALTER TABLE ycsb_report ADD FOREIGN KEY ycsb_report(testID) REFERENCES container_system(testID) \
	                ON DELETE NO ACTION ON UPDATE CASCADE;")
	cursor.execute("insert into ycsb_report values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",data_tuple)
	print("inserted")




# latency: ['[READ]', ' AverageLatency(us)', ' 5843.84440227704\n']
# return: the value: 5843.84440227704
def parsing_latency(latency):
	latency_list = latency.split(",")
	READ_AVG_Latency = latency_list[2]
	READ_AVG_Latency = READ_AVG_Latency.replace("\n","")
	READ_AVG_Latency = READ_AVG_Latency.replace(" ","")     # at this stage, the READ_AVG_Latency returns right number as str
	return READ_AVG_Latency

# parameter:
# All_data = all data from each workload
# function: 
# parse each workload data and commit them into database
def update_to_database(All_data,workload):
	OVERALL_runtime    = None
	OVERALL_throughput = None
	READ_AVG_Latency   = None
	SCAN_AVG_Latency   = None
	UPDATE_AVG_Latency   = None
	# CLEANUP_AVG_Latency   = "NULL"    # no need for clean up
	READ_MODIFY_WRITE_AVG_Latency = None
	INSERT_AVG_Latency = None

	length_of_All_data = len(All_data)
	for i in range(0,length_of_All_data):
		category = All_data[i]     # category should be a list ["[READ] ", "[CLEANUP]"]
		if "[READ]" in category[0]:
			latency = category[1]   # latency returns the line with average_latency
			READ_AVG_Latency = parsing_latency(latency)

		elif "[CLEANUP]" in category[0]:
			latency = category[1]   # latency returns the line with average_latency
			CLEANUP_AVG_Latency = parsing_latency(latency)
			# this just ignore the CLEANUP section in ycsb report

		elif "[UPDATE]" in category[0]:
			latency = category[1]   # latency returns the line with average_latency
			UPDATE_AVG_Latency = parsing_latency(latency)
			
		elif "[INSERT]" in category[0]:
			latency = category[1]   # latency returns the line with average_latency
			INSERT_AVG_Latency = parsing_latency(latency)

		elif "[SCAN]" in category[0]:
			latency = category[1]   # latency returns the line with average_latency
			SCAN_AVG_Latency = parsing_latency(latency)

		elif "[READ-MODIFY-WRITE]" in category[0]:
			latency = category[1]   # latency returns the line with average_latency
			READ_MODIFY_WRITE_AVG_Latency = parsing_latency(latency)

		else:
			latency0 = category[2]   # latency returns the line with average_latency
			OVERALL_runtime    = parsing_latency(latency0)
			latency1 = category[4]
			OVERALL_throughput = parsing_latency(latency1)
			

	data_tuple = (testID,workload,OVERALL_runtime,OVERALL_throughput,READ_AVG_Latency,SCAN_AVG_Latency,UPDATE_AVG_Latency,READ_MODIFY_WRITE_AVG_Latency,INSERT_AVG_Latency)

	put_in_table(data_tuple)
	print("update to database finished")


#
# get all data from all_result.txt and parse them into section of different workloads
#
def commit_data(data):
	buffers = data[0].split(" ")
	workload = buffers[len(buffers)-1]     # workload return single letter
	workload = workload.replace('\n','')
	# print(data)   # all data returns 

	if workload == "a":
		All = parsing_raw_data(data)
		update_to_database(All,workload)
	elif workload == "b":
		All = parsing_raw_data(data)
		update_to_database(All,workload)
	elif workload == "c":
		All = parsing_raw_data(data)
		update_to_database(All,workload)

	elif workload == "f":
		All = parsing_raw_data(data)
		update_to_database(All,workload)
	elif workload == "d":
		All = parsing_raw_data(data)
		update_to_database(All,workload)
	elif workload == "e":
		All = parsing_raw_data(data)
		update_to_database(All,workload)

	else:
		print(workload+"doesn't exist")

# parsing each data from each workload and get the desired component
# append them to list and return to commit_data(data) function
def parsing_raw_data(data):

	read = []
	scan = []
	cleanup = []
	update = []
	insert = []
	read_modify_write = []
	total = []

	All = []

	for i in data:
		if "[READ]" in i:
			read.append(i)
		elif "[CLEANUP]" in i:
			cleanup.append(i)
		elif "[UPDATE]" in i:
			update.append(i)
		elif "[INSERT]" in i:
			insert.append(i)
		elif "[SCAN]" in i:
			scan.append(i)
		elif "[READ-MODIFY-WRITE]" in i:
			read_modify_write.append(i)
		else:
			total.append(i)


	if len(read) != 0:
		All.append(read)
	if len(scan) != 0:
		All.append(scan)
	if len(cleanup) != 0:
		All.append(cleanup)
	if len(update) != 0:
		All.append(update)
	if len(insert) != 0:
		All.append(insert)
	if len(read_modify_write) != 0:
		All.append(read_modify_write)
	if len(total) != 0:
		All.append(total)

	return All

# add_ycsb_report_data = ("insert into ycsb() values (?,?,?,?,?,?)" )

# cursor.execute(add_ycsb_report_data,report_data)


def main():

	outputFile = open("all_result.txt")
	outputFiles = outputFile.readlines()
	global testID
	global db
	global cursor
	#container system input
	memory = sys.argv[1]
	cpu    = float(sys.argv[2])
	vms  = int(sys.argv[3])
	configuration = sys.argv[4]
	testID = memory + str(cpu) + "_" + str(vms) + "_" + configuration

	


	try:
	    db = mysql.connector.connect(user='root', password='password',host='162.246.156.220',database='smartdeployer')
	except mysql.connector.Error as err:
	    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
	        print("Something is wrong with your user name or password")
	    elif err.errno == errorcode.ER_BAD_DB_ERROR:
	        print("Database does not exist")
	    else:
	        print(err)

	cursor = db.cursor()


	if developmentMode == True:
		drop_table()


	
	container_system(cpu,memory,vms,configuration,testID)

	index = 0
	indexs = []
	data = []
	while (index<len(outputFiles)):
		if "========================================================" in outputFiles[index]:
			indexs.append(index)
		index += 1



	for i in range(0,(len(indexs)-1)):
			first_index = indexs[i]
			second_index = indexs[i+1]
			for i in range(first_index+1,second_index-1):
				data.append(outputFiles[i])
			commit_data(data)
			data = []


	db.commit()
	cursor.close()
	db.close()


if __name__ == "__main__":
	main()


