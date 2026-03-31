#!/usr/bin/env python3
"""
Backup all notebooks before making fixes.
Creates a timestamped backup directory with all .ipynb files.
"""

import shutil
import sys
from pathlib import Path
from datetime import datetime

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Exclude directories
EXCLUDE_DIRS = {
    ".git", "__pycache__", ".ipynb_checkpoints",
    "artifacts", "node_modules", ".venv", "venv", "SOLUTIONS_ALL"
}

def find_all_notebooks(base_dir: Path) -> list[Path]:
    """Find all .ipynb files in the repository."""
    notebooks = []
    
    for nb_path in base_dir.rglob("*.ipynb"):
        # Skip if in excluded directory
        if any(excluded in nb_path.parts for excluded in EXCLUDE_DIRS):
            continue
        notebooks.append(nb_path)
    
    return sorted(notebooks)

def create_backup():
    """Create backup of all notebooks."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = BASE_DIR / "artifacts" / "backups" / f"notebooks_{timestamp}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"🔍 Finding all notebooks...")
    notebooks = find_all_notebooks(BASE_DIR)
    print(f"✅ Found {len(notebooks)} notebooks")
    
    print(f"📦 Creating backup in {backup_dir}...")
    backed_up = 0
    
    for nb_path in notebooks:
        # Create relative path structure in backup
        rel_path = nb_path.relative_to(BASE_DIR)
        backup_path = backup_dir / rel_path
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Copy notebook
        shutil.copy2(nb_path, backup_path)
        backed_up += 1
        
        if backed_up % 100 == 0:
            print(f"  Backed up {backed_up}/{len(notebooks)} notebooks...")
    
    print(f"✅ Backup complete: {backed_up} notebooks backed up")
    print(f"📁 Backup location: {backup_dir}")
    
    # Create manifest
    manifest = backup_dir / "manifest.txt"
    with open(manifest, "w") as f:
        f.write(f"Backup created: {datetime.now().isoformat()}\n")
        f.write(f"Total notebooks: {len(notebooks)}\n")
        f.write(f"Backup directory: {backup_dir}\n\n")
        f.write("Notebooks backed up:\n")
        for nb_path in notebooks:
            f.write(f"{nb_path.relative_to(BASE_DIR)}\n")
    
    print(f"📄 Manifest created: {manifest}")
    
    return backup_dir

if __name__ == "__main__":
    try:
        backup_dir = create_backup()
        print(f"\n✅ Backup successful!")
        print(f"💾 To restore, use: python tools/rollback_notebook_fixes.py {backup_dir.name}")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Backup failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
