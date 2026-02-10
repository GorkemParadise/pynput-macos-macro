# macOS Toggle Macro (F8)

A Python macro that repeats a key sequence (`2 → 3 → 4`) in a loop when toggled on with **F8**.

## Install

```bash
pip install pynput
```

## macOS Accessibility Permission (Required)

`pynput` needs Accessibility access to listen to and simulate key presses.

1. Open **System Settings → Privacy & Security → Accessibility**
2. Click the **+** button
3. Add the app you run the script from:
   - **Terminal.app** (`/System/Applications/Utilities/Terminal.app`)
   - or **iTerm**, **VS Code**, **PyCharm**, etc.
4. Ensure the toggle is **ON**
5. **Restart** the terminal app after granting permission

## Run

```bash
python3 macro.py
```

Press `F8` to toggle the macro ON/OFF. Press `Ctrl+C` to quit.

## Mouse Side Button → F8 via Karabiner-Elements

Since `pynput` cannot capture mouse side buttons (button4/button5) on macOS,
use [Karabiner-Elements](https://karabiner-elements.pqrs.org/) to remap them.

### Setup

1. Install Karabiner-Elements from https://karabiner-elements.pqrs.org/
2. Open **Karabiner-Elements → Complex Modifications → Add your own rule**
3. Paste this JSON into `~/.config/karabiner/assets/complex_modifications/mouse_to_f8.json`:

```json
{
  "title": "Mouse Side Button to F8",
  "rules": [
    {
      "description": "Map mouse button4 (back) to F8",
      "manipulators": [
        {
          "type": "basic",
          "from": {
            "pointing_button": "button4"
          },
          "to": [
            {
              "key_code": "f8"
            }
          ]
        }
      ]
    }
  ]
}
```

4. Go to **Complex Modifications → Add Rule** and enable "Map mouse button4 (back) to F8"

> Change `button4` to `button5` if you want the forward button instead.

## Configuration

Edit these variables at the top of `macro_toggle.py`:

| Variable     | Default | Description                    |
|--------------|---------|--------------------------------|
| `TOGGLE_KEY` | `F8`    | Key to toggle macro            |
| `MACRO_KEYS` | `2,3,4` | Keys pressed in sequence       |
| `DELAY`      | `0.200` | Delay between keys (seconds)   |