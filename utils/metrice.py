import psutil
import os
import time


class UtilsMethod:

    _process = psutil.Process(os.getpid())

    @staticmethod
    def get_metrices():
        mem_mb = UtilsMethod._process.memory_info().rss / (1024 * 1024)

        cpu_percent = psutil.cpu_percent(interval=None)

        cpu_times = UtilsMethod._process.cpu_times()
        cpu_user_time = cpu_times.user
        cpu_system_time = cpu_times.system

        num_threads = UtilsMethod._process.num_threads()

        ctx_switches = UtilsMethod._process.num_ctx_switches()
        voluntary_ctx = ctx_switches.voluntary
        involuntary_ctx = ctx_switches.involuntary

        disk_io = psutil.disk_io_counters()
        disk_read_mb = disk_io.read_bytes / (1024 * 1024)
        disk_write_mb = disk_io.write_bytes / (1024 * 1024)

        net_io = psutil.net_io_counters()
        net_sent_mb = net_io.bytes_sent / (1024 * 1024)
        net_recv_mb = net_io.bytes_recv / (1024 * 1024)

        open_files = len(UtilsMethod._process.open_files())

        return {
            "timestamp": time.time(),

            "memory_mb": round(mem_mb, 3),
            "cpu_percent": round(cpu_percent, 2),

            "cpu_user_time": round(cpu_user_time, 3),
            "cpu_system_time": round(cpu_system_time, 3),

            "threads": num_threads,

            "voluntary_ctx_switches": voluntary_ctx,
            "involuntary_ctx_switches": involuntary_ctx,

            "disk_read_mb": round(disk_read_mb, 3),
            "disk_write_mb": round(disk_write_mb, 3),

            "net_sent_mb": round(net_sent_mb, 3),
            "net_recv_mb": round(net_recv_mb, 3),

            "open_file_descriptors": open_files
        }
