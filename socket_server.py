import socket


# server类
class Server:
    IP_PORT = ('127.0.0.1', 8080)
    MAX_DATA = 1024

    # 等待连接
    def sock_request(self):
        server = socket.socket()
        server.bind(self.IP_PORT)
        server.listen()
        return server.accept()

    # 发送信息
    def send_data(self, conn):
        msg = input('请输入你想要发送的数据:').strip()
        conn.send(msg.encode('utf-8'))
        return msg

    # 接收数据
    def recv_data(self, conn):
        from_client_msg = conn.recv(self.MAX_DATA)
        print('from_client_msg:', from_client_msg.decode('utf-8'))
        return from_client_msg

    def main(self):
        flag = True
        conn, *_ = self.sock_request()
        while flag:
            while flag:
                from_client_msg = self.recv_data(conn)
                # print(from_client_msg)
                if from_client_msg.decode('utf-8') == 'q':
                    print('接收数据完成，准备发送数据了')
                    break
            while flag:
                msg = self.send_data(conn)
                if msg == 'q':
                    print('数据发送完成，准备接收数据了')
                    break


if __name__ == '__main__':
    s = Server()
    s.main()


