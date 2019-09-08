Ubuntu commands





### Week 1 - Day 1

#### Session 1

[Command Line Fun](https://xkcd.com/196/)

**The Linux Command Line (Part 1)**

```
date` `cal` `df` `free` `pwd` `cd` `ls` `less` `file` `mkdir` `cp` `mv` `rm` `wget` `unzip
```

#### NOTES

**Why Use the Command Line?**

Both the GUI(Graphical User Interface) and CLI(Command Line Interface) are ways you can interact with your computer.
But when it comes to the command line, once you learn the commands, it is faster and more powerful to navigate and use your computer. This is why many programmers prefer the command line.

***Graphical user interfaces make easy tasks easy, while command line interfaces make difficult tasks possible”***

### What is the shell?

When we speak of the command line, we are really referring to the shell. The shell is a program that takes keyboard commands and passes them to the operating system to carry out.
Almost all Linux distributions supply a shell program from the GNU Project called bash.
The name “bash” is an acronym for “Bourne Again SHell”, a reference to the fact bash is an enhanced replacement for sh, the original Unix shell.

------

**Note**: Don't be tempted to use Ctrl-c and Ctrl-v to perform copy and paste inside a terminal window. They don't work. These control codes have different meanings to the shell and were assigned many years before the release of Microsoft Windows.

------

### Some Simple Commands

`date` - displays current date and time
`cal` - displays a calendar of the current month
`df` - see the current amount of free space on our disk drives
`free` - display the amount of free memory

### Flags

Most command line utilities take parameters using **flags**.
Flags usually come in short form (`-h`) and long form (`--help`).
Usually running `CMD -h` or `man CMD` will give you a list of the flags the program takes.
Short flags can usually be combined, running `date -u -R` is equivalent to running `date -uR` or `date -Ru`.

`tab` - auto fill (very handy)
`q` - quit from command

### Navigation

`pwd` - print working directory
`cd` - change directory
`cd /usr/bin` - absolute path
`cd ..` - working directory parent
`cd ./bin` or `cd bin` - relative path
`cd` or `cd ~` - home directory
`cd -` - previous working directory
`ls` - list files
`ls -l` - show detailed info in columns
`ls -a` - include hidden files also
`ls -t` - sort by last modified date newest first
`ls -S` - sort by size
`ls -R` - recursively list subdirectories
`ls -F` - indicator at the end of each file `/` if it is a directory

```
`ls /usr` - specify directory to list   
ls [-ABCFGHLOPRSTUW@abcdefghiklmnopqrstuwx1]
```

`file <filename>` - determine the file type
`less <filename>` - show the contents of a file
`b` - scroll back one page
`space` - scroll forward one page
`up arrow` - scroll up one line
`down arrow` - scroll down one line
`G` - move to the end of file
`g` - move to the beginning of file
`/characters` - search forward the next occurance of characters
`n` - search for the next occurrence of the previous search

### Wildcards

Before we begin using our commands, we need to talk about a shell feature that makes these commands so powerful. Since the shell uses filenames so much, it provides special characters to help us rapidly specify groups of filenames. These special characters are called wildcards. Using wildcards allows us to select filenames based on patterns of characters.

`*` - Matches any characters `?` - Matches any single character

### Manipulation

`mkdir <directory>` - create directory
`mkdir <dir1> <dir2> <dir3>` - create multiple directories
`mkdir -p <dir1>/<dir2>/<dir3>` - create intermediate directories as required

`cp <item1> <item2>` - copies the single file or directory item1 to the file or directory item2
`cp file1 file2 dir1` - Copy file1 and file2 into directory
`cp dir1/* dir2` - Using a wildcard, copy all the files in dir1 into dir2. The directory dir2 must already exist.
`cp -r dir1 dir2` - Copy the contents of directory dir1 to directory dir2.
If directory dir2 does not exist, it is created and, after the copy, will contain the same contents as directory dir1.
If directory dir2 does exist, then directory dir1 (and its contents) will be copied into dir2.

`mv <item1> <item2>` - performs both file moving and file renaming `mv file1 file2` - Move file1 to file2. If file2 exists, it is overwritten with the contents of file1. If file2 does not exist, it is created. In either case, file1 ceases to exist. `mv file1 file2 dir1` - Move file1 and file2 into directory dir1. The dierctory dir1 must already exist.
`mv dir1 dir2` - If directory dir2 does not exist, create directory dir2 and move the contents of directory dir1 into dir2 and delete directory dir1.If directory dir2 does exist, move directory dir1 (and its contents) into directory dir2.

`rm <item>` - used to remove (delete) files and directories
`rm -r dir1` - Delete dir1 and its contents.
`rm -r file1 dir1` - Delete file1 and dir1 and its contents.

**CAUTION**

Unix-like operating systems such as Linux do not have an undelete command.
**Once you delete something with rm, it's gone!**
Linux assumes you're smart and you know what you're doing.

**TIP**

Whenever you use wildcards with rm (besides carefully checking your typing!), test the wildcard first with ls.
This will let you see the files that will be deleted. Then press the up arrow key to recall the command and replace ls with rm.

### Extra Commands

`wget <location>` - command-line program for file downloading `unzip <file>` - command to unzip a file



### Week 1 - Day 1

#### Session 2

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



### Week 1 - Day 2

#### Session 1

[Command Line Fun](https://xkcd.com/196/)

**The Linux Command Line (Part 2)**

```
>` `>>` `cat` `sort` `grep` `wc` `head` `tail
```

#### NOTES

**Standard Input, Output, and Error**

All programs you launch (“processes”) have three “streams”:

`STDIN` - when the program reads input, it comes from here `STDOUT` - when the program prints something, it goes here`STDERR` - a 2nd output the program can choose to use

**Redirecting Standard Output**

I/O redirection allows us to redefine where standard output goes. To redirect standard output to another file instead of the screen, we use the `>` redirection operator followed by the name of the file.

Send the output of the `ls` command to the file `ls-output.txt` instead of the screen

```
$ ls -l ~/masai > ls-output.txt
```

Having a look at the `ls-output.txt` file

```
$ less ls-output.txt
```

Doing the same with a directory that doesn't exist

```
$ ls -l ~/random > ls-output.txt
ls: cannot access '/home/username/random': No such file or directory
```

`ls` program does not send its error messages to standard output instead it sends its error messages to standard error

`>` The destination file is always rewritten from the beginning

`>>` Append redirected output to a file instead of overwriting the file from the beginning

Doing the `ls` with `>>` redirection

```
$ ls -l ~/masai >> ls-output.txt
$ ls -l ~/masai >> ls-output.txt
$ ls -l ~/masai >> ls-output.txt
```

Having a look at the `ls-output.txt` file

```
$ less ls-output.txt
```

**cat – Concatenate Files**

The cat command reads one or more files and copies them to standard output

```
$ cat file1.txt file2.txt
```

This shows the combined output joining both the files

Using the redirection `>` you can write the combined into a new file

```
$ cat file_* > combined.txt
```

TIP: You can use the wildcards to select the files if there are many files

**sort - sort lines of text files**

The sort command sorts the lines of the file in ascending order

```
$ sort file.txt
```

This shows the lines of the file in sorted order

```
$ sort file.txt > sorted_file.txt
```

In case you want to save the file in sorted order

```
$ sort -r file.txt
```

This sorts the file in reverse order

Suggestion: Explore `man` pages for more options

**grep – Print Lines Matching a Pattern**

grep is a powerful program used to find text patterns within files

```
$ grep search_word file.txt
```

This shows all the lines in `file.txt` which contain the `search_word`

You can also use this to search in multiple files along with wild cards also

```
$ grep search_word file_1.txt file_2.txt 
$ grep search_word file_*
```

**wc – Print Line, Word, and Byte Counts**

The wc (word count) command is used to display the number of lines, words, and bytes contained in files

```
$ wc file.txt
```

This shows the lines, words and bytes of `file.txt`

```
$ wc files_*
```

TIP: You can also use wild cards

MORE OPTIONS

```
$ wc -l
```

shows the no of lines

```
$ wc -w
```

shows the no of words

```
$ wc -m
```

shows the no of characters

**head / tail – Print First / Last Part of Files**

Sometimes we don't want all the output from a command. We may only want the first few lines or the last few lines. The head command prints the first ten lines of a file, and the tail command prints the last ten lines.

```
$ head file.txt
```

shows the first 10 lines of the file

```
$ tail file.txt
```

shows the last 10 lines of the file

```
$ head -n 20 file.txt
```

shows the first 20 lines of the file

```
$ tail -n 20 file.txt
```

shows the last 20 lines of the file



### Week 1 - Day 2

#### Session 2

[GIT](https://xkcd.com/1597/)

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



### Week 1 - Day 2

#### Session 1

[tar](https://xkcd.com/1168/)

**The Linux Command Line (Part 3)**

```
|` `find` `echo` `uniq` `<` `tar` `nano` `touch
```

**| - Pipelines**

Using the pipe operator | (vertical bar), the standard output of one command can be piped into the standard input of another.

```
$ grep masai demo.txt > masai.txt
```

Finds the occurrence word `masai` in the file `demo.txt` and writes it to masai.txt

```
$ wc -l masai.txt
```

Count the no of lines in the file `masai.txt` (Effectively giving the count of no. of times the word `masai` appears in the files `demo.txt`)

**The same can be done using | with the single line of commands**

```
$ grep masai demo.txt | wc -l
```

| (pipes) can also be used to connect any number of commands the syntax remains the same

```
$ command1 | command2 | command3 | command4
```

**find – Find Files the Hard Way**

The find program searches a given directory (and its sub-directories) for files based on a variety of attributes

```
$ find <path>
```

Find all the folders (including sub folders) and files in the given path

```
$ find <path> -type d
```

Adding the flag -type d limits the search to directories

```
$ find <path> -type f
```

Adding the flag -type f limits the search to files

```
$ find <path> -type d | wc -l
```

Remember pipes now the above command counts all the files in a particular folder

```
$ find <path> -type f -name "*.csv"
```

Finds all the files in the given path whose name ends with `.csv`

```
$ find <path> type f -name "*.csv" -size -1M
```

Finds all the files in the given path whose name ends with `.csv` and having size less than 1MB

**echo – Display a line of text**

```
$ echo "Hello MASAI"
```

That's pretty straightforward. Any argument passed to echo gets displayed

```
$ echo "Hello MASAI" > masai.txt
```

Writes the output of echo to the given file name

Expansion

```
$ echo *
```

Why didn't echo print *?

As we recall from our work with wild-cards, the * character means match any characters in a filename, but what we didn't see in our original discussion was how the shell does that. The simple answer is that the shell expands the * into something else (in this instance, the names of the files in the current working directory) before the echo command is executed. When the Enter key is pressed, the shell automatically expands any qualifying characters on the command line before the command is carried out, so the echo command never saw the *, only its expanded result.

Brace Expansion

```
$ echo string_{a,b,c}
```

Output

```
string_a string_b string_c
$ echo number_{1..5}
```

Output

```
number_1 number_2 number_3 number_4 number_5
```

**uniq - Report or Omit Repeated Lines**

When given a sorted file (or standard input), it removes any duplicate lines and sends the results to standard output

```
$ uniq demo.txt
```

The results are no different from our original file; the duplicates were not removed. For `uniq` to do its job, the input must be sorted first. This is because uniq only removes duplicate lines that are adjacent to each other.

```
$ sort demo.txt | uniq
```

This will now gives us the unique lines from the file `demo.txt`

```
$ uniq -d sorted.txt
```

This will only show the duplicate lines from the files

```
$ uniq -c sorted.txt
```

Outputs the list of lines preceded by the number of times the line occurs

**tar**

The tar program is the classic tool for archiving files

`c` Create an archive from a list of files and/or directories
`x` Extract an archive
`t` List the contents of an archive

```
$ tar -cf demo.tar demo
```

Creates a tar file from all the folders and files in the folder `demo` to a file called `demo.tar`

```
$ tar -tf demo.tar
```

Lists the contents of the tar file `demo.tar`

```
$ tar -xf demo.tar
```

Extracts the contents of the file `demo.tar`

**nano**

Popular command line text editor

```
$ nano
```

Opens the editor

```
$ nano file.txt
```

Opens the editor with the file `file.txt`

`[Ctrl]o` - Write to file

`[Ctrl]w` - Search for word

`[Ctrl][Shift]-` `[Ctrl]_` - Go to line

`[Ctrl]k` - Cut line

`[Ctrl]u`- Uncut (Paste)

**touch**

The touch command is usually used to set or update the access, change, and modify times of files. However, if a filename argument is that of a nonexistent file, an empty file is created

```
$ touch file.txt
```

Creates the file `file.txt` if not exists

```
$ touch file1 file2
```

Creates the files `file1` and `file2` if not exists

```
$ touch file-{a,b,c,d}
```

Creates the files `file-a` `file-b` `file-c` `file-d` if not exists

**< Standard Input**

Using the `<` redirection operator, we change the source of standard input from the key board to the file `demo.txt`



### Week 2 - Day 1

#### Session 2

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

## Week 5 - Day 4

### Git Branch & Pull Request

When the project becomes big you will run into multiple problems because of many people/teams working on the same project, so the common problems are

- What is the code running on the production
- What is the code that the QA team should test
- How multiple features can be built by seperate teams simultaneously
- How to quickly fix some serious issue that is occuring in production

Git Branching makes it harder for unstable code to get into the main code

**HOW IT WORKS**

A branch represents an independent line of development. It is kind of creating a copy of your project at a certain point and working independently on it

### COMMANDS

List all the branch in the repo

```
$ git branch --list
```

`*` - current branch you are using

Create a new branch with the given name

```
$ git branch <name>
```

Rename the branch to with the new name

```
$ git branch -m <new_name>
```

Switching to the new branch name

```
$ git checkout <branch_name>
```

Push a particular branch to the remote repo

```
$ git push origin <branch_name>
```