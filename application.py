from flask import Flask,render_template,request,redirect,url_for,session
from flask_pymongo import PyMongo
from cryptography.fernet import Fernet
import pickle
import numpy as np
import pandas as pd
import numpy as np 
import pandas as pd
import missingno as mno
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.express as px
import json
import plotly




key=Fernet.generate_key()
salt=key.decode('utf8')



def create_burst_one():
  df = pd.read_csv("data.csv")
  df = df.iloc[0:295]
  x = df['Year']
  y = df['Month']
  z = df['Date']
  k= df['India-Infected']
  fig = px.sunburst(df, path=[x,y,z,k],values=z)
  fig.update_layout(margin = dict(t=50, l=0, r=0, b=0))
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return graphJSON

def create_bar_two():
  df = pd.read_csv("data.csv")
  hf = df
  df=hf.iloc[111:142]
  x1=df['Date']
  y1=df['India-Deaths']
  fig = px.bar(df, x = x1, y = y1 , color = y1, text=y1)
  fig.update_xaxes(title_text = 'July 2020')
  fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
  fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
  fig.update_layout(barmode='stack')
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return graphJSON

def create_plot():
  df = pd.read_csv("data.csv")
  hf = df
  df=hf.iloc[111:142]
  x1=df['Date']
  mf=hf.iloc[295:326]
  y1=df['India-Infected']
  y2=mf['India-Infected']
  kf=hf.iloc[264:295]
  y3=kf['India-Infected']
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=x1, y=y1,
                    mode='lines+markers',
                    name='July 2020'))
  fig.add_trace(go.Scatter(x=x1, y=y2,
                    mode='lines+markers',
                    name='December 2020'))
  fig.add_trace(go.Scatter(x=x1, y=y3,
                    mode='lines+markers',
                    name='January 2021'))
  fig.update_xaxes(type='category')
  fig.update_xaxes(title_text='month')
  fig.update_yaxes(title_text='India-Infected')
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return graphJSON

def create_plot_two():
  df = pd.read_csv("data.csv")
  hf = df
  df=hf.iloc[111:142]
  x1=df['Date']
  mf=hf.iloc[295:326]
  y1=df['India-Deaths']
  y2=mf['India-Deaths']
  kf=hf.iloc[264:295]
  y3=kf['India-Deaths']
  fig = go.Figure()
  fig.add_trace(go.Scatter(x=x1, y=y1,
                      mode='lines+markers',
                      name='July 2020'))
  fig.add_trace(go.Scatter(x=x1, y=y2,
                      mode='lines+markers',
                      name='December 2020'))
  fig.add_trace(go.Scatter(x=x1, y=y3,
                      mode='lines+markers',
                      name='January 2021'))
  fig.update_xaxes(type='category')
  fig.update_xaxes(title_text='month')
  fig.update_yaxes(title_text='India-Deaths')
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return graphJSON





def create_burst_two():
  df = pd.read_csv("data.csv")
  hf = df
  df=hf.iloc[296:378]
  x = df['Year']
  y = df['Month']
  z = df['Date']
  k= df['India-Infected']
  fig = px.sunburst(df, path=[x, y, z, k],
                    values=z)
  fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return graphJSON

def create_bar_two():
  df = pd.read_csv("data.csv")
  hf = df
  df=hf.iloc[111:142]
  x1=df['Date']
  y1=df['India-Deaths']
  fig = px.bar(df, x = x1, y = y1 , color = y1, text=y1)
  fig.update_xaxes(title_text = 'July 2020')
  fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
  fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
  fig.update_layout(barmode='stack')
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return graphJSON



def create_bar_one():
  hf = pd.read_csv("data.csv")
  hf=hf.iloc[111:142]
  x1=hf['Date']
  y1=hf['India-Infected']
  fig = px.bar(hf, x = x1, y = y1 , color = x1,text=y1)
  fig.update_xaxes(title_text = 'July 2020')
  fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
  fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
  fig.update_layout(barmode='stack')
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return graphJSON


app=Flask(__name__)
app.config['MONGO_URI']="mongodb+srv://me:me@cluster0.zl6ie.mongodb.net/manager?authSource=admin&replicaSet=atlas-g6aula-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
mongo=PyMongo(app)
unity_db  = mongo.db['datas'] 

@app.route("/",methods=["POST","GET"])
def log():
  return render_template("srp_home.html")



@app.route("/dashboard",methods=["POST","GET"])
def dashboard():
  return render_template("index3.html")

@app.route("/table",methods=["POST","GET"])
def table():

  contacts_year = unity_db.distinct('Year')
  contacts_month = unity_db.distinct('Month')

  contact_list = []
  year_list = []
  contact_obj = {}
  year_obj = {}

  for item in contacts_month :
    contact_obj = {
      'month' : item 
    }
    contact_list.append(contact_obj)
  
  for item in contacts_year :
    year_obj = {
      'year' : item 
    }
    year_list.append(year_obj)
 
  return render_template("tables.html", rows = contact_list , column = year_list)

@app.route("/table_data",methods=["POST","GET"])
def table_data():

  if request.method == "POST":
    f_month = request.form["month"]
    f_year = request.form["year"]
    f_country = request.form["country"]
    f_category = request.form["category"]

    f_category=f_country + "-" + f_category
    users = unity_db.find({ 'Month' : f_month , 'Year' : f_year })

    user_list = []
    user_obj = {}
    index_list=[]
    index_list.append(f_category)
    
    for item in users :
      user_obj = {
          "month"         : item['Month'],
          "year" : item['Year'] ,
          "date" : item['Date'] ,
          "category" : item[f_category] ,
          "country" : f_country      
      }
      user_list.append(user_obj)
    
    contacts_year = unity_db.distinct('Year')
    contacts_month = unity_db.distinct('Month')

    contact_list = []
    year_list = []
    contact_obj = {}
    year_obj = {}

    for item in contacts_month :
      contact_obj = {
        'month' : item 
      }
      contact_list.append(contact_obj)
    
    for item in contacts_year :
      year_obj = {
        'year' : item 
      }
      year_list.append(year_obj)
  
    return render_template("tables.html", rows = contact_list , column = year_list , index = index_list , user = user_list)

@app.route("/dashboard1",methods=["POST","GET"])
def dashboard1():

  df = pd.read_csv('state_wise_daily.csv')
  inspect = df.groupby(['Status']).sum()
  inspect_two=inspect.transpose()
  inspect_one=inspect_two.drop(['TT'])
  inspect_three=inspect_one
  inspect_one=inspect_one.drop(['Maharashtra'])

  u_confirmed=inspect_three['Confirmed'].sum()
  u_deceased=inspect_three['Deceased'].sum()
  u_recovered=inspect_three['Recovered'].sum()
  
  covid_data = {}
  
  covid_data = {
    'f_confirmed' : f"{u_confirmed:,}" ,
    'f_deceased' : f"{u_deceased:,}" ,
    'f_recovered' : f"{u_recovered:,}"
  }

  covid_list = []
  covid_list.append(covid_data)

  items = inspect_three['Confirmed'].nlargest(8).reset_index()
  products_list = [items.columns.values.tolist()] + items.values.tolist()

  top_list = {}
  full_list = []

  for item in products_list :
    if item[0] != 'index' :
      k = item[1]
      top_list = {
        'State' : item[0],
        'Total_Count' : f"{k:,}"
      }
      full_list.append(top_list)

  inspect_one=inspect_one.loc[inspect_one['Confirmed'] >= 700000]

  fig = px.bar(inspect_one, x=inspect_one.index, y='Confirmed',color='Confirmed' ,
              title='State Wise Total Covid Cases',
              text='Confirmed')
  fig.update_xaxes(title_text='State')
  fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
  fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  bar_one = graphJSON

  fig = px.bar(inspect_one, x=inspect_one.index, y='Deceased', color='Deceased', 
              title='State Wise Total Covid Death Cases' , 
              text='Deceased')
  fig.update_xaxes(title_text='State')
  fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
  fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

  bar_two = graphJSON

  fig = px.bar(inspect_one, x=inspect_one.index, y='Recovered', color='Recovered', 
              title='State Wise Total Covid Recovered Cases' ,
              text='Deceased')
  fig.update_xaxes(title_text='State')
  fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
  fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

  bar_three = graphJSON
  

  return render_template("index3.html" , plot1 = bar_one , plot2 = bar_two , plot3 = bar_three , rows = covid_list , column = full_list )


@app.route("/switch1",methods=["POST","GET"])
def index():
  
  sun = create_burst_one()
  bar2 = create_bar_two()
  bar = create_bar_one()
  line = create_plot()
  line2 = create_plot_two()
  sun2 = create_burst_two()
  print(sun2)
  return render_template('chart_1.html', plot1 = sun , plot2= bar, plot3 = line, plot4 = bar2, plot5 = sun2, plot6 = line2)
  

@app.route("/signup",methods=["POST","GET"])
def signup():
  return render_template("srp_register.html")

@app.route("/returnlist/<v>",methods=["POST","GET"])
def returnlist(v):
  return render_template("srp_home.html",v=v)

@app.route("/register",methods=["POST","GET"])
def reg():
  message=''
  if request.method =='POST':
    u=request.form['id']
    pw=request.form['pwd']
    rpw=request.form['repwd']
    ur=str(u).lower()
    obj=pw.encode()
    instance=salt.encode()
    crypter=Fernet(instance)
    bush=crypter.encrypt(obj)
    k=str(bush,'utf8')
    users=mongo.db.users.find({})
    for x in users:
      usr=x['username']
      if usr == ur:
        message="Username already exists"
        return render_template("srp_register.html",msg=message)
    if pw != rpw:
      message="Password doesn't match"
      return render_template("srp_register.html",msg=message)
    else:
      users=mongo.db.users.insert({"username":ur,"password":k,"salt":salt})
      return render_template("srp_home.html") 

@app.route("/allow",methods=["POST","GET"])
def allow():
  message=''
  flag=0
  if request.method == "POST":
    u=request.form["id"]
    pas=request.form["key"]
    name=str(u).lower()
    users=mongo.db.users.find({})
    for x in users:
      n=x['username']
      if n == name:
        flag=1
    if(flag==0):
      message="Invalid Username"  
      return render_template("srp_home.html",msg=message) 
    user=mongo.db.users.find({"username":name})
    for x in user:
      pwd=x['password']
      sss=x['salt']
      s=pwd.encode()
      instance=sss.encode()
      crypter=Fernet(instance)
      decryptpw=crypter.decrypt(s)
      returned=decryptpw.decode('utf8')
      print(returned)
      if returned == pas:
        return render_template("indexpage.html",v=u)
      else:
        message="Invalid Password"  
        return render_template("srp_home.html",msg=message) 

    



if __name__ == "__main__":
 app.run(debug=True)