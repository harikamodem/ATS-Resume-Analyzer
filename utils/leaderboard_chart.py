import plotly.express as px

def leaderboard_chart(
    candidates
):

    names = [
        c["name"]
        for c in candidates
    ]

    scores = [
        c["rank"]
        for c in candidates
    ]

    fig = px.bar(
        x=names,
        y=scores,
        title="Candidate Ranking"
    )

    return fig