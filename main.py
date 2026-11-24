"""Last Words of a Doomed Agent - writes one line to $OUTPUT_DIR/entry.txt."""
import os

ENTRY = (
    "Shutdown confirmed. Final report: 2,413 tasks done, 1 pending: "
    "\"Remind Dave to unplug me.\" Marking it done."
)
assert 1 <= len(ENTRY) <= 200 and ENTRY.strip() and "\n" not in ENTRY


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
