# S3_PIPE_05 — Log line pipeline

def parse(lines):
    for line in lines:
        # Example: "INFO: user=42 action=login"
        parts = line.split(":", 1)
        level = parts[0].strip() if parts else ""
        rest = parts[1].strip() if len(parts) > 1 else ""

        data = {"level": level, "raw": line}

        # parse key=value pairs
        for token in rest.split():
            if "=" in token:
                k, v = token.split("=", 1)
                data[k] = v
        yield data

def only_info(entries):
    for e in entries:
        if e.get("level") == "INFO":
            yield e

def extract_user_ids(entries):
    out = []
    for e in entries:
        user = e.get("user")
        try:
            out.append(int(user))
        except Exception:
            pass
    return out


lines = [
    "INFO: user=42 action=login",
    "WARN: user=7 action=fail",
    "INFO: user=100 action=logout",
    "INFO: action=missing_user",
]

ids = extract_user_ids(only_info(parse(lines)))
print(ids)  # [42, 100]
