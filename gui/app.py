import customtkinter as ctk
import random
from src.ride_share_system import RideShareSystem

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.system = RideShareSystem()

        self.title("Ride Sharing Dispatch Simulator")
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

        self.canvas = ctk.CTkCanvas(self, bg="#020b1a")
        self.canvas.pack(fill="both", expand=True)

        self.panel = ctk.CTkFrame(self, width=320)
        self.panel.place(relx=1, rely=0, anchor="ne", relheight=1)

        ctk.CTkLabel(self.panel, text="CONTROL PANEL",
                     font=("Arial", 22, "bold")).pack(pady=20)

        self.status = ctk.CTkLabel(self.panel, text="No activity yet")
        self.status.pack(pady=10)

        ctk.CTkButton(self.panel, text="Add Driver",
                      height=45, command=self.add_driver).pack(pady=10)

        ctk.CTkButton(self.panel, text="Request Ride",
                      height=45, command=self.request_ride).pack(pady=10)

        ctk.CTkButton(self.panel, text="Clear",
                      height=40, command=self.clear).pack(pady=20)

    def rand_pos(self):
        return random.randint(60, self.winfo_width()-360), random.randint(60, self.winfo_height()-60)

    def add_driver(self):
        x, y = self.rand_pos()
        self.system.add_driver(x, y)
        self.canvas.create_oval(x-6, y-6, x+6, y+6, fill="#38bdf8")

    def request_ride(self):
        sx, sy = self.rand_pos()
        dx, dy = self.rand_pos()

        self.canvas.create_oval(sx-7, sy-7, sx+7, sy+7, fill="#fb923c")
        self.canvas.create_rectangle(dx-6, dy-6, dx+6, dy+6, fill="#22c55e")

        trip = self.system.request_ride(sx, sy, dx, dy)
        if not trip:
            return

        # driver → rider
        self.canvas.create_line(trip.driver.x, trip.driver.y,
                                sx, sy, fill="white", width=2)

        # rider → destination
        self.canvas.create_line(sx, sy, dx, dy,
                                fill="#22c55e", dash=(4, 3))

        self.system.complete_trip(trip)
        self.status.configure(text=self.system.stats())

    def clear(self):
        self.canvas.delete("all")
        self.system = RideShareSystem()
        self.status.configure(text="Cleared")

if __name__ == "__main__":
    app = App()
    app.mainloop()