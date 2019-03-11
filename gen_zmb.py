from multiprocessing import Process, current_process
import logging
import os
import time

print(os.getcwd())
print(os.path.abspath(__file__))

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)-15s - %(levelname)s -%(message)s'
)


def run():
    logging.info('exit child process %s', current_process().pid)
    os._exit(3)


p = Process(target=run)
p.start()
time.sleep(100)
