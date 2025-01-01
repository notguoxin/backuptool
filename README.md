# Backup Script
> [!CAUTION]
> NOT for production use

This project contains a Python script (`redacted.py`) designed for personal use to automate the process of creating backups, compressing them, and sending notifications via Discord.

## Files

- `redacted.py`: A example script created by me.
- `main.py`: Contains helper functions used by `redacted.py`.

## Requirements

- Python 3.x
- `7-Zip` installed and added to the system PATH

## Setup

1. Clone the repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Install the required Python libraries:
    ```sh
    pip install requests
    ```
4. Make sure `7-Zip` is installed and added to your system PATH.
5. Create the necessary files and directories:
    - `/path/to/password.txt`: Contains the password for the backup archive.
    - `/path/to/logs.txt`: Contains logs.
    - `/path/to/info.txt`: Contains backup information.
    - `/path/to/discord_hook.json`: Contains the Discord webhook URL and embed details.
    - `/path/to/discord_hook_failed.json`: Contains the Discord webhook URL and embed details for failure notifications.
    - `/path/to/.ignorefile`: Contains the list of files to ignore.
    - `/path/to/.allowedfile`: Contains the list of files to include.

## Usage

Run the `redacted.py` script to create a backup:
```sh
python redacted.py
```

## Functions

### `redacted.py`

- **Backup Creation**: Creates a backup of the specified files and directories.
- **Compression**: Compresses the backup using `7-Zip` with encryption.
- **Logging**: Updates the log file with the latest backup information.
- **Discord Notification**: Sends a notification to a Discord webhook with the backup details.

### `main.py`

- **create_cli**: Generates the command line string for `7-Zip` based on the ignore and allowed files.
- **save_text**: Sanitizes input text to be safe for Windows file paths.
- **gentoken**: Generates a random token.
- **create_info**: Creates an information file about the backup process and compresses it.

## Notes

- Ensure all paths in the script are correctly set to your local environment.
- The script assumes a certain directory structure and file presence. Adjust the paths as necessary.