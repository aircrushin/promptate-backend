from zhipuai import ZhipuAI
client = ZhipuAI(api_key="c87755766bf2af696e8fef3a715ff2f2.Vn5KXqmxFOgxig8K")
user_content = "帮我写一首诗"
contentPrompt = "you are a helpful assistant"
completion = client.chat.completions.create(
    model="glm-4",
    messages=[
        {"role": "system", "content": contentPrompt},    
        {"role": "user", "content": user_content}
        ],
    max_tokens=150,
    temperature=0.5,
)

    # 将 ChatCompletionMessage 对象转换为可序列化的格式
response_message = completion.choices[0].message.content if completion.choices[0].message else "No response"

print(response_message)