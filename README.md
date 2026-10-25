# 圆光电子官网

一个以 Flask 构建的单页公司官网。

## 本地运行

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

打开 `http://127.0.0.1:8000` 即可预览。

## 部署

本项目已包含 `render.yaml`，可以部署到 Render；也可部署到 Railway 或任意 Linux 服务器。

生产启动命令：

```text
gunicorn app:app
```

在托管平台中设置：

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`

## Render 快速发布

1. 把本项目上传到一个 GitHub 仓库。
2. 在 Render 新建 Blueprint，并选择该仓库。
3. Render 会读取 `render.yaml`，完成安装、启动与健康检查。
4. 发布完成后，可在 Render 的 Custom Domains 中绑定自己的域名。

上线前建议补充公司地址、企业邮箱、营业资质和真实产品图片。若面向中国大陆用户提供经营性互联网信息服务，请根据所在地的要求办理相关备案。
