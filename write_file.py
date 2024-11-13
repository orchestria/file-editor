# /// script
# requires-python = "~=3.12"
# ///

import json
import sys
from pathlib import Path


def run():
    args = sys.argv[-1]
    data = json.loads(args)
    if "path" not in data:
        raise ValueError("path not provided")
    if "content" not in data:
        raise ValueError("content not provided")

    path = Path(data["path"])
    content = data["content"]

    if not path.exists():
        path.touch()

    path.write_text(content, "utf-8")

    print(json.dumps({"status": "success"}))


if __name__ == "__main__":
    run()
