import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

FONT_AWESOME = ["https://use.fontawesome.com/releases/v5.10.2/css/all.css"]
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
load_figure_template("pulse")

app = dash.Dash(__name__, external_stylesheets=[FONT_AWESOME, dbc.themes.PULSE, dbc_css])

app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True
server = app.server
