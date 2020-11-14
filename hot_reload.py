import time
import logging
import sys
from hotreload import Loader


if __name__ == "__main__":
    script = Loader("main.py")

    while True:
        # if script has been modified since last poll
        if script.has_changed():
            try:
                # excecute function from script
                script.main()
            except Exception as e:
                # catch all exceptions
                print('Error: {}'.format(e))

        time.sleep(1)
