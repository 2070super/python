from pyecharts.charts import Bar,Line
import pyecharts.options as opts
num = [110,136,108,48,111,112,103]
lab = ['哈士奇','萨摩耶','泰迪','金毛','牧羊犬','吉娃娃','柯基']

bar =(
    Bar(init_opts=opts.InitOpts(width='720px',height='320px'))
    .add_xaxis(xaxis_data=lab)
    .add_yaxis(series_name='',yaxis_data=num)

)
lines = (
    Line(init_opts=opts.InitOpts(width='720px',height='320px'))
    .add_xaxis(xaxis_data=lab)
    .add_yaxis(series_name='',y_axis=num,label_opts=opts.LabelOpts(is_show=False))
)
bar.overlap(lines).render_notebook()