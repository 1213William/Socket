import socket


# 客户端类
class Client:
    IP_PORT = ('127.0.0.1', 8080)
    MAX_DATA = 1024

    # 等待连接
    def sock_request(self):
        client = socket.socket()
        client.connect(self.IP_PORT)
        return client

    # 发送信息
    def send_data(self, client):
        msg = input('请输入你想要发送的数据:').strip()
        client.send(msg.encode('utf-8'))
        return msg

    # 接收数据
    def recv_data(self, client):
        from_server_msg = client.recv(self.MAX_DATA)
        print('from_server_msg:', from_server_msg.decode('utf-8'))
        return from_server_msg

    def main(self):
        flag = True
        client = self.sock_request()
        while flag:
            while flag:
                msg = self.send_data(client)
                if msg == 'q':
                    print('数据发送完成，准备接收数据了')
                    break
            while flag:
                from_server_msg = self.recv_data(client)
                if from_server_msg.decode('utf-8') == 'q':
                    print('数据接收完成，准备接收数据了')
                    break


if __name__ == '__main__':
    c = Client()
    c.main()
