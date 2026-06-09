import plotly.express as px
def create_match_chart(
        matched,
        missing):
    fig = px.pie(
        values=[
            len(matched),
            len(missing)
        ],
        names=[
            "Matched",
            "Missing"
        ]
    )
    return fig