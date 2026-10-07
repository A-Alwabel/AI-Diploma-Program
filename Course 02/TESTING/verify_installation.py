#!/usr/bin/env python3
"""
Installation Verification Script
Verifies all required libraries are installed and working correctly.
"""

import sys

def check_library(library_name, import_name=None):
    """Check if a library is installed and can be imported."""
    if import_name is None:
        import_name = library_name
    
    try:
        __import__(import_name)
        print(f"✅ {library_name}: Installed and working")
        return True
    except ImportError as e:
        print(f"❌ {library_name}: NOT INSTALLED - {e}")
        return False
    except Exception as e:
        print(f"⚠️  {library_name}: Installed but error - {e}")
        return False


def check_version(library_name, import_name, min_version=None):
    """Check library version."""
    try:
        module = __import__(import_name)
        version = getattr(module, '__version__', 'Unknown')
        print(f"   Version: {version}")
        
        if min_version:
            # Simple version comparison (can be improved)
            print(f"   Required: >= {min_version}")
        
        return True
    except Exception as e:
        print(f"   Could not get version: {e}")
        return False


def test_numpy():
    """Test NumPy functionality."""
    try:
        import numpy as np
        arr = np.array([1, 2, 3, 4, 5])
        mean = np.mean(arr)
        assert mean == 3.0, "NumPy mean calculation failed"
        print("   ✅ NumPy operations working correctly")
        return True
    except Exception as e:
        print(f"   ❌ NumPy test failed: {e}")
        return False


def test_matplotlib():
    """Test Matplotlib functionality."""
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        # Create simple plot (don't show)
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        plt.figure()
        plt.plot(x, y)
        plt.close()  # Close without showing
        print("   ✅ Matplotlib plotting working correctly")
        return True
    except Exception as e:
        print(f"   ❌ Matplotlib test failed: {e}")
        return False


def test_sklearn():
    """Test Scikit-learn functionality."""
    try:
        from sklearn.datasets import load_iris
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LogisticRegression
        
        # Load data
        iris = load_iris()
        X_train, X_test, y_train, y_test = train_test_split(
            iris.data, iris.target, test_size=0.2, random_state=42
        )
        
        # Train simple model
        model = LogisticRegression(max_iter=200)
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        
        assert score > 0.8, "Model training failed"
        print(f"   ✅ Scikit-learn working correctly (test accuracy: {score:.2f})")
        return True
    except Exception as e:
        print(f"   ❌ Scikit-learn test failed: {e}")
        return False


def test_networkx():
    """Test NetworkX functionality."""
    try:
        import networkx as nx
        G = nx.Graph()
        G.add_node("A")
        G.add_node("B")
        G.add_edge("A", "B")
        assert len(G.nodes()) == 2, "NetworkX node addition failed"
        assert len(G.edges()) == 1, "NetworkX edge addition failed"
        print("   ✅ NetworkX graph operations working correctly")
        return True
    except Exception as e:
        print(f"   ❌ NetworkX test failed: {e}")
        return False


def main():
    """Main verification function."""
    print("=" * 70)
    print("🔍 VERIFYING PYTHON LIBRARIES FOR AI COURSE")
    print("=" * 70)
    print()
    
    # Check Python version
    print(f"Python Version: {sys.version}")
    print(f"Python Path: {sys.executable}")
    print()
    
    # Required libraries
    libraries = [
        ("NumPy", "numpy", "1.24.0"),
        ("SciPy", "scipy", "1.10.0"),
        ("Matplotlib", "matplotlib", "3.7.0"),
        ("Scikit-learn", "sklearn", "1.3.0"),
        ("NetworkX", "networkx", "3.0"),
        ("Pandas", "pandas", "2.0.0"),
        ("Seaborn", "seaborn", "0.12.0"),
    ]
    
    results = []
    
    print("📦 Checking Library Installation:")
    print("-" * 70)
    
    for lib_name, import_name, min_ver in libraries:
        print(f"\n{lib_name}:")
        installed = check_library(lib_name, import_name)
        if installed:
            check_version(lib_name, import_name, min_ver)
        results.append(installed)
    
    print()
    print("=" * 70)
    print("🧪 Testing Library Functionality:")
    print("-" * 70)
    
    # Test functionality
    test_results = []
    
    print("\nTesting NumPy:")
    test_results.append(test_numpy())
    
    print("\nTesting Matplotlib:")
    test_results.append(test_matplotlib())
    
    print("\nTesting Scikit-learn:")
    test_results.append(test_sklearn())
    
    print("\nTesting NetworkX:")
    test_results.append(test_networkx())
    
    print()
    print("=" * 70)
    print("📊 SUMMARY")
    print("=" * 70)
    
    installed_count = sum(results)
    total_libraries = len(results)
    
    test_count = sum(test_results)
    total_tests = len(test_results)
    
    print(f"\nLibraries Installed: {installed_count}/{total_libraries}")
    print(f"Functionality Tests Passed: {test_count}/{total_tests}")
    
    if installed_count == total_libraries and test_count == total_tests:
        print("\n✅ ALL CHECKS PASSED! You're ready for the course!")
        return 0
    else:
        print("\n⚠️  SOME CHECKS FAILED. Please review errors above.")
        print("\n💡 TIP: Run 'pip install -r ../../requirements.txt' to install missing libraries.")
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)

