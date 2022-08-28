# 1. Git Log

### `git log` flags

While many Git-based tools will give you a visualization of this history to help you review the state of the system, it is less well-known that the git log command has many useful flags that give you the power to view the history in whatever way you like.

Familiarity with the git log command can not only save you a lot of time, but it can also speed up the Git learning process and is available wherever Git is, so you’re not dependent on a particular tool to use Git effectively.

## A Realistic Log History

```bash
1   git clone https://github.com/ianmiell/shutit.git
2   cd shutit
```

Once cloned (it can take a while), run this command to view the kind of output git log can show you. Type this out:

```bash
git log --graph --oneline --all --decorate --topo-order
```

# 2. Bare Repositories

## Setting up a Bare Repository

### Configuration

```bash
1   mkdir lgthw_bare_repo
2   cd lgthw_bare_repo
3   git init --bare
```

### The `--bare` flag

This time, you created a Git repository with the --bare flag. Have a look around the folder that you are in now. What’s the main difference you notice between this and a “normal” repository?

```bash
cat config
```

```bash
5   cd ..
6   git clone lgthw_bare_repo lgthw_bare_repo_alice
7   git clone lgthw_bare_repo lgthw_bare_repo_bob
```

```bash
8   cd lgthw_bare_repo_alice
9   git remote -v
10  touch afile
11  git add afile
12  git commit -m 'Initial'
13  for i in {1..10}
14  > do
15  > echo $i >> afile
16  > git commit -am "commit:${i}"
17  > done
18  git log --oneline
19  git push
```

### Squashing the squashed commits

What will happen if Alice pushes? Think about it, then guess:
```bash
5   git push origin master
```

## Git Pull and Merge Hell

### Squash on a branch and locally

If there’s a moral to all this, it is that you should squash on a branch and only locally (if possible).

It’s yet another reason to take advantage of Git’s cheap cost of branching.

If there’s a second moral, it’s to avoid force-pushing wherever other users are involved. Many Git products have options to forbid or only allow certain privileged users to force-push changes to repositories for this reason.

# Git hooks

## A pre-commit Hook

### Create Repositories

```bash
1   mkdir lgthw_hooks
2   cd lgthw_hooks
3   mkdir git_origin
4   cd git_origin
5   git init --bare
6   cd ..
7   git clone git_origin git_clone
```

### Adding a "pre-commit" hook

```bash
13  echo 'second change in clone' >> file1
14  ls .git/hooks
```

What you’re going to do now is create a script that is run before any commit is accepted into your local Git repository:

```bash
15  cat > .git/hooks/pre-commit << EOF
16  > echo NO WORKING AT WEEKENDS!
17  > exit 1
18  > EOF
19  chmod +x .git/hooks/pre-commit
```

You have created a pre-commit script in the hooks folder of the repository’s local .git folder and made it executable. The script prints a message about not working on weekends and exits with a code of 1, which is a generic error code in a shell script (exit 0 would mean “OK”).


```bash
git comit -am 'Second change'
```

## A More Sophisticated Example

### Banning keywords

Imagine that you’ve decided against o allowing any mention of politics in your code. The following hook will reject any mention of politics (or any word beginning with “politic”).

```bash
1   echo 'a political comment' >> file1
2   cat > .git/hooks/pre-commit << EOF
3   > if grep -rni politic *
4   > then
5   >   echo 'no politics allowed!'
6   >   exit 1
7   > fi
8   > echo OK
9   > exit 0
10  > EOF
11  git commit -am 'Political comment'
```

Again, the commit should have been rejected. If you change the content to something else that doesn’t mention politics, it will commit and push just fine.

```bash
12  echo 'a boring comment' > file1
13  git commit -am 'Boring comment'
14  git push
```

Even more sophisticated scripts are possible but require a deeper knowledge of bash (or other scripting languages), which is out of scope. You will, however, look at one much more realistic example in the last section of this chapter.

```bash
rm .git/hooks/pre-commit
```

## Additional information on Hooks

### Are hooks part of Git content?

A question you may be asking yourself at this point is whether the hooks are part of the code or not. You wouldn’t have seen any mention of the hooks in your commits; so does it move with the repository as you commit and push or not?

```bash
cd ../git_origin
ls hooks
```

## Pre-receive hooks

Type this out, and then I’ll explain what it’s doing. As best you can, try and work out what it’s doing as you go, but don’t worry if you can’t figure it out.

```bash
3   cat > hooks/pre-receive << 'EOF'
4   > #!/bin/bash
5   > read _oldrev newrev _branch
6   > git cat-file -p $newrev | grep '[A-Z][A-Z]*-[0-9][0-9]*'
7   > EOF
```

This time you created a pre-receive script, which will be run when anything is pushed to this repository. These pre-receive scripts work in a different way to the pre-commit hook scripts because the pre-commit script allows you to grep the content that was being committed; pre-receive scripts do not. This is because the commit has been packaged up by Git, and the contents of the commit are delivered up as that packaged content.

The read command in the above code is the key one to understand. It reads three variables: _oldrev, newrev, and _branch from standard input (i.e., the data that is coming in to the script). The contents of these variables will match. The previous Git revision reference commit refers to the branch it is committed on. The new Git revision reference commit refers to the branch it is committed on. Git arranges that these references are given to the pre-receive script on standard input so that action can be taken accordingly.

Then, you use the (previously unseen in this course) git cat-file command to output details of the latest commit value stored in the newrev variable. The output of this latest commit is run through a grep command that looks for a specific string format in the commit message. If the grep finds a match, then it returns no error and all is OK. If it doesn’t find a match, then grep returns an error as does the script.


