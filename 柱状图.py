from pyecharts.charts import Bar
import pyecharts.options as opts
num = [110,136,108,48,111,112,103]
lab = ['哈士奇','萨摩耶','泰迪','金毛','牧羊犬','吉娃娃','柯基']

(
    Bar(init_opts=opts.InitOpts(width='720px',height='320px'))
    .add_xaxis(xaxis_data=lab)
    .add_yaxis(series_name='',yaxis_data=num)

).render_notebook()