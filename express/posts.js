const router  = require('express').Router()
const authenticate = require('./utils')
const Posts = require('./models')

router.get('/', authenticate, async (request, response, next) => {
    try {
      const allPosts = await Posts.findAll({ limit: null })
      return response.json(allPosts)
    } catch (error) {
      return next(error)
    }
  })

  
  module.exports = router 