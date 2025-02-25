import subprocess
import time

NIOS_CMD_SHELL_BAT = "C:/intelFPGA_lite/18.1/nios2eds/Nios II Command Shell.bat"

def send_on_jtag(cmd):
    # check if atleast one character is being sent down
    assert (len(cmd) >= 1), "Please make the cmd a single character"

    # create a subprocess which will run the nios2-terminal
    process = subprocess.Popen(
        NIOS_CMD_SHELL_BAT,
        bufsize=0,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )

    # send the cmd string to the nios2-terminal, read the output and terminate the process
    try:
        vals, err = process.communicate(
            ("nios2-terminal <<< {}".format(cmd), "utf-8")
        )
        process.terminate()
    except subprocess.TimeoutExpired:
        vals = "Failed"
        process.terminate()
    return vals

def main():
    while True:
        mode = input("Enter Mode (0 = no filtering, 1 = filtering, q = quit): ")
        if mode == 'q':
            break
        elif mode in ['0', '1']:
            response = send_on_jtag(mode)
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
