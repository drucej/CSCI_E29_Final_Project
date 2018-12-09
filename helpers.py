import pandas as pd

table = pd.read_html("https://www.pgatour.com/stats/stat.295.html")

print(table[0])


