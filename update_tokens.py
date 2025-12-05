#!/usr/bin/env python3
"""
Update token count for the HUD widget
Can be called manually or integrated into Claude Code
"""

import json
import sys
from pathlib import Path

def update_token_count(used, total=200000):
    """Update the token status file"""
    status_file = Path.home() / '.claude' / 'token_status.json'
    status_file.parent.mkdir(parents=True, exist_ok=True)

    remaining = total - used
    percentage = (remaining / total) * 100 if total > 0 else 0

    data = {
        'used': used,
        'total': total,
        'remaining': remaining,
        'percentage': percentage
    }

    with open(status_file, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Token count updated: {remaining:,} remaining ({percentage:.1f}%)")

def main():
    if len(sys.argv) < 2:
        print("Usage: update_tokens.py <used_tokens> [total_tokens]")
        print("Example: update_tokens.py 25000 200000")
        sys.exit(1)

    used = int(sys.argv[1])
    total = int(sys.argv[2]) if len(sys.argv) > 2 else 200000

    update_token_count(used, total)

if __name__ == '__main__':
    main()
