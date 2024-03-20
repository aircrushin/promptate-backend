from flask import Flask, jsonify
from flask_cors import CORS
import os
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from models import db
from config import ConfigClass
from routes.data_routes import data_blueprint
from routes.community_data_routes import community_data_blueprint
from routes.auth_routes import auth_blueprint
from routes.glm_routes import glm_blueprint
from routes.prompt_routes import prompt_blueprint
from routes.share_data_routes import share_data_blueprint

#set flask configs
app = Flask(__name__)
app.config.from_object(ConfigClass)

#set proxy
os.environ["HTTP_PROXY"] = "http://127.0.0.1:33210"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:33210"

##init app
jwt = JWTManager(app)
db.init_app(app)

# 允许所有来源
CORS(app, supports_credentials=True)

#routes
app.register_blueprint(data_blueprint)
app.register_blueprint(community_data_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(glm_blueprint)
app.register_blueprint(prompt_blueprint)
app.register_blueprint(share_data_blueprint)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/api/hello', methods=['GET'])
def hello():
    return 'Hello World!'

# 受保护的路由
@app.route('/api/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({'logged_in_as': current_user}), 200

if __name__ == '__main__':
    app.run(debug=True)