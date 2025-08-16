# GitHub Issue Notifier for Polybar

![Python](https://img.shields.io/badge/python-3.13-blue?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/github-api-black?logo=github)
![License](https://img.shields.io/badge/license-MIT-green)

A simple **Python script** to display your **unread GitHub issues** directly in [**Polybar**](https://wiki.archlinux.org/title/Polybar).

![Description](assets/screenshot.png)


## Features

- Shows the number of unread GitHub issues.
- Displays a warning icon if authentication fails or a network error occurs.
- Fully compatible with Polybar.

---

## Requirements

This project uses the following Python libraries:

[aiohttp](https://pypi.org/project/aiohttp/) — asynchronous HTTP client for making API requests.

[gidgethub](https://pypi.org/project/gidgethub/) — GitHub API client built on top of aiohttp.

---
## Installation

1. **Create a Python virtual environment** (if not already created):

```bash
mkdir -p ~/.local/python-envs/polybar
python3 -m venv ~/.local/python-envs/polybar
source ~/.local/python-envs/polybar/bin/activate
pip install aiohttp gidgethub
```

2. **Clone or download** this script to your system:

```bash
~/.config/polybar/scripts/github_issues.py
```

3. **Make it executable**:

```bash
chmod +x ~/.config/polybar/scripts/github_issues.py
```

---

## Polybar Configuration

Add the following module to your `~/.config/polybar/modules.ini`:

```ini
[module/github_issues]
type = custom/script
exec = ~/.config/polybar/scripts/github_issues.py
interval = 60
```
and add module to `~/.config/polybar/config.ini`:

```ini
module-left= ...
module-center= github_issues
module-right= ...
```
---

## Configuration

Before using, edit the script to add your GitHub **personal access token** and **username**:

```python
TOKEN = "your_personal_access_token"
gh = GitHubAPI(session, "your_github_username", oauth_token=TOKEN)
```

- **TOKEN**: Generate a GitHub personal access token with `notifications` scope: [GitHub Token](https://github.com/settings/tokens)
- **USERNAME**: Your GitHub username.

---

## Usage

- After configuring Polybar, your bar will show:
  - `` → no unread issues.
  - ` <number>` → number of unread issues.
  - ` !` → error in authentication or network issue.

---

## Notes

- Ensure your virtual environment Python path matches the shebang at the top of the script:

```python
#!/home/user/.local/python-envs/polybar/bin/python
```

- This script requires **Python 3.13+**.

---

## License

This project is licensed under the MIT License.

