# urn-resolver
Proof of concept URN resolver

```bash
pip3 install -r requirements.txt

flask  --app urn_resolver run

# resolver should be running at http://localhost:5000

# Examples:

curl http://localhost:5000/urn:wmo:md:int-eumetsat:EO:EUM:DAT:MSG:HRSEVIRI
```
