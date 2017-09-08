
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

	git clone https://github.com/ILDAnaSoft/ILDDoc.git   			clone ILDDoc.git
	cd ILDDoc
	
	git remote add downstream
	https://<yourUserName>@github.com/<yourUserName>/ILDDoc.git 	use your github username
	
	git checkout -b <myNewBranch>									create a new branch; choose a name
	
		open the file you want to change and execute your changes
		
	git diff														you can check the changed version
	git ci -a 														commit your changes to local repository	
																	write a commit message in editor window	
	git push downstream	<myNewBranch>									upload file back to our github account
	
	git pull origin
	git push downstream master										push file from your to official website
	git checkout master


## ILD DST format

The DST files used for ILD are described [here](./dst/ild_dst_collections.md).


 ... hello world ...

	
	



