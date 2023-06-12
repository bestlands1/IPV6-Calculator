import ipaddress
import tkinter as tk
from tkinter import messagebox, Toplevel
import itertools


def validate_ipv6_address(address, prefix_length):
    try:
        ipv6 = ipaddress.IPv6Interface(f"{address}/{prefix_length}")
        return ipv6
    except (ipaddress.AddressValueError, ValueError):
        return None


def expand_ipv6_address(address):
    try:
        return str(ipaddress.IPv6Address(address).exploded)
    except ipaddress.AddressValueError:
        return None


def clear_entry():
    entry.delete(0, tk.END)


def display_addresses(ipv6_address, prefix_length):
    network = validate_ipv6_address(ipv6_address, prefix_length)
    if network is None:
        messagebox.showerror("Invalid IPv6 Address", "Please enter a valid IPv6 address.")
        return

    addresses = list(itertools.islice(network.network.hosts(), 128))  # Limit to 128 addresses

    window = Toplevel()
    window.title("IPv6 Addresses")
    window.geometry("600x400")  # Set a larger size for the window

    listbox = tk.Listbox(window)
    listbox.pack(fill=tk.BOTH, expand=True)  # Make the listbox expand to fill the window

    for address in addresses:
        listbox.insert(tk.END, str(address))

    scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox.config(yscrollcommand=scrollbar.set)

    window.mainloop()



def check_ipv6_address():
    ipv6_address = entry.get().strip()  # Remove leading and trailing spaces
    prefix_length = prefix_length_var.get()

    if ipv6_address.lower() == 'exit':
        window.destroy()
    elif ipv6_address == '':
        messagebox.showerror("Invalid IPv6 Address", "Please enter an IPv6 address.")
    else:
        ipv6 = validate_ipv6_address(ipv6_address, prefix_length)

        if ipv6 is None:
            messagebox.showerror("Invalid IPv6 Address", "Please enter a valid IPv6 address.")
            return

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "The IPv6 address is valid.\n")
        result_text.insert(tk.END, f"IPv6 Address: {ipv6_address}\n")
        result_text.insert(tk.END, f"Network: {ipv6.network.network_address}\n")

        if ipv6.network.is_multicast:
            result_text.insert(tk.END, "Type: Multicast\n")
        elif any(ipv6.ip in unicast_range for unicast_range in unicast_ranges):
            result_text.insert(tk.END, "Type: Unicast\n")
        else:
            result_text.insert(tk.END, "Type: Anycast\n")

        # Display original IPv6 address
        result_text.insert(tk.END, "IP Address (full): ")
        ip_parts = ipv6.ip.exploded.split(":")
        for i, part in enumerate(ip_parts):
            if i < prefix_length // 16:
                result_text.insert(tk.END, part)
            else:
                result_text.insert(tk.END, part, "highlight")
            if i < len(ip_parts) - 1:
                result_text.insert(tk.END, ":")

        # Display number of addresses possible for the selected prefix length
        num_addresses = 2 ** (128 - prefix_length)
        result_text.insert(tk.END, f"\nNumber of Addresses Possible: {num_addresses}\n")

        # Update the command of the display_button
        display_button.config(command=lambda: display_addresses(ipv6_address, prefix_length))

        clear_entry()



# Define unicast address ranges
unicast_ranges = [
    ipaddress.IPv6Network('2000::/3'),
    ipaddress.IPv6Network('fc00::/7'),
    ipaddress.IPv6Network('::/128')
]

# Create the main window
window = tk.Tk()
window.title("IPv6 Address Validator")

# Create a label for IPv6 address
label_ipv6 = tk.Label(window, text="Enter an IPv6 address:")
label_ipv6.pack()

# Create an entry field for IPv6 address
entry = tk.Entry(window)
entry.pack()

# Create a label for prefix length
label_prefix = tk.Label(window, text="Select Prefix Length:")
label_prefix.pack()

# Create a dropdown menu for prefix length
prefix_length_var = tk.IntVar()
prefix_length_dropdown = tk.OptionMenu(window, prefix_length_var, *range(128, 0, -1))
prefix_length_dropdown.pack()

# Create a button to validate the address
button = tk.Button(window, text="Validate", command=check_ipv6_address)
button.pack()

# Create a textbox with larger font
result_text = tk.Text(window, height=20, width=80, font=("Arial", 12))
result_text.pack()

# Define text tags for highlighting
result_text.tag_configure("normal", foreground="black")
result_text.tag_configure("highlight", foreground="red")

# Create a button to display all addresses
display_button = tk.Button(window, text="Display")
display_button.pack()

# Run the GUI main loop
window.mainloop()
