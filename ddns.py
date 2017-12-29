import requests

#domain whose DNS records are to be retrieved
domain = ""
#DNS record name for which DNS records are to be retrieved
name = ""
#public (production) key for godaddy developer api
key = ""
#private (production) key for godaddy developer api
secret = ""
#url address for godaddy api
godaddy_api = "https://api.godaddy.com/v1/domains/" + domain + "/records/A/" + name
#url address for ipinfo api
ipinfo_api = "https://ipinfo.io/json"

#headers required by godaddy for authorization
headers = {
    "Accept": "application/json",
    "Authorization": "sso-key " + key + ":" + secret
}

def get(url, headers):
    r = requests.get(url, headers = headers)
    if r.status_code == 200:
        return r.json()
    else:
        print("something went wrong... status code: " + r.status_code)
        quit()

def put(url, headers, data):
    r = requests.put(url, headers = headers, data = data)
    if r.status_code != 200:
        print("something went wrong... status code: " + r.status_code)
        quit()

godaddy_ip = get(godaddy_api, headers)[0]["data"]

current_ip = get(ipinfo_api, {})["ip"]

if godaddy_ip != current_ip:
    put(godaddy_api, headers, {"data": current_ip})
    print("ip changed to " + current_ip)
else:
    print "no change required"
