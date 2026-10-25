# Michael Lee · Portfolio

个人简历与工程能力展示站。项目采用原生 HTML、CSS 和 JavaScript 构建，通过 Docker 与 Nginx 部署，线上地址为 [me.michaellee.win](https://me.michaellee.win/)。

## 项目特点

- 响应式单页设计，适配桌面端与移动端
- 无前端框架与运行时依赖，页面轻量、加载路径简单
- 提供 PDF 简历下载入口
- 使用 Nginx 提供静态资源、健康检查与基础安全响应头
- Docker Compose 一键启动，网站内容以只读卷挂载，日常更新无需重建镜像
- 适合通过 Cloudflare、反向代理或本地网络发布

## 技术栈

- HTML5 / CSS3 / Vanilla JavaScript
- Nginx Alpine
- Docker / Docker Compose
- Cloudflare DNS 与 HTTPS 入口（线上环境）

## 目录结构

```text
.
├── dist/               # 网站内容与 PDF 简历
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│   ├── resume.pdf
│   ├── llms.txt
│   └── robots.txt
├── compose.yaml        # 容器编排与健康检查
├── Dockerfile          # Nginx 运行镜像
├── nginx.conf          # 静态站点及安全响应头配置
└── README.md
```

## 本地预览

直接打开 `dist/index.html`，或者使用任意静态文件服务器：

```bash
python -m http.server 4173 --directory dist
```

访问 <http://127.0.0.1:4173/>。

## Docker 部署

```bash
docker compose up -d --build
```

默认映射到宿主机 `18080` 端口。如需更换端口：

```bash
RESUME_PORT=18081 docker compose up -d --build
```

验证运行状态：

```bash
docker compose ps
curl -I http://127.0.0.1:18080/
curl http://127.0.0.1:18080/healthz
```

## 更新内容

`dist/` 以只读卷挂载到容器。修改 HTML、CSS、JavaScript 或 PDF 后会直接生效，无需重新构建镜像。

只有 `Dockerfile`、`nginx.conf` 或 `compose.yaml` 改动时，才需要重新执行：

```bash
docker compose up -d --build
```

生产环境可将反向代理指向宿主机 `18080` 端口。TLS 证书应由 Cloudflare或现有反向代理入口负责，不需要放入仓库或镜像。

## 隐私说明

本仓库仅保留用于求职联系的公开邮箱，不包含手机号、家庭地址、服务器登录凭据或内网地址。发布个人简历前，建议再次检查 PDF 元数据及正文中的个人信息。
