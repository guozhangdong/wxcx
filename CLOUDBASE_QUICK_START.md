# 微信云托管快速开始 - 5分钟部署"邻·生活"

## ⚡ 一键部署流程

### 第1步：准备环境 (1分钟)
```bash
# 安装云开发CLI
npm install -g @cloudbase/cli

# 登录微信云开发
cloudbase login
```

### 第2步：创建云托管环境 (2分钟)
1. 访问 [微信云托管控制台](https://cloud.weixin.qq.com/)
2. 创建新环境，选择地域：`ap-shanghai`
3. 记录环境ID，如：`env-12345678`

### 第3步：一键部署 (2分钟)
```bash
# 进入项目目录
cd backend

# 修改环境ID
sed -i 's/your-env-id/env-12345678/g' cloudbaserc.json

# 一键部署
cloudbase framework:deploy
```

## 🎯 配置检查清单

部署前请确认：
- ✅ 已开通微信云托管
- ✅ 已获取小程序AppID和AppSecret  
- ✅ 已安装cloudbase CLI
- ✅ 已修改cloudbaserc.json中的环境ID

## 🚀 部署成功验证

部署完成后访问：
```
https://你的环境ID.ap-shanghai.tcb.qcloud.la/neighbor-life-api/health
```

看到以下响应表示部署成功：
```json
{
  "success": true,
  "message": "服务正常",
  "timestamp": "2024-01-01T00:00:00.000Z",
  "env": "你的环境ID"
}
```

## 📱 小程序配置

修改 `miniprogram/utils/cloudbase.js`:
```javascript
// 更新为你的环境ID
wx.cloud.init({
  env: '你的环境ID'
});

// 更新API地址
const CLOUDBASE_API_BASE = 'https://你的环境ID.ap-shanghai.tcb.qcloud.la/neighbor-life-api';
```

## 🎉 完成！

现在您的"邻·生活"平台已成功部署到微信云托管，享受：
- 🔄 自动扩缩容
- 📊 实时监控
- 🛡️ 高可用保障
- 💰 按量计费

**问题反馈**: 遇到问题请查看详细部署指南 `CLOUDBASE_DEPLOYMENT_GUIDE.md` 