from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline

# 创建 Timeline 实例
timeline = Timeline()

# 模拟不同年份的 GDP 数据
years = ['2017', '2018', '2019', '2020']
gdp_data = [
    [12345, 23456, 34567, 45678],
    [23456, 34567, 45678, 56789],
    [34567, 45678, 56789, 67890],
    [45678, 56789, 67890, 78901]
]

# 遍历每个年份
for i, year in enumerate(years):
    # 创建 Bar 实例
    bar = (
        Bar()
        .add_xaxis(["城市A", "城市B", "城市C", "城市D"])
        .add_yaxis(year, gdp_data[i])
        .set_global_opts(title_opts=opts.TitleOpts(title="{} 年 GDP 柱状图".format(year)))
    )
    # 添加到 Timeline 中
    timeline.add(bar, year)

# 渲染生成 HTML 文件
timeline.render("GDP_bar_chart.html")