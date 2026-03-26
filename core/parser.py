def parse_irc_message(raw):
    lines = raw.split("\r\n")
    parsed = []

    for line in lines:
        if not line:
            continue

        prefix = None
        trailing = None

        if line.startswith(":"):
            prefix, line = line[1:].split(" ", 1)

        if " :" in line:
            line, trailing = line.split(" :", 1)

        parts = line.split()

        command = parts[0]
        params = parts[1:]

        parsed.append({
            "prefix": prefix,
            "command": command,
            "params": params,
            "trailing": trailing
        })

    return parsed