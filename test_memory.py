import pytest
import psutil
import datetime
import math

memory = memory = psutil.virtual_memory()[2]
print(memory)


@pytest.mark.cli
def test_virtual_memory():
    # here taken virtual memory % is 90
    if memory:
        assert memory <= 90
        print("Testcase passed")
        data = "current virtual memory usage in % is:"
        time = datetime.datetime.now()
        details = data, memory, time
        with open("pass_result.txt", "a") as f:
            f.write("\n")
            f.write(str(details))
            f.close()


cpu_usage = psutil.cpu_percent(1)
print(cpu_usage)


@pytest.mark.cli
def test_cpu_usage():
    # here taken cpu usage % is 90 for 4 secs
    if cpu_usage:
        assert cpu_usage <= 90
        print("Testcase passed")
        data = "current CPU usage in % is:"
        time = datetime.datetime.now()
        details = data, cpu_usage, time
        with open("pass_result.txt", "a") as f:
            f.write("\n")
            f.write(str(details))
            f.close()
