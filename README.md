
# Running ILD software and analysis

This package serves as an entry point for general documentation on running iLCSoft (see: [https://github.com/iLCSoft](https://github.com/iLCSoft) ) for [ILD](https://confluence.desy.de/display/ILD).

Other places to find documentation on iLCSoft:


- [https://github.com/iLCSoft](https://github.com/iLCSoft)
	- the Github project that holds most of the software repositories
	- here you can post questions and issues to the software tools

	
- [http://ilcsoft.desy.de/portal](http://ilcsoft.desy.de/portal)
	- general entry page for iLCSoft tools (somewhat outdated)

- [http://forum.linearcollider.org/](http://forum.linearcollider.org/)
	- discussion forum for iLCSoft (Marlin et al)
	- this is where new iLCSoft releases are announced


## First Steps

If you are new to iLCSoft you can follow this [tutorial](./tutorial/gaede_ilcsoft_tutorial.pdf)
to familiarize yourself with the basic software and analysis tools.

for a short version, see below:

### how to download, change and upload files/repositories (ILDDoc.git in this example)
	
	####clone ILDDoc.git
	git clone https://github.com/ILDAnaSoft/ILDDoc.git   			
	cd ILDDoc
	
	git remote add downstream
	https://<yourUserName>@github.com/<yourUserName>/ILDDoc.git 	
	(use your github username)
	
	####create a new branch; choose a name
	git checkout -b <myNewBranch>									
	
	open the file you want to change and execute your changes (e.g.: gedit <filename> &)
	
	####check the changed version
	git diff														
	
	####commit your changes to local repository; write a commit message in editor window; close the window
	git ci -a 														
																	
	####upload file back to your github account
	git push downstream	<myNewBranch>									
	
    reload your own github webite (https://github.com/<yourUserName>/ILDDoc)
    you should see your commit
    trigger pull request on website 

	####bring downstream master in synch with origin master after pull request has been accepted:
	
	git checkout master	
	git pull origin
	git push downstream master										




while doing this you can check your branches with: 	git lola
	if everything went fine, you shoud be able to see sth like 
		* b6f0c82 (HEAD, refs/heads/<myNewBranch>) <your commit message> 
	in the first line after upoading the branch



### configuration of git
	open a terminal and log in
	ls -a
	open .gitconfig with an editor 
	check your data and adapt them to the example below:
	
	[user]
		name = <you name>
		email = <your email> 
	[alias]
		what = whatchanged
		stat = status
		ci = commit
		co = checkout
		lola = log --graph --decorate --pretty=oneline --abbrev-commit --all
		logf = "!echo \"Remember to add -S<string>\" ; git log --color -p --source --all"
  		logrl = log --pretty=format:\"%aN %ad %n  - %s\" --date=short
  	[color]
		ui = true
		diff = auto
		status = auto
  	[core]
		excludesfile = <YourHomeFolde>/.gitignore_global
		editor = gedit
  	[branch]
		autosetuprebase = always
 	 [push]
  		## for newer versions of git, otherwise try "simple"
		default = matching
		
	save your changes
	
	
	

## ILD DST format

The DST files used for ILD are described [here](./dst/ild_dst_collections.md).



	
	



