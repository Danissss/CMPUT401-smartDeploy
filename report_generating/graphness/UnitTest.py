import mysql.connector
import sys



def connect_to_db():
	global cursor
	global db
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
	

def retrieve_info(testID):
	# print(testID)
	ALLTBALE = ["CLEANUP","INSERTS","TOTAL","READSS","SCAN","UPDATES"]
	for table in ALLTBALE:
		try:
			query = "select * from "+ table +" where testID = "+ "\"" + testID +"\";"
			cursor.execute(query)
			rows = cursor.fetchall()
			print(table+"Table:")
			for row in rows:
				print(row)
			print("\n")

		except:
			print(table+"is not found!")
			continue
		

def main():

	memory = sys.argv[1]
	cpu    = sys.argv[2]
	blkio  = sys.argv[3]
	ID     = memory+cpu+blkio

	connect_to_db()

	retrieve_info(ID)

	print("end of testing...")





if __name__ == "__main__":
	main()
