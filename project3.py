from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
HTTP_ACCESS_LOG = 'local_file.log'

local_file, headers = urlretrieve(URL_PATH, HTTP_ACCESS_LOG)

request_six = 0
request_total = 0

for line in open(local_file):
    if "May/1995" in line:
        request_six += 1
    elif "Jun/1995" in line:
        request_six += 1
    elif "Jul/1995" in line:
        request_six += 1
    elif "Aug/1995" in line:
        request_six += 1
    elif "Sep/1995" in line:
        request_six += 1
    elif "Oct/1995" in line:
        request_six += 1

for line in open(local_file):
    if "1994" in line or "1995" in line:
        request_total += 1

print("Total requests made in the last 6 months:", request_six)
print("Total requests made in the time period represented by the log:", request_total)
