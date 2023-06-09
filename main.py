from dash import Dash, html, dcc
import dash

app = Dash(__name__, use_pages=True)

app.layout = html.Div([html.H1('Dota 2 stats'), dash.page_container])

if __name__ == "__main__":
    app.run_server(debug=True, port=80, host="0.0.0.0")
