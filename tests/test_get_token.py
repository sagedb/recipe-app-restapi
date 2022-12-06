import http.client

conn = http.client.HTTPSConnection("dev-mi7tccuttmum7131.us.auth0.com")

payload = "{\"client_id\":\"cMnz0ybRFRwBnWFyKk0pMZFVBwJTajxc\",\"client_secret\":\"6exl7WbxYhr5BTa9mYdeFQb6PRJGKzcINtiQ9AQSULs71pI8nx8Pd_nz0FeMFT7M\",\"audience\":\"https://icykitchen/api\",\"grant_type\":\"client_credentials\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
