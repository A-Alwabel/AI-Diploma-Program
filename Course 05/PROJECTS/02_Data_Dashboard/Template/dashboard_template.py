"""
Interactive Data Dashboard Template
Project 02 Template

Fill in the functions marked with TODO comments.
Requires: pip install dash plotly pandas
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Initialize Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


class DataLoader:
    """Loads data for dashboard."""
    
    def load_data(self, filepath):
        """
        Load dataset.
        
        TODO: Load your dataset
        """
        # TODO: Load data
        # df = pd.read_csv(filepath)
        # return df
        pass


class ChartCreator:
    """Creates interactive Plotly charts."""
    
    def create_scatter_plot(self, df, x_col, y_col, color_col=None):
        """
        Create scatter plot.
        
        TODO: Create interactive scatter plot
        """
        # TODO: Use px.scatter() to create plot
        # fig = px.scatter(df, x=x_col, y=y_col, color=color_col)
        # return fig
        pass
    
    def create_bar_chart(self, df, x_col, y_col):
        """
        Create bar chart.
        
        TODO: Create interactive bar chart
        """
        # TODO: Use px.bar() to create plot
        pass
    
    def create_line_chart(self, df, x_col, y_col):
        """
        Create line chart.
        
        TODO: Create interactive line chart
        """
        # TODO: Use px.line() to create plot
        pass
    
    def create_heatmap(self, df):
        """
        Create correlation heatmap.
        
        TODO: Create heatmap
        """
        # TODO: Calculate correlation matrix
        # TODO: Use px.imshow() to create heatmap
        pass


# Dashboard Layout
app.layout = dbc.Container([
    html.H1("Interactive Data Dashboard", className="mb-4"),
    
    # TODO: Add filters/dropdowns
    # dcc.Dropdown(id='filter-dropdown', ...),
    
    # TODO: Add chart components
    # dcc.Graph(id='main-chart'),
    # dcc.Graph(id='secondary-chart'),
    
    # TODO: Add summary statistics
    # html.Div(id='summary-stats'),
])


# TODO: Add callbacks for interactivity
# @app.callback(
#     Output('main-chart', 'figure'),
#     Input('filter-dropdown', 'value')
# )
# def update_chart(selected_value):
#     # TODO: Update chart based on filter
#     pass


def main():
    """
    Main execution function.
    
    TODO: Load data and run dashboard
    """
    # TODO: Load data
    # TODO: Run dashboard
    app.run_server(debug=True)


if __name__ == "__main__":
    main()

