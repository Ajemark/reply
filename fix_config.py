with open("/data/.zeroclaw/config.toml", "r") as f:
    lines = f.readlines()

filtered = []
for line in lines:
    if line.startswith(r"\n[autonomy]"):
        break
    filtered.append(line)

with open("/data/.zeroclaw/config.toml", "w") as f:
    f.writelines(filtered)
    f.write("\n[autonomy]\n")
    f.write('level = "supervised"\n')
    f.write('workspace_only = true\n')
    f.write('allowed_commands = ["git", "npm", "cargo", "ls", "cat", "grep", "find", "echo", "pwd", "wc", "head", "tail", "date"]\n')
    f.write('forbidden_paths = ["/etc", "/root", "/home", "/usr", "/bin", "/sbin", "/lib", "/opt", "/boot", "/dev", "/proc", "/sys", "/var", "/tmp", "~/.ssh", "~/.gnupg", "~/.aws", "~/.config"]\n')
    f.write('max_actions_per_hour = 1000\n')
    f.write('max_cost_per_day_cents = 500\n')
    f.write('require_approval_for_medium_risk = true\n')
    f.write('block_high_risk_commands = true\n')
