"""
Do Nothing Script
This script doesn't actually _do_ any of the steps of the procedure. That's why it's called a do-nothing script.
It feeds the user a step at a time and waits for them to complete each step manually.
The value of this is immense:
  - It's now much less likely that you'll lose your place and skip a step.
    This makes it easier to maintain focus and power through the slog.
  - Each step of the procedure is now encapsulated in a function.
    This makes it possible to replace the text in any given step with code that performs the action automatically.
  - Over time, you'll develop a library of useful steps, which will make future automation tasks more efficient.

A do-nothing script doesn't save you any manual effort.
It lowers the activation energy for automating tasks, which allows you to eliminate toil over time.
"""

import sys

def wait_for_enter():
    input("Press Enter to continue: ")

class CreateSSHKeypairStep(object):
    def run(self, context):
        print()
        print("Run:")
        print(" ssh-keygen -t rsa -f ~/{0}".format(context["username"]))
        wait_for_enter()

class GitCommitStep(object):
    def run(self, context):
        print()
        print("Copy ~/new_key,pub into the `user keys` Git repository, then run:")
        print(" git commit {0}".format(context["username"]))
        print(" git push")
        wait_for_enter()

class WaitForBuildStep(object):
    build_url = "http://example.com/builds/user_keys"
    def run(self, context):
        print()
        print("Wait for the build job at {0} to finish".format(self.build_url))
        wait_for_enter()

class RetrieveUserEmailStep(object):
    dir_url = "http://example.com/directory"
    def run(self, context):
        print()
        print("Go to {0}".format(self.dir_url))
        print("Find the email address for user `{0}`".format(context["username"]))
        context["email"] = input("Paste the email address and press enter: ")

class SendPrivateKeyStep(object):
    def run(self, context):
        print()
        print("Go to 1Password")
        print("Paste the contents of ~/new_key into a new document")
        print("Share the document with {0}".format(context["email"]))
        wait_for_enter()

if __name__ == '__main__':
    #context = {"username": sys.argv[1]}
    context = {"username": "johndoe"}

    procedure = [
        CreateSSHKeypairStep(),
        GitCommitStep(),
        WaitForBuildStep(),
        RetrieveUserEmailStep(),
        SendPrivateKeyStep()
    ]

    for step in procedure:
        step.run(context)

    print()
    print("Done.")
