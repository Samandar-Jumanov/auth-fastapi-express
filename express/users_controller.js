const User = require('./models')
const HttpError = require('./utils')
const bcrypt = require('bcrypt')
require('dotenv').config()
const  secret = process.env.secret
const jwt = require('jsonwebtoken')

exports.allUsers  = async (request , response , next )=>{
try{
    const allUsers = await User.findAll({limit : null})
    response.json(allUsers)
}catch(err){
   console.log(err)
   return  next (new HttpError(500,err))
}
}



exports.createNewUser = async (request, response, next) => {
    const { name, email, password } = request.body;
  
    const user = await User.findOne({ where: { email } });
    if (user) {
      return response.status(401).json({ message: 'You already have an account' });
    }
  
    try {
      const hashPassword = await bcrypt.hash(password, 12);
      const newUser = await User.create({ name, password: hashPassword, email });
      const token =  jwt.sign({user:newUser.id }, secret)
      response.json(newUser  , token);
    } catch (err) {
      console.log(err);
      response.status(500).json({"message":"An err occured when creating user"})

    }
  };
  
 

  exports.signin = async (request, response, next) => {
    const { email, password } = request.body;
    const user = await User.findOne({ where: { email } });
    const validPassword = await bcrypt.compare(password, user.password);
     
    if (!user || !validPassword) {
            next( new HttpError(404, 'Cannot find user'))
    }
    try {
      const token = jwt.sign({user : user.id}, secret )
      response.json({user , token});
    } catch (err) {
      response.status(500).json({ "message":"Error while logging in"})
    }
  };
  

  async function refresh(token) {
    try {
      const decoded = jwt.verify(token,secret);
      const { user_id, email } = decoded;
  
      const newToken = jwt.sign({user_id,email,},secret,{ expiresIn:50000,});
  
      return newToken;
    } catch (err) {
      console.log('Error refreshing token:', err);
      throw new Error(err);
    }
  }

exports.signOut = async (request , response , next ) =>{
  const token = request.cookies.jwt;
  if (token) {
    jwt.verify(token, secret, (err, decodedToken) => {
      if (err) {
        console.error(err);
      } else {
        response.clearCookie('jwt');
      }
    });
  }
  response.status(200).json({ message: 'User signed out successfully' })
}

 
