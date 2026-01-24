import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

MAX_DRIVERS = 5
MAX_CUSTOMERS = 3
MAX_LOCATIONS = 6


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Ride-Sharing Dispatch System")
        self.attributes("-fullscreen", True)
        self.bind("<Escape>", lambda e: self.attributes("-fullscreen", False))

        self.home_frame = ctk.CTkFrame(self, corner_radius=0)
        self.route_frame = ctk.CTkFrame(self, corner_radius=0)

        self.driver_count = 0
        self.customer_count = 0
        self.location_count = 0

        self.create_home_screen()
        self.create_route_screen()

        self.show_home()

    def show_home(self):
        self.route_frame.pack_forget()
        self.home_frame.pack(fill="both", expand=True)

    def show_route(self):
        self.home_frame.pack_forget()
        self.route_frame.pack(fill="both", expand=True)

    def create_home_screen(self):
        self.home_frame.pack(fill="both", expand=True)

        container = ctk.CTkFrame(self.home_frame, fg_color="transparent")
        container.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(container, text="HOME SCREEN", font=("Arial", 14, "bold")).pack(pady=(0, 40))
        ctk.CTkLabel(container, text="Ride-Sharing Dispatch System", font=("Arial", 36, "bold")).pack(pady=(0, 10))
        ctk.CTkButton(container, text="Start Simulation", width=260, height=55,
                      font=("Arial", 18, "bold"), command=self.show_route).pack()

    def create_route_screen(self):
        container = ctk.CTkFrame(self.route_frame)
        container.pack(fill="both", expand=True, padx=30, pady=30)

        left_panel = ctk.CTkFrame(container)
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 20))

        ctk.CTkLabel(left_panel, text="Live Graph", font=("Arial", 26, "bold")).pack(pady=10)

        self.canvas = ctk.CTkCanvas(left_panel, bg="#020b1a", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=20, pady=20)

        right_panel = ctk.CTkFrame(container, width=320)
        right_panel.pack(side="right", fill="y")
        right_panel.pack_propagate(False)

        ctk.CTkLabel(right_panel, text="Controls", font=("Arial", 24, "bold")).pack(pady=20)

        self.status_label = ctk.CTkLabel(right_panel, text="Drivers: 0 | Customers: 0 | Locations: 0",
                                         font=("Arial", 14))
        self.status_label.pack(pady=10)

        ctk.CTkButton(right_panel, text="Add Driver", height=45, command=self.add_driver).pack(pady=10)
        ctk.CTkButton(right_panel, text="Add Customer", height=45, command=self.add_customer).pack(pady=10)
        ctk.CTkButton(right_panel, text="Add Location", height=45, command=self.add_location).pack(pady=10)

        ctk.CTkButton(right_panel, text="Clear Graph", height=40, command=self.clear_graph).pack(pady=20)
        ctk.CTkButton(right_panel, text="Back to Home", height=40, command=self.show_home).pack(pady=20)

    def random_position(self):
        x = random.randint(50, self.canvas.winfo_width() - 50)
        y = random.randint(50, self.canvas.winfo_height() - 50)
        return x, y

    def add_driver(self):
        if self.driver_count >= MAX_DRIVERS:
            return
        x, y = self.random_position()
        self.canvas.create_oval(x-6, y-6, x+6, y+6, fill="#22d3ee", outline="")
        self.driver_count += 1
        self.update_status()

    def add_customer(self):
        if self.customer_count >= MAX_CUSTOMERS:
            return
        x, y = self.random_position()
        self.canvas.create_oval(x-7, y-7, x+7, y+7, fill="#f97316", outline="")
        self.customer_count += 1
        self.update_status()

    def add_location(self):
        if self.location_count >= MAX_LOCATIONS:
            return
        x, y = self.random_position()
        self.canvas.create_rectangle(x-6, y-6, x+6, y+6, fill="#22c55e", outline="")
        self.location_count += 1
        self.update_status()

    def clear_graph(self):
        self.canvas.delete("all")
        self.driver_count = 0
        self.customer_count = 0
        self.location_count = 0
        self.update_status()

    def update_status(self):
        self.status_label.configure(
            text=f"Drivers: {self.driver_count} | Customers: {self.customer_count} | Locations: {self.location_count}"
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()
