# request with injection:
# http://127.0.0.1:8383/user?email=alice@ntu.edu.sg%27%20or%20%271%27=%271
# alice@ntu.edu.sg' or '1'='1

DB_CONFIG = {
    "host": "127.0.0.1", 
    "port": 3306, 
    "user": "read_only", 
    "password": "readonly1", 
    "database": "user_test"
}

from unsafe_sql_api import UserDBManager
from flask import Flask, abort, request, jsonify
from flask.views import MethodView

user_manager = UserDBManager(db_config = DB_CONFIG)

app = Flask(__name__)



class User(MethodView):
    def get(self):
        email_address = str(request.args["email"])
        return jsonify(user_manager.get_user_info_with_email_address(email_address))
app.add_url_rule('/user', view_func = User.as_view(name='user'))



if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 8383)