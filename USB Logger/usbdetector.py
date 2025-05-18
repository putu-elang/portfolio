import pyudev
import logging

#logger file setup
logging.basicConfig(
    filename='usbdetector.log',
    level=logging.INFO,
    format = "%(asctime)s - %(message)s"
)

#setup the logging function

def log_usb(action, device):
    if action == 'add':
        vendor = device.get("ID_VENDOR", "UnknownVenor")
        model = device.get("ID_MODEL", "UnknownModel")
        serial = device.get("ID_SERIAL_SHORT", "UnknownSerial")
        msg = f"USB device detected: {vendor} {model} with serial code: {serial}"
        logging.info(msg)
        print(msg)

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by('usb')

def usb_callback(action, device):
    log_usb(action, device)

observer = pyudev.MonitorObserver(monitor, usb_callback)
observer.start()

print("USB Logger Active Waiting for USB devices...")

import time
while True:
    time.sleep(1)

        