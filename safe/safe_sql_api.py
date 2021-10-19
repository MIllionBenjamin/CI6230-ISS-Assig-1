import logging
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    
    __tablename__ = 'user'

    username = Column(String(20), primary_key=True)
    email_address = Column(String(30))
    home_address = Column(String(50))


class UserDBManager:
    def __init__(self, db_config: dict):
        self.engine = create_engine('mysql+mysqlconnector://'+ db_config["user"]\
                                                             + ':' + db_config["password"]\
                                                             + '@' + db_config["host"]\
                                                             + ':' + str(db_config["port"])\
                                                             + '/' + db_config["database"])
        self.DBSession = sessionmaker(bind = self.engine)
        self.session = self.DBSession()
        self.name = "safe_UserDBManager-"+ db_config["user"] + "-" + db_config["host"] + "-" + db_config["database"]
        print(self.name)
        logging.basicConfig(filename = self.name + ".log")
        self.logger = logging.getLogger()
        print("Log File:", self.name + ".log")
    
    def get_user_info_with_email_address(self, email_address: str):
        try:
            user_info = self.session.query(User).filter(User.email_address==email_address).all()
            result = []
            for item in user_info:
                result.append([item.username, item.email_address, item.home_address])
            return result
        except Exception as e:
            self.logger.error("error in get_todo_task: " + str(e))
            return []
s