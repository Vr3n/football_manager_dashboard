import pandas as pd
import plotly.express as px
import plotly.io as pio


# Disable plotly default theme.
pio.templates.default = 'seaborn' 

def nationality_proportion(df: pd.DataFrame):
    fig = px.pie(df, names="Nat", hole=.3)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
        title_text="Squad Nationality"
    )

    return fig

def age_spread(df: pd.DataFrame):
    fig = px.histogram(df, x="Age", nbins=20)
    fig.update_layout(
        title_text="Squad Age Distribution."
    )

    return fig

def dnascore_vs_age(df: pd.DataFrame):
    fig = px.scatter(df, 'Age', 'dna_score', hover_data=['Name', 'Position'], text="Name", width=1200, height=600)

    fig.update_traces(textposition='top center', textfont_size=10)
    fig.update_layout(
        title_text='Age V/s DNa score',
        
    )
    fig.add_hline(df['dna_score'].mean(), line_color='red')
    fig.add_vline(df['Age'].mean(), line_color='red')

    return fig


def dnascore_vs_wage(df: pd.DataFrame):
    fig = px.scatter(df, 'Wage', 'dna_score', hover_data=['Name', 'Position'], text="Name", width=1200, height=600)
    fig.update_traces(textposition='top center', textfont_size=10)
    fig.update_layout(
        title_text='Wage V/s DNa score',
        
    )
    # px.line(x=df['Wage'].mean(), y=df['dna_score'].mean())
    fig.add_hline(df['dna_score'].mean(), line_color='red')
    fig.add_vline(df['Wage'].mean(), line_color='red')

    return fig