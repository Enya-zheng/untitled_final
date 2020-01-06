from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go

app = Flask(__name__)

# 准备工作 
df = pd.read_csv('NCHS_-_Potentially_Excess_Deaths_from_the_Five_Leading_Causes_of_Death.csv')
States_available_loaded = list(df.State.dropna().unique())

# 基本cufflinks 及ploty設置, 查文檔看書貼上而已
cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()

@app.route('/',methods=['GET'])
def IV_final_2019():
    data_str = df.to_html()
    States_available = States_available_loaded #下拉选单还没内容
    return render_template('results2.html',
                           the_res = data_str,
                           the_select_State=States_available)

@app.route('/IV_final',methods=['POST'])
def IV_final_select() -> 'html':
    the_State= request.form["the_State_selected"]  ## 取得用户交互输入
    print(the_State)                                 ## 检查用户输入, 在后台

    dfs = df.query("State=='{}'".format(the_State)) ## 使用df.query()方法. 按用户交互输入the_region过滤

    data_str = dfs.to_html()  # <------------------数据产出dfs, 完成互动过滤呢
    
    fig = dfs.iplot(kind="bar", x="Cause of Death", y="Year", asFigure=True)  # 使用iplot 做bar圖
    py.offline.plot(fig, filename="成果.html",auto_open=False)                  # 備出"成果.html"檔案之交互圖
    with open("成果.html", encoding="utf8", mode="r") as f:                     # 把"成果.html"當文字檔讀入成字符串
        plot_all = "".join(f.readlines())

    States_available =  States_available_loaded
    return render_template('results2.html',
                            the_plot_all = plot_all,
                            the_res = data_str,
                            the_select_State=States_available,
                           )

if __name__ == '__main__':
    app.run(port = 8000)   # debug=True, 在py使用, 在ipynb不使用
    
