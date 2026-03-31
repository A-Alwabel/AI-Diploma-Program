#!/usr/bin/env python3
"""
Monitor notebook execution progress and report every 5 minutes.
"""

import json
import time
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
PROGRESS_FILE = BASE_DIR / "artifacts" / "execution_progress.json"
CHECK_INTERVAL = 300  # 5 minutes in seconds

def get_status():
    """Get current execution status."""
    if not PROGRESS_FILE.exists():
        return None
    
    with open(PROGRESS_FILE) as f:
        progress = json.load(f)
    
    completed = len(progress.get("completed", []))
    results = progress.get("results", {})
    successful = sum(1 for r in results.values() if r.get("status") == "success")
    failed = sum(1 for r in results.values() if r.get("status") == "error")
    
    # Check last update time
    mtime = PROGRESS_FILE.stat().st_mtime
    last_update = datetime.fromtimestamp(mtime)
    now = datetime.now()
    age = (now - last_update).total_seconds() / 60
    
    return {
        "completed": completed,
        "total": 793,
        "successful": successful,
        "failed": failed,
        "remaining": 793 - completed,
        "last_update_minutes": age,
        "timestamp": now
    }

def print_status(status):
    """Print formatted status report."""
    print("\n" + "=" * 70)
    print(f"STATUS REPORT - {status['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    print()
    
    progress_pct = (status['completed'] / status['total']) * 100
    print(f"📊 PROGRESS: {status['completed']}/{status['total']} ({progress_pct:.1f}%)")
    print(f"   ✓ Successful: {status['successful']}")
    print(f"   ✗ Failed: {status['failed']}")
    print(f"   ⏳ Remaining: {status['remaining']}")
    print()
    
    print(f"📁 Last update: {status['last_update_minutes']:.1f} minutes ago")
    print()
    
    if status['completed'] < status['total']:
        if status['last_update_minutes'] < 10:
            # Execution is active
            remaining = status['remaining']
            estimated = (remaining / 26) if remaining > 0 else 0  # ~26 notebooks per minute
            print(f"⏰ Estimated completion: ~{estimated:.0f} minutes")
            print()
            print("🔄 STATUS: Execution running")
        else:
            print("⚠️  STATUS: No recent updates - execution may have stopped")
    else:
        print("✅ STATUS: Execution complete!")
    
    print()
    print("=" * 70)
    print()

def main():
    """Main monitoring loop."""
    print("Starting progress monitor (checking every 5 minutes)...")
    print("Press Ctrl+C to stop")
    print()
    
    last_completed = 0
    
    try:
        while True:
            status = get_status()
            
            if status is None:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Waiting for progress file...")
            else:
                # Check if progress has changed
                if status['completed'] != last_completed:
                    print_status(status)
                    last_completed = status['completed']
                else:
                    # Still report every 5 minutes even if no change
                    print_status(status)
            
            # Wait 5 minutes
            time.sleep(CHECK_INTERVAL)
            
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped by user")
    except Exception as e:
        print(f"\n\nError: {e}")

if __name__ == "__main__":
    main()
