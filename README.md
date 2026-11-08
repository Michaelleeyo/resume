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
python3 -m http.server 4173 --directory dist
```

访问 <http://127.0.0.1:4173/>。

## Docker 部署

```bash
docker compose up -d --build
```

当前配置不发布宿主机端口；服务加入已有外部网络 `nas-edge`，由同网络的反向代理访问 `resume-site:80`。部署前需确认该网络和反向代理规则已存在。

验证运行状态：

```bash
docker compose ps
docker compose exec resume-site wget -q -O /dev/null http://127.0.0.1/
```

## 更新内容

`dist/` 以只读卷挂载到容器。修改 HTML、CSS、JavaScript 或 PDF 后会直接生效，无需重新构建镜像。

只有 `Dockerfile`、`nginx.conf` 或 `compose.yaml` 改动时，才需要重新执行：

```bash
docker compose up -d --build
```

生产环境反向代理指向同网络中的 `resume-site:80`。TLS 证书由现有入口负责，不放入仓库或镜像。

## 公开简历更新

`resume-public.md`是公开版源稿，仅保留城市、公开邮箱及网站。先核实事实，再生成PDF：

```bash
python3 tools/build_public_resume.py
```

需要`reportlab`，默认使用macOS的Arial Unicode字体。PDF分两页：概况与工作经历、完整项目经历。修改后必须渲染检查分页，并检查正文和元数据没有手机号、微信或登录凭据。

页面下载链接及CSS使用版本查询参数。更换资源时同时更新版本，避免七天静态缓存返回旧文件。内联JSON-LD受Nginx CSP哈希约束，修改时需重新计算，不能直接放宽CSP。

## 隐私说明

本仓库仅保留用于求职联系的公开邮箱，不包含手机号、家庭地址、服务器登录凭据或内网地址。发布个人简历前，建议再次检查 PDF 元数据及正文中的个人信息。
