import random

def generate_mac_address():
    # List of common OUIs (first 3 bytes of MAC address)
    common_ouis = ['00:1A:79', '00:15:5D', '00:0C:29', '00:50:56', '00:15:5D']

    # Choose a random OUI from the list
    selected_oui = random.choice(common_ouis)

    # Generate the last 3 bytes (6 hexadecimal characters) of the MAC address
    device_id = [random.randint(0x00, 0xff) for _ in range(3)]

    # Format the device ID into the MAC address format
    device_id_formatted = ':'.join(f'{part:02x}' for part in device_id)

    # Combine the OUI and device ID to form the MAC address
    mac_address = selected_oui + ':' + device_id_formatted

    return mac_address
