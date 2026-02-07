# S1_MC_02 — Command router (match/case)

def run_command(cmd: str):
    match cmd:
        case "start":
            return "STARTED"
        case "stop":
            return "STOPPED"
        case "status":
            return "STATUS_OK"
        case _:
            return "UNKNOWN_COMMAND"


# Tests
tests = ["start", "stop", "status", "restart", "", None]

for t in tests:
    print(repr(t), "->", run_command(t))
