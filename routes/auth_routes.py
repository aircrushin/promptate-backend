from flask import Blueprint, jsonify, request
from models import User
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

auth_blueprint = Blueprint('auth_blueprint', __name__)

@auth_blueprint.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Missing username or password'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@auth_blueprint.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'message': 'Missing username or password'}), 400

    # 检查用户是否存在
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify({'message': 'Login successful', 'access_token': access_token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
    
@auth_blueprint.route('/api/login_admin', methods=['POST'])
def loginAdmin():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    access_token = create_access_token(identity=username)
    
    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, password):
        if user.is_admin:  # 检查用户是否为管理员
            return jsonify({
                'code': 200,
                'msg': '登陆成功',
                'data': user.to_dict(),
                'token': access_token  
            })
        else:
            return jsonify({
                'code': 403,
                'msg': '没有权限，仅管理员可登录'
            })
    else:
        return jsonify({
            'code': 401,
            'msg': '登录失败，用户名或密码错误'
        })

@auth_blueprint.route('/api/register_admin', methods=['POST'])
def register_admin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # 假设传入一个特殊的秘钥来验证是否有权创建管理员账户
    admin_secret = 123

    # 这里的 'your_admin_secret' 应替换为您保存在环境变量或配置文件中的实际秘钥
    if not admin_secret or admin_secret != 123:
        return jsonify({
            'code': 403,
            'msg': '没有权限创建一个管理员账号'
            })

    if not username or not password:
        return jsonify({
            'code': 400,
            'msg': '请输入用户名和密码'
            })

    if User.query.filter_by(username=username).first():
        return jsonify({
            'code': 400,
            'msg': '用户名已经存在！'}
            )

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, is_admin=True)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        'code': 200,
        'msg': '注册成功！'
        })