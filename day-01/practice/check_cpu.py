#Day 1 Task: Check CPU disk and memory usage using Python
# Today’s goal is to write your **first Python script**.

# You will create a Python script that:
# - Takes threshold values (CPU, disk, memory) from **user input**
# - Also fetches system metrics using a Python library (example: `psutil`)
# - Compares metrics against thresholds
# - Prints the result to the **terminal**

# This is your first step towards thinking like a DevOps engineer using Python.

# apko kaam karna hai ki aapko apne system ki CPU usage check karni hai. Aapko ek Python script likhni hai jo aapko aapke system ki current CPU threshold lo
# current Cpu usage pata karo
#agar cpu usage 80% se zyada hai to ek warning message print karo
#agar cpu usage 80% se kam hai to ek message print karo ki CPU usage normal hai
import psutil 
#checking CPU Usage
def check_cpu_threshold():
    cpu_threshold = int(input("Enter the CPU usage threshold:"))
    current_cpu = psutil.cpu_percent(interval=1) # current CPU usage check karna in last 1 second percentage
    print(f"Current CPU usage: {current_cpu}%")
    if current_cpu > cpu_threshold: 
        print("CPU Alert Email sent...")
    else:
        print("CPU usage is normal.")   
check_cpu_threshold()

#Checking Disk Usage
def check_disk_threshold():
    disk_threshold=int(input("Enter the disk usage threshold:"))
    disk_usage=psutil.disk_usage('/').percent # disk usage check karna in percentage
    print(f"Current disk usage: {disk_usage}%")
    if disk_usage > disk_threshold:
        print("Disk Alert Email sent...")
    else:
        print("Disk usage is normal.")
check_disk_threshold()

Checking Memory Usage
def check_memory_threshold():
    memory_threshold=int(input("Enter the memory usage threshold:"))
    memory_usage=psutil.virtual_memory().percent # memory usage check karna in percentage
    print(f"Current memory usage: {memory_usage}%")
    if memory_usage > memory_threshold:
        print("Memory Alert Email sent...")
    else:
        print("Memory usage is normal.")
check_memory_threshold()
