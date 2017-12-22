# SessionProxyReplayer

## Goal

This project aim to permit role cloisoning breach finding by saving first all the request you make with mitmproxy
and replay it automatically with changed cookie.

## Installation

You only need to have latest version of [Mitmproxy](http://mitmproxy.org) ( *installed version in Kali Linux need to be reinstalled* )

## Usage

First logging your navigation 
**Do not forget to add mitmproxy certificat to your browser(~/.mitmproxy/mitmproxy-ca-cert.cer)**:

```bash
./log_proxy.sh <outfile>
```

Replay it using another cookie :

```bash
./replay.sh <infile> <outfile> <cookie-name> <new-value>
```

Then you can analyze it using Mitmweb

```bash
  mitmweb -r <file>
```
