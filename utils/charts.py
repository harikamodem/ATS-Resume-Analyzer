import plotly.graph_objects as go
def create_score_chart(score):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={
                "text": "ATS Score"
            },
            gauge={
                "axis": {
                    "range": [0, 100]
                }
            }
        )
    )
    return fig 