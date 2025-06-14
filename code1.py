import tkinter as tk
from datetime import datetime
import time
class SimpleStopwatchClock:
    def __init__(self, root):
        self.root = root
        self.root.title("⏰ Clock & Stopwatch")
        self.root.geometry("400x500")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.start_time = 0
        self.elapsed_time = 0
        self.is_running = False
        self.lap_times = []

        self.create_widgets()
        self.update_clock()

    def create_widgets(self):
        # Clock display
        tk.Label(self.root, text="Digital Clock", font=("Arial", 20, "bold"),
                 fg="#00ff9f", bg="#1e1e1e").pack(pady=10)

        self.time_label = tk.Label(self.root, font=("Courier", 36, "bold"),
                                   fg="white", bg="#1e1e1e")
        self.time_label.pack(pady=5)

        self.date_label = tk.Label(self.root, font=("Arial", 14),
                                   fg="#aaaaaa", bg="#1e1e1e")
        self.date_label.pack(pady=5)

        # Stopwatch display
        tk.Label(self.root, text="Stopwatch", font=("Arial", 20, "bold"),
                 fg="#ff5252", bg="#1e1e1e").pack(pady=10)

        self.stopwatch_label = tk.Label(self.root, text="00:00:00.00",
                                        font=("Courier", 28, "bold"),
                                        fg="#ffffff", bg="#333333", width=15, relief=tk.SUNKEN)
        self.stopwatch_label.pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#1e1e1e")
        btn_frame.pack(pady=10)

        self.start_stop_btn = tk.Button(btn_frame, text="▶️ Start", width=10,
                                        command=self.toggle_stopwatch, bg="#00ff9f", fg="black")
        self.start_stop_btn.pack(side=tk.LEFT, padx=5)

        tk.Button(btn_frame, text="🔄 Reset", width=10,
                  command=self.reset_stopwatch, bg="#ff5252", fg="white").pack(side=tk.LEFT, padx=5)

        self.lap_btn = tk.Button(self.root, text="📍", command=self.record_lap,
                                 state=tk.DISABLED, bg="#ffaa00", fg="black")
        self.lap_btn.pack(pady=5)

        # Lap list
        self.lap_listbox = tk.Listbox(self.root, font=("Courier", 10),
                                      bg="#1e1e1e", fg="#ffffff", height=8)
        self.lap_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def update_clock(self):
        now = datetime.now()
        self.time_label.config(text=now.strftime("%H:%M:%S"))
        self.date_label.config(text=now.strftime("%A, %B %d, %Y"))

        if self.is_running:
            self.elapsed_time = time.time() - self.start_time
            self.update_stopwatch_display()

        self.root.after(100, self.update_clock)

    def toggle_stopwatch(self):
        if not self.is_running:
            self.start_time = time.time() - self.elapsed_time
            self.is_running = True
            self.start_stop_btn.config(text="⏸️ Pause", bg="#ff5252", fg="white")
            self.lap_btn.config(state=tk.NORMAL)
        else:
            self.is_running = False
            self.start_stop_btn.config(text="▶️ Start", bg="#00ff9f", fg="black")
            self.lap_btn.config(state=tk.DISABLED)

    def reset_stopwatch(self):
        self.is_running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.stopwatch_label.config(text="00:00:00.00")
        self.start_stop_btn.config(text="▶️ Start", bg="#00ff9f", fg="black")
        self.lap_btn.config(state=tk.DISABLED)
        self.lap_times.clear()
        self.lap_listbox.delete(0, tk.END)

    def update_stopwatch_display(self):
        formatted = self.format_time(self.elapsed_time)
        self.stopwatch_label.config(text=formatted)

    def record_lap(self):
        if self.is_running:
            formatted = self.format_time(self.elapsed_time)
            self.lap_times.append(formatted)
            self.lap_listbox.insert(tk.END, f"Lap {len(self.lap_times):02d}: {formatted}")
            self.lap_listbox.see(tk.END)

    def format_time(self, seconds):
        minutes = int(seconds // 60)
        remaining = seconds % 60
        hours = int(minutes // 60)
        minutes = minutes % 60
        return f"{hours:02d}:{minutes:02d}:{remaining:05.2f}"

def main():
    root = tk.Tk()
    app = SimpleStopwatchClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()