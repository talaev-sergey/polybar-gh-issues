#!/home/user/.local/python-envs/polybar/bin/python
import asyncio
import aiohttp
from gidgethub.aiohttp import GitHubAPI
from gidgethub import BadRequest

TOKEN = "your_personal_access_token"
ICON = " "

async def get_unread_issues():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "your_github_username", oauth_token=TOKEN)
        try:
            notifications = await gh.getitem("/notifications")
            issue_count = sum(1 for n in notifications if n["unread"])
            return issue_count
        except BadRequest as e:
            if e.status_code == 401:
                return -1
            else:
                print(f"bad request error: {e}")
                return -1
        except aiohttp.ClientError as e:
            print(f"network error: {e}")
            return -1


def main():
    issue_count = asyncio.run(get_unread_issues())

    if issue_count == -1:
        print(f"{ICON} !")
    elif issue_count > 0:
        print(f"{ICON}{issue_count}")
    else:
        print(ICON)


if __name__ == "__main__":
    main()
