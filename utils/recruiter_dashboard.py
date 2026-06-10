import plotly.graph_objects as go

def recruiter_dashboard(
    ats,
    semantic,
    career,
    education,
    rank
):

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=[
                "ATS",
                "Semantic",
                "Career",
                "Education",
                "Rank"
            ],
            y=[
                ats,
                semantic,
                career,
                education,
                rank
            ]
        )
    )

    return fig