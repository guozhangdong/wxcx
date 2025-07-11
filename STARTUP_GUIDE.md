# 邻·生活项目启动指南

## 🎯 项目概述

**邻·生活** 是一个完整的本地生活服务平台，包含：
- **后端API服务** (Node.js + Koa2 + MySQL)
- **微信小程序** (原生微信小程序)
- **管理后台** (React + Ant Design + ECharts)

## 📋 环境准备

### 必须安装的软件

1. **Node.js** (版本 >= 16.0.0)
   - 下载地址: https://nodejs.org/
   - 安装后会自动包含 npm

2. **MySQL** (版本 >= 8.0)
   - 下载地址: https://dev.mysql.com/downloads/mysql/
   - 或使用 XAMPP: https://www.apachefriends.org/

3. **Redis** (可选，用于缓存)
   - Windows: https://github.com/tporadowski/redis/releases
   - 或使用云服务

4. **微信开发者工具**
   - 下载地址: https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html

## 🚀 快速启动

### 1. 后端服务启动

```bash
# 1. 进入后端目录
cd backend

# 2. 安装依赖
npm install

# 3. 复制环境配置文件
copy env.example .env

# 4. 编辑 .env 文件，配置数据库等信息
# 设置数据库连接、Redis连接、JWT密钥等

# 5. 启动服务
npm start
```

后端服务将在 http://localhost:3000 启动

### 2. 管理后台启动

```bash
# 1. 进入管理后台目录
cd admin

# 2. 安装依赖
npm install

# 3. 启动开发服务器
npm start
```

管理后台将在 http://localhost:3001 启动

### 3. 微信小程序启动

```bash
# 1. 打开微信开发者工具
# 2. 选择"导入项目"
# 3. 选择 miniprogram 目录
# 4. 填入 AppID (测试可使用测试号)
# 5. 点击"导入"
```

## 📂 项目结构说明

```
邻·生活项目/
├── backend/                 # 后端API服务
│   ├── app.js              # 应用入口
│   ├── config/             # 配置文件
│   ├── controllers/        # 控制器
│   ├── models/             # 数据模型
│   ├── routes/             # 路由定义
│   ├── middleware/         # 中间件
│   ├── utils/              # 工具函数
│   └── package.json        # 依赖配置
├── miniprogram/            # 微信小程序
│   ├── app.js              # 小程序入口
│   ├── app.json            # 小程序配置
│   ├── pages/              # 页面文件
│   ├── components/         # 组件文件
│   └── utils/              # 工具函数
├── admin/                  # 管理后台
│   ├── src/                # 源代码
│   │   ├── pages/          # 页面组件
│   │   ├── components/     # 公共组件
│   │   ├── stores/         # 状态管理
│   │   └── utils/          # 工具函数
│   ├── public/             # 静态资源
│   └── package.json        # 依赖配置
└── README.md               # 项目说明
```

## 🗄️ 数据库配置

### MySQL数据库创建

```sql
-- 1. 创建数据库
CREATE DATABASE neighbor_life CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 2. 创建用户 (可选)
CREATE USER 'neighbor_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON neighbor_life.* TO 'neighbor_user'@'localhost';
FLUSH PRIVILEGES;
```

### 环境变量配置 (backend/.env)

```env
# 数据库配置
DB_HOST=localhost
DB_PORT=3306
DB_DATABASE=neighbor_life
DB_USERNAME=root
DB_PASSWORD=your_mysql_password

# Redis配置 (可选)
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=

# JWT密钥
JWT_SECRET=your-super-secret-jwt-key-here

# 微信小程序配置
WECHAT_APP_ID=your-wechat-appid
WECHAT_APP_SECRET=your-wechat-secret

# 支付配置
WECHAT_MCH_ID=your-merchant-id
WECHAT_PAY_KEY=your-pay-key

# 服务器配置
PORT=3000
NODE_ENV=development
```

## 🔧 开发调试

### 后端API测试

```bash
# 测试API是否正常
curl http://localhost:3000/api/health

# 测试用户注册
curl -X POST http://localhost:3000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"phone":"13800138000","password":"123456"}'
```

### 管理后台访问

- 地址: http://localhost:3001
- 默认账号: admin
- 默认密码: 123456

### 小程序开发

1. 在微信开发者工具中打开项目
2. 修改 `miniprogram/utils/api.js` 中的API地址
3. 点击"编译"进行测试

## 📱 功能模块说明

### 🏠 微信小程序功能
- ✅ 用户注册/登录
- ✅ 商家列表/详情
- ✅ 商品浏览/搜索
- ✅ 购物车管理
- ✅ 订单下单/支付
- ✅ 订单列表/详情
- ✅ 实时配送跟踪
- ✅ 个人中心/积分
- ✅ 地址管理
- ✅ 优惠券系统

### 🖥️ 管理后台功能
- ✅ 数据可视化仪表板
- ✅ 用户管理
- ✅ 商家管理
- ✅ 订单管理
- ✅ 配送管理
- ✅ 财务报表
- ✅ 数据分析
- ✅ 系统设置

### 🔧 后端API功能
- ✅ 用户认证系统
- ✅ 商家管理
- ✅ 商品管理
- ✅ 订单处理
- ✅ 支付集成
- ✅ 配送管理
- ✅ 积分系统
- ✅ 优惠券系统

## 🐛 常见问题

### 1. npm 命令不存在
**问题**: `npm: 无法将"npm"项识别为 cmdlet`
**解决**: 安装 Node.js，下载地址: https://nodejs.org/

### 2. 数据库连接失败
**问题**: `ECONNREFUSED 127.0.0.1:3306`
**解决**: 
- 确保MySQL服务已启动
- 检查.env文件中的数据库配置
- 确认数据库用户名密码正确

### 3. 小程序API调用失败
**问题**: 网络请求失败
**解决**:
- 检查后端服务是否启动
- 在小程序开发工具中开启"不校验合法域名"
- 确认API地址配置正确

### 4. 管理后台登录失败
**问题**: 登录时提示网络错误
**解决**:
- 确认后端服务已启动
- 检查API地址配置
- 查看浏览器控制台错误信息

## 📞 技术支持

如遇到问题，请按以下步骤排查：

1. **检查服务状态**
   - 后端服务: http://localhost:3000/api/health
   - 管理后台: http://localhost:3001

2. **查看日志信息**
   - 后端日志: 终端输出
   - 前端日志: 浏览器开发者工具

3. **检查配置文件**
   - 后端: .env 文件
   - 前端: API地址配置

## 🎉 项目特色

### 技术亮点
- **后端**: Node.js + Koa2 + MySQL + Redis
- **前端**: React + Ant Design + ECharts
- **小程序**: 原生微信小程序
- **数据库**: 25个数据表，完整业务模型
- **功能**: 实时配送跟踪、积分系统、优惠券

### 业务特色
- **多角色**: 用户、商家、配送员、管理员
- **全流程**: 注册→浏览→下单→支付→配送→完成
- **实时性**: GPS跟踪、消息推送、状态同步
- **智能化**: 自动分配配送员、智能推荐

---

**🏠 邻·生活 - 连接社区，服务生活** ✨

祝您使用愉快！如有问题，欢迎交流。 