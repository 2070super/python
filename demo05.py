
from pyecharts.charts import Bar
from pyecharts import options as opts
# 内置主题类型可查看 pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

import pandas as pd

xlsx_path = "data/baidu_stocks.xlsx"
df = pd.read_excel(xlsx_path, index_col="datetime", parse_dates=True)

df = df.head(30)

# 行和列都按区间查询
v1 = df.loc[:, :]
print(v1)


# 不习惯链式调用的开发者依旧可以单独调用方法
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(df.index.to_list())
bar.add_yaxis("开盘价", df["open"].round(2).to_list())
bar.add_yaxis("收盘价", df["close"].round(2).to_list())
bar.set_global_opts(title_opts=opts.TitleOpts(title="百度股价", subtitle="柱状图"))
bar.render("demo05.html")
bar.render("demo05.html")