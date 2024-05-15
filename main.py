import instaloader
import getpass

# Get instance
loader = instaloader.Instaloader()


# Login using the credentials
username = input("Enter your Instagram username: ")
password = getpass.getpass("Enter your Instagram password: ")
loader.login(username, password)

# Use Profile class to access metadata of account
profile_username = 'geeks_for_geeks'  # Replace this with desired username
profile = main.Profile.from_username(loader.context, profile_username)
print(profile)
