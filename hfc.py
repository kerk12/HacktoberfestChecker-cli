import requests

class PullRequest:
	
	# Constructor and initialization of instance variables
    def __init__(self, title, url, repo, number, created_at):
        self.title = title
        self.url = url
        self.repo = repo
        self.created_at = created_at  # TODO Might do something with it later
        self.number = number

	# Overloading the string representation of the object
    def __str__(self):
        output = ""
        output += '{} (#{}) -> {}'.format(self.title, self.number,self.url)
        return output

# Check if the file is called as an executable
if __name__ == "__main__":
    print("""Hacktoberfest Checker CLI
Developed by Kyriakos Giannakis
https://github.com/kerk12
    
Licenced under GNU/GPLv3
    
""")

	# Github Username
    gh_name = input("Please enter your github username: ")

	# Request object holding PR data from the github API
    req = requests.get("https://api.github.com/search/issues?q=author:{}%20type:pr%20created:%3E2017-09-30%20created:%3C2017-11-01".format(gh_name))

    json_out = req.json()  # Converts values in req variable to json representation
	
	# Check for errors in variable json_out
    if "errors" in json_out:
        print("The username you typed does not exist or you don't have access to view this user's profile.")
        exit(1)
    prs = []
    pr_count = json_out["total_count"]  # Get the number of PRs submitted by the user

	# Checks the number of pull requests and stores them as objects
    if pr_count > 0:
        for item in json_out["items"]:
            pr = PullRequest(title=item["title"],
                             url=item["url"],
                             number=item["number"],
                             repo=item["repository_url"],
                             created_at=item["created_at"])
            prs.append(pr)  # Adds object that holds pull request data to end of list
    else:
        print("0/0\nNo pull requests yet.")
        exit(0)

    print("You have completed {}/4 pull requests:\n".format(pr_count))
	
	# Prints out whats stored in the list
    for pr in prs:
        print(pr)

	# Checks if the number of pull request are enough to have completed the challenge
    if pr_count >= 4:
        print("\nCongratulations! You have completed the Hacktoberfest challenge!")

    exit(0)
