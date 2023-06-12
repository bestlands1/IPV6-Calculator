# IPV6-Calculator

This program is a simple GUI application for validating and analyzing IPv6 addresses. It allows you to enter an IPv6 address along with a prefix length and validates the address. It also provides information about the type of address (multicast, unicast, or anycast) and displays the original IPv6 address with highlighted portions based on the prefix length. Additionally, it calculates the number of possible addresses for the given prefix length and provides an option to display all the addresses within the network.

## Requirements

- Python 3.x
- `ipaddress` module
- `tkinter` module

## Usage

1. Make sure you have Python 3.x installed on your system.
2. Install the required modules by running the following command:
   ```shell
   pip install ipaddress
   ```
3. Save the program code to a file with a `.py` extension (e.g., `ipv6_validator.py`).
4. Run the program using the following command:
   ```shell
   python ipv6_validator.py
   ```
5. The program will open a GUI window titled "IPv6 Address Validator".
6. Enter an IPv6 address in the provided text field.
7. Select the desired prefix length from the dropdown menu.
8. Click the "Validate" button to validate the address and display the analysis in the textbox.
9. If the address is valid, the program will show the following information:
   - The IPv6 address is valid.
   - The entered IPv6 address.
   - The network address derived from the entered address and prefix length.
   - The type of the address (multicast, unicast, or anycast).
   - The original IPv6 address with highlighted portions based on the prefix length.
   - The number of possible addresses for the selected prefix length.
10. Click the "Display" button to open a new window that shows all the addresses within the network.
11. The new window titled "IPv6 Addresses" will display a list of all the addresses within the network.
12. Close the main window or enter "exit" as the IPv6 address to exit the program.

## Notes

- The program uses the `ipaddress` module to validate and manipulate IPv6 addresses.
- The program limits the display of addresses to 128 due to the large number of possible addresses for longer prefix lengths.
- The program highlights the parts of the original IPv6 address that fall within the prefix length.
- The program categorizes addresses as multicast, unicast, or anycast based on predefined unicast address ranges.
- The program uses the `tkinter` module for creating the graphical user interface.

