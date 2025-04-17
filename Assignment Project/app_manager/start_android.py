import os
import subprocess

ANDROID_IMAGE_PATH = "android_x86.iso"

def start_virtual_android():
    command = [
        "qemu-system-x86_64",
        "-cdrom", ANDROID_IMAGE_PATH,
        "-boot", "d",
        "-m", "2048",
        "-enable-kvm"
    ]
    subprocess.run(command)

if __name__ == "__main__":
    print("Launching Virtual Android Environment...")
    start_virtual_android()
