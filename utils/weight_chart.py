import pandas as pd
import plotly.express as px

def weight_chart(weights):

    df = pd.DataFrame({

        "Skill": list(weights.keys()),
        "Weight": list(weights.values())

    })

    fig = px.bar(
        df,
        x="Skill",
        y="Weight",
        title="Skill Importance"
    )

    return fig