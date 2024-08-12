import tkinter as tk
from time import strftime

class Clock:
  def __init__(self, root):
    self.root = root
    self.root.title("Digital Clock")

    # Get time format preference (default 12-hour)
    self.time_format = "%I:%M:%S %p"  # 12-hour format

    self.label = self.create_label()
    self.update_time()
    self.root.mainloop()

  def create_label(self):
    label = tk.Label(self.root, font=("calibri", 40, "bold"),  background="white", foreground="black")
    label.pack(anchor='center')
    return label

  def get_time_text(self):
  
    return strftime(self.time_format + "  |  %A %d, %B %Y")

  def update_time(self):
   
    self.label.config(text=self.get_time_text())
    self.label.after(1000, self.update_time)

if __name__ == "__main__":
  root = tk.Tk()
  clock = Clock(root)
