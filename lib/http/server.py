from http.server import HTTPServer
from lib.http.pingback_handler import PingbackHandler
import threading


class NodeHttpServer:
    PINGBACK_PORT = 5800

    PINGBACK_SERVER = None

    def start_pingback_server(self):
        try:

            # Create a web server and define the handler to manage the
            # incoming request
            self.PINGBACK_SERVER = HTTPServer(('0.0.0.0', self.PINGBACK_PORT), PingbackHandler)
            print
            'Pingback server for client running on port ', self.PINGBACK_PORT

            # thread = threading.Thread(target=self.PINGBACK_SERVER.serve_forever())
            #
            # thread.setdaemon = True
            #
            # thread.start()
            self.PINGBACK_SERVER.serve_forever()

        except KeyboardInterrupt:
            print
            '^C received, shutting down the pingback web server'
            self.PINGBACK_SERVER.socket.close()
