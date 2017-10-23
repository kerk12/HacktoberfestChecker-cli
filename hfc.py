try:
    import requests
except ImportError:
    print("You're missing requests module. Please install it using pip")
    exit(1)
    #This checks for module error either it is present or not in the package
except Exception:
    print("An exception has occured while importing the requests module.")
    exit(1)
    #This prints error when an module import error occurs

#Function implementation for pull request
class PullRequest:
    def __init__(self, title, url, repo, number, created_at):
        self.title = title
        self.url = url
        self.repo = repo
        self.created_at = created_at  # TODO Might do something with it later
        self.number = number

    def __str__(self):
        output = ""
        output += '{} (#{}) -> {}'.format(self.title, self.number,self.url)
        return output

if __name__ == "__main__":
    print("""Hacktoberfest Checker CLI
Developed by Kyriakos Giannakis
https://github.com/kerk12

Licenced under GNU/GPLv3

""")
    gh_name = ""
    while gh_name == "":
        gh_name = input("Please enter your github username: ")

    req = requests.get("https://api.github.com/search/issues?q=author:{}%20type:pr%20created:%3E2017-09-30%20created:%3C2017-11-01".format(gh_name))

    json_out = req.json()
    if "errors" in json_out:
        print("The username you typed does not exist or you don't have access to view this user's profile.")
        exit(1)
    prs = []
    pr_count = json_out["total_count"]

    if pr_count > 0:
        for item in json_out["items"]:
            pr = PullRequest(title=item["title"],
                             url=item["url"],
                             number=item["number"],
                             repo=item["repository_url"],
                             created_at=item["created_at"])
            prs.append(pr)
    else:
        print("0/0\nNo pull requests yet.")
        exit(0)

    print("You have completed {}/4 pull requests:\n".format(pr_count))
    for pr in prs:
        print(pr)

    if pr_count >= 4:
        print("\nCongratulations! You have completed the Hacktoberfest challenge!")

    exit(0)
