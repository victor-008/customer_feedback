
from dash import Dash, html, dcc, dash_table
import pandas as pd
import plotly.express as px


from sqlalchemy import create_engine
from app.core.env import DB_URL

engine = create_engine(DB_URL)


def load_data():
    df = pd.read_sql("SELECT * FROM feedback", engine)
    return df

df = load_data()
category_fig = px.bar(
    df["category"].value_counts(),
    title="Category"
)

problem_fig = px.bar(
    df["problem"].value_counts(),
    title="Problems"
)

app = Dash(__name__)

app.layout = html.Div([

    html.H1("Feedback Automation Dashboard"),

    html.H3(f"Total feedback: {len(df)}"),
    dcc.Graph(figure=category_fig),
    dcc.Graph(figure=problem_fig),

    dash_table.DataTable(
        data=df.to_dict("records"),
        page_size=10
    )
])


if __name__ == "__main__":
    app.run(debug=True)