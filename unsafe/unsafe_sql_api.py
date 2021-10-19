import pymysql
import logging

class UserDBManager:
    def __init__(self, db_config: dict):
        self.db_connection = pymysql.connect(host = db_config["host"], 
                                             port = db_config["port"], 
                                             user = db_config["user"], 
                                             password = db_config["password"], 
                                             database = db_config["database"])
        self.cursor = self.db_connection.cursor()
        self.name = "unsafe_UserDBManager-"+ db_config["user"] + "-" + db_config["host"] + "-" + db_config["database"]
        print(self.name)
        logging.basicConfig(filename = self.name + ".log")
        self.logger = logging.getLogger()
        print("Log File:", self.name + ".log")
    
    def __del__(self):
        self.db_connection.commit()
        self.db_connection.close()
    
    def get_user_info_with_email_address(self, email_address: str):
        try:
            self.cursor.execute("select * from user where email_address = '%s'" % (email_address))
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            self.logger.error("error in get_todo_task: " + str(e))
            return []

