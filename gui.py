import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import os
import queue
import ids_engine

# setup shared queue
gui_alert_queue = queue.Queue()
ids_engine.alert_queue = gui_alert_queue

def launch_gui():
    root = tk.Tk()
    root.title("intrusion detection system")
    root.geometry("650x500")

    dark_mode = False

    # title
    title = tk.Label(root, text="intrusion detection system", font=("Arial", 16))
    title.pack(pady=10)

    # sniffing status label
    status_label = tk.Label(root, text="status: inactive ❌", font=("Arial", 12), fg="red")
    status_label.pack(pady=5)

    # alert display box
    alert_box = scrolledtext.ScrolledText(root, width=75, height=15, state="disabled")
    alert_box.pack(pady=10)

    # monitor queue and show alerts
    def poll_alerts():
        alerts = ids_engine.get_alerts()
        for alert in alerts:
            alert_box.config(state="normal")
            alert_box.insert(tk.END, alert + "\n")
            alert_box.yview(tk.END)
            alert_box.config(state="disabled")
        root.after(1000, poll_alerts)

    def start_monitoring():
        threading.Thread(target=ids_engine.start_sniffing, daemon=True).start()
        status_label.config(text="status: sniffing active ✅", fg="green")
        messagebox.showinfo("IDS", "monitoring started.")

    def stop_monitoring():
        ids_engine.stop_sniffing()
        status_label.config(text="status: inactive ❌", fg="red")
        messagebox.showinfo("IDS", "monitoring stopped.")

    def view_logs():
        if os.path.exists("suspicious_log.txt"):
            with open("suspicious_log.txt", "r") as log:
                data = log.read()
            alert_box.config(state="normal")
            alert_box.delete(1.0, tk.END)
            alert_box.insert(tk.END, data)
            alert_box.config(state="disabled")
        else:
            messagebox.showinfo("IDS", "no logs found.")

    def toggle_theme():
        nonlocal dark_mode
        dark_mode = not dark_mode
        if dark_mode:
            root.configure(bg="#2e2e2e")
            title.configure(bg="#2e2e2e", fg="white")
            status_label.configure(bg="#2e2e2e", fg=status_label.cget("fg"))
            alert_box.configure(bg="black", fg="white", insertbackground="white")
        else:
            root.configure(bg="SystemButtonFace")
            title.configure(bg="SystemButtonFace", fg="black")
            status_label.configure(bg="SystemButtonFace", fg=status_label.cget("fg"))
            alert_box.configure(bg="white", fg="black", insertbackground="black")

    # buttons
    start_btn = tk.Button(root, text="start monitoring", command=start_monitoring, bg="green", fg="white")
    start_btn.pack(pady=5)

    stop_btn = tk.Button(root, text="stop monitoring", command=stop_monitoring, bg="red", fg="white")
    stop_btn.pack(pady=5)

    log_btn = tk.Button(root, text="view log file", command=view_logs, bg="blue", fg="white")
    log_btn.pack(pady=5)

    # theme toggle button (top right corner)
    theme_btn = tk.Button(root, text="🌗", command=toggle_theme)
    theme_btn.place(relx=0.97, rely=0.02, anchor="ne")

    poll_alerts()
    root.mainloop()

if __name__ == "__main__":
    launch_gui()
