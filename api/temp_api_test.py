import urllib.request
import urllib.error
import json

for url, payload in [
    ('http://127.0.0.1:8000/api/email/', {'email': 'test@example.com'}),
    ('http://127.0.0.1:8000/api/suggestion/', {'email': 'test@example.com', 'message': 'hello'})
]:
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=5) as res:
            print(url, res.status)
            print(res.read().decode())
    except urllib.error.HTTPError as e:
        print(url, 'HTTPError', e.code)
        print(e.read().decode())
    except Exception as e:
        print(url, 'ERROR', e)
