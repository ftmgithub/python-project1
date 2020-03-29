import pandas as pd

df = pd.read_csv('F:/test/py.project/log2.txt', names= ['Data'])

pd.set_option('display.max_colwidth', None)

df1 = df[df['Data'].str.contains(" up ")]

df2 = df[df['Data'].str.contains(" down ")]

from flask import Flask, render_template,request,Response

app = Flask(__name__)

@app.route('/')

def tables():

              return render_template('myhtml.html', tables =[df.to_html(classes = 'data', header='2'), df1.to_html() , df2.to_html()])


if __name__ == '__main__':

  app.run()
