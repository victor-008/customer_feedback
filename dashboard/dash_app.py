from dash import Dash, html, dcc, dash_table, Input, Output
import pandas as pd
import plotly.express as px

from sqlalchemy import create_engine
from app.core.env import DB_URL


engine = create_engine(
    DB_URL,
    connect_args={"check_same_thread":False})

def load_data():
    try:
        df = pd.read_sql("SELECT * FROM feedback", engine)

        if df is None:
            df = pd.DataFrame()

    except Exception as e:
        print("Db ERROR:", e)

        df = pd.DataFrame()
    return df

app = Dash(__name__)


app.layout = html.Div([

    html.H1("Feedback Automation Dashboard"),

    dcc.Interval(
        id="interval",
        interval=5000,  # refresh every 5 sec
        n_intervals=0
    ),

    html.Div(id="stats"),

    html.Div([
        dcc.Graph(id="category-chart"),
        dcc.Graph(id="problem-chart"),
    ], style={"display": "flex"}),

    html.Div([
        dcc.Graph(id="time-chart"),
    ]),

    dash_table.DataTable(
        id="table",
        page_size=10,
        style_table={"overflowX": "auto"},
    )

])

@app.callback(
    Output("stats", "children"),
    Output("category-chart", "figure"),
    Output("problem-chart", "figure"),
    Output("time-chart", "figure"),
    Output("table", "data"),
    Input("interval", "n_intervals"),
)
def update_dashboard(n):

    df = load_data()
    print("ROWS:", len(df))

    if df.empty:

        return (
            "No data",
            {},
            {},
            {},
            []
        )

    # ---------- stats ----------
    ###########################################################################################
    if "embedding" in df.columns:
        df = df.drop(columns=["embedding"])
    
    #convert timestamp to string
    if "created_at" in df.columns:
        df["created_at"] = df["created_at"].astype(str)
    
    ############################################################################################

    stats = f"Total feedback: {len(df)}"

    # ---------- category ----------
    category_counts = df["category"].value_counts().reset_index()
    category_counts.columns = ["category", "count"]

    category_fig = px.pie(
        category_counts,
        names="category",
        values="count",
        title="Category"
    )

    # ---------- problem ----------
    problem_counts = df["problem"].value_counts().reset_index()
    problem_counts.columns = ["problem", "count"]

    problem_fig = px.pie(
        problem_counts,
        names="problem",
        values="count",
        title="Problem"
    )

    # ---------- time ----------
    if "created_at" in df.columns:

        df["created_at"] = pd.to_datetime(
            df["created_at"],
            errors="coerce"
        )

        time_fig = px.histogram(
            df,
            x="created_at",
            title="Feedback over time"
        )

    else:
        time_fig = {}

    return (
        stats,
        category_fig,
        problem_fig,
        time_fig,
        df.to_dict("records"),
    )

#usiguze murima    
if __name__ == "__main__":
 app.run(debug=True)
