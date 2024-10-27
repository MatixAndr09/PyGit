import subprocess


def gitINIT():
    """Initialize a new GitHub repo in the current directory"""
    subprocess.run(["git", "init"], check=True)


def gitCLONE(url):
    """Clone a GitHub public repo into the current directory"""
    subprocess.run(["git", "clone", url], check=True)


def gitADD(filepath):
    """Adds files to the staging area. If you use the '.' argument, it will add all files in the current directory"""
    subprocess.run(["git", "add", filepath], check=True)


def gitCOMMIT(message):
    """Commits the files in the staging area with the message"""
    subprocess.run(["git", "commit", "-m", message], check=True)


def gitSTATUS():
    """Shows the status of the current repo. (Modified, deleted, created, files)"""
    subprocess.run(["git", "status"], check=True)


def gitPULL():
    """Pulls the latest changes from the remote repo"""
    subprocess.run(["git", "pull"], check=True)


def gitPUSH():
    """Pushes the changes to the remote repo"""
    subprocess.run(["git", "push"], check=True)


def gitBRANCH(branch):
    """Creates a new branch or change to other branch"""
    subprocess.run(["git", "branch", branch], check=True)


def gitCHECKOUT(branch):
    """[NOT AVAILABLE]"""
    pass


def gitMERGE(branch):
    """[NOT AVAILABLE]"""
    pass


def gitLOG():
    """Shows the commit log"""
    subprocess.run(["git", "log"], check=True)
