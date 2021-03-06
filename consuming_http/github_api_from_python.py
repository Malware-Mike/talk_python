import requests

def main():

    user, repo = get_repo_info()

    url = 'https://api.github.com/repos/{}/{}'.format(user, repo)

    resp = requests.get(url)

    if resp.status_code != 200:
        print('Error accessing repo: {}'.format(resp.status_code))

    repo_data = resp.json()
    clone = repo_data.get('clone_url', 'Error: NO DATA')
    print(repo_data)

    print("To clone {}'s repo named {}".format(user, repo))
    print("The command is: ")
    print()
    print("git clone {}".format(clone))




def get_repo_info():
    user = input("What is the username? ")
    repo = input("What is the name of the repo? ")

    return user, repo


if __name__ == '__main__':
    main()