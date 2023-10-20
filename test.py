import requests
from time import sleep

twse_url = "https://www.twse.com.tw/en/exchangeReport/MI_INDEX?response=csv&type=ALLBUT0999&date=20231013"
tpex_url = "https://www.tpex.org.tw/web/stock/aftertrading/daily_close_quotes/stk_quote_result.php?l=en-us&o=csv&se=EW&s=0,asc,0&d=20231013"

#Fu
def get_exchange_report(url):
    report = requests.get(url)
    sleep(10)
    content = report.text
    return content

print("### TWSE REPORT ###")
twse_report = get_exchange_report(twse_url).splitlines()
for line in twse_report:
    print(line)

print("### TPEX REPORT ###")
tpex_report = get_exchange_report(tpex_url).splitlines()
for line in tpex_report:
    print(line)

