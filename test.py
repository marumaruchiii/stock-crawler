import requests
import numpy as np
from bokeh.plotting import figure, show
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




#graphic
x = np.arange(0, 10, 1)
y1 = x **2
y2 = x **3
y3 = x **4


p = figure (title="Simple Line Charts", x_axis_label="x", y_axis_label="y")


p.line(x, y1, legend_label="", line_width=2, color="red")
p.line(x, y2, legend_label="", line_width=2, color="green")
p.line(x, y3, legend_label="", line_width=2, color="blue")

show(p)