# 项目启动
```
pip install -r requirements.txt
python app.py
```

# 更新依赖项
```
pipreqs . --encoding=utf8 --force
```

# Vercel.json
```
{
  "rewrites": [{ "source": "/(.*)", "destination": "/app" }]
}
```

# docker
```
docker pull aircrushin/promptate:backend
```