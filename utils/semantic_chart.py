import plotly.graph_objects as go

def semantic_chart(
        score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            gauge={
                "axis": {
                    "range": [0, 100]
                }
            }
        )
    )

    return fig