import urllib.request

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

fp = urllib.request.urlopen("https://t.me/c/1726846911/33")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)