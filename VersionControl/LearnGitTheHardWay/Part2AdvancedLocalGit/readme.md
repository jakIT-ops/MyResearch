# 1. Git Stash

Often when you are working, you want to return to a pristine state but you don’t want to lose the work you have done so far. Traditionally, with other source control tools, you’ve copied files that have changed locally aside, then updated your repository, and then diffed and re-applied the changed files.

### Stash away your changes

Git has a concept of the “stash” to store all local changes ready to re-apply at will. You can get very sophisticated with the stash. But 99% of the time, I use it like this:

```bash
[do some work]
[get interrupted]
git stash
[deal with interruption]
git stash pop
```

## 1.1 Dealing With a Scenario

### Scenario

Here is a basic example of a change I want to "stash"

```bash
mkdir lgthw_git_stash_1
cd lgthw_git_stash_1
git init
echo 'Some content' > file1
git add file1
git commit -am initial
git commit -am initial
echo 'Some changes I am not sure about' >> file1
```

#### Stashing changes

To store away these changes locally, run git stash. Run the following three commands in the terminal given below.
```bash
git stash
```
A quick git status confirms that your working directory is “clean”:
```bash
git status
```

What happened to your change? If you are interested, you can run the following command to view the graph:
```bash
git log --graph --all --decorate
```

#### Retrieving stash list

You can see your “stash list” by running this command:
```bash
git stash list
```

#### Popping stashed work

```bash
git stash pop
```

## 1.2 Choosing Your Stash

### Applying two stashes

```bash
mkdir lgthw_git_stash_2
cd lgthw_git_stash_2
git init
echo 'Some content' > file1
git add file1
git commit -am initial
echo 'First changes I am not sure about' >> file1
git stash
echo 'Second change I am also not sure about' >> file1
git stash
git stash list
```
### Getting individual stash information

Some minimal information is available if you type `git stassh show <ID>`:

```bash
git stash show stash@{0}
git stash show stash@{1}
```

`git stash show --patch <ID>` gives you the information in a different format also. Run this command in the terminal provided above:

```bash
git stash show --patch stash@{0}
git stash show --patch stash@{1}
```

### Applying a specific stash

```bash
git stash apply stash@{1}
git diff
```

# 2. Reflog

### What is reflog?

The reflog gives you references to a sequential history of what you have done to the repository. This can come in ver handy when you play with your local repository's history as you will see here.

## Lost a Commit, Get it Back

### Add commits

```bash
1   mkdir lgthw_reflog
2   cd lgthw_reflog
3   git init
4   echo first commit > file1
5   git add file1
6   git commit -m "first commit"
7   echo second commit >> file1
8   git add file1
9   git commit -am 'second commit message for file1.1'
10  git log
```

### Remove commit

Then do some magic to effectively remove the last commit by entering the following commands in the terminal given above:

```bash
10  git checkout HEAD^
11  git branch -f master
12  git checkout master
13  git log
```

### Retrieve commit

Git reflog records all movements of branches in the repository. As with git stashes, it is local to your repository.

```bash
git reflog
```

### Use `git reset` to restore state

If you `git reset --hard` the repository to the given reference (in this case, 40e99f7; your ID will differ!):

```bash
15  git reset --hard 40e99f7
16  git log
```

# 3. Cherry Picking

## 3.1 A Simple Cherry-Pick

### Port changes from one branch to another

Since every commit in Git is chage set with reference ID, you can easily port changes from one branch to another.

#### Setup

```bash
1   mkdir lgthw_cherry_pick
2   cd lgthw_cherry_pick
3   git init
4   echo change1 > file1
5   git add file1
6   git commit -am change1
7   echo change2 >> file1
8   git commit -am change2
9   git log --all --oneline --decorate --graph
```

#### Branch off 

```bash
10  git branch experimental
11  git checkout experimental
12  echo crazy change >> file1
13  cat file1
14  git commit -am crazy
15  echo more sensible change >> file1
16  cat file1
17  git commit -am sensible
```

#### Cherry-picking a commit 

You decide that the “sensible” change is the one you want to keep.

First, get the reference ID for that “sensible” commit with a git log:
```bash
18  git log --all --oneline --decorate --graph
```
Then, checkout the master and run a cherry-pick command using the identifier (replace “ID” with the below).
```bash
19  git checkout master
20  git cherry-pick ID
```

# 4. Git Rebase

### What is a rebase?

A rebase is actually a more abstract concept that we will be covered in slightly more detail in a later section. But for now, you don’t need to worry about that. In 99% of daily discussions about rebases, this is what people mean.

### Squashing

Be aware that people also talk about rebasing to “squash” commits. This is a slightly different scenario that uses the same rebase command in a slightly different way. We will cover this part later.


# 5. Git Bisect

### What is bisecting?

Bisecting is a very powerful tool for finding bugs. You won’t necessarily need it that often. But when you do, it will come in very handy and possibly make you a hero.

However, it’s not magical and understanding what it is will help you understand where it will be useful.

When it is magical, you create a Git bisect “session” and interact with the repository until you get the answer to your problem.

### The git bisect command

The git bisect command is a useful tool for finding out where a bug was introduced. If you know where a bug was introduced, you can look at the diff of the commit that caused it and work out what the source of the problem is.

### How does it works?

It works by picking a starting point where the bug definitely did not exist (the “good” point). In this case, you’ll choose point A1. Then you pick a point where the bug definitely did exist (the “bad” point). In this case, that’s A100.

## A real 'git bisect' Session

### Requirements

What you’re going to do is create a Git repository with one file (projectfile). In this file, you are going to add a line for each commit. The first line will be 1, the second 2, and so on until the hundredth commit, which adds the line 100.

```bash
if grep -w 63 projectfile
> then
>   echo BAD
> else
>   echo GOOD
```


### Implementation

```bash
1   mkdir -p lgthw_bisect
2   cd lgthw_bisect
3   git init
4   touch projectfile
5   git add projectfile
6   cat > test.sh << END
7   > if grep 63 projectfile
8   > then
9   >   echo BAD
10  > else
11  >   echo GOOD
12  > fi
13  > END
14  chmod +x test.sh
15  git add test.sh
```
### Adding 100 commits

```bash
16  for ((i=1;i<=100;i++))
17  > do
18  > echo $i >> projectfile
19  > git commit -am "A$i"
20  > done
```





















































