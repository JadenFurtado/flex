const express = require('express')
const app = express()
const schema = require('./schema')
app.get('/', async(req, res)=>{
  try{
    var endpoint = req.query.endpoint;
    var sch = await schema.getSchema(endpoint);
    res.setHeader('Content-Type', 'application/json');
    res.send(JSON.stringify(sch));
  }catch (error) {
    return next(error)
  }
})

app.listen(3000)