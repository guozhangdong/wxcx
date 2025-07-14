const Koa = require('koa');
const bodyParser = require('koa-bodyparser');
const routes = require('./routes');
const app = new Koa();

app.use(bodyParser());

app.use(routes.routes()).use(routes.allowedMethods());

module.exports = app;

if (!module.parent) {
  const PORT = process.env.PORT || 3000;
  app.listen(PORT, () => {
    console.log(`API server running on port ${PORT}`);
  });
}
