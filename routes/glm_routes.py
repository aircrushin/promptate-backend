from flask import Blueprint, jsonify, request
from zhipuai import ZhipuAI
from config import GLM_KEY, prompt_generator, prompt_optimizer, prompt_midjourney, prompt_translation

glm_blueprint = Blueprint('glm_blueprint', __name__)
client = ZhipuAI(api_key=GLM_KEY)

@glm_blueprint.route('/api/glmPrompt', methods=['POST'])
def generate_prompt():
    user_content = request.json.get('user-content')
    if not user_content:
        return jsonify({'error': 'No user-content provided'}), 400

    contentPrompt = prompt_generator
    userPrompt = 'input:' + user_content

    completion = client.chat.completions.create(
        model='glm-3-turbo-8602765858450333765',
        messages=[
            {"role": "system", "content": contentPrompt},
            {"role": "user", "content": userPrompt}
        ],
        max_tokens=100,
        temperature=0.1,
    )

    # 将 ChatCompletionMessage 对象转换为可序列化的格式
    response_message = completion.choices[0].message.content if completion.choices[0].message else "No response"

    return jsonify({"response": response_message})

@glm_blueprint.route('/api/glmOptimize', methods=['POST'])
def optimize():
    user_content = request.json.get('user-content')
    if not user_content:
        return jsonify({'error': 'No user-content provided'}), 400

    contentPrompt = prompt_optimizer

    completion = client.chat.completions.create(
        model='glm-4',
        messages=[
            {"role": "system", "content": contentPrompt},
            {"role": "user", "content": user_content}
        ],
        max_tokens=100,
        temperature=0.5,
    )

    # 将 ChatCompletionMessage 对象转换为可序列化的格式
    response_message = completion.choices[0].message.content if completion.choices[0].message else "No response"

    return jsonify({"response": response_message})

@glm_blueprint.route('/api/glmPromptMid', methods=['POST'])
def generate_prompt_mid():
    user_content = request.json.get('user-content')
    if not user_content:
        return jsonify({'error': 'No user-content provided'}), 400

    contentPrompt = prompt_midjourney

    completion = client.chat.completions.create(
        model='glm-4',
        messages=[
            {"role": "system", "content": contentPrompt},
            {"role": "user", "content": user_content}
        ],
        max_tokens=200,
        temperature=0.8,
    )

    # 将 ChatCompletionMessage 对象转换为可序列化的格式
    response_message = completion.choices[0].message.content if completion.choices[0].message else "No response"

    return jsonify({"response": response_message})

@glm_blueprint.route('/api/glmTranslation', methods=['POST'])
def translation():
    user_content = request.json.get('user-content')
    if not user_content:
        return jsonify({'error': 'No user-content provided'}), 400

    contentPrompt = prompt_translation
    userPrompt = " 我要翻译的文字是： " + user_content + " "

    completion = client.chat.completions.create(
        model='glm-4',
        messages=[
            {"role": "system", "content": contentPrompt},
            {"role": "user", "content": userPrompt}
        ],
        max_tokens=200,
    )

    # 将 ChatCompletionMessage 对象转换为可序列化的格式
    response_message = completion.choices[0].message.content if completion.choices[0].message else "No response"

    return jsonify({"response": response_message})

@glm_blueprint.route('/api/glmChat', methods=['POST'])
def chat():
    user_content = request.json.get('user-content')
    if not user_content:
        return jsonify({'error': 'No user-content provided'}), 400
    completion = client.chat.completions.create(
        model= 'glm-4',
        messages=[
            {"role": "system", "content": "你是一个有用的聊天助手,名为 promptate 机器人,可以完成用户的各种请求和问题"},
            {"role": "user", "content": user_content}
        ],
        max_tokens=200,
        temperature=0.1,
    )

    # 将 ChatCompletionMessage 对象转换为可序列化的格式
    response_message = completion.choices[0].message.content if completion.choices[0].message else "No response"

    return jsonify({"response": response_message})

# @glm_blueprint.route('/api/glmDraw', methods=['POST'])
# def draw():
#     user_content = request.json.get('user-content')
#     if not user_content:
#         return jsonify({'error': 'No user-content provided'}), 400
#     completion = client.images.generations(
#     model = "cogview-3", 
#     prompt = user_content,
#     )

#     response_message = completion.data[0].url

#     return jsonify({"response": response_message})

@glm_blueprint.route('/api/glmSuno', methods=['POST'])
def suno():
    pass