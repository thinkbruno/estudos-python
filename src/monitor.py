import psutil
import time


def get_disk_usage():
    disk_usage = psutil.disk_usage('/')
    return {
        'total': disk_usage.total,
        'used': disk_usage.used,
        'free': disk_usage.free,
        'percent': disk_usage.percent
    }


def get_memory_usage():
    memory_info = psutil.virtual_memory()
    return {
        'total': memory_info.total,
        'available': memory_info.available,
        'used': memory_info.used,
        'percent': memory_info.percent
    }


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def display_usage():
    disk_usage = get_disk_usage()
    memory_usage = get_memory_usage()
    cpu_usage = get_cpu_usage()

    print(f"Uso do Disco: {disk_usage['percent']}%")
    print(f"    Total: {disk_usage['total'] / (1024 ** 3):.2f} GB")
    print(f"    Usado: {disk_usage['used'] / (1024 ** 3):.2f} GB")
    print(f"    Livre: {disk_usage['free'] / (1024 ** 3):.2f} GB\n")

    print(f"Uso da Memória: {memory_usage['percent']}%")
    print(f"    Total: {memory_usage['total'] / (1024 ** 3):.2f} GB")
    print(f"    Usado: {memory_usage['used'] / (1024 ** 3):.2f} GB")
    print(f"    Livre: {memory_usage['available'] / (1024 ** 3):.2f} GB\n")

    print(f"Uso da CPU: {cpu_usage}%\n")


def monitor(interval=5):
    try:
        while True:
            display_usage()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Monitoramento desligado.")


if __name__ == "__main__":
    monitor()