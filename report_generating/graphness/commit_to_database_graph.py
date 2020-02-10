
import mysql.connector
import sys

developmentMode = True


def drop_table():
	#this function will be invoke only if the development mode is on
	
	cursor.execute("drop table if exists CLEANUP;")
	cursor.execute("drop table if exists INSERTS;")
	cursor.execute("drop table if exists UPDATES;")
	cursor.execute("drop table if exists READSS;")
	cursor.execute("drop table if exists SCAN;")
	cursor.execute("drop table if exists TOTAL;")
	cursor.execute("drop table if exists container_system;")

def parsing_DATA(workload_data):
	only_num = []
	for i in workload_data:
		data = i.split(",")
		data_length = len(data)
		tem_num = data[data_length-1].replace("\n","")
		only_num.append(tem_num.replace(" ",""))
	return only_num

def container_system(cpu,memory,blockio,testid):

	cursor.execute("create table if not exists container_system (testID char(20),\
					CPU float, Memory char(20), BlockIO integer, \
					primary key(testID));")
	cursor.execute("insert into container_system (testID,\
					CPU, Memory, BlockIO) values (%s,%s,%s,%s)",(testid,cpu,memory,blockio))

def TOTAL(total_data,workload):
	
	only_num = []
	for i in total_data:
		if "[TOTAL" in i or "[OVERALL]" in i:
			data = i.split(",")
			data_length = len(data)
			tem_num = data[data_length-1].replace("\n","")
			only_num.append(tem_num.replace(" ",""))
	# print(only_num[0],only_num[1],only_num[2],only_num[3],only_num[4],only_num[5],only_num[6],only_num[7],only_num[8],only_num[9])

	cursor.execute("create table if not exists TOTAL (testID char(20), \
														workload char(5), \
														RunTime_ms char(20), \
	                									Throughput char(20), \
	                									TOTAL_GCS_PS_Scavenge char(20), \
	                									TOTAL_GC_TIME_PS_Scavenge_ms char(20),\
	                									TOTAL_GC_TIME_PS_Scavenge_per char(20),\
	                									TOTAL_GCS_PS_MarkSweep char(20),\
	                									TOTAL_GC_TIME_PS_MarkSweep_ms char(20),\
	                									TOTAL_GC_TIME_PS_MarkSweep_per char(20),\
	                									TOTAL_GCs char(20),\
	                									TOTAL_GC_TIME_ms char(20),\
	                									TOTAL_GC_TIME_per char(20)); ")

	cursor.execute("ALTER TABLE TOTAL ADD FOREIGN KEY TOTAL(testID) REFERENCES container_system(testID)\
					ON DELETE NO ACTION ON UPDATE CASCADE;")
	cursor.execute("insert into TOTAL values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(testID,workload,\
					only_num[0],only_num[1],only_num[2],only_num[3],only_num[4],only_num[5],only_num[6],\
					only_num[7],only_num[8],only_num[9],only_num[10]))


def CLEANUP(cleanup_data,workload):

	only_num = parsing_DATA(cleanup_data)
	cursor.execute("create table if not exists CLEANUP (testID char(20), workdload char(5), Operations char(20),\
	                AverageLatency char(20), MinLatency char(20), MaxLatency char(20),\
	                95thPercentileLatency char(20), 99thPercentileLatency char(20));")
	cursor.execute("ALTER TABLE CLEANUP ADD FOREIGN KEY CLEANUP(testID) REFERENCES container_system(testID)\
	                ON DELETE NO ACTION ON UPDATE CASCADE;")
	cursor.execute("insert into CLEANUP values (%s,%s,%s,%s,%s,%s,%s,%s)",(testID,workload,only_num[0],only_num[1],\
					only_num[2],only_num[3],only_num[4],only_num[5]))


def INSERT(insert_data,workload):
	only_num = parsing_DATA(insert_data)

	cursor.execute("create table if not exists INSERTS (testID char(20), workdload char(5), Operations char(20),\
	                AverageLatency char(20), MinLatency char(20), MaxLatency char(20),\
	                95thPercentileLatency char(20), 99thPercentileLatency char(20));")
	cursor.execute("ALTER TABLE INSERTS ADD FOREIGN KEY INSERTS(testID) REFERENCES container_system(testID) \
	                ON DELETE NO ACTION ON UPDATE CASCADE;")
	cursor.execute("insert into INSERTS values (%s,%s,%s,%s,%s,%s,%s,%s)",(testID,workload,only_num[0],only_num[1],\
					only_num[2],only_num[3],only_num[4],only_num[5]))

def SCAN(scan_data,workload):
	only_num = parsing_DATA(scan_data)
	cursor.execute("create table if not exists SCAN (testID char(20), workload char(5), Operations char(20),\
	                AverageLatency char(20), MinLatency char(20), MaxLatency char(20),\
	                95thPercentileLatency char(20), 99thPercentileLatency char(20));")
	cursor.execute("ALTER TABLE SCAN ADD FOREIGN KEY SCAN(testID) REFERENCES container_system(testID) \
	                ON DELETE NO ACTION ON UPDATE CASCADE;")
	cursor.execute("insert into SCAN values (%s,%s,%s,%s,%s,%s,%s,%s);",(testID, workload, only_num[0],only_num[1],only_num[2],\
					only_num[3],only_num[4],only_num[5]))



#this parsing give correct list
def READ(read_data,workload):
	only_num = parsing_DATA(read_data)
	cursor.execute("create table if not exists READSS (testID char(20), \
														workload char(5), \
														Operations char(20),\
	                									AverageLatency char(20), \
	                									MinLatency char(20), \
	                									MaxLatency char(20),\
	                									95thPercentileLatency char(20), \
	                									99thPercentileLatency char(20));")
	cursor.execute("ALTER TABLE READSS ADD FOREIGN KEY READSS(testID) REFERENCES container_system(testID) \
	                ON DELETE NO ACTION ON UPDATE CASCADE;")
	cursor.execute("insert into READSS values (%s,%s,%s,%s,%s,%s,%s,%s);",(testID, workload, only_num[0],only_num[1],only_num[2],\
					only_num[3],only_num[4],only_num[5]))



def UPDATE(update_data,workload):
	only_num = parsing_DATA(update_data)
	cursor.execute("create table if not exists UPDATES (testID char(20), workdload char(5), Operations char(20),\
	                AverageLatency char(20), MinLatency char(20), MaxLatency char(20),\
	                95thPercentileLatency char(20), 99thPercentileLatency char(20));")
	cursor.execute("ALTER TABLE UPDATES ADD FOREIGN KEY UPDATES(testID) REFERENCES container_system(testID) \
	                ON DELETE NO ACTION ON UPDATE CASCADE;")
	cursor.execute("insert into UPDATES values (%s,%s,%s,%s,%s,%s,%s,%s);",(testID, workload, only_num[0],only_num[1],only_num[2],\
					only_num[3],only_num[4],only_num[5]))





def commit_data(data):
	buffers = data[0].split(" ")
	workload = buffers[len(buffers)-1]
	read = []
	scan = []
	cleanup = []
	update = []
	insert = []
	total = []
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
		else:
			total.append(i)
	if len(read) != 0:
		print("read not empty")
		READ(read,workload)
	if len(scan) != 0:
		print("scan not empty")
		SCAN(scan,workload)
	if len(cleanup) != 0:
		print("cleanup not empty")
		CLEANUP(cleanup,workload)
	if len(update) != 0:
		print("update not empty")
		UPDATE(update,workload)
	if len(insert) != 0:
		print("insert not empty")
		INSERT(insert,workload)
	if len(total) != 0:
		print("total not empty")
		TOTAL(total,workload)
	

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
	blkio  = int(sys.argv[3])
	testID = memory + str(cpu) + str(blkio)

	


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


	
	container_system(cpu,memory,blkio,testID)

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
			print(first_index,second_index)
			for i in range(first_index+1,second_index-1):
				data.append(outputFiles[i])
			commit_data(data)
			data = []


	db.commit()
	cursor.close()
	db.close()


if __name__ == "__main__":
	main()


