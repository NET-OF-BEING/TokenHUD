# Token HUD Widget

Desktop overlay widget that displays live Claude Code token usage.

## Features

- **Always-on-top display** - Stays visible over other windows
- **Live updates** - Refreshes every second
- **Color-coded status** - Changes color based on remaining tokens
  - Teal: > 25% remaining
  - Orange: 10-25% remaining
  - Red: < 10% remaining
- **Draggable** - Click and drag to reposition
- **Progress bar** - Visual representation of token usage
- **Semi-transparent** - Unobtrusive overlay

## Files

- `token_hud.py` - Main HUD widget application
- `update_tokens.py` - Script to update token count
- `launch_hud.sh` - Shell script to launch the HUD
- `~/.local/share/applications/token-hud.desktop` - Desktop entry

## Usage

### Launch the HUD

```bash
/home/panda/Documents/PythonScripts/TokenHUD/launch_hud.sh
```

Or search for "Token HUD" in your application launcher.

### Update Token Count

```bash
python3 /home/panda/Documents/PythonScripts/TokenHUD/update_tokens.py <used_tokens> [total_tokens]
```

Example:
```bash
python3 /home/panda/Documents/PythonScripts/TokenHUD/update_tokens.py 25000 200000
```

### Close the HUD

Click the × button in the top-right corner of the widget.

## Data Storage

Token data is stored in: `~/.claude/token_status.json`

Format:
```json
{
  "used": 25000,
  "total": 200000,
  "remaining": 175000,
  "percentage": 87.5
}
```

## Integration

To integrate with Claude Code or other tools, simply update the JSON file:

```python
import json
from pathlib import Path

status_file = Path.home() / '.claude' / 'token_status.json'
data = {
    'used': 25000,
    'total': 200000,
    'remaining': 175000,
    'percentage': 87.5
}

with open(status_file, 'w') as f:
    json.dump(data, f)
```

The HUD will automatically pick up the changes within 1 second.
