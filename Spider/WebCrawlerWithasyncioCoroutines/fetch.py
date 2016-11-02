import socket
from selectors import DefaultSelector, EVENT_WRITE


class Fetcher(object):
    def __init__(self,url):
        self.response = b''  # Empty array of bytes.
        self.url = url
        self.sock = None
        self.selector=DefaultSelector()
        self.urls_todo = set(['/'])
        self.seen_urls = set(['/'])

    def fetch(self):
        self.sock=socket.socket()
        self.sock.setblocking(False)
        self.selector=DefaultSelector()
        self.selector.register(self.sock.fileno(), EVENT_WRITE, self.connected)
        try:
            self.connect(('xkcd.com', 80))
        except BlockingIOError:
            pass

        request = 'GET {} HTTP/1.0\r\nHost: xkcd.com\r\n\r\n'.format(url)
        encoded=request.encode('ascii')

    def read_response(self, key, mask):
        global stopped

        chunk = self.sock.recv(4096)  # 4k chunk size.
        if chunk:
            self.response += chunk
        else:
            self.selector.unregister(key.fd)  # Done reading.
            links = self.parse_links()

            # Python set-logic:
            for link in links.difference(self.seen_urls):
                self.urls_todo.add(link)
                Fetcher(link).fetch()  # <- New Fetcher.

            self.seen_urls.update(links)
            self.urls_todo.remove(self.url)
            if not self.urls_todo:
                stopped = True

    def loop(self):
        while not stopped:
            events = self.selector.select()
            for event_key, event_mask in events:
                callback = event_key.data
                callback()

