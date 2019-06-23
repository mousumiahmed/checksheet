#### 

[GIT](https://xkcd.com/1597/)

**Introduction to git (Part 1)**

```
git init` `git config` `git add` `git commit` `git remote` `git clone` `git pull` `git push
```

#### NOTES

**Why Use the Version Control?**

A big software project involves 100s of developers working simultaneously on 1000s of files changing millions of lines of code over a long time.

***Imagine all these developers using pen drives or email to share the changes they are making to the code***

Whenever you are working on something that changes over time, it’s useful to be able to track those changes. This can be for a number of reasons: it gives you a record of what changed, how to undo it, who changed it, and possibly even why.

Version control systems (VCS) give you that ability. They let you commit changes to a set of files, along with a message describing the change, as well as look at and undo changes you’ve made in the past.

**Main categories of VCS**

- Centralised
- Distributed

Centralised Version Control

Centralized version control systems are based on the idea that there is a single “central” copy of your project somewhere (probably on a server), and programmers will “commit” their changes to this central copy.
“Committing” a change simply means recording the change in the central system. Other programmers can then see this change. They can also pull down the change, and the version control tool will automatically update the contents of any files that were changed.

When you’re working with a centralised version control system, your workflow for adding a new feature or fixing a bug in your project will usually look something like this:

- Pull down any changes other people have made from the central server.
- Make your changes, and make sure they work properly.
- Commit your changes to the central server, so other programmers can see them.

Distributed Version Control

These systems do not necessarily rely on a central server to store all the versions of a project’s files. Instead, every developer “clones” a copy of a repository and has the full history of the project on their own hard drive. This copy (or “clone”) has all of the metadata of the original.

The act of getting new changes from a repository is usually called “pulling,” and the act of moving your own changes to a repository is called “pushing”. In both cases, you move changesets (changes to files groups as coherent wholes), not single-file diffs.

One common misconception about distributed version control systems is that there cannot be a central project repository. This is simply not true – there is nothing stopping you from saying “this copy of the project is the authoritative one.” This means that instead of a central repository being required by the tools you use, it is now optional and purely a social issue.

`git config` - sets or see the configuration for git
`git config --global user.name [Firstname Lastname]` - set a name that is identifiable for credit when review version history
`git config --global user.email [email]` - set an email address that will be associated with each history marker
`git config user.name` - see the name set

`git init` - initialize an existing directory as a Git repository

`git clone [url]` - retrieve an entire repository from a hosted location via URL

`git add [file]` - add a file as it looks now to your next commit (stage)

`git commit -m "[descriptive message]"` - commit your staged content as a new commit snapshot

`git remote add orgin [url]` - add a git URL as a remote

`git pull` - Fetch and merge any commits from the tracking remote branch

`git push` - Transmit local branch commits to the remote repository branch



**Introduction to git (Part 2)**

```
git init` `git add` `git commit` `git remote` `git clone` `git pull` `git push` `git status` `git log
```

#### NOTES

**git init**

```
$ git init
```

Initialise an existing directory as a Git repository

**git add**

```
$ git add file.txt
```

Tell git to start tracking changes to the file `file.txt`

```
$ git add file1.txt file2.txt file3.txt
```

Tell git to start tracking changes to the file `file1.txt` `file2.txt` `file3.txt`

```
$ git add directory
```

Tell git to start tracking changes made in the folder with the name `directory`

```
$ git add directory/*.csv
```

Tell git to start tracking changes to all the `.csv` files in the folder with the name `directory`

**git commit**

```
$ git commit -m "message for the commit"
```

Create a new commit containing any changes to the previously added files with the mentioned message

**git remote**

```
$ git remote add origin https://github.com/username/test.git
```

Add a git URL as a remote

**git push**

```
$ git push origin master
```

Transmit local commits to the remote repository

**git clone**

```
$ git clone https://github.com/username/test.git
```

retrieves an entire repository from a hosted location via URL

**git pull**

```
$ git pull origin master
```

Fetch and merge any commits from the tracking remote branch

**git status**

```
$ git status
```

show modified files in working directory, staged for your next commit

**git log**

```
$ git log
```

show all commits in the current repository history

CAUTION

git is generally used for tracking changes to code file so don't put huge files of images, videos or any others. (remember everyone ends up copying those file)



**Introduction to git (Part 3)**

```
git checkout` `git revert` `git reset` `git diff
```

**git diff**

```
$ git diff
```

diff of what is changed but not staged

```
$ git diff --staged
```

diff of what is staged but not yet commited

```
$ git diff file.txt
```

diff of what is changed in `file.txt`

```
$ git diff folder
```

diff of what is changed in the directory `folder`

```
$ git diff <commit1> <commit2>
```

diff between two commits

**git reset**

```
$ git reset file.txt
```

unstage a file while retaining the changes

**git checkout**

```
$ git checkout file.txt
```

discards any modifications made to the file that are not staged

**NOTE: Be careful before using this command you might loose some data**

**git revert**

```
$ git revert <commit>
```

reverts the changes to the mentioned commit

**Resolving merge conflicts**

User 1 Project

```
~/masai/account1/project$ echo "Content 1" > file.txt
~/masai/account1/project$ git add file.txt
~/masai/account1/project$ git commit -m "user1 commit"
~/masai/account1/project$ git push origin master
```

User 2 Project

```
~/masai/account2/project$ echo "Content 2" > file.txt
~/masai/account2/project$ git add file.txt
~/masai/account2/project$ git commit -m "user2 commit"
~/masai/account2/project$ git pull origin master
```

You will get below message

```
Auto-merging file.txt
CONFLICT (add/add): Merge conflict in file.txt
Automatic merge failed; fix conflicts and then commit the result.
```

Contents of `file.txt`

```
<<<<<<< HEAD
Content 2
=======
Content 1
>>>>>>> 160199578ad0a96b3130233595a905bca4e52fae
```

Make changes to `file.txt`

```
Content 2
```

If you want to keep the new content

```
Content 1
```

If you want to keep the old content

```
$ git add file.txt
```

To mark the resolution of conflicts

```
$ git commit
```

To conclude the merge after resolving conficts

```
$ git push origin master
```

To push the changes back to the online repo