import http.client

conn = http.client.HTTPConnection("icykitchen.com")

headers = { 'authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkRmQUdxcElLeF8zeWNXN0lsZWFIayJ9.eyJpc3MiOiJodHRwczovL2Rldi1taTd0Y2N1dHRtdW03MTMxLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJjTW56MHliUkZSd0JuV0Z5S2swcE1aRlZCd0pUYWp4Y0BjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9pY3lraXRjaGVuL2FwaSIsImlhdCI6MTY3MDM1MDk1MSwiZXhwIjoxNjcwNDM3MzUxLCJhenAiOiJjTW56MHliUkZSd0JuV0Z5S2swcE1aRlZCd0pUYWp4YyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyJ9.QHbGJ3oARVZwsq-A6OfONF6Yt8kUwxpr46ofNTfGR1pQWXhzOkocjW1vLR_4-6UP-lJA4p3_2re92iw6wpFFsKGEbYpiAYrBUi0nYVK7g2FdJACoSPJPyQyaMB9lCcHLUykJ69VRnot2hSau8eqF-hTJP7ZlOH4wc9HgMWRSaTU_BOhUOH7qwmpnXRqz40MUESd7yAEM2AkUYuOc0wJUgrPmcM3pYzWUPOkRbCCDwfC-krOEnmXPsF20a51DgMG-80x64pSwP-zwlHVkPzl5-xe_YzcMwTMaFgThn8LVdhUQnDWd5uwq9VBrx7rtO1dOqBQH5A39ncFZsAiC1kUVNA" }

conn.request("GET", "/api", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
