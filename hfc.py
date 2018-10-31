
try:
    """Trying to import requests module,if any from the client's python library."""
    import requests
except ImportError:
    print("You're missing requests module. Please install it using pip")
    exit(1)
except Exception:
    print("An exception has occured while importing the requests module.")
    exit(1)

class PullRequest:
    """Class definition for PullRequest Objects. """
    def __init__(self, title, url, repo, number, created_at):
        """Constructor for PullRequest. """
        self.title = title
        self.url = url.replace("https://api.", "https://")
        self.url = self.url.replace("/repos", "") 
        self.repo = repo
        self.created_at = created_at  # TODO Might do something with it later
        self.number = number


    def __str__(self):
        """Method to return the instance variables in the below format whenever we use print(an_object_of_PullRequest). """
        output = ""
        output += '{} (#{}) ─> {}'.format(self.title, self.number,self.url)
        return output


def get_url(username):
    """ Forms the API request url. """
    return "https://api.github.com/search/issues?q=author:{}%20type:pr%20created:%3E2018-09-30".format(username)


def check_if_user_not_exists(json):
    """ Determines if the user exists via the message produced. """
    return ("errors" in json and json["errors"][0]["message"] == "The listed users cannot be searched either because the users do not exist or you do not have permission to view the users.")


if __name__ == "__main__":
    print("""Hacktoberfest Checker CLI
Developed by Kyriakos Giannakis
https://github.com/kerk12

Licenced under GNU/GPLv3

""")
    gh_name = ""
    while gh_name == "":
        gh_name = input("Please enter your github username: ")

    try:
        # Make request to github api
        req = requests.get(get_url(gh_name))

    except requests.RequestException:
        print('\nERROR CONNECTING TO THE INTERNET\n')
        exit(1)

    # Get a json from the request
    json_out = req.json()
    if check_if_user_not_exists(json_out):
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
        print("0/5\nNo pull requests yet.")
        exit(0)

    print("You have completed {}/5 pull requests:\n".format(pr_count))
    for pr in prs:
        print(pr)
        
    # If the number of pull request that you have is equals or less than 5 the profile don't have completed the challenge
    if pr_count >= 5:
        print("\nCongratulations! You have completed the Hacktoberfest challenge!")
    
    exit(0)
