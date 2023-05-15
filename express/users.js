const router = require('express').Router()
const usersController  = require('./users_controller')




router.route('/users')
.get(usersController.allUsers)

router.route('/signup')
.post(usersController.createNewUser)

router.route('/login')
.post(usersController.signin)
module.exports = router 
