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