from mitmproxy.script import concurrent
import sys

@concurrent
def request(flow):
	if sys.argv[1] in flow.request.cookies:
		flow.request.cookies[sys.argv[1]]=[sys.argv[2]]
