# 1. Starting from Scratch: Basic Web Application

### Creating our application

> We will need git and npm installed. But don’t worry, these are already installed on our platform. So you can straight away use them in our terminal widget.

```bash
mkdir aws-bootstrap && cd aws-bootstrap
git init
npm init -y
```

```js
const { hostname } = require("os");
const http = require("http");
const message = "Hello World\n";
const port = 8080;
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");
  res.end(message);
});
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname()}:${port}/`);
});
```

We can run our application directly with the node command.

```node
node server.js
Server running at http://localhost:8080/
```

And we can test it with curl from another terminal window.

```node
curl localhost:8080
Hello World
```

Next, let’s use a process manager to monitor our application so that it automatically restarts if it crashes. To do this, we need to modify our package.json file.

```json
{
  "name": "aws-bootstrap",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "start": "node ./node_modules/pm2/bin/pm2 start ./server.js --name hello_aws --log ../logs/app.log ",
    "stop": "node ./node_modules/pm2/bin/pm2 stop hello_aws",
    "build": "echo 'Building...'"
  },
  "dependencies": {
    "pm2": "^4.2.0"
  }
}
```
