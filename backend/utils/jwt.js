const jwt = require('jsonwebtoken');
const secret = process.env.JWT_SECRET || 'secret';

exports.sign = payload => jwt.sign(payload, secret, { expiresIn: '7d' });
exports.verify = token => jwt.verify(token, secret);
