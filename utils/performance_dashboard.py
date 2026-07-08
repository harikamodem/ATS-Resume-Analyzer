import pandas as pd
import plotly.express as px

def performance_dashboard():

    try:

        df = pd.read_csv(
            "logs/analysis_log.csv"
        )

        fig = px.scatter(
            df,
            x="ATS",
            y="Semantic",
            hover_name="Candidate",
            title="Analysis History"
        )

        return fig

    except:

        return None