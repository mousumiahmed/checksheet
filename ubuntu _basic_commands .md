Ubuntu commands





#### 

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