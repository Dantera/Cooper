# POST OFFICE MODULE


# PostOffice Class
# -Inbox Queue
# -Outbox Queue
# -Incoming Worker Class (threaded)
# -Outgoing Worker Class (threaded)
class PostOffice:

    def __init__(self):
        # Queue's
        self.inbox = queue.Queue()
        self.outbox = queue.Queue()
        # Sender Worker Thread
        self.sender = threading.Thread(target=postoffice.Inbound, args=(self.inbox,))
        self.sender.setDaemon(True)
        self.sender.start()
        # Reciever Worker Thread
        self.reciever = threading.Thread(target=postoffice.Outbound, args=(self.outbox,))
        self.reciever.setDaemon(True)
        self.reciever.start()

    def send(self, message):
        with lock:
            self.outbox.put(message)

    def recieve(self):
        if self.inbox.empty():
            return None
        with lock:
            message = self.inbox.get()
        self.inbox.task_done()
        return message

    def compose(self, name, address, head, body):
        return {"from":name, "to":address, "head":head, "body":body}
    
    def is_valid_message(self, message):
        #return if message passes regex
        #^\{"{from}":"{+}","{to}":"{+}","{head}":"{+}","{body}":"{*}"\}$
        return True
    
    def sends(self, message, addresses):
        for address in addresses:
            self.send(message, address)
    
    def valid_message(message):
        #return if message passes regex
        #^\{"{from}":"{+}","{to}":"{+}","{head}":"{+}","{body}":"{*}"\}$
        return True


# Inbound Class
# -inbox queue reference
# -quit boolean
class Inbound:

    def __init__(self, inbox):
        self.io = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.io.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.io.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.io.bind(('', PORT))
        self.quit = False
        self.inbox = inbox

    def run():
        while not self.quit:
            # get incoming message
            message = self.recieve()
            # lock inbox and add message
            with lock:
                self.inbox.put(message)

    def recieve():
        data, address = io.recvfrom(1024) # get the data and address from IO
        print ('I')
        return json.loads(data.decode()), address # convert the bits to ascii to json object and return with address


# Outbound Class
# -outbox queue reference
# -quit boolean
# -delay int
class Outbound:

    def __init__(self, outbox):
        self.io = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.io.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.io.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.io.bind(('', PORT))
        self.quit = False
        self.outbox = outbox
        self.delay = 1

    def run():
        while not self.quit:
            if not self.outbox.empty():
                with lock:
                    message = self.outbox.get()
                self.send(message)
                self.outbox.task_done()
            time.sleep(self.delay)

    def send(self, message, address):
        print('O')
        io.sendto(json.dumps(message).encode, (address[0], address[1]))
