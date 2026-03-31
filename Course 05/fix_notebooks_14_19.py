#!/usr/bin/env python3
"""Fix concatenated imports in notebooks 14-19"""

import json
import re
import os

def fix_concatenated_imports(source):
    """Split concatenated import statements"""
    # Pattern: import X as Yimport or import Ximport
    source = re.sub(
        r'(import\s+\w+(?:\s+as\s+\w+)?)(import\s+)',
        r'\1\n\2',
        source
    )
    # Pattern: from X import Yfrom
    source = re.sub(
        r'(from\s+[\w.]+\s+import[^\n]+?)(from\s+)',
        r'\1\n\2',
        source
    )
    return source

notebooks_to_fix = {
    'unit5-scaling/examples/14_dask_distributed.ipynb': {
        'cell_1': {
            'old': 'import pandas as pdimport numpy as npimport dask.dataframe as ddimport matplotlib.pyplot as pltimport time',
            'new': '''import pandas as pd
import numpy as np
import dask.dataframe as dd
import matplotlib.pyplot as plt
import time'''
        },
        'cell_2': {
            'new': '''print("=" * 70)
print("Example 14: Distributed Computing with Dask | الحوسبة الموزعة مع Dask")
print("=" * 70)
print("\\n📚 Prerequisites: Unit 4 completed, basic ML knowledge")
print("🔗 This is the FIRST example in Unit 5 - distributed computing")
print("🎯 Goal: Master distributed computing with Dask")
        }
    },
    'unit5-scaling/examples/15_rapids_workflows.ipynb': {
        'cell_1': {
            'old': 'import pandas as pdimport numpy as npimport matplotlib.pyplot as pltimport timefrom sklearn.linear_model import LinearRegression as skLinearRegression',
            'new': '''import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn.linear_model import LinearRegression as skLinearRegression'''
        },
        'cell_2': {
            'new': '''# Try to import RAPIDS
try:
    import cudf
    import cuml
    from cuml.linear_model import LinearRegression
    RAPIDS_AVAILABLE = True
    print("✓ RAPIDS is available")
except ImportError:
    RAPIDS_AVAILABLE = False
    print("⚠ RAPIDS not available - Using simulation")

print("=" * 70)
print("Example 15: GPU Workflows & RAPIDS | سير عمل GPU و RAPIDS")
print("=" * 70)
print("\\n📚 Prerequisites: Example 14 completed, basic GPU knowledge")
print("🔗 This is the SECOND example in Unit 5 - GPU workflows")
print("🎯 Goal: Master GPU-accelerated data science with RAPIDS")
        }
    },
    'unit5-scaling/examples/16_production_pipelines.ipynb': {
        'cell_0': {
            'old': 'import pandas as pdimport numpy as npfrom sklearn.pipeline import Pipelinefrom sklearn.preprocessing import StandardScaler, Imputerfrom sklearn.linear_model import LinearRegressionfrom sklearn.model_selection import train_test_splitfrom sklearn.metrics import mean_squared_error, r2_scoreimport loggingimport jsonfrom datetime import datetime',
            'new': '''import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import logging
import json
from datetime import datetime'''
        },
        'cell_1': {
            'new': '''# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('unit5-scaling/examples/pipeline.log'),
                              logging.StreamHandler()])
logger = logging.getLogger(__name__)

print("=" * 70)
print("Example 16: Production Pipelines | خطوط الإنتاج")
print("=" * 70)
print("\\n📚 Prerequisites: Examples 14-15 completed, pipeline knowledge")
print("🔗 This is the THIRD example in Unit 5 - production pipelines")
print("🎯 Goal: Master building production-ready ML pipelines")
print("Reference: Study 16.pdf before running this code example.\\n")'''
        }
    },
    'unit5-scaling/examples/17_performance_optimization.ipynb': {
        'cell_1': {
            'old': 'import pandas as pdimport numpy as npimport matplotlib.pyplot as pltimport timeimport cProfileimport pstatsfrom io import StringIO',
            'new': '''import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import cProfile
import pstats
from io import StringIO'''
        },
        'cell_2': {
            'new': '''print("=" * 70)
print("Example 17: Performance Optimization | تحسين الأداء")
print("=" * 70)
print("\\n📚 Prerequisites: Examples 14-16 completed, performance knowledge")
print("🔗 This is the FOURTH example in Unit 5 - performance optimization")
print("🎯 Goal: Master performance profiling and optimization")
print("Reference: Study 17.pdf before running this code example.\\n")'''
        }
    },
    'unit5-scaling/examples/18_large_datasets.ipynb': {
        'cell_1': {
            'old': 'import pandas as pdimport numpy as npimport matplotlib.pyplot as pltimport time',
            'new': '''import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time'''
        },
        'cell_2': {
            'new': '''print("=" * 70)
print("Example 18: Large Dataset Handling | التعامل مع مجموعات البيانات الكبيرة")
print("=" * 70)
print("\\n📚 Prerequisites: Examples 14-17 completed, memory management knowledge")
print("🔗 This is the FIFTH example in Unit 5 - large dataset handling")
print("🎯 Goal: Master processing large datasets efficiently")
print("Reference: Study 18.pdf before running this code example.\\n")'''
        }
    },
    'unit5-scaling/examples/19_deployment.ipynb': {
        'cell_0': {
            'old': 'import pandas as pdimport numpy as npimport jsonimport picklefrom datetime import datetimefrom sklearn.linear_model import LinearRegressionfrom sklearn.model_selection import train_test_splitfrom sklearn.metrics import mean_squared_error, r2_scoreimport logging',
            'new': '''import pandas as pd
import numpy as np
import json
import pickle
from datetime import datetime
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import logging'''
        },
        'cell_1': {
            'new': '''logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

print("=" * 70)
print("Example 19: Deployment & Monitoring | النشر والمراقبة")
print("=" * 70)
print("\\n📚 Prerequisites: Examples 14-18 completed, deployment knowledge")
print("🔗 This is the SIXTH example in Unit 5 - deployment and monitoring")
print("🎯 Goal: Master deploying and monitoring ML models")
print("Reference: Study 19.pdf before running this code example.\\n")'''
        }
    }
}

for nb_path, fixes in notebooks_to_fix.items():
    if not os.path.exists(nb_path):
        print(f"⚠️  {nb_path} not found, skipping...")
        continue
    
    print(f"📄 Fixing {nb_path.split('/')[-1]}...")
    
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    fixed_cells = 0
    for cell_key, fix_data in fixes.items():
        cell_idx = int(cell_key.split('_')[1])
        if cell_idx < len(nb['cells']):
            cell = nb['cells'][cell_idx]
            if cell['cell_type'] == 'code':
                source = ''.join(cell.get('source', []))
                if fix_data['old'] in source or source.strip() == fix_data['old'].replace('\n', ''):
                    nb['cells'][cell_idx]['source'] = [line + '\n' for line in fix_data['new'].split('\n')]
                    fixed_cells += 1
                    print(f"   ✅ Fixed cell {cell_idx}")
    
    if fixed_cells > 0:
        with open(nb_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)
        print(f"   ✅ Saved {fixed_cells} cell(s)")
    else:
        print(f"   ⚠️  No cells needed fixing")

print("\n✅ All fixes complete!")

