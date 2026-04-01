import os
import shutil

def check_disk_usage(path="/"):
                  """Monitors disk space and alerts if usage is above 85%."""
    total, used, free = shutil.disk_usage(path)
    percent_used = (used / total) * 100
    if percent_used > 85:
        print(f"ALERT: Disk usage is at {percent_used:.2f}%! Action required.")
    else:
        print(f"System Healthy: Disk usage at {percent_used:.2f}%.")
if __name__ == "__main__":
    check_disk_usage()
