class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


class Server:
    __ip_counter = 0

    def __init__(self):
        Server.__ip_counter += 1
        self.ip = Server.__ip_counter
        self.buffer = []
        self.router = None

    def send_data(self, data):

        if self.router is not None:
            self.router.buffer.append(data)

    def get_data(self):

        received = self.buffer[:]
        self.buffer.clear()
        return received

    def get_ip(self):

        return self.ip


class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):

        self.servers[server.get_ip()] = server
        server.router = self

    def unlink(self, server):

        self.servers.pop(server.get_ip(), None)
        server.router = None

    def send_data(self):

        for data in self.buffer:
            target = self.servers.get(data.ip)
            if target is not None:
                target.buffer.append(data)
        self.buffer.clear()