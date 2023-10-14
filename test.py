import requests
from time import sleep

twse_url = "https://www.twse.com.tw/en/exchangeReport/MI_INDEX?response=csv&type=ALLBUT0999&date=20231013"

report = requests.get(twse_url)
sleep(10)

print(type(report))

content_of_report = report.text
print(type(content_of_report))

content_str_list = content_of_report.splitlines()

for line in content_str_list: 
    print(line)