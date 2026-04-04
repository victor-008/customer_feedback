from dash import Dash, html, dcc, Input, Output, State
import requests

API_URL = "http://127.0.0.1:8000/chat"

app = Dash(__name__)

chat_history = []

app.layout = html.Div([
    html.H1("AI Feedback Chat"),
    
    html.Div(
        id="chat-box",
        style={
            "height": "400px",
            "overflowY": "scroll",
            "border": "1px solid black",
            "padding": "10px"
        }
    ),
    dcc.Input(
        id="input",
        type="text",
        placeholder="Enter feedback",
        style={"width": "80%"}
    ),
    html.Button("Send", id="send"),
])

@app.callback(
    Output("chat-box", "children"),
    Input("send", "n_clicks"),
    State("input", "value"),
    prevent_initial_call = True
)

def send(n, text):
    global chat_history

    if not text:
        return chat_history
    
    r = requests.post(
        API_URL,
        params={"text": text}
    )

    reply = r.json()["reply"]

    chat_history.append(
        html.Div([
            html.B("AI: "),
            reply
        ])
    )

    return chat_history

if __name__ == "__main__":
    app.run(debug=True, port=8051)