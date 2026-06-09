import plotly.express as px

def section_chart(
        sections):

    present = sum(
        sections.values()
    )

    missing = (
        len(sections)
        - present
    )

    fig = px.pie(
        names=[
            "Present",
            "Missing"
        ],
        values=[
            present,
            missing
        ]
    )

    return fig