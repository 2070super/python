from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

import pandas as pd

fpath = "data/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)
# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')

v1 = df["tianqi"].unique()
v2 = df["tianqi"].value_counts()

Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))\
    .add_xaxis(list(v1))\
    .add_yaxis("天气", v2.to_list())\
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))\
    .render("views/tianqi.html")