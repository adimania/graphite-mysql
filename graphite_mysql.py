import MySQLdb
import socket
import time

def get_db_object(db_user, db_pwd, db_host = "localhost"):
	db=MySQLdb.connect(user=db_user, passwd=db_pwd, host=db_host)
	return db.cursor()

def get_num_queries(cur):
	cur.execute('show status where Variable_name="Queries"')
	return long(cur.fetchone()[1])

def send_to_graphite(graphite_host, graphite_port, graphite_base_string, value):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto("%s %f %d" % (graphite_base_string, value, int(time.time())), (graphite_host, graphite_port))
