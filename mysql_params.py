import MySQLdb

def get_db_object(db_user, db_pwd, db_host):
	db=MySQLdb.connect(user=db_user, passwd=db_pwd, host=db_host)
	return db.cursor()

def get_num_queries(cur):
	cur.execute('show status where Variable_name="Queries"')
	return long(cur.fetchone()[1])