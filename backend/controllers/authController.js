const Joi = require('joi');
const jwt = require('../utils/jwt');

const users = []; // in-memory users for demo

exports.register = async ctx => {
  const schema = Joi.object({ username: Joi.string().required(), password: Joi.string().required() });
  const { error, value } = schema.validate(ctx.request.body);
  if (error) { ctx.status = 400; ctx.body = { error: error.details[0].message }; return; }
  const user = { id: users.length + 1, ...value };
  users.push(user);
  ctx.body = { success: true, data: user };
};

exports.login = async ctx => {
  const { username, password } = ctx.request.body;
  const user = users.find(u => u.username === username && u.password === password);
  if (!user) { ctx.status = 401; ctx.body = { error: 'Invalid credentials' }; return; }
  const token = jwt.sign({ id: user.id, username: user.username });
  ctx.body = { success: true, token };
};
