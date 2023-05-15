const express = require('express')
const app = express()
const http  = require('http')
const router = require('./users')
const postsRouter = require('./posts')
const bodyParser = require('body-parser')
require('dotenv').config()
const server = http.createServer(app)
const session = require('express-session')
require('dotenv').config()
const secret = process.env.secret

app.use(express.json())
app.use(session({
    secret,
    cookie:{
        sameSite:'strict'
    }
}))


app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended:true}))
app.use(router)
app.use(postsRouter)

server.listen(3001 , ()=>{
    console.log('Server is running ')
})