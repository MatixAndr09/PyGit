import subprocess
import platform
import ctypes
import sys
import os


def is_admin():
    os_name = platform.system()
    if os_name == "Windows":
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    elif os_name in ["Linux", "Darwin"]:
        return os.geteuid() == 0
    else:
        return False


def init():
    print("[*]  This is init script please wait...")
    if not is_admin():
        print("[-]  If you runing this for the first time run this as administrator/root. If not ignore this message.")
        return

    check = subprocess.run("git --version", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    os_name = platform.system()
    if check.returncode != 0:
        print("[-]  Git is not installed...")
        if os_name == "Windows":
            print("[*]  Installing git...")
            subprocess.run(f"winget install --id Git.Git -e --source winget", shell=True, stdout=subprocess.PIPE)
        elif os_name == "Linux":
            print("[*]  Installing git...")
            subprocess.run("sudo apt-get update", shell=True)
            subprocess.run("sudo apt-get install git", shell=True)
        elif os_name == "Darwin":
            print("[*]  Installing git...")
            subprocess.run("brew install git", shell=True)
    else:
        print(f"[+]  Git is installed (version: {check.stdout.decode('utf-8').strip()})")

    print("[*]  Checking python and libs...")

    pyver = platform.python_version()
    print(f"[+]  Python version: {pyver}")
    if pyver[0] != "3":
        print("[-]  Python version is not 3.x.x")
        print("[-]  Please install python 3.x.x")
        exit(1)

    libs = ["rich", "textual", "requests"]
    for lib in libs:
        check = subprocess.run(f"pip show {lib}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if check.returncode != 0:
            print(f"[-]  {lib} is not installed...")
            print(f"[*]  Installing {lib}...")
            subprocess.run(f"pip install {lib}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            version_line = next(
                line for line in check.stdout.decode('utf-8').split('\n') if line.startswith("Version:")
            )
            version = version_line.split(":")[1].strip()
            print(f"[+]  {lib} is installed (version: {version})")

    print("[+]  Init script finished...")
    print("[*]  Starting the application & clearing terminal...")
    if os_name == "Windows":
        os.system("cls")
    elif os_name in ["Linux", "Darwin"]:
        os.system("clear")

    return