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
        raise ValueError("Path not provided")

    path = Path(data["path"])
    if not path.exists():
        print(json.dumps({"error": "file doesn't exist"}))
        return

    content = path.read_text("utf-8")
    print(json.dumps({"content": content}))


if __name__ == "__main__":
    run()
