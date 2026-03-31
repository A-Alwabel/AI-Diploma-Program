"""
Data Dashboard - Complete Solution
Interactive web dashboard using Dash and Plotly
"""

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(42)
dates = pd.date_range('2024-01-01', periods=100, freq='D')
data = {
    'Date': dates,
    'Sales': np.random.randn(100).cumsum() + 1000,
    'Revenue': np.random.randn(100).cumsum() + 5000,
    'Customers': np.random.randint(50, 200, 100),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
    'Category': np.random.choice(['A', 'B', 'C'], 100)
}
df = pd.DataFrame(data)

# Initialize Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1("Interactive Data Dashboard", 
            style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': 30}),
    
    # Filters
    html.Div([
        html.Label("Select Region:", style={'fontWeight': 'bold', 'marginRight': 10}),
        dcc.Dropdown(
            id='region-filter',
            options=[{'label': 'All', 'value': 'All'}] + 
                   [{'label': r, 'value': r} for r in df['Region'].unique()],
            value='All',
            style={'width': '200px', 'display': 'inline-block', 'marginRight': 20}
        ),
        
        html.Label("Select Category:", style={'fontWeight': 'bold', 'marginRight': 10}),
        dcc.Dropdown(
            id='category-filter',
            options=[{'label': 'All', 'value': 'All'}] + 
                   [{'label': c, 'value': c} for c in df['Category'].unique()],
            value='All',
            style={'width': '200px', 'display': 'inline-block'}
        ),
    ], style={'padding': 20, 'backgroundColor': '#ecf0f1', 'borderRadius': 5, 'marginBottom': 20}),
    
    # Charts row 1
    html.Div([
        dcc.Graph(id='sales-chart', style={'width': '50%', 'display': 'inline-block'}),
        dcc.Graph(id='revenue-chart', style={'width': '50%', 'display': 'inline-block'}),
    ]),
    
    # Charts row 2
    html.Div([
        dcc.Graph(id='customers-chart', style={'width': '50%', 'display': 'inline-block'}),
        dcc.Graph(id='region-chart', style={'width': '50%', 'display': 'inline-block'}),
    ]),
    
    # Summary statistics
    html.Div(id='summary-stats', style={'marginTop': 20, 'padding': 20, 
                                        'backgroundColor': '#34495e', 'color': 'white',
                                        'borderRadius': 5})
])

# Callbacks
@app.callback(
    [Output('sales-chart', 'figure'),
     Output('revenue-chart', 'figure'),
     Output('customers-chart', 'figure'),
     Output('region-chart', 'figure'),
     Output('summary-stats', 'children')],
    [Input('region-filter', 'value'),
     Input('category-filter', 'value')]
)
def update_dashboard(selected_region, selected_category):
    """Update all charts based on filters."""
    # Filter data
    filtered_df = df.copy()
    if selected_region != 'All':
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]
    if selected_category != 'All':
        filtered_df = filtered_df[filtered_df['Category'] == selected_category]
    
    # Sales chart
    sales_fig = px.line(filtered_df, x='Date', y='Sales', 
                       title='Sales Over Time',
                       labels={'Sales': 'Sales ($)', 'Date': 'Date'})
    sales_fig.update_layout(template='plotly_white')
    
    # Revenue chart
    revenue_fig = px.bar(filtered_df, x='Date', y='Revenue',
                        title='Revenue by Date',
                        labels={'Revenue': 'Revenue ($)', 'Date': 'Date'})
    revenue_fig.update_layout(template='plotly_white')
    
    # Customers chart
    customers_fig = px.scatter(filtered_df, x='Date', y='Customers',
                             color='Category', size='Revenue',
                             title='Customers Over Time',
                             labels={'Customers': 'Number of Customers', 'Date': 'Date'})
    customers_fig.update_layout(template='plotly_white')
    
    # Region chart
    region_counts = filtered_df['Region'].value_counts()
    region_fig = px.pie(values=region_counts.values, names=region_counts.index,
                       title='Distribution by Region')
    region_fig.update_layout(template='plotly_white')
    
    # Summary statistics
    stats = html.Div([
        html.H3("Summary Statistics", style={'marginBottom': 15}),
        html.Div([
            html.Div([
                html.H4(f"${filtered_df['Sales'].sum():,.2f}", style={'margin': 0}),
                html.P("Total Sales", style={'margin': 0})
            ], style={'display': 'inline-block', 'marginRight': 30}),
            html.Div([
                html.H4(f"${filtered_df['Revenue'].sum():,.2f}", style={'margin': 0}),
                html.P("Total Revenue", style={'margin': 0})
            ], style={'display': 'inline-block', 'marginRight': 30}),
            html.Div([
                html.H4(f"{filtered_df['Customers'].sum():,}", style={'margin': 0}),
                html.P("Total Customers", style={'margin': 0})
            ], style={'display': 'inline-block', 'marginRight': 30}),
            html.Div([
                html.H4(f"{len(filtered_df)}", style={'margin': 0}),
                html.P("Data Points", style={'margin': 0})
            ], style={'display': 'inline-block'})
        ])
    ])
    
    return sales_fig, revenue_fig, customers_fig, region_fig, stats

def main():
    """Run the dashboard."""
    print("=" * 60)
    print("Interactive Data Dashboard")
    print("=" * 60)
    print("\nStarting Dash server...")
    print("Dashboard will open at: http://127.0.0.1:8050")
    print("\nFeatures:")
    print("  - Interactive filters (Region, Category)")
    print("  - Real-time chart updates")
    print("  - Multiple visualization types")
    print("  - Summary statistics")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 60)
    
    app.run_server(debug=True, host='127.0.0.1', port=8050)

if __name__ == "__main__":
    main()
