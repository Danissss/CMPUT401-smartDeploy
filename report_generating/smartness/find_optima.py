
import mysql.connector
import sys




def main():

	if len(sys.argv) > 1:
		weight = sys.argv[1].upper()
	else:
		weight = "GENERAL"

	global db
	global cursor


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
	# # cursor.execute("select * from ycsb_report;")
	# # optima = cursor.fetchall();
	# # for i in optima:

	# # 	print(i)

	# sys.exit(0)


	if weight == "READ":
		query = "select max(READ_AVG_Latency),workload from ycsb_report where workload = " + '\'a\'' + " group by workload;"
		cursor.execute(query)
		optima = cursor.fetchall()
		for i in optima:
			print(i)
	elif weight == "WRITE":
		query = "select max(READ_MODIFY_WRITE_AVG_Latency),workload from ycsb_report where workload = " + 'a' + " group by workload;"
		cursor.execute(query)
		optima = cursor.fetchall()
		for i in optima:
			print(i)
	else:
		query = "select max(OVERALL_runtime),testID from ycsb_report group by testID;"
		cursor.execute(query)
		optima = cursor.fetchall()
		for i in optima:
			print(i)





	



	db.commit()
	cursor.close()
	db.close()


if __name__ == "__main__":
	main()


