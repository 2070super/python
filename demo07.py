
#词云图
import pyecharts.options as opts
from pyecharts.charts import WordCloud
import pandas as pd

fpath = "data/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)
# 替换掉温度的后缀℃
df.loc[:, "bWendu"] = df["bWendu"].str.replace("℃", "").astype('int32')
df.loc[:, "yWendu"] = df["yWendu"].str.replace("℃", "").astype('int32')

v1 = df["tianqi"].unique()
v2 = df["tianqi"].value_counts()

list = [tuple(z) for z in zip(list(v1), v2.to_list())]

(
    WordCloud()
    .add(series_name="热点分析", data_pair=list, word_size_range=[20, 46])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="热点分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("views/basic_wordcloud.html")
)