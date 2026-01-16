import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Ride-Sharing Dispatch System")
    window.geometry("500x300")

    label = tk.Label(
        window,
        text="HELLO FROM DSA PROJECT",
        font=("Arial", 16)
    )
    label.pack(pady=50)

    window.mainloop()

if __name__ == "__main__":
    main()
