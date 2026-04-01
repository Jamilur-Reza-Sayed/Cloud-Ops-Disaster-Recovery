# Incident Response Playbook: Infrastructure Recovery
## Scenario 1: Disk Exhaustion (Critical)
**Symptoms:** Website returns 500 errors; Database fails to start; SSH login is slow.
**Diagnostic Steps:**
1. Run `df -h` to identify which partition is at 100%.
2. Run `du -sh /*` to find the largest directories (usually `/var/log`).
**Resolution:**
1. Clear old logs or temporary files: `sudo rm -rf /tmp/*`.
2. Online Volume Expansion: Increase the Elastic Volume Service (EVS) size in the Cloud Console.
3. Rescan the partition: `sudo resize2fs /dev/vda1`.
## Scenario 2: Linux Kernel Panic (Fatal)
**Symptoms:** Instance status is "Running" but the console shows a "Kernel Panic" error.
**Diagnostic Steps:**
1. Check the Serial Console logs in the Cloud Dashboard.
2. Identify if the cause is a recent driver update or memory corruption.
**Resolution:**
1. Attempt a "Soft Reboot" from the console.
2. If persistent, perform a **Cloud Backup Recovery (CBR)** to restore the instance to the last healthy snapshot (e.g., from 24 hours ago).
