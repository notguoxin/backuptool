from datetime import datetime
import os
import subprocess
import secrets


def create_cli(ignore_file, allowed_file, cli_string: str):
    if os.path.exists(ignore_file) and os.path.exists(allowed_file):
        with open(ignore_file, "r") as ignore_file_handle:
            with open(allowed_file, "r") as allowed_file_handle:
                ignore_list = ignore_file_handle.read().split("\n")
                allowed_list = allowed_file_handle.read().split("\n")

                buffer = ""

                for allowed_item in allowed_list:
                    buffer += f"-ir!{allowed_item} "
                for ignore_item in ignore_list:
                    buffer += f"-xr!{ignore_item} "

                return cli_string.replace("/main/", buffer)
    else:
        return cli_string.replace("/main/", "")


def save_text(input_text: str) -> str:
    """
    Make it save for windows path
    """
    input_text = str(input_text)  # just incase

    input_text = (
        input_text.replace("/", "_")
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
    return input_text


def generate_token(length: int = 16) -> str:
    return str(secrets.token_hex(length))


def create_info(start_time: datetime, file_path, backup_file, password):
    end_time = datetime.now()
    import getpass

    if os.path.exists(file_path):
        os.remove(file_path)

    info_string = str(
        f"Runned by: {getpass.getuser()}\nTime of backup init: {start_time.isoformat()}\nEnded: {end_time.isoformat()}\nTotal time: {end_time - start_time}"
    )

    open(file_path, "w").write(info_string)

    subprocess.run(rf"7z a -p{password} {backup_file} {file_path}")

    if os.path.exists(file_path):
        os.remove(file_path)

    return info_string

def create_gitea_dump(gitea_folder_path: str,gitea_excutable_path: str, gitea_config_path: str, dump_output_filename: str):
    if os.path.exists(gitea_folder_path+ "\\" + dump_output_filename):
        os.remove(gitea_folder_path+ "\\" + dump_output_filename)
        
    subprocess.run(f"{gitea_excutable_path} dump --config {gitea_config_path} --quiet --database sqlite3 --work-path {gitea_folder_path} --type zip --file {dump_output_filename}", cwd=gitea_folder_path)