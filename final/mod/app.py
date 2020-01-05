from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie, Timeline,Map,Line
from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly.graph_objects as go
import plotly as py
app = Flask(__name__)

# 准备工作
df = pd.read_csv('Potentially_Excess_Deaths_from_the_Five_Leading_Causes_of_Death_2005_Fixed.csv')#读取
Locality_available = list(df.Locality.dropna().unique())#列表下拉值赋予给regions_available
cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()

@app.route('/',methods=['GET'])
def IV_final() -> 'html':
    Year = list(df['Year'].unique())
    Locality = list(df['Locality'].unique())

    def line_base() -> Line:
        a1 = []
        a2 = []
        a3 = []
        a4 = []
        a5 = []
        for st in Year:
            df4 = df[df.Year == st]
            a1.append(sum(df4['Percent Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Heart Disease')]))
            a2.append(sum(df4['Percent Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Cancer')]))
            a3.append(sum(df4['Percent Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Chronic Lower Respiratory Disease')]))
            a4.append(sum(df4['Percent Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Stroke')]))
            a5.append(sum(df4['Percent Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Unintentional Injury')]))
        c = (
            Line()
                .add_xaxis(Year)
                .add_yaxis(
                "Heart Disease",
                a1
            )
               
                .add_yaxis(
                "Cancer",
                a2
            )
                .add_yaxis(
                "Chronic Lower Respiratory Disease",
                a3
            )
               
                .add_yaxis(
                "Stroke",
                a4
            )
                .add_yaxis(
                "Unintentional Injury",
                a5
            )


                .set_global_opts( title_opts=opts.TitleOpts(title="美国2005-2015年五个主要原因潜在死亡人数占比趋势",subtitle="潜在死亡人数",pos_top="5%"),toolbox_opts=opts.ToolboxOpts(),datazoom_opts=opts.DataZoomOpts(),)
        )
        return c

    line_base().render()
    with open("render.html", encoding="utf8", mode="r") as f:
        plot_all2 = "".join(f.readlines())

    data_str = df.to_html()
##to here
    return render_template('results2.html',
                            the_plot_all2 = plot_all2,
                            the_select_region=Locality_available,
                           )

@app.route('/IV_final',methods=['POST'])
def IV_final_select() -> 'html':
    time = list(df['Year'].unique())
    Reason = list(df['Cause of Death'].unique())
    Locality = list(df['Locality'].unique())
    Locality.remove('All')
    Year = list(df['Year'].unique())
    Locality = list(df['Locality'].unique())

    def line_base() -> Line:
        a1 = []
        a2 = []
        a3 = []
        a4 = []
        a5 = []
        for st in Year:
            df4 = df[df.Year == st]
            a1.append(sum(df4['Percent Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Heart Disease')]))
            a2.append(sum(df4['Percent Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Cancer')]))
            a3.append(sum(df4['Percent Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Chronic Lower Respiratory Disease')]))
            a4.append(sum(df4['Percent Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Stroke')]))
            a5.append(sum(df4['Percent Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Unintentional Injury')]))
        c = (
            Line()
                .add_xaxis(Year)
                .add_yaxis(
                "Heart Disease",
                a1
            )
               
                .add_yaxis(
                "Cancer",
                a2
            )
                .add_yaxis(
                "Chronic Lower Respiratory Disease",
                a3
            )
               
                .add_yaxis(
                "Stroke",
                a4
            )
                .add_yaxis(
                "Unintentional Injury",
                a5
            )


                .set_global_opts( title_opts=opts.TitleOpts(title="美国2005-2015年五个主要原因潜在死亡人数占比趋势",subtitle="潜在死亡人数",pos_top="5%"),toolbox_opts=opts.ToolboxOpts(),datazoom_opts=opts.DataZoomOpts(),)
        )
        return c

    line_base().render()
    with open("render.html", encoding="utf8", mode="r") as f:
        plot_all2 = "".join(f.readlines())

    data_str = df.to_html()
##to here
    return render_template('results2.html',
                            the_plot_all2 = plot_all2,
                            the_select_region=Locality_available,
                           )

    def timeline_bar() -> Timeline:
        x = Reason
        tl = Timeline()
        for i in time:
            df2 = df[df.Year == int(i)]
            n1 = []
            n2 = []
            n3 = []
            n4 = []
            n5 = []         
            for a in Reason:
                df3 = df2[df2['Cause of Death'] == a]
                n1.append(sum(df2['Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Heart Disease')]))
                n2.append(sum(df2['Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Cancer')]))
                n3.append(sum(df2['Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Chronic Lower Respiratory Disease')]))
                n4.append(sum(df2['Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Stroke')]))
                n5.append(sum(df2['Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Unintentional Injury')]))
            bar = (
                Bar()
                    .add_xaxis(x)
                    .add_yaxis("Heart Disease", n1)
                    .add_yaxis("Cancer", n2)
                    .add_yaxis("Chronic Lower Respiratory Disease", n3)
                    .add_yaxis("Stroke", n4)
                    .add_yaxis("Unintentional Injury", n5)

                    .set_global_opts(title_opts=opts.TitleOpts("美国{}年药物中毒死亡人数".format(i)))
            )
            tl.add(bar, "{}年".format(i))
        return tl

    timeline_bar().render()
    with open("render.html", encoding="utf8", mode="r") as f:
        plot_all1 = "".join(f.readlines())

    data_str = df.to_html()
