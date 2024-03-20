from flask import Blueprint, jsonify, request
from models import ShareData
from extensions import db

share_data_blueprint = Blueprint('share_data_blueprint', __name__)

# 查询所有数据
@share_data_blueprint.route('/api/shareData', methods=['GET'])
def get_all_Data():
    entries = ShareData.query.all()
    return jsonify([entry.to_dict() for entry in entries])

#查询一条数据
@share_data_blueprint.route('/api/shareData/<int:id>', methods=['GET'])
def get_data(id):
    data = ShareData.query.get_or_404(id)
    return jsonify(data.to_dict())

# 增加一条数据
@share_data_blueprint.route('/api/shareData', methods=['POST'])
def create_Data():
    data_json = request.json
    new_data = ShareData(
        src=data_json['src'],
        title=data_json['title'],
        content=data_json['content'],
        type=data_json['type'],
    )
    db.session.add(new_data)
    db.session.commit()
    return jsonify(new_data.to_dict()), 201

#删除一条数据
@share_data_blueprint.route('/api/shareData/<int:id>', methods=['DELETE'])
def delete_data(id):
    data = ShareData.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify({'message': 'Data deleted'})