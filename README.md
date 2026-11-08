# 圆光电子官网

单页公司官网。`public/` 就是可直接部署的静态站点，Flask 只负责本地预览和可选的服务端托管。

## 目录

```
public/                   ← 部署产物：整个目录上传即可
  index.html              首页
  404.html                404 页（Cloudflare Pages / OSS 自动生效）
  robots.txt
  static/style.css
  static/favicon.svg
app.py                    ← 可选：本地预览（含 /health、/robots.txt、404）
render.yaml               ← Render 部署配置
requirements.txt
.python-version
```

页面里的资源路径是 `/static/...`，所以 `public/` 必须部署在域名根目录（不要放在子路径下）。

## 本地预览

纯静态（不需要 Python 依赖）：

```powershell
python -m http.server 4173 --directory public
```

→ http://127.0.0.1:4173

走 Flask（能顺带验证 `/health`、`/robots.txt`、404 行为）：

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

→ http://127.0.0.1:8000

## 部署

| 平台 | 做法 | 备案 |
|---|---|---|
| Cloudflare Pages / Netlify | 直接上传 `public/`，不用构建命令 | 不需要 |
| 阿里云 OSS / 腾讯云 COS | 静态网站托管，把 `public/` 内容传到 Bucket 根目录 | 绑定自定义域名需备案 |
| Render | 按 `render.yaml` 新建 Blueprint，启动命令已绑 `$PORT` | 不需要 |
| 任意 Linux 服务器 | `gunicorn app:app --bind 0.0.0.0:$PORT` | 需备案 |

注意：OSS / COS 用**默认域名**访问 HTML 会被强制下载而不是展示，必须绑定自己的域名。

## 上线前还需要补

- ~~域名~~：已确定为 `https://yuanguang.com`（canonical、`og:url`、`og:image`、`sitemap.xml` 均已指向该域名。**换域名时全站只改这几处**：`public/index.html` 头部的 5 个绝对 URL、`public/sitemap.xml`、`public/robots.txt`）
- **ICP 备案号**：用大陆节点时，页脚需要挂备案号；Cloudflare Pages 不需要备案
- **素材**：真实产品图、企业邮箱、微信二维码
- **字体**：目前走 Google Fonts（`fonts.googleapis.com` 在国内不可用），建议改自托管或系统字体

## 分享图

`public/static/og-image.png`（1200×630）由 `.dev/make_og.py` 生成，改文案后重新跑一次脚本即可：

```powershell
python .dev\make_og.py
```

