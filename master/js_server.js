const net = require('net');

const server = net.createServer((socket) => {
	console.log('Client connected');

	socket.on('data', (data) => {
		//console.log(JSON.stringify(data));
		data = data.toString();
		data = data.split(",");
		data = data.slice(0,2);
		console.log(data)
		socket.write('ACK');
	});

	socket.on('end', () => {
		console.log('Client disconnected');
	});
});

const PORT = 10000;
server.listen(PORT, () => {
	console.log(`Server listening on port ${PORT}`);
});

