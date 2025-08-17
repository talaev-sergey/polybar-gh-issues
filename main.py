#!/home/user/.local/python-envs/polybar/bin/python
"""
This script checks the number of unread GitHub notifications for a user
and prints an icon with the count, suitable for Polybar integration.

The script uses aiohttp and gidgethub for asynchronous GitHub API access.
It prints different icons in case of network errors or unauthorized access.
"""

import asyncio
import aiohttp
from gidgethub.aiohttp import GitHubAPI
from gidgethub import BadRequest

# GitHub personal access token (keep it secure)
TOKEN = ""
# GitHub username to check notifications for
USER_NAME_GITHUB = ""
# Icon to display in Polybar when showing notifications
ICON_GITHUB = " "


async def get_unread_count():
    """Fetch the number of unread GitHub notifications for the user.

    Connects to the GitHub API asynchronously and counts all notifications
    that are marked as unread.

    Returns:
        int: Number of unread notifications if successful.
        -1: If authentication failed (invalid or expired token).
        -2: If a network-related error occurred.
    """
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, USER_NAME_GITHUB, oauth_token=TOKEN)
        try:
            notifications = await gh.getitem("/notifications")
            return sum(1 for n in notifications if n["unread"])
        except BadRequest as e:
            if e.status_code == 401:
                return -1
        except aiohttp.ClientError:
            return -2


def main():
    """Run the GitHub notification check and print the appropriate icon.

    Uses the get_unread_count coroutine to fetch unread notifications
    and prints:
        - ICON_GITHUB + count if there are unread notifications
        - Special icons for network or authentication errors
        - Just ICON_GITHUB if there are no unread notifications
    """
    count = asyncio.run(get_unread_count())
    if count == -1:
        print(f"{ICON_GITHUB}󰰥")
    elif count == -2:
        print(f"{ICON_GITHUB}")
    elif count > 0:
        print(f"{ICON_GITHUB}{count}")
    else:
        print(ICON_GITHUB)


if __name__ == "__main__":
    main()
