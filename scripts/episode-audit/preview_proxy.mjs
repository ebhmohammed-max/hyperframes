// Expose the loopback-only HyperFrames editor through Arena's preview host.
// No remote service calls: HTTP and websocket traffic stays in the workspace.
import http from 'node:http';
import net from 'node:net';

const upstreamPort = Number(process.env.UPSTREAM_PORT || 3002);
const previewPort = Number(process.env.PREVIEW_PORT || 3000);
const server = http.createServer((request, response) => {
  const upstream = http.request({
    hostname: '127.0.0.1', port: upstreamPort, path: request.url, method: request.method,
    headers: { ...request.headers, host: `localhost:${upstreamPort}` },
  }, (reply) => {
    const headers = { ...reply.headers };
    delete headers['x-frame-options'];
    response.writeHead(reply.statusCode ?? 502, headers);
    reply.pipe(response);
  });
  upstream.on('error', () => { response.writeHead(502); response.end('Editor is starting.'); });
  request.pipe(upstream);
});
server.on('upgrade', (request, socket, head) => {
  const upstream = net.connect(upstreamPort, '127.0.0.1', () => {
    upstream.write(`${request.method} ${request.url} HTTP/1.1\r\n`);
    for (const [key, value] of Object.entries(request.headers)) {
      upstream.write(`${key}: ${key === 'host' ? `localhost:${upstreamPort}` : value}\r\n`);
    }
    upstream.write('\r\n');
    if (head.length) upstream.write(head);
    socket.pipe(upstream).pipe(socket);
  });
  upstream.on('error', () => socket.destroy());
  socket.on('error', () => upstream.destroy());
});
server.listen(previewPort, '0.0.0.0', () => console.log(`Documentary editor available on port ${previewPort}`));
