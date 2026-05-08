INPUT_FILE = "ads.txt"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    lines = [
        line.strip()
        for line in f
        if line.strip() and not line.strip().startswith("#")
    ]

# remove duplicates + sort alphabetically
lines = sorted(set(lines), key=str.lower)

with open(INPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Sorted {len(lines)} rules")