##to here
    return render_template('results2.html',
                            the_plot_all = plot_all1,
                            the_plot_all2 =  plot_all2,
                            the_res = data_str,
                            the_select_region=Locality_available,
                           )


@app.route('/2', methods=['GET'])
def IV_final_2020():
    Locality_available = list(df.Year.dropna().unique())
    cf.set_config_file(offline=True, theme="ggplot")
    py.offline.init_notebook_mode()
    data_str = df.to_html()
    return render_template('results3.html',
                           the_res = data_str,
                           the_select_region=Locality_available)

@app.route('/IV_final2',methods=['POST'])
def map() -> 'html':
    Locality_available = list(df.Year.dropna().unique())
    cf.set_config_file(offline=True, theme="ggplot")
    py.offline.init_notebook_mode()
    the_region = request.form["the_region_selected"]
    dfs = df.query("Year=='{}'".format(the_region))
    State = list(dfs['State'].unique())
    State.remove('United States')
    z = []
    for st in State:
        df4 = dfs[dfs.State == st]
        z.append(sum(df4['Potentially Excess Deaths'][(df['Locality'] == 'All')][(df['Cause of Death'] == 'Stroke')]))

    fig = go.Figure(data=go.Choropleth(
    locations=State,  # Spatial coordinates
    z=z,  # Data to be color-coded
    locationmode='USA-states',  # set of locations match entries in `locations`
    colorscale='Reds',
    colorbar_title="人数",
    ))

    fig.update_layout(
        title_text='2005-2015年美国各州中风潜在死亡人数',
        geo_scope='usa',  # limite map scope to USA
    )

    py.offline.plot(fig, filename="us.html", auto_open=False)
    with open("us.html", encoding="utf8", mode="r") as f:
        plot_all2 = "".join(f.readlines())

    #with open("render1.html", encoding="utf8", mode="r") as f:
        #plot_all3 = "".join(f.readlines())


    data_str = df.to_html()

    return render_template('results3.html',
                           the_plot_all2 = plot_all2,
                            the_res = data_str,
                            the_select_region=Locality_available,
                           )

@app.route('/3',methods=['GET'])
def IV_final_2021():
    data_str = df.to_html()
    return render_template('results4.html',
                           the_res = data_str,
                           the_select_region=Locality_available)

@app.route('/IV_final3',methods=['POST'])
#图表
def IV_final_select2() -> 'html':
    the_region = request.form["the_region_selected"]
    time = list(df['Year'].unique())
    Locality = list(df['Locality'].unique())
    Locality.remove('All')
    dfs = df.query("Locality=='{}'".format(the_region))

    def line_base() -> Line:
        z1 = []
        z2 = []
        z3 = []
        z4 = []
        z5 = []
        times = []
        for t in list(time):
            times.append(str(t))
        for t in time:
            df5 = dfs[dfs.Year == t]
            z1.append(sum(df5['Percent Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Heart Disease')]))
            z2.append(sum(df5['Percent Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Cancer')]))
            z3.append(sum(df5['Percent Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Chronic Lower Respiratory Disease')]))
            z4.append(sum(df5['Percent Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Stroke')]))
            z5.append(sum(df5['Percent Potentially Excess Deaths'][(df['State'] == 'United States')][(df['Cause of Death'] == 'Unintentional Injury')]))
        c = (
            Line()
                .add_xaxis(times)
                .add_yaxis(
                "Heart Disease",
                z1
            )
               
                .add_yaxis(
                "Cancer",
                z2
            )
                .add_yaxis(
                "Chronic Lower Respiratory Disease",
                z3
            )
               
                .add_yaxis(
                "Stroke",
                z4
            )
                .add_yaxis(
                "Unintentional Injury",
                z5
            )


                .set_global_opts( title_opts=opts.TitleOpts(title="美国2005-2015年五个主要原因潜在死亡人数占比趋势",subtitle="潜在死亡人数",pos_top="5%"),toolbox_opts=opts.ToolboxOpts(),datazoom_opts=opts.DataZoomOpts(),)
        )
        return c

    line_base().render()
    with open("render.html", encoding="utf8", mode="r") as f:
        plot_all3 = "".join(f.readlines())

    data_str = df.to_html()
##to here
    return render_template('results4.html',
                            the_plot_all3 = plot_all3,
                            the_res = data_str,
                            the_select_region=Locality_available,
                           )

if __name__ == '__main__':
    app.run(debug=True,port=8000)
