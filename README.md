# 🗣️ Suzanne – Voice-Activated Blender via MCP

Suzanne is a voice-controlled interface that lets users operate Blender hands-free using natural language commands. It connects a speech recognition engine to a code assistant (Cursor) and Blender via the **Model Context Protocol (MCP)**, enabling speech-based 3D modeling and scene editing.

> “Say it. Model it.” — Suzanne

---

## 📦 Features

- 🎤 Wake word detection using "Suzanne"
- 🧠 Voice-to-command pipeline with Vosk
- ⌨️ Automatic typing of commands into Cursor
- 🔁 Supports Blender Python API integration
- 🤖 Natural language interpreted via MCP
- 🧩 Ideal for accessibility, automation, and creative toolchains

---

## 🧰 Tools & Technologies

| Tool                  | Role                                              |
|-----------------------|---------------------------------------------------|
| **Blender**           | 3D modeling software                              |
| **Python**            | Script automation and voice handling              |
| **Vosk**              | Offline speech-to-text engine                     |
| **MCP (Model Context Protocol)** | Structures text for LLMs to extract intent |
| **Cursor**            | AI-assisted coding interface for Blender          |
| **PyAutoGUI & xdotool** | Sends keystrokes and types into Cursor          |

---

## 🚀 Getting Started

### ✅ Prerequisites

- Blender 3.x or later installed
- Python 3.8+
- [Vosk Model Download](https://alphacephei.com/vosk/models)
- Cursor open and configured for Python
- Microphone access
- Linux (recommended for `xdotool` support)

---

### 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/duverglas01/blender-mcp-suzanne.git
   cd blender-mcp-suzanne
   ```

2. **Install dependencies**
   ```bash
   pip install vosk pyaudio pyautogui
   ```

3. **Download and unzip the Vosk model**
   ```bash
   mkdir -p vosk-model
   # Place your model here, e.g., vosk-model-small-en-us-0.15
   ```

4. **Run the main script**
   ```bash
   python voice_to_cursor.py
   ```

   This will:
   - Listen for the word “Suzanne”
   - Transcribe the following command
   - Map or send it to Cursor for Blender execution

---

## 🗂️ Main Script

### `voice_to_cursor.py`

This script controls the listening and command pipeline:

- Listens for commands like `"Suzanne, add cube"`
- Translates the voice input into text via Vosk
- Maps predefined commands like `"add cube"` to Blender Python
- Sends those commands to Cursor’s input field
- Presses `Enter` or `Ctrl+Enter` to run the script

---

## 🧪 Example Commands

```plaintext
Suzanne, add cube  
Suzanne, scale up  
Suzanne, delete cube  
Suzanne, clear scene  
Suzanne, move cube up one meter  
```

> ℹ️ All commands are typed and executed inside Cursor’s code interface.

---

## 🔁 Command Mapping Examples

| Spoken Command         | Mapped Python Command                                 |
|------------------------|--------------------------------------------------------|
| "add cube"             | `bpy.ops.mesh.primitive_cube_add()`                   |
| "scale up"             | `bpy.ops.transform.resize(value=(2, 2, 2))`            |
| "clear scene"          | `bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete()` |
| "delete cube"          | `bpy.ops.object.delete()`                              |

If no mapping is found, the freeform text is typed as-is.

---

## 🧬 System Architecture

```plaintext
[User Voice]
    ↓
[Wake Word Detector ("Suzanne")]
    ↓
[Vosk Speech-to-Text Engine]
    ↓
[MCP (Optional) Intent Parsing]
    ↓
[Command Mapping or Raw Text]
    ↓
[Cursor (AI code environment)]
    ↓
[Blender via Python API]
```
