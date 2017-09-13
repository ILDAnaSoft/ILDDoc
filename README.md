
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


## ILD DST format

The DST files used for ILD are described [here](./dst/ild_dst_collections.md).


   The most common used is MCParticle and PandoraPFOs. 
   For MCParticle, the detail information are

   |[id]| index | PDG | px, py, pz | px_ep, py_ep, pz_ep | energy | gen | [simstat] | vertex x, y, z | endpoint x, y, z | mass | charge | spin | colorflow | [parents] - [daughters]|
   |----|-------|-----|------------|---------------------|--------|-----|-----------|----------------|------------------|------|--------|------|-----------|------------------------|
   
   You can use the command like getPDG() to get the information of a MCParticle.

   For PandoraPFOs, the detail information are

   |[id]| com | type | momentum | energy | mass | charge | position ( x,y,z ) | pidUsed | GoodnessOfPID | covariance( px,py,pz,E ) | particles([id]) | tracks ([id]) | clusters ([id]) | particle ids ([id],PDG,(type)) | vertices|
   |----|-----|------|----------|--------|------|--------|--------------------|---------|---------------|--------------------------|-----------------|---------------|-----------------|--------------------------------|---------|

   The way to call this variables can be found at [here](http://lcio.desy.de/v02-09/doc/doxygen_api/html/namespaces.html), which is all the c++ API for lcio.


	
### How to run Marlin for analysis
You can learn how to write a Marlin steering file from [here](https://github.com/YancyW/ilcsoftDoc/blob/master/README.md)
In this section, we will introduce some usually used Marlin processor for physics analysis.

#### how to create a ROOT file out of a LCIO file for the use of LC Tuple
	e.g. Marlin lctuple.xml --global.GearXMLFile=gear_ILD_l4_v02_dd4hep.xml 
(change data considering your own simulation)

this creates a file <...>_REC_lctuple.root which can be analyzed.
For more information about LCTuple, see 
[here](https://github.com/iLCSoft/LCTuple)



### How to program for a new Marlin processor for analysis
First, you should know some general information about how to write a Marlin [processor](https://github.com/YancyW/ilcsoftDoc/blob/master/README.md)

Here, we will show some notes of processor programming for analysis.









