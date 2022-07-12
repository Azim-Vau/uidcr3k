import os,platform

def run():
    try:
        vau = platform.architecture()[0]
        if vau =="64bit":
            __import__("uidcr3k64").azimvau()
        elif vau =="32bit":
            __import__("uidcr3k32").azimvau()
        else:
            print(" UNKNOWN DEVICE ! ")
    except:
        print(" ERROR! UNKNOWN DEVICE ! ")

if __name__ == '__main__':
    os.system("git pull")
    run()

