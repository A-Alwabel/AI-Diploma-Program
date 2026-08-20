# Complete Project Guide: 01 Data Pipeline

---

## 🎯 Real-World Application

---

## 🚀 Quick Start (For Experienced Students)

> 💡 **New to this project?** Skip to [Complete Tutorial](#-complete-tutorial-for-beginners) section below.

## Step-by-Step Implementation

---

## 📚 Complete Tutorial (For Beginners)

> 💡 **Already familiar with this?** See [Quick Start](#-quick-start-for-experienced-students) section above.

### Step 1: Understand Scalable Processing (Day 1)

**What is Scalable Processing?**
Processing data that:
- Doesn't fit in memory
- Takes too long with regular tools
- Needs to run on multiple machines
- Benefits from GPU acceleration

**Example:**
```
Regular pandas: 1 million rows = 5 minutes
Dask (distributed): 1 million rows = 30 seconds
cuDF (GPU): 1 million rows = 5 seconds
```

---

### Step 2: Set Up Project (Day 1)

**Create structure:**
```
data_pipeline/
├── data/
│   └── large_dataset.csv
├── src/
│   ├── data_loader.py
│   ├── processor_pandas.py
│   ├── processor_dask.py
│   └── processor_cudf.py
├── main.py
└── README.md
```

**Install:**
```bash
pip install pandas dask[complete] cudf-cu11
```

---

### Step 3: Implement Pandas Processor (Day 2)

**File: `src/processor_pandas.py`**

```python
import pandas as pd
import time

class PandasProcessor:
    """Process data using pandas (baseline)"""
    
    def load_data(self, filepath, chunksize=10000):
        """Load data in chunks"""
        chunks = []
        for chunk in pd.read_csv(filepath, chunksize=chunksize):
            chunks.append(chunk)
        return pd.concat(chunks, ignore_index=True)
    
    def process_data(self, df):
        """Process data with pandas"""
        start_time = time.time()
        
        # Clean data
        df = df.dropna()
        df = df.drop_duplicates()
        
        # Transformations
        df['total'] = df['quantity'] * df['price']
        df['date'] = pd.to_datetime(df['date'])
        
        # Aggregations
        summary = df.groupby('category').agg({
            'total': 'sum',
            'quantity': 'sum'
        }).reset_index()
        
        processing_time = time.time() - start_time
        print(f"Pandas processing time: {processing_time:.2f} seconds")
        
        return summary
```

---

### Step 4: Implement Dask Processor (Day 3)

**File: `src/processor_dask.py`**

```python
import dask.dataframe as dd
import time

class DaskProcessor:
    """Process data using Dask (distributed)"""
    
    def load_data(self, filepath):
        """Load data with Dask"""
        return dd.read_csv(filepath)
    
    def process_data(self, ddf):
        """Process data with Dask"""
        start_time = time.time()
        
        # Clean data (lazy evaluation)
        ddf = ddf.dropna()
        ddf = ddf.drop_duplicates()
        
        # Transformations
        ddf['total'] = ddf['quantity'] * ddf['price']
        ddf['date'] = dd.to_datetime(ddf['date'])
        
        # Aggregations (compute triggers execution)
        summary = ddf.groupby('category').agg({
            'total': 'sum',
            'quantity': 'sum'
        }).compute()
        
        processing_time = time.time() - start_time
        print(f"Dask processing time: {processing_time:.2f} seconds")
        
        return summary
```

---

### Step 5: Implement cuDF Processor (Day 4)

**File: `src/processor_cudf.py`**

```python
import cudf
import time

class CuDFProcessor:
    """Process data using cuDF (GPU)"""
    
    def load_data(self, filepath):
        """Load data with cuDF"""
        return cudf.read_csv(filepath)
    
    def process_data(self, gdf):
        """Process data with cuDF on GPU"""
        start_time = time.time()
        
        # Clean data (GPU-accelerated)
        gdf = gdf.dropna()
        gdf = gdf.drop_duplicates()
        
        # Transformations (GPU-accelerated)
        gdf['total'] = gdf['quantity'] * gdf['price']
        gdf['date'] = cudf.to_datetime(gdf['date'])
        
        # Aggregations (GPU-accelerated)
        summary = gdf.groupby('category').agg({
            'total': 'sum',
            'quantity': 'sum'
        })
        
        processing_time = time.time() - start_time
        print(f"cuDF processing time: {processing_time:.2f} seconds")
        
        return summary
```

---

### Step 6: Create Comparison Tool (Day 5)

**File: `src/comparator.py`**

```python
import time
from processor_pandas import PandasProcessor
from processor_dask import DaskProcessor
from processor_cudf import CuDFProcessor

class PipelineComparator:
    """Compare different processing methods"""
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.results = {}
    
    def compare_all(self):
        """Compare pandas, Dask, and cuDF"""
        print("=" * 60)
        print("Processing Pipeline Comparison")
        print("=" * 60)
        
        # Pandas
        print("\n[1] Processing with Pandas...")
        pandas_proc = PandasProcessor()
        df_pandas = pandas_proc.load_data(self.filepath)
        result_pandas = pandas_proc.process_data(df_pandas)
        self.results['pandas'] = result_pandas
        
        # Dask
        print("\n[2] Processing with Dask...")
        dask_proc = DaskProcessor()
        ddf = dask_proc.load_data(self.filepath)
        result_dask = dask_proc.process_data(ddf)
        self.results['dask'] = result_dask
        
        # cuDF (if GPU available)
        try:
            print("\n[3] Processing with cuDF (GPU)...")
            cudf_proc = CuDFProcessor()
            gdf = cudf_proc.load_data(self.filepath)
            result_cudf = cudf_proc.process_data(gdf)
            self.results['cudf'] = result_cudf
        except:
            print("   GPU not available, skipping cuDF")
        
        return self.results
    
    def print_summary(self):
        """Print comparison summary"""
        print("\n" + "=" * 60)
        print("Comparison Summary")
        print("=" * 60)
        
        for method, result in self.results.items():
            print(f"\n{method.upper()}:")
            print(f"  Rows processed: {len(result)}")
            print(f"  Columns: {list(result.columns)}")
```

---

### Step 7: Create Main Program (Day 6)

**File: `main.py`**

```python
from src.comparator import PipelineComparator

def main():
    # Path to large dataset
    filepath = 'data/large_ecommerce_data.csv'
    
    # Compare processing methods
    comparator = PipelineComparator(filepath)
    results = comparator.compare_all()
    
    # Print summary
    comparator.print_summary()
    
    print("\n✅ Pipeline comparison complete!")

if __name__ == "__main__":
    main()
```

---

---