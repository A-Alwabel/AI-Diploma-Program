# Complete Project Guide: 02 Data Dashboard

---

## 🎯 Real-World Application

---

## 🚀 Quick Start (For Experienced Students)

> 💡 **New to this project?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.

## Step-by-Step Implementation

---

## 📚 Complete Tutorial (For Beginners)

> 💡 **Already familiar with this?** See [Quick Start](#-quick-start-for-experienced-students) section above.

### Step 1: Understand Dashboards (Day 1)

**What is a Dashboard?**
A visual interface that:
- Shows key metrics
- Displays multiple charts
- Allows interaction
- Updates automatically

**Example:**
```
Sales Dashboard:
- Total Revenue: $1.2M
- Top Products: Chart
- Sales by Region: Map
- Trends: Line Chart
```

---

### Step 2: Set Up Project (Day 1)

**Create structure:**
```
dashboard/
├── app.py
├── components/
│   ├── charts.py
│   └── layout.py
├── data/
│   └── sales_data.csv
└── README.md
```

**Install:**
```bash
pip install dash plotly pandas
```

---

### Step 3: Create Basic Dashboard (Day 2-3)

**File: `app.py`**

```python
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv('data/sales_data.csv')

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("Sales Dashboard", style={'textAlign': 'center'}),
    
    # Filters
    html.Div([
        dcc.Dropdown(
            id='region-filter',
            options=[{'label': region, 'value': region} 
                    for region in df['region'].unique()],
            value='All',
            placeholder="Select Region"
        )
    ], style={'width': '30%', 'margin': '20px'}),
    
    # Charts
    html.Div([
        dcc.Graph(id='revenue-chart'),
        dcc.Graph(id='products-chart')
    ], style={'display': 'flex'})
])

# Callbacks
@app.callback(
    [Output('revenue-chart', 'figure'),
     Output('products-chart', 'figure')],
    [Input('region-filter', 'value')]
)
def update_charts(selected_region):
    # Filter data
    if selected_region == 'All':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    
    # Revenue chart
    revenue_fig = px.line(
        filtered_df, 
        x='date', 
        y='revenue',
        title='Revenue Over Time'
    )
    
    # Products chart
    products_fig = px.bar(
        filtered_df.groupby('product')['quantity'].sum().reset_index(),
        x='product',
        y='quantity',
        title='Top Products'
    )
    
    return revenue_fig, products_fig

if __name__ == '__main__':
    app.run_server(debug=True)
```

---

### Step 4: Add More Visualizations (Day 4)

**File: `components/charts.py`**

```python
import plotly.express as px
import plotly.graph_objects as go

class DashboardCharts:
    """Create dashboard charts"""
    
    def create_revenue_chart(self, df):
        """Revenue over time"""
        fig = px.line(
            df, 
            x='date', 
            y='revenue',
            title='Revenue Trend',
            color='region'
        )
        return fig
    
    def create_sales_map(self, df):
        """Sales by region map"""
        region_sales = df.groupby('region')['revenue'].sum().reset_index()
        fig = px.choropleth(
            region_sales,
            locations='region',
            locationmode='country names',
            color='revenue',
            title='Sales by Region'
        )
        return fig
    
    def create_pie_chart(self, df):
        """Product distribution"""
        product_sales = df.groupby('product')['revenue'].sum().reset_index()
        fig = px.pie(
            product_sales,
            values='revenue',
            names='product',
            title='Revenue by Product'
        )
        return fig
    
    def create_heatmap(self, df):
        """Sales heatmap"""
        pivot = df.pivot_table(
            values='revenue',
            index='product',
            columns='region',
            aggfunc='sum'
        )
        fig = px.imshow(
            pivot,
            title='Revenue Heatmap',
            labels=dict(x="Region", y="Product", color="Revenue")
        )
        return fig
```

---

### Step 5: Create Advanced Layout (Day 5)

**File: `components/layout.py`**

```python
from dash import html, dcc

def create_dashboard_layout():
    """Create complete dashboard layout"""
    return html.Div([
        # Header
        html.Div([
            html.H1("Business Intelligence Dashboard", 
                   style={'textAlign': 'center', 'color': '#2c3e50'})
        ], className='header'),
        
        # Summary Cards
        html.Div([
            html.Div([
                html.H3("Total Revenue"),
                html.H2(id='total-revenue', children='$0')
            ], className='summary-card'),
            html.Div([
                html.H3("Total Orders"),
                html.H2(id='total-orders', children='0')
            ], className='summary-card'),
            html.Div([
                html.H3("Top Product"),
                html.H2(id='top-product', children='-')
            ], className='summary-card')
        ], className='summary-row'),
        
        # Filters
        html.Div([
            dcc.Dropdown(id='region-filter', placeholder='Region'),
            dcc.Dropdown(id='product-filter', placeholder='Product'),
            dcc.DatePickerRange(id='date-range')
        ], className='filters'),
        
        # Charts Grid
        html.Div([
            html.Div([
                dcc.Graph(id='revenue-chart')
            ], className='chart-container'),
            html.Div([
                dcc.Graph(id='products-chart')
            ], className='chart-container'),
            html.Div([
                dcc.Graph(id='map-chart')
            ], className='chart-container'),
            html.Div([
                dcc.Graph(id='heatmap-chart')
            ], className='chart-container')
        ], className='charts-grid')
    ])
```

---

### Step 6: Add Interactivity (Day 6)

**File: `app.py` (Enhanced)**

```python
from dash import dcc, html, Input, Output
from components.charts import DashboardCharts
from components.layout import create_dashboard_layout

app = dash.Dash(__name__)
app.layout = create_dashboard_layout()

charts = DashboardCharts()

@app.callback(
    [Output('revenue-chart', 'figure'),
     Output('products-chart', 'figure'),
     Output('map-chart', 'figure'),
     Output('heatmap-chart', 'figure'),
     Output('total-revenue', 'children'),
     Output('total-orders', 'children'),
     Output('top-product', 'children')],
    [Input('region-filter', 'value'),
     Input('product-filter', 'value'),
     Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_dashboard(region, product, start_date, end_date):
    # Filter data based on inputs
    filtered_df = df.copy()
    
    if region:
        filtered_df = filtered_df[filtered_df['region'] == region]
    if product:
        filtered_df = filtered_df[filtered_df['product'] == product]
    if start_date and end_date:
        filtered_df = filtered_df[
            (filtered_df['date'] >= start_date) & 
            (filtered_df['date'] <= end_date)
        ]
    
    # Create charts
    revenue_fig = charts.create_revenue_chart(filtered_df)
    products_fig = charts.create_pie_chart(filtered_df)
    map_fig = charts.create_sales_map(filtered_df)
    heatmap_fig = charts.create_heatmap(filtered_df)
    
    # Calculate summary stats
    total_revenue = f"${filtered_df['revenue'].sum():,.0f}"
    total_orders = f"{len(filtered_df):,}"
    top_product = filtered_df.groupby('product')['revenue'].sum().idxmax()
    
    return (revenue_fig, products_fig, map_fig, heatmap_fig,
            total_revenue, total_orders, top_product)

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
```

---

---