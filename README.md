# DigitalOcean Commit Counter

DigitalOcean is offering a
[Hacktoberfest Giveaway](https://www.digitalocean.com/company/blog/hacktoberfest/).
During October 2014, if you make 50 commits to any public repository, they will
give you a free limited edition t-shirt.

As Github doesn't provide an easy method through the UI to view your public
commit count over a specific date range, I thought it would be a fun little
project to build a script to count those commits for me.

## Setup

Clone this repository to the directory of your choice.  Install the
dependencies with

    pip install -r requirements.txt

In the `commit-count.py` script, provide your username and your
[application token](https://help.github.com/articles/creating-an-access-token-for-command-line-use/).

## TODO

Currently, there are a few more issues that need to be addressed.  I haven't
yet provided a mechanism for specifying the ending boundary.  As the repository
stands, this will count all commits from a given point forward.

In addition to this, there seems to be problems with it counting commits sent
to another repository.  This definitely needs to be addressed as it is likely a
huge source of commits for some people.



