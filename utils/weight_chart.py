import plotly.express as px
def weight_chart(
        importance):
    fig = px.bar(
        x=list(
            importance.keys()
        ),
        y=list(
            importance.values()
        )
    )
    return fig