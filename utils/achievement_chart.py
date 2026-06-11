import plotly.express as px

def achievement_chart(
    score
):

    fig = px.bar(
        x=["Impact Score"],
        y=[score],
        title="Achievement Impact Analysis"
    )

    return fig