from pyecharts.charts import Geo,Map
import pyecharts.options as opts
from pyecharts.globals import ChartType,SymbolType

city_num = [('广州',105),('成都',105),('北京',105),('西安',105)]
start_end = [('广州','成都'),('广州','北京'),('广州','西安')]

(
    Geo()
    .add_schema(maptype='china',#设置地图类型
               itemstyle_opts = opts.ItemStyleOpts(color='#323c48',#设置背景颜色
                                                   border_color='#111'))#边界颜色
    .add('',data_pair =  city_num,color = 'white')#添加数据，默认是点
    .add('',data_pair=start_end,type_=ChartType.LINES,#把start_end用线描绘
         effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW, #把特效的线改成箭头
                                     color='blue',
                                     symbol_size=8   #箭头的大小
                                    )
        )
).render("views/basic_scatter_chart.html")