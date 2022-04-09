from pyecharts.charts import Geo
import pyecharts.options as opts
from commons import Faker
from pyecharts.globals import ChartType
(
    Geo()
    .add_schema(maptype='china')
    .add(series_name='',data_pair=[(i,j) for i,j in zip(Faker.provinces,Faker.values())],
         type_=ChartType.EFFECT_SCATTER)#特效散点图效果
    .set_global_opts(
        title_opts=opts.TitleOpts(title='中国地图'),
        visualmap_opts = opts.VisualMapOpts(
        is_piecewise=True))  #不是连续型的区域
).render_notebook()