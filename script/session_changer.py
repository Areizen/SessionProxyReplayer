from mitmproxy.script import concurrent
import sys

@concurrent
def request(flow):
	flow.request.cookies[sys.argv[1]]=[sys.argv[2]]
