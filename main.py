from lib.network.scanner import Scanner
from lib.http.server import NodeHttpServer
import threading
import time

# sc = Scanner()
#
#
# def scan_stuffs():
#     while True:
#         sc.find_all_peers()
#         time.sleep(10)
#
#
# thread = threading.Thread(target=scan_stuffs())

pb = NodeHttpServer()
pb.start_pingback_server()
