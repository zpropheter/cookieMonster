import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import threading
import os
import time

def clear_safari_cookies():
    safari_cookie_path = os.path.expanduser('~/Library/Cookies/Cookies.binarycookies')
    if os.path.exists(safari_cookie_path):
        os.remove(safari_cookie_path)
        print("Safari cookies cleared.")

def clear_chrome_cookies():
    chrome_cookie_path = os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/Cookies')
    if os.path.exists(chrome_cookie_path):
        os.remove(chrome_cookie_path)
        print("Chrome cookies cleared.")

def clear_firefox_cookies():
    firefox_profiles_path = os.path.expanduser('~/Library/Application Support/Firefox/Profiles')
    if os.path.exists(firefox_profiles_path):
        for profile in os.listdir(firefox_profiles_path):
            cookie_path = os.path.join(firefox_profiles_path, profile, 'cookies.sqlite')
            if os.path.exists(cookie_path):
                os.remove(cookie_path)
                print(f"Firefox cookies cleared in profile: {profile}")

def clear_edge_cookies():
    edge_cookie_path = os.path.expanduser('~/Library/Application Support/Microsoft Edge/Default/Cookies')
    if os.path.exists(edge_cookie_path):
        os.remove(edge_cookie_path)
        print("Edge cookies cleared.")

def clear_cookies(window):
    clear_safari_cookies()
    time.sleep(1)
    clear_chrome_cookies()
    time.sleep(1)
    clear_firefox_cookies()
    time.sleep(1)
    clear_edge_cookies()
    print("All cookies cleared. Call me when you have more cookies!")

    # After clearing cookies, wait 3 seconds, then close the window safely in the main thread:
    def close_window():
        window.destroy()

    window.after(3000, close_window)  # schedule window to close 3 seconds later

def play_gif():
    window = tk.Tk()
    window.title("Cookie Monster")
    window.geometry("400x400")
    window.configure(bg='black')
    window.resizable(False, False)

    script_dir = os.path.dirname(os.path.realpath(__file__))
    gif_path = os.path.join(script_dir, "9xj64y.gif")

    gif = Image.open(gif_path)
    frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(gif)]

    label = tk.Label(window, bg='black')
    label.pack(expand=True)

    def animate(counter=0):
        label.config(image=frames[counter])
        window.after(100, animate, (counter+1) % len(frames))

    animate()

    # Start cookie clearing in a thread, passing the window reference
    threading.Thread(target=clear_cookies, args=(window,), daemon=True).start()

    window.mainloop()

if __name__ == "__main__":
    play_gif()
