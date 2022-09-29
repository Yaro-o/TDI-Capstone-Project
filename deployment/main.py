from dash import Dash, page_container, html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

#url_theme = dbc.themes.MINTY

url_theme1 = dbc.themes.SANDSTONE
url_theme2 = dbc.themes.SLATE

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(__name__, use_pages=True, external_stylesheets=[url_theme1, dbc_css])
server = app.server
app.config.suppress_callback_exceptions = True

navbar = dbc.NavbarSimple(
    dbc.Nav(
        [ 
            dbc.NavLink('Dashboard', href="/"),
            dbc.DropdownMenu(
                [
                    dbc.DropdownMenuItem('Problem Statement', href="/intro"),                    
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Data Analysis", header=True),
                    dbc.DropdownMenuItem('Exploratory Data Analysis', href='/eda'),
                    dbc.DropdownMenuItem('Exploratory Spatial Data Analysis', href='/esda'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Time Series Analysis", header=True),
                    dbc.DropdownMenuItem('Baseline Predictive Models', href='/bm'),
                    dbc.DropdownMenuItem('Machine Learning Predictive Models', href='/ml'),
                    dbc.DropdownMenuItem('State-of-the-Art Predictive Models', href='/art'),
                ],
                nav=True,
                in_navbar=True,
                label="Under the Hood",
            ), 
            html.Div(ThemeSwitchAIO(aio_id="theme",  icons={"left": "fa fa-moon", "right": "fa fa-sun"}, 
                    themes=[url_theme1, url_theme2]), 
                style={'border':'1px solid', 'border-radius': 10, 'padding': 5, 'backgroundColor':'white', 'margin-left' : '50px', "height": "100%", 
                    'display': 'inline-block', 'verticalAlign': 'middle', 'textAlign': 'center'}
                ),
        ], style={'margin-left' : '50px', 'margin-top' : '10px', "height": "100%", 'verticalAlign': 'middle', 'textAlign': 'center', 'padding':5}
    ),
    brand="Ardi - TDI Capstone Project",
    color="primary",
    dark=True,
    className="mb-2",
    style={'font-size': 15, 'verticalAlign': 'middle', 'textAlign': 'center'}
)

app.layout = dbc.Container([navbar, page_container],
                           fluid=True, className="dbc")

app.index_string = """<!DOCTYPE html>
<html>
    <head>
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-Y0C8Q07J7Y"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());

        gtag('config', 'G-Y0C8Q07J7Y');
        </script>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>"""

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True, use_reloader=True)