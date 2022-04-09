from pyecharts.charts import Pie
import pyecharts.options as opts
import numpy as np

num = [110,136,108,111,112,103]
lab = ['哈士奇','萨摩耶','泰迪','金毛','牧羊犬','吉娃娃','柯基']
(
    Pie(init_opts=opts.InitOpts(width='720px',height='320px'))#默认900，600
    .add(series_name='', data_pair=[(j, i) for i, j in zip(num, lab)])#饼图
    #.add(series_name='',data_pair=[(j,i) for i,j in zip(num,lab)],radius=['40%','75%'])#环图
    #.add(series_name='', data_pair=[(j, i) for i, j in zip(num, lab)], rosetype='radius')#南丁格尔图
).render_notebook()



