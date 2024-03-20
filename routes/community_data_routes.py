from flask import Blueprint, jsonify, request
from models import CommunityData
from extensions import db

community_data_blueprint = Blueprint('community_data_blueprint', __name__)

# 查询所有数据
@community_data_blueprint.route('/api/communityData', methods=['GET'])
def get_all_comData():
    entries = CommunityData.query.all()
    return jsonify([entry.to_dict() for entry in entries])

# 增加一条数据
@community_data_blueprint.route('/api/communityData', methods=['POST'])
def create_comData():
    data_json = request.json
    new_data = CommunityData(
        src=data_json['src'],
        title=data_json['title'],
        content=data_json['content'],
        type=data_json['type']
    )
    db.session.add(new_data)
    db.session.commit()
    return jsonify(new_data.to_dict()), 201

# 查询一条数据
@community_data_blueprint.route('/api/communityData/<int:id>', methods=['GET'])
def get_comData(id):
    data = CommunityData.query.get_or_404(id)
    return jsonify(data.to_dict())

# 更新一条数据
@community_data_blueprint.route('/api/communityData/<int:id>', methods=['PUT'])
def update_comData(id):
    data = CommunityData.query.get_or_404(id)
    data_json = request.json
    data.src = data_json.get('src', data.src)
    data.title = data_json.get('title', data.title)
    data.content = data_json.get('content', data.content)
    data.type = data_json.get('type', data.type)
    db.session.commit()
    return jsonify(data.to_dict())

# 删除一条数据
@community_data_blueprint.route('/api/communityData/<int:id>', methods=['DELETE'])
def delete_comData(id):
    data = CommunityData.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify({'message': 'Data deleted'})