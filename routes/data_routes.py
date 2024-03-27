from flask import Blueprint, jsonify, request
from models import Data
from extensions import db

data_blueprint = Blueprint('data_blueprint', __name__)

#查询所有数据
@data_blueprint.route('/api/data', methods=['GET'])
def get_all_data():
    entries = Data.query.all()
    return jsonify([entry.to_dict() for entry in entries])

#查询一条数据
@data_blueprint.route('/api/data/<int:id>', methods=['GET'])
def get_data(id):
    data = Data.query.get_or_404(id)
    return jsonify(data.to_dict())

#增加一条数据
@data_blueprint.route('/api/data', methods=['POST'])
def create_data():
    data_json = request.json
    new_data = Data(
        keyWord=data_json['keyWord'],
        type=data_json['type'],
        detail=data_json['detail'],
        useTime=data_json['useTime'],
        color=data_json['color'],
        varNum=data_json['varNum']
    )
    db.session.add(new_data)
    db.session.commit()
    return jsonify(new_data.to_dict()), 200

#更新一条数据
@data_blueprint.route('/api/data/<int:id>', methods=['PUT'])
def update_data(id):
    data = Data.query.get_or_404(id)
    data_json = request.json
    data.keyWord = data_json.get('keyWord', data.keyWord)
    data.type = data_json.get('type', data.type)
    data.detail = data_json.get('detail', data.detail)
    data.useTime = data_json.get('useTime', data.useTime)
    data.color = data_json.get('color', data.color)
    data.varNum = data_json.get('varNum', data.varNum)
    db.session.commit()
    return jsonify(data.to_dict())

#删除一条数据
@data_blueprint.route('/api/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    data = Data.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify({'message': 'Data deleted'})