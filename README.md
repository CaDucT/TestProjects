# TestProjects
Implement a program that will launch a specified process and periodically (with a provided time interval) collect the
following data about it:
    • CPU usage (percent);
    • Memory consumption: Working Set and Private Bytes (for Windows systems) or Resident Set Size and Virtual Memory Size (for Linux systems);
    • Number of open handles (for Windows systems) or file descriptors (for Linux systems).
Data collection should be performed all the time the process is running. Path to the executable file for the process
and time interval between data collection iterations should be provided by user. Collected data should be stored on the
disk. Format of stored data should support automated parsing to potentially allow, for example, drawing of charts.
