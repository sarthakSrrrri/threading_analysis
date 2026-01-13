import psutil
import os
import time


class UtilsMethod:

    _process = psutil.Process(os.getpid())

    @staticmethod
    def get_metrices():
        mem_mb = UtilsMethod._process.memory_info().rss / (1024 * 1024)

        cpu_percent = psutil.cpu_percent(interval=None)

        num_threads = UtilsMethod._process.num_threads()

        disk_io = psutil.disk_io_counters()
        disk_read_mb = disk_io.read_bytes / (1024 * 1024)
        disk_write_mb = disk_io.write_bytes / (1024 * 1024)

        return {
            "memory_mb": round(mem_mb, 3),
            "cpu_percent": round(cpu_percent, 2),
            "threads": num_threads,
            "disk_read_mb": round(disk_read_mb, 3),
            "disk_write_mb": round(disk_write_mb, 3)
        }
