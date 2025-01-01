from datetime import datetime
import os
import subprocess
import secrets


def create_cli(ignorefile, allowedfile, cli_string: str):
    if os.path.exists(ignorefile) and os.path.exists(allowedfile):
        with open(ignorefile, "r") as igfile:
            with open(allowedfile, "r") as afile:
                file = igfile.read().split("\n")
                fileb = afile.read().split("\n")

                buffer = ""

                for a in fileb:
                    buffer += f"-ir!{a} "
                for b in file:
                    buffer += f"-xr!{b} "

                return cli_string.replace("/main/", buffer)
    else:
        return cli_string.replace("/main/", "")


def save_text(input: str) -> str:
    """
    Make it save for windows path
    """
    input = str(input)  # just incase

    input = (
        input.replace("/", "_")
        .replace("\\", "_")
        .replace(":", "_")
        .replace("*", "_")
        .replace("?", "_")
        .replace("'", "_")
        .replace("<", "_")
        .replace(">", "_")
        .replace("|", "_")
        .replace(" ", "-")
    )
    return input


def gentoken(length: int = 16) -> str:
    return str(secrets.token_hex(length))


def create_info(dt: datetime, file_path, backupfile, password):
    ended = datetime.now()
    import getpass

    if os.path.exists(file_path):
        os.remove(file_path)

    string = str(
        f"Runned by: {getpass.getuser()}\nTime of backup init: {dt.isoformat()}\nEnded: {ended.isoformat()}\nTotal time: {ended - dt}"
    )

    open(file_path,"w").write(string)

    subprocess.run(
        rf"7z a -p{password} {backupfile} {file_path}"
    )

    if os.path.exists(file_path):
        os.remove(file_path)
        
    return string