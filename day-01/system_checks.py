import psutil   # Import psutil library to fetch system metrics (CPU, Disk, Memory)
def threshold_check():   # Define a function to check system thresholds

    # Take user input for threshold values and convert them to float (decimal)
    user_cpu_threshold= float(input("Enter CPU threshold value (%): "))    
    user_disk_threshold = float(input("Enter Disk threshold (%): "))
    user_memory_threshold = float(input("Enter Memory threshold(%) : "))

    # Fetch current system metrics
    cpu_threshold= psutil.cpu_percent(interval=1)    # CPU usage % over 1 second
    disk_threshold = psutil.disk_usage('/').percent    # Disk usage % of root directory
    memory_threshold = psutil.virtual_memory().percent  # RAM usage %

  # Print table headert
  print("\n\t\tYour Metric (%)\t\tSystem Metric (%)")

    # Print user-defined thresholds vs actual system values
    print("CPU\t\t", f"{user_cpu_threshold}%", "\t\t\t", f"{cpu_threshold}%")
    print("Disk\t\t", f"{user_disk_threshold}%", "\t\t\t", f"{disk_threshold}%")
    print("Memory\t\t", f"{user_memory_threshold}%", "\t\t\t", f"{memory_threshold}%")

    # Compare CPU usage with threshold
    if cpu_threshold  > user_cpu_threshold:
        print("CPU usage exceeds threshold")     # Alert if exceeded
    else:
        print("CPU usage is within threshold")   # Safe
    
    # Compare Disk usage with threshold  
    if disk_threshold  > user_disk_threshold:
        print("Disk usage exceeds threshold")
    else:
        print("Disk usage is within threshold")

    # Compare Memory usage with threshold
    if memory_threshold > user_memory_threshold:
        print("Memory usage exceeds threshold")
    else:
        print("Memory usage is within threshold")

# Call the function to execute the program
threshold_check()
