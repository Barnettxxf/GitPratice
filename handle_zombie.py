import errno
from multiprocessing import Process, current_process
import logging
import os
import signal
import time


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)-15s - %(levelname)s -%(message)s'
)

logging.info('hello %s', 'my friend')


def run():
    exitcode = 3
    logging.info('exit child process %s', current_process().pid)
    os._exit(exitcode)


def wait_child(signum, frame):
    logging.info('receive SIGCHLD')
    try:
        while True:
            cpid, status = os.waitpid(-1, os.WNOHANG)
            if cpid == 0:
                logging.info('no child process was immediately available')
                break
            exitcode = status >> 8
            logging.info('child process %s exit with exitcode %s', cpid, exitcode)
    except OSError as e:
        if e.errno == errno.ECHILD:
            logging.error('current process has no existing unwaited-for child process.')
        else:
            raise
    logging.info('handle SIGCHID end')


signal.signal(signal.SIGCHLD, wait_child)
p = Process(target=run)
p.start()

while True:
    time.sleep(100)
