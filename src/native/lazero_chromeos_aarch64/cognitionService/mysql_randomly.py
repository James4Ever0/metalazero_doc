import pymysql
from ssh_randomly import *
user = "root"
password = "root"
dbname = "users"
if __name__ == "__main__":
    ip = get_ip()
    while True:
        try:
            db = pymysql.connect(host=ip,user=user,password=password,database=dbname,connect_timeout=3)
            print("connected?",ip)
        except:
            import traceback
            traceback.print_exc()
