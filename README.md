# 项目启动

```bash
pip install -r requirements.txt

python app.py
```

## 更新依赖项

```bash
pipreqs . --encoding=utf8 --force
```

## Vercel.json

```json
{
  "rewrites": [{ "source": "/(.*)", "destination": "/app" }]
}
```

## docker

```bash
docker pull aircrushin/promptate:backend
```
