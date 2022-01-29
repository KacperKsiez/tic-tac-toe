import socket as s

class Network():
    def __init__(self):
        self.format = 'utf-8'
        self.size = 128
        self.sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        
    def wait_for_client(self, ip='0.0.0.0', port=2137):
        self.addr = (ip, port)
        self.sock.bind(self.addr)
        self.sock.listen()
        self.sock, self.client_addr = self.sock.accept()
    
    def connect(self, ip, port):
        self.to_addr = (ip, port)
        self.sock.connect((ip, port))
        
    def send(self, text : str):
        self.sock.send(text.encode(self.format))
        
    def recv(self):
        return self.sock.recv(self.size).decode(self.format)
    
    def close(self):
        self.sock.close()
    
    def __del__(self):
        self.sock.close()