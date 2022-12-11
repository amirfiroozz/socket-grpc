const WebSocket = require('ws');
var babar = require('babar');
const closeConn = ()=>{
  ws.close()
}

const create = (arr)=>{
  n = []
  for (let index = 0; index < arr.length; index++) {
    n.push([index,arr[index]])
    
  }
  return n
}
function update(e){ 
  let data = JSON.parse(e.data)
  if (data.isDone) {
    console.log("finished")
    closeConn()
    return
  }
  console.log(babar(create(data.array)))
  
};
var ws = new WebSocket("ws:\/\/localhost:8080/sort");

ws.onmessage = update;
const object = {
  array:Array.from({length: 30}, () => Math.floor(Math.random() * 20)),
  type:"merge",
  sleepTime: 1
}
console.log(object.array)
ws.onopen = () => {
  ws.send(JSON.stringify(object)) 
}
