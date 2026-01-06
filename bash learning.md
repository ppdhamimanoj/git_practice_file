**BASH**
*Introduction*
- used to write a command & write a scripts
- default shell in macos and linux

History
    Bash was developed in 1989 by Brian Fox.
**Practical Uses of Bash**
    <!-- System administrators use Bash to: -->
    - Automate tasks
    - System operations
    - Process data
    <!-- Developers use Bash for: -->
    - Build automation
    - Testing
    - Deployment
    - Data processing and manipulation

# To check version of bash ` bash --version`
# To install `sudo apt-get install bash`

**Basic Commands**
# `ls` - list the directory contents
# `cd` - change the directory
# `pwd` - print the current working directory
# `echo` - disply the line of text
# `cat` - concatinate and display the files
# `cp` - copy files and directories
# `mv` - moves or rename files and directories 
# `rm` - deletes files or folders
# `touch` - create a empty file and update its time 
# `mkdir` - create a new folder

**`ls` Command details**
    -l -> Long listing format
    -a -> Include hidden files
    -h -> Human-readable sizes
    -t -> Sort by modification time
    -r -> Reverse order while sorting
    -R -> List subdirectories recursively
    -S -> Sort by file size
    -1 -> List one file per line
    -d -> List directories themselves, not their contents
    -F -> Append indicator (one of */=@|) to entries

**`cd` command details**
  - `cd ..`: Move up one directory level
  - `cd ~` : Change to the home directory
  - `cd -` : Switch to the previous directory
  - `cd /` : Change to the root directory

**`pwd` print working directory basic details**
 - `-L`: Display the logical current working directory
 - `-P`: Display the physical current working directory (without symbolic links)

**`echo` command basic details**
# Basic command syntax : `echo "message"`
 - `-n` - Don't add a new line at the end
 - `-e` - Allow special characters like \n for new lines
 - `-E` - Don't allow special characters (default)

**`cat` command details**
 - `-n` - Add numbers to each line
 - `-b` - Add numbers only to lines with text
 - `-s` - Remove extra empty lines
 - `-v` - Show non-printing characters (except for tabs and end of line)

**`cp` command details**
 - `-r` - Copy all files and folders inside a directory
 - `-i` - Ask before replacing files
 - `-u` - Copy only if the source is newer
 - `-v` - Verbose mode, show files being copied

**`mv` command details**
 - `-i` - Ask before replacing files
 - `-u` - Move only if the source is newer
 - `-v` - Verbose mode, show files being moved

**`rm` command details**
 - `-r` - Delete a folder and everything inside it
 - `-i` - Ask before deleting each file
 - `-f` - Force delete without asking
 - `-v` - Verbose mode, show files being removed

**`touch` command details**
 - `-a` - Update only when the file was last read
 - `-m` - Update only when the file was last changed
 - `-t` - Set the timestamp to a specific time
 - `-c` - Do not create any files

**`mkdir` command details**
 - `-p` - Create parent directories as needed
 - `-v` - Show a message for each created directory
 - `-m` - Set file mode (permissions)

# `man` command ->The man command is used to display the user manual of any command that can be run on the terminal.
    eg `man ls`

