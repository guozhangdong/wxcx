const Router = require('koa-router');
const auth = require('./auth');

const router = new Router({ prefix: '/api/v1' });

router.get('/health', async ctx => {
  ctx.body = { success: true, message: '服务正常', timestamp: new Date() };
});

router.use('/auth', auth.routes());

module.exports = router;
