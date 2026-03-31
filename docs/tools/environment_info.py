#!/usr/bin/env python3
"""
Record environment information for notebook execution.
This helps ensure reproducibility and debugging.
"""

import sys
import subprocess
import json
from datetime import datetime

def get_python_version():
    """Get Python version."""
    return sys.version.split()[0]

def get_package_version(package_name):
    """Get version of a package, or None if not installed."""
    try:
        result = subprocess.run(
            [sys.executable, "-c", f"import {package_name}; print({package_name}.__version__)"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except:
        pass
    return None

def get_jupyter_info():
    """Get Jupyter version info."""
    try:
        result = subprocess.run(
            ["jupyter", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except:
        pass
    return None

def get_kernel_info():
    """Get available Jupyter kernels."""
    try:
        result = subprocess.run(
            ["jupyter", "kernelspec", "list"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except:
        pass
    return None

def main():
    """Record environment information."""
    info = {
        "timestamp": datetime.now().isoformat(),
        "python": {
            "version": get_python_version(),
            "executable": sys.executable,
        },
        "jupyter": {
            "version_info": get_jupyter_info(),
            "kernels": get_kernel_info(),
        },
        "packages": {}
    }
    
    # Key packages to check
    key_packages = [
        "numpy", "pandas", "scipy", "scikit-learn",
        "tensorflow", "keras", "torch", "torchvision",
        "nltk", "spacy", "transformers",
        "matplotlib", "seaborn", "plotly",
        "gym", "flask", "fastapi",
        "jupyter", "ipykernel", "notebook"
    ]
    
    for package in key_packages:
        version = get_package_version(package)
        info["packages"][package] = version if version else "NOT INSTALLED"
    
    # Print summary
    print("=" * 60)
    print("ENVIRONMENT INFORMATION")
    print("=" * 60)
    print(f"Python: {info['python']['version']}")
    print(f"Executable: {info['python']['executable']}")
    print(f"\nJupyter Kernels:")
    if info['jupyter']['kernels']:
        print(info['jupyter']['kernels'])
    print(f"\nKey Packages:")
    for pkg, ver in info['packages'].items():
        status = "✓" if ver != "NOT INSTALLED" else "✗"
        print(f"  {status} {pkg}: {ver}")
    
    # Save to file
    output_file = "artifacts/environment_info.json"
    with open(output_file, "w") as f:
        json.dump(info, f, indent=2)
    
    print(f"\nEnvironment info saved to: {output_file}")
    
    return info

if __name__ == "__main__":
    main()
