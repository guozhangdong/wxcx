# 邻·生活 - 微信云托管部署指南

## 🎯 云托管方案概述

使用微信云托管部署"邻·生活"平台具有以下优势：
- ✅ **零运维**: 无需管理服务器、数据库
- ✅ **自动扩缩容**: 根据访问量自动调整资源
- ✅ **深度集成**: 与微信小程序无缝对接
- ✅ **高可用**: 99.9%的服务可用性保证
- ✅ **成本优化**: 按实际使用量计费

## 📋 部署前准备

### 1. 开通微信云托管
1. 访问 [微信云托管控制台](https://cloud.weixin.qq.com/)
2. 使用小程序账号登录
3. 创建云托管环境
4. 记录环境ID (env-id)

### 2. 安装必要工具

```bash
# 安装云开发CLI
npm install -g @cloudbase/cli

# 登录云开发
cloudbase login

# 安装Docker (用于本地调试)
# Windows: 下载 Docker Desktop
# macOS: 下载 Docker Desktop
# Linux: 参考官方文档安装
```

## 🚀 部署步骤

### 第一步：配置云托管环境

1. **修改配置文件**
   
   编辑 `backend/cloudbaserc.json`:
   ```json
   {
     "envId": "你的环境ID",
     "region": "ap-shanghai"
   }
   ```

2. **配置环境变量**
   
   在云托管控制台设置环境变量：
   - `TCB_ENV`: 你的环境ID
   - `WECHAT_APP_ID`: 小程序AppID
   - `WECHAT_APP_SECRET`: 小程序AppSecret
   - `NODE_ENV`: production

### 第二步：部署后端服务

```bash
# 1. 进入后端目录
cd backend

# 2. 使用云托管专用配置
cp package-cloudbase.json package.json

# 3. 部署到云托管
cloudbase framework:deploy --env 你的环境ID

# 或者使用Docker方式部署
docker build -t neighbor-life-backend .
cloudbase run:deploy --name neighbor-life-api --image neighbor-life-backend
```

### 第三步：配置数据库

云托管使用云数据库，需要创建以下集合：

```javascript
// 在云开发控制台数据库中创建集合：
// 1. users - 用户信息
// 2. merchants - 商家信息  
// 3. dishes - 菜品信息
// 4. orders - 订单信息
// 5. coupons - 优惠券信息
// 6. addresses - 地址信息
// 7. delivery_tasks - 配送任务
```

### 第四步：配置小程序

1. **修改云配置**
   
   编辑 `miniprogram/project.config.json`:
   ```json
   {
     "cloudbaseEnv": "你的环境ID"
   }
   ```

2. **更新API配置**
   
   编辑 `miniprogram/utils/cloudbase.js`:
   ```javascript
   // 更新环境ID
   wx.cloud.init({
     env: '你的环境ID'
   });
   
   // 更新API基础地址
   const CLOUDBASE_API_BASE = 'https://你的环境ID.ap-shanghai.tcb.qcloud.la/neighbor-life-api';
   ```

### 第五步：测试部署

```bash
# 1. 检查服务状态
curl https://你的环境ID.ap-shanghai.tcb.qcloud.la/neighbor-life-api/health

# 2. 测试API接口
curl -X POST https://你的环境ID.ap-shanghai.tcb.qcloud.la/neighbor-life-api/auth/wx-login \
  -H "Content-Type: application/json" \
  -d '{"code":"test-code"}'
```

## 🔧 高级配置

### 自定义域名绑定

1. 在云托管控制台 -> 服务管理 -> 域名管理
2. 添加自定义域名
3. 配置SSL证书
4. 更新小程序API地址

### 版本管理

```bash
# 发布新版本
cloudbase run:deploy --name neighbor-life-api --version v1.1.0

# 流量切换
cloudbase run:switch --name neighbor-life-api --version v1.1.0 --traffic 100
```

### 监控与日志

1. **实时监控**: 云托管控制台 -> 监控告警
2. **日志查看**: 云托管控制台 -> 日志管理
3. **设置告警**: 当CPU/内存使用率过高时发送通知

## 📊 性能优化

### 1. 容器配置优化

```json
// cloudbaserc.json
{
  "framework": {
    "plugins": {
      "node": {
        "inputs": {
          "cpu": 1,
          "mem": 2,
          "minNum": 0,
          "maxNum": 50,
          "envVariables": {
            "NODE_ENV": "production"
          }
        }
      }
    }
  }
}
```

### 2. 数据库索引优化

在云数据库控制台为以下字段创建索引：
- `users.openid`
- `orders.customer_openid`
- `orders.status`
- `merchants.status`
- `dishes.merchant_id`

### 3. 缓存策略

```javascript
// 使用云数据库缓存
const cache = {
  async get(key) {
    const result = await db.collection('cache').where({ key }).get();
    return result.data[0]?.value;
  },
  
  async set(key, value, ttl = 3600) {
    await db.collection('cache').add({
      key,
      value,
      expires_at: new Date(Date.now() + ttl * 1000)
    });
  }
};
```

## 💰 成本控制

### 1. 资源用量监控

- **CPU时长**: 按秒计费，建议设置合理的最小实例数
- **内存用量**: 按GB*秒计费，根据实际需求调整
- **数据库读写**: 按次数计费，优化查询语句

### 2. 成本优化建议

- 设置合理的自动扩缩容策略
- 使用数据库索引减少查询时间
- 实现接口缓存减少重复计算
- 定期清理过期数据

## 🐛 常见问题解决

### 1. 部署失败

**问题**: `Error: deploy failed`
**解决**: 
- 检查cloudbaserc.json配置是否正确
- 确认环境ID是否有效
- 检查网络连接

### 2. 接口调用失败

**问题**: 小程序调用API返回404
**解决**:
- 确认服务已成功部署
- 检查API路径是否正确
- 验证环境ID配置

### 3. 数据库连接失败

**问题**: `Database connection failed`
**解决**:
- 确认已开通云数据库
- 检查集合权限设置
- 验证环境变量配置

## 📈 监控指标

### 关键指标监控

1. **服务可用性**: > 99.9%
2. **响应时间**: < 500ms
3. **错误率**: < 1%
4. **并发用户数**: 根据业务需求设定
5. **数据库连接数**: 监控连接池使用情况

### 告警设置

```bash
# 设置CPU使用率告警
cloudbase run:alarm --name neighbor-life-api --metric cpu --threshold 80

# 设置内存使用率告警  
cloudbase run:alarm --name neighbor-life-api --metric memory --threshold 80

# 设置错误率告警
cloudbase run:alarm --name neighbor-life-api --metric error-rate --threshold 5
```

## 🔐 安全配置

### 1. 网络安全

- 启用HTTPS加密传输
- 配置IP白名单（如需要）
- 使用云数据库安全规则

### 2. 数据安全

```javascript
// 云数据库安全规则示例
{
  "read": "auth != null && auth.openid == resource.openid",
  "write": "auth != null && auth.openid == resource.openid"
}
```

### 3. 接口安全

- 实现请求频率限制
- 添加参数验证
- 使用微信小程序登录态验证

## 🎉 部署成功验证

部署完成后，请验证以下功能：

1. ✅ 小程序能正常启动
2. ✅ 用户能成功登录
3. ✅ 能正常浏览商家和商品
4. ✅ 能成功下单和支付
5. ✅ 管理后台能正常访问
6. ✅ 数据统计正常显示

---

**🎊 恭喜！您的"邻·生活"平台已成功部署到微信云托管！**

现在您拥有了一个高可用、可扩展的本地生活服务平台，可以为用户提供优质的服务体验。

**技术支持**: 如遇问题，请参考微信云托管官方文档或联系技术支持。 