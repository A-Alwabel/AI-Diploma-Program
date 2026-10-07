"""
Scalable Data Pipeline Template
Project 01 Template

Fill in the functions marked with TODO comments.
"""

import pandas as pd
import dask.dataframe as dd
import numpy as np
import time
from pathlib import Path

# Optional: cuDF for GPU acceleration
# import cudf


class LargeDataLoader:
    """Handles loading of large datasets."""
    
    def load_chunked(self, filepath, chunk_size=10000):
        """
        Load large CSV file in chunks.
        
        TODO: Implement chunked loading
        """
        # TODO: Use pd.read_csv with chunksize parameter
        # for chunk in pd.read_csv(filepath, chunksize=chunk_size):
        #     yield chunk
        pass
    
    def load_dask(self, filepath):
        """
        Load data using Dask for distributed processing.
        
        TODO: Implement Dask loading
        """
        # TODO: Use dd.read_csv()
        # df = dd.read_csv(filepath)
        # return df
        pass
    
    # Optional: GPU acceleration
    # def load_cudf(self, filepath):
    #     """Load using cuDF for GPU acceleration."""
    #     # TODO: Use cudf.read_csv() if GPU available
    #     pass


class ScalableProcessor:
    """Processes large datasets efficiently."""
    
    def process_with_pandas(self, df, operations):
        """
        Process data using pandas.
        
        TODO: Implement pandas operations
        """
        # TODO: Handle missing values
        # TODO: Remove duplicates
        # TODO: Apply transformations
        # return processed_df
        pass
    
    def process_with_dask(self, df_dask, operations):
        """
        Process data using Dask.
        
        TODO: Implement Dask operations
        """
        # TODO: Handle missing values with Dask
        # TODO: Remove duplicates with Dask
        # TODO: Apply transformations
        # TODO: Compute result
        # return result.compute()
        pass


class PerformanceBenchmark:
    """Benchmarks different processing methods."""
    
    def benchmark_pandas(self, df, operations):
        """
        Benchmark pandas performance.
        
        TODO: Measure pandas processing time
        """
        # TODO: Start timer
        # TODO: Perform operations
        # TODO: End timer
        # TODO: Return time and memory usage
        pass
    
    def benchmark_dask(self, df_dask, operations):
        """
        Benchmark Dask performance.
        
        TODO: Measure Dask processing time
        """
        # TODO: Similar to pandas benchmark
        pass
    
    def compare_methods(self, results):
        """
        Compare performance of different methods.
        
        TODO: Create comparison table
        """
        # TODO: Create DataFrame with comparison
        # TODO: Display results
        pass


def main():
    """
    Main execution function.
    
    TODO: Implement complete scalable pipeline
    """
    # TODO: Load data (start with small sample)
    # TODO: Process with pandas
    # TODO: Process with Dask
    # TODO: Compare performance
    # TODO: Scale to larger dataset
    
    print("Scalable data pipeline complete!")


if __name__ == "__main__":
    main()

