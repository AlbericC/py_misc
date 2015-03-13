# -*- coding: UTF-8 -*-

# ---------------------------------------------------------------------
# Author:      Atrament
# Copyright:   (c) Atrament 2014
# Licence:     CC-BY-SA https://creativecommons.org/licenses/by-sa/4.0/
# ---------------------------------------------------------------------
import queue
from threading import Thread

__author__ = 'Albéric'


class ThreadedWorker():

    def __init__(self,function=None,number_of_threads=8):
        self.queue = queue.Queue()

        def func():
            while True:
                item = self.queue.get()
                if function:
                    function(item)
                else:
                    print(item,"is being processed.")
                self.queue.task_done()

        self.function = func

        for i in range(number_of_threads):
            t = Thread(target=self.function)
            t.daemon = True
            t.start()

    def put(self,object_to_queue):
        self.queue.put(object_to_queue)

    def join(self):
        self.queue.join()


def main():
    import os
    import imghdr
    os.chdir("c:/Users/Albéric/Pictures/sinfest/")

    def file_needs_download(filename):
        test_me = filename
        # print(filename, os.path.getsize(test_me))
        if not os.path.isfile(test_me):
            print("IS NOT FILE :",filename)
            return True
        elif os.path.getsize(test_me) == 0:
            print("WRONG SIZE for", filename)
            return True
        elif imghdr.what(test_me) is None:  # Encoding error...
            print("WRONG FILE STRUCTURE for", filename)
            return True
        elif filename.split(".")[-1] != "gif":
            print(filename, "IS NOT GIF")
        return False

    # Make a worker with this function and run it
    T = ThreadedWorker(function=file_needs_download)
    for file in os.listdir():
        T.put(file)
    T.join()


if __name__ == "__main__":
    main()
    pass
