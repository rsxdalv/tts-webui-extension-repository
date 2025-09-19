#!/usr/bin/env python3
"""Minimal static file server for the `simple/` pip index.

This intentionally does one thing only: change into `simple/` and call
the standard library's `http.server.test()` function. No argument
parsing, no extra features — just a small wrapper so you can run:

  python serve_index.py

which will listen on port 8787 by default (like the previous wrapper).
"""
import os
import sys
from http.server import test

ROOT = os.path.dirname(__file__)
SIMPLE = os.path.join(ROOT, 'simple')


def main():
    port = 8787
    # Allow overriding port with a single numeric argument for convenience
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except Exception:
            pass

    if not os.path.isdir(SIMPLE):
        print('Run generate_index.py first: no simple/ directory found', file=sys.stderr)
        return 1

    os.chdir(SIMPLE)
    # Delegate to stdlib test() which uses SimpleHTTPRequestHandler
    test(port=port)


if __name__ == '__main__':
    sys.exit(main())
