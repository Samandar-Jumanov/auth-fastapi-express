const bcrypt = require('bcrypt')
require('dotenv').config()
const secret = process.env.secret
class HttpError extends Error {
    constructor(status, errCode) {
      super(status)
      this.status = status;
      this.errCode = errCode;
    }
  }



module.exports = HttpError







function authanticate(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (token == null) return res.sendStatus(401);

  jwt.verify(token,secret,  (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
} 
module.exports = authanticate