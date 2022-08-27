const http = require('http');
const fs = require("fs");
const urlLib = require("url");
const path = require("path");

const server = http.createServer((req, res) => {
    const {headers, url, method} = req;
    res.setHeader('content-type', 'text/html');
    if(url === '/') {
        fs.readFile('./src/index.html', 'utf8', (error, data) => {
            if(error) {
                res.statusCode = 500;
                res.write('<h1>Error!</h1>');
                res.end();
            }else {
                res.statusCode = 200;
                res.write(data);
                res.end();
            }
        });
    }else if(url === '/login'){
        // Login form html butsaana
        fs.readFile('./src/login.html', 'utf8', (error, data) => {
            res.statusCode = 200;
            res.write(data);
            res.end();
        });
    } else if(url === '/logincheck' && method === "POST") {
        // login hiisnii daraa usreh heseg
        // DATA ==> CHUNK1 ===> CHUNK2 ===> CHUNK ==
        const body = [];
        req.on('data', (chunk)=>{
            body.push(chunk)
        });
        req.on('end', ()=> {
            const parsedBody = Buffer.concat(body).toString();
            const password = parsedBody.split('=')[2];
            if(password === 'jakit123'){
                // login successful
                res.statusCode = 302; // request has been temporarily moved to the URL given by the Location header
                res.setHeader('Location', '/home');
                res.end();
            }else {
                // login failed
                res.statusCode = 302; 
                res.setHeader('Location', '/error');
                res.end();
            }
            // fs.writeFileSync('logininfo.txt', parsedBody);
            // res.write('Za hvleej awlaa.');
            // res.end();
        })
    }else if (url === '/home'){
        fs.readFile('./src/home.html', 'utf8', (error, data) => {
            res.statusCode = 200;
            res.write(data);
            res.end();
        });
    }else if(url === '/error'){
        fs.readFile('./src/error.html', 'utf8', (error, data) => {
            res.statusCode = 200;
            res.write(data);
            res.end();
        });
    }else if(url.endsWith('.jpg') || url.endsWith(".png")) {
        const parsed = urlLib.parse(url);
        const fileName = path.basename(parsed.pathname);
        // console.log('------>', fileName);
        fs.readFile('./src/img/' + fileName, (error, data) => {
            res.statusCode = 200;
            res.setHeader('content-type', 'image/jpg');
            res.end(data);
        });
    }else if(url.endsWith('.pdf')){
        const parsed = urlLib.parse(url);
        const fileName = path.basename(parsed.pathname);
        fs.readFile('./src/pdf/'+ fileName, (error, data) => {
            res.statusCode = 200;
            res.setHeader('content-type', 'application/pdf');
            res.end(data);
        });
    }else if(url.endsWith('.css')){
        const parsed = urlLib.parse(url);
        const fileName = path.basename(parsed.pathname);
        fs.readFile('./src/css/'+ fileName, (error, data) => {
            res.statusCode = 200;
            res.setHeader('content-type', 'text/css');
            res.end(data);
        });
    }else if(url.endsWith('.js')){
        const parsed = urlLib.parse(url);
        const fileName = path.basename(parsed.pathname);
        fs.readFile('./src/js/'+ fileName, (error, data) => {
            res.statusCode = 200;
            res.setHeader('content-type', 'text/javascript');
            res.end(data);
        });
    }else {
        res.statusCode = 404;
        res.write('<h1>404 not found</h1>');
        res.end();
    }
});

server.listen(5000, () => { 
    console.log('http сервер 5000 порт дээр аслаа...');
});