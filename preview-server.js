// Local visual preview helper. The production application remains app.py.
const http = require('http');
const fs = require('fs');
const path = require('path');
const root = __dirname;

http.createServer((req, res) => {
  const target = req.url === '/' ? 'templates/index.html' : req.url.replace(/^\//, '');
  const file = path.join(root, target);
  if (!file.startsWith(root) || !fs.existsSync(file)) return res.writeHead(404).end('Not found');
  let body = fs.readFileSync(file);
  if (target.endsWith('.html')) body = body.toString().replace("{{ url_for('static', filename='style.css') }}", '/static/style.css');
  const type = target.endsWith('.css') ? 'text/css' : 'text/html; charset=utf-8';
  res.writeHead(200, { 'Content-Type': type });
  res.end(body);
}).listen(4173, '127.0.0.1');
