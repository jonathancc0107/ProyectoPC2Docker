import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import mysql.connector
import pandas as pd

db = mysql.connector.connect(host='mysql', user='root', password='root', db='Proyecto_G01')
data1 = pd.read_sql('SELECT * FROM ConsumoAlcohol where Pais = "Colombia"', db)
data2 = pd.read_sql('SELECT * FROM ConsumoAlcohol where Cerveza = (Select max(Cerveza) from ConsumoAlcohol)', db)
data3 = pd.read_sql('SELECT * FROM ConsumoAlcohol', db)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
app.layout = html.Div([
    html.H2('Proyecto Docker, servidor Dash'),

    html.H2('Tabla de resultados de Colombia'),
    dash_table.DataTable(
        id='table1',
        columns=[{'name': i, 'id': i} for i in data1.columns],
        data=data1.to_dict('records'),
    ),

    html.H2('Tabla de resultados del país con mayor consumo de cerveza'),
    dash_table.DataTable(
        id='table',
        columns=[{'name': i, 'id': i} for i in data2.columns],
        data=data2.to_dict('records'),
    ),

    html.H2('Tabla de todos los resultados'),
    dash_table.DataTable(
        id='table2',
        columns=[{'name': i, 'id': i} for i in data3.columns],
        data=data3.to_dict('records'),
    )
])

if __name__ == '__main__':
  app.run_server(host='0.0.0.0', port=8080, debug=True)