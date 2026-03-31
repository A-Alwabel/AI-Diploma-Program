#!/usr/bin/env python3
"""
Rollback notebook fixes by restoring from backup.
Usage: python rollback_notebook_fixes.py <backup_folder_name>
Example: python rollback_notebook_fixes.py notebooks_20250124_143022
"""

import shutil
import sys
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent
BACKUPS_DIR = BASE_DIR / "artifacts" / "backups"

def rollback(backup_name: str, dry_run: bool = False):
    """Rollback notebooks from backup."""
    backup_dir = BACKUPS_DIR / backup_name
    
    if not backup_dir.exists():
        print(f"❌ Backup not found: {backup_dir}")
        print(f"Available backups:")
        for b in BACKUPS_DIR.iterdir():
            if b.is_dir() and b.name.startswith("notebooks_"):
                print(f"  - {b.name}")
        sys.exit(1)
    
    print(f"🔍 Finding notebooks in backup: {backup_dir}")
    backup_notebooks = list(backup_dir.rglob("*.ipynb"))
    print(f"✅ Found {len(backup_notebooks)} notebooks in backup")
    
    if dry_run:
        print("\n🔍 DRY RUN - No files will be modified")
        print("Notebooks that would be restored:")
        for nb_path in backup_notebooks[:10]:
            rel_path = nb_path.relative_to(backup_dir)
            target = BASE_DIR / rel_path
            print(f"  {rel_path} -> {target}")
        if len(backup_notebooks) > 10:
            print(f"  ... and {len(backup_notebooks) - 10} more")
        return
    
    print(f"\n⚠️  WARNING: This will overwrite current notebooks!")
    response = input("Type 'yes' to continue: ")
    if response.lower() != 'yes':
        print("❌ Rollback cancelled")
        sys.exit(0)
    
    print(f"📦 Restoring notebooks...")
    restored = 0
    errors = []
    
    for nb_path in backup_notebooks:
        rel_path = nb_path.relative_to(backup_dir)
        target = BASE_DIR / rel_path
        
        try:
            # Ensure target directory exists
            target.parent.mkdir(parents=True, exist_ok=True)
            
            # Restore notebook
            shutil.copy2(nb_path, target)
            restored += 1
            
            if restored % 100 == 0:
                print(f"  Restored {restored}/{len(backup_notebooks)} notebooks...")
        except Exception as e:
            errors.append((rel_path, str(e)))
    
    print(f"✅ Rollback complete: {restored} notebooks restored")
    
    if errors:
        print(f"\n⚠️  {len(errors)} errors occurred:")
        for rel_path, error in errors[:10]:
            print(f"  {rel_path}: {error}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more errors")
    
    print(f"\n✅ Rollback successful!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rollback_notebook_fixes.py <backup_folder_name> [--dry-run]")
        print("\nAvailable backups:")
        for b in BACKUPS_DIR.iterdir():
            if b.is_dir() and b.name.startswith("notebooks_"):
                print(f"  - {b.name}")
        sys.exit(1)
    
    backup_name = sys.argv[1]
    dry_run = "--dry-run" in sys.argv
    
    rollback(backup_name, dry_run)
