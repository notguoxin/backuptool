from datetime import datetime
import time
from main import create_cli, save_text, create_info
import subprocess
import os
import json
import requests

try:
    cdatetime = datetime.now()
    bkfoldername = f"BK-{save_text(cdatetime.strftime('%d-%m-%Y'))}"
    passwd = open(
        r"/path/to/password.txt",
        "r",
        encoding="utf-8",
    ).read()
    clistr = rf'7z a -spf -mx9 -md128m -ms16g -mhe -p{passwd} "/path/to/backups/{bkfoldername}/backup.7z" /main/ '
    logs = str(open(r"/path/to/logs.txt", "r").read()).replace("$LATEST|", "")
    info_file = r"/path/to/info.txt"

    open(r"/path/to/k.txt", "w").write(f"$LATEST|{bkfoldername}/n------/n" + logs)

    backups = os.listdir(r"/path/to/backups")

    if len(backups) >= 150:
        print("WARN: Too many backups")

    subprocess.run("schtasks /End /TN Autorun")
    time.sleep(1)
    subprocess.run(
        create_cli(
            r"/path/to/.ignorefile",
            r"/path/to/.allowedfile",
            clistr,
        ),
    )

    info = create_info(
        cdatetime, info_file, rf'"/path/to/backups/{bkfoldername}/backup.7z"', passwd
    )
    subprocess.run("schtasks /Run /TN Autorun")

    dc_webhook = json.loads(
        open(
            r"/path/to/discord_hook.json"
        ).read()
    )
    for id in dc_webhook["embeds"]:
        if id["id"] == 131227103:
            for fields in id["fields"]:
                if fields["value"] == "{allowedfileread}":
                    fields["value"] = str(
                        open(
                            r"/path/to/.allowedfile"
                        ).read()
                    ).replace("name", "\\???")

                if fields["value"] == "{ignoredfileread}":
                    fields["value"] = (
                        str(
                            open(
                                r"/path/to/.ignorefile"
                            ).read()
                        )
                        .replace("name", "\\???")
                        .replace(
                            r"/path/to/password.txt",
                            "",
                        )
                    )

        if id["id"] == 10674342:
            id["description"] = info.replace("name", "")

    requests.post(
        "https://discord.com/api/webhooks/REDACTED",
        json=dc_webhook,
    )

except Exception as e:
    dc_webhook = json.loads(
        open(
            r"/path/to/discord_hook_failed.json"
        ).read()
    )
    for id in dc_webhook["embeds"]:
        if id["description"] == "{info}":
            id["description"] = (
                f"Failed at time: {datetime.now().isoformat()}./nError: {e}"
            )

    requests.post(
        "https://discord.com/api/webhooks/REDACTED",
        json=dc_webhook,
    )
    
    
    