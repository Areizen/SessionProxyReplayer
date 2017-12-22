from mitmproxy.script import concurrent
import sys

@concurrent
def request(flow):
	replace = ""
	if len(sys.argv) == 3 :
		replace = sys.argv[2]
	if sys.argv[1] in flow.request.cookies.keys():
		flow.request.cookies[sys.argv[1]] = replace