# `alias` Aliases in Bash allow you to create shortcuts for long or frequently used commands
    eg.. `alias gs='git status'

## Text processing commands
1. The `grep` command is used to search for text patterns within files.
   - Syntax `grep 'pattern' filename`
    `-i` - Search ignoring case differences (uppercase or lowercase)
    `-r` - Search through all files in a directory and its subdirectories
    `-v` - Find lines that do not match the pattern

2. The `awk` command is used for pattern scanning and processing language.
   - Syntax `awk -F"," '{print $1}' filename`
    `-F` - Set what separates the data fields
    `-v` - Set a variable to be used in the script
    `-f` - Use a file as the source of the awk program

3. The `sed` command is a stream editor used to perform basic text transformations on an input      stream (a file or input from a pipeline).
   - Syntax `sed 's/old/new/' filename`
    `-i` - Edit files directly without needing to save separately
    `-e` - Add the script to the commands to be executed
    `-n` - Don't automatically print lines
    `-r` - Use extended regular expressions
    `-f` - Add script from a file
    `-l` - Specify line length for l command

4. The `sort` command is used to sort lines of text files.
    - Syntax `sort filename`
    `-r` - Sort in reverse order
    `-n` - Sort numbers correctly
    `-k` - Sort by a specific column
    `-u` - Remove duplicate lines
    `-t` - Specify a delimiter for fields

5. The `tail` command is used to display the last part of files.
 - Syntax `tail [OPTION]... [FILE]...`
 - `-n` [number]: Display the last [number] lines of the file.
 - `-f`: Follow the file as it grows, useful for monitoring log files.
 - `-c [number]`: Display the last [number] bytes of the file.
 - `--pid=[pid]`: Terminate after the process with the given PID dies.
 - `--retry`: Keep trying to open a file even if it is inaccessible.

6. The `head` command is used to display the first part of files.
 - `-n [number]`: Display the first [number] lines of the file.
 - `-c [number]`: Display the first [number] bytes of the file.

**System Processing commands**
1. `ps` command
   -  The `ps` command is used to report a snapshot of current processes.
   - It's a useful tool for monitoring and managing processes on your system.
   # options 
    `-e` - Show all processes
    `-f` - Show detailed information
    `-u` - Show processes for a specific user
    `-a` - Show all processes with a terminal
    `-x` - Show processes without a terminal
2. `top` command
    - The `top` command is used to display Linux tasks.
    - It's a powerful tool for monitoring system performance in real-time.
    <!-- The top command output consists of several columns, each representing different aspects of the system's processes:
    # PID: Process ID, a unique identifier for each process.
    # USER: The user account that owns the process.
    # PR: Priority of the process.
    # NI: Nice value, which affects scheduling priority.
    # VIRT: Virtual memory size used by the process.
    # RES: Resident memory size, the non-swapped physical memory the process uses.
    # SHR: Shared memory size.
    # S: Process status (e.g., S for sleeping, R for running).
    # %CPU: CPU usage percentage.
    # %MEM: Memory usage percentage.
    # TIME+: Total CPU time the process has used since it started.
    # COMMAND: The command that started the process. -->
    # options 
    `-d` - Set the time between updates
    `-p` - Monitor specific PIDs
    `-u` - Show tasks for a specific user
    `-n` - Set the number of iterations
    `-b` - Batch mode operation

3. `df` command
    - The df command is used to report file system disk space usage.
    - It's a useful tool for checking available storage on your system.
      The df command output consists of several columns, each representing different aspects of the file system's disk usage:
    a. Filesystem: The name of the file system.
    b. 1K-blocks: Total size of the file system in 1K blocks.
    c. Used: Amount of space used.
    d. Available: Amount of space available for use.
    e. Use%: Percentage of space used.
    f. Mounted on: Directory where the file system is mounted.
    # options
    `-h` - Show sizes in human-readable format (e.g., KB, MB)
    `-a` - Show all file systems, even empty ones
    `-T` - Show the type of file system
    `-i` - Show inode usage
    `-P` - Use POSIX output format

4. `du` command
- The du command is used to estimate file space usage.
- It's helpful for finding out how much space files and directories take up.
# options
    `-h` - Show sizes in human-readable format (e.g., KB, MB)
    `-s` - Show only the total size for each item
    `-a` - Show sizes for all files, not just directories
    `-c` - Produce a grand total
    `--max-depth=N` - Limit the depth of directory traversal

5. `free` command
- The free command is used to display the amount of free and used memory in the system.
- It's useful for monitoring memory usage and managing system resources.
# options
    `-h` - Show memory in human-readable format (e.g., KB, MB, GB)
    `-b` - Show memory in bytes
    `-k` - Show memory in kilobytes (KB)
    `-m` - Show memory in megabytes (MB)
    `-g` - Show memory in gigabytes (GB)
    `-s` [interval] - Continuously display memory usage at specified intervals
    `-t` - Display total memory

6. `kill` command
    The kill command is commonly used to:
    a. Terminate unresponsive processes.
    b. Manage system resources by stopping unnecessary processes.
    c. Send specific signals to processes for custom handling.
    # options   
    `-9`: Forcefully terminate a process.
    `-l`: List all signal names.
    `-s [signal]`: Specify a signal to send.
    `-p`: Print the process ID.
7. `uptime` command
   -  this command displays information like the current time, uptime duration, number of users, and load averages.
