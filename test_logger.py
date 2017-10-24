# test_logger.py (infectorSimulation)

import pytest
from logger import Logger

def test_write_log_survival():
    test_log = Logger("test.log")
    test_log.write_log_survival("person", True)
    file = open("./test.log", "r")
    test_complete = file.readline(2)
    file.close()

    print(test_complete)