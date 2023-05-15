const pool = require('./db')
const { Sequelize, DataTypes } = require('sequelize');


require('dotenv').config()
const databaseConnection = process.env.databaseConnection
const sequelize = new Sequelize(databaseConnection)


const User = sequelize.define('User', {
    name: {
      type: DataTypes.STRING,
      allowNull: false
    },
    email: {
      type: DataTypes.STRING,
      allowNull: false,
      unique: true
    },
    password: {
      type: DataTypes.STRING,
      allowNull: false ,
      validate: {
        len: [6, 100] // Require password to be at least 6 characters long
      }
    }
  });
  
  (async () => {
    await sequelize.sync({ force: true });
    console.log('Tables created!');
  })();



module.exports = User

const Posts =  sequelize.define('Posts', {
  title:{
    type :  DataTypes.STRING ,
    allowNull: false 
  },
  content :{
    type : DataTypes.STRING ,
    allowNull : false 
  }
})

async function sequelizePosts(){
  await sequelize.sync({force : true})
  console.log('Posts table created ')
}

sequelizePosts()



module.exports = Posts

