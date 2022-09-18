# Importing the library
import datetime
import pytest
import psutil
import math

memory = psutil.virtual_memory()[2]
print(memory)

@pytest.mark.cli
def memoryu(memory):
    #here taken CPU % is 90
    if memory <= 90:
        num = 25
        assert math.sqrt(num) == 5
        print ("Testcase passed")
        time = datetime.datetime.now()
        details = memory , time
        with open("pass_result.txt", "w") as f:
            f.write(str(details))
            f.close()
    else:
        with open("fail_result.txt", "w") as f:
            insufficient = "CPU usage is above 90%, testcase failed"
            time = datetime.datetime.now()
            details = insufficient, memory, time
            f.write(str(details))
            f.close()


memoryu(memory)
