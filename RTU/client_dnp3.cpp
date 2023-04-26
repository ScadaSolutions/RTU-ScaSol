#include <iostream>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>
#include <chrono>
#include <thread>
#include <sstream>

using namespace std;

int main(){
	int sock=0, valread;
	struct sockaddr_in serv_addr;
	char buffer[1024] = {0};
	const char* conn_msg = "CONN";
	float servo, temp_f, temp_c, rocker, relay;


	if((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0){
		cout << "Socket creation error" << endl;
		return -1;
	}

	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(65432);

	if(inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr)<=0){
		cout << "Addr not supported" << endl;
		return -1;
	}

	if(connect(sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr))<0){
		cout << "Addr not supported" <<endl;
		return -1;
	}

	while(1){
		send(sock, conn_msg, strlen(conn_msg), 0);
		valread = read(sock, buffer, 1024);
		cout << "Received: " << buffer << endl;
		std::stringstream ss(buffer);
		char delimiter;

		ss >> servo >> delimiter >> temp_c >> delimiter >> temp_f >> delimiter >> rocker >> delimiter >> relay;

		cout << "Servo: " << servo << endl;
		cout << "temp C: " << temp_c << endl;
		cout << "Temp F: " << temp_f << endl;
		cout << "Rocker: " << rocker << endl;
		cout << "Relay: " << relay << endl;

		//std::this_thread::sleep_for(std::chrono::seconds(0.5));
	}

	close(sock);

	return 0;
}
