import sounddevice as sd
import queue
import vosk
import os
import sys
import json
import pyautogui
import time

q = queue.Queue()

# Setup Vosk model
model_path = "/home/duverglas01/CMPSC-580/Junior-Seminar Project/vosk-model/vosk-model-small-en-us-0.15"
model = vosk.Model(model_path)

# Predefined command corrections
command_mapping = {
    "add cuba": "bpy.ops.mesh.primitive_cube_add()",
    "and cuba": "bpy.ops.mesh.primitive_cube_add()",
    "add cube": "bpy.ops.mesh.primitive_cube_add()",
    "create cube": "bpy.ops.mesh.primitive_cube_add()",
    "add plane": "bpy.ops.mesh.primitive_plane_add()",
    "clear scene": "bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete()",
    "delete cube": "bpy.ops.object.delete()",
    "scale up": "bpy.ops.transform.resize(value=(2, 2, 2))",
    "scale down": "bpy.ops.transform.resize(value=(0.5, 0.5, 0.5))"
}

# Callback to put audio into a queue
def callback(indata, frames, time_info, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

# Clean and extract command
def clean_command(command):
    if command.lower().startswith("suzanne"):
        return command[7:].strip()
    return None

with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    rec = vosk.KaldiRecognizer(model, 16000)
    print("🎙️ Voice control activated. Say 'Suzanne...' to issue commands.")
    time.sleep(2)

    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            heard = result.get('text', '').strip()

            if heard:
                print(f"📝 Heard: {heard}")

                command = clean_command(heard)

                if command:
                    # Focus Cursor chatbox
                    os.system('xdotool search --name "Cursor" windowactivate')
                    time.sleep(0.2)
                    os.system('xdotool key ctrl+alt+b')
                    time.sleep(0.2)

                    if command.lower() == "enter":
                        print("🚀 Running Blender tool (Ctrl+Enter)")
                        pyautogui.hotkey('ctrl', 'enter')
                        time.sleep(2)
                    else:
                        # Try mapping the command
                        mapped_command = command_mapping.get(command.lower())

                        if mapped_command:
                            print(f"✅ Mapped to Blender Python: {mapped_command}")
                            pyautogui.write(mapped_command, interval=0.05)
                        else:
                            print(f"✍️ Typing free command: {command}")
                            pyautogui.write(command, interval=0.05)

                        pyautogui.press('enter')
                        time.sleep(0.2)

                else:
                    print("❌ No valid Suzanne command detected.")
        else:
            pass
