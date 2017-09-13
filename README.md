
# Running ILD software and analysis

This package serves as an entry point for general documentation on running iLCSoft (see: [https://github.com/iLCSoft](https://github.com/iLCSoft) ) for [ILD](https://confluence.desy.de/display/ILD).

Other places to find documentation on iLCSoft:


- [https://github.com/iLCSoft](https://github.com/iLCSoft)
	- the Github project that holds most of the software repositories
	- here you can post questions and issues to the software tools

- [https://github.com/iLCSoft](https://github.com/iLCSoft/ilcsoftDoc)
	- a breif introduction for how to use iLCSoft

	
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




## How to run Marlin for analysis
You can learn how to write a Marlin steering file from [here](https://github.com/iLCSoft/ilcsoftDoc/blob/master/README.md)

In this section, we will introduce some common Marlin processors for physics analysis.

### how to create a ROOT file out of a LCIO file for the use of LC Tuple
	e.g. Marlin lctuple.xml --global.GearXMLFile=gear_ILD_l4_v02_dd4hep.xml 
(change data considering your own simulation)

this creates a file <...>_REC_lctuple.root which can be analyzed.
For more information about LCTuple, see 
[here](https://github.com/iLCSoft/LCTuple)



## How to program for analysis
Some general information about how to write a Marlin processor is [here](https://github.com/iLCSoft/ilcsoftDoc/blob/master/README.md)

Here, we will show some examples of processor programming for analysis. With these basic commands, you can begin to program your own processor for analysis. The further usages of lcio can be found [here](http://lcio.desy.de/v02-09/doc/)

The most common used collections are MCParticle, PandoraPFOs, MCTruthRecoLink and RecoMCTruthLink.
You can load MCParticle collection in your processor by  

```
    registerInputCollection( LCIO::MCPARTICLE,
    		"MCParticleCollection", 
    		"Name of the MC particle collection",
    		_colMC,
    		std::string("MCParticle") );
```
And with the similar command you can load PandoraPFOs, MCTruthRecoLink RecoMCTruthLink collections. 
We suppose the name for MCParticle, PandoraPFOs and RecoMCTruthLink collections are _colMC, _colPFO, _mcpfoRelation and _pfomcRelation.
Now after you load them, they are only strings, to get the real collections, you should use command as
```
	LCCollection* AllMC= evt->getCollection( _colMC) ;
```
where "evt" is the pointer of the event.

To get the pointer of one specific MCParitcle, you can use
```
	int nMC = AllMC->getNumberOfElements();
	MCParticle* MC = dynamic_cast< MCParticle* >( AllMC->getElementAt(i) );
```
In the first line, "nMC" tells you how many MCParticles for this event,
where i in the second line is an integer, which begin from 0 and should smaller than "nMC"


   For MCParticle, the detail information in slcio file is

  | name |[id]| index | PDG | px, py, pz | px_ep, py_ep, pz_ep | energy | gen | [simstat] | vertex x, y, z | endpoint x, y, z | mass | charge | spin | colorflow | [parents] - [daughters]|
  |------|----|-------|-----|------------|---------------------|--------|-----|-----------|----------------|------------------|------|--------|------|-----------|------------------------|
  |method|    |       |getPDG()|getMomentum()|getMomentumAtEndpoint()|getEnergy()|getGeneratorStatus()|getVertex()|getEndpoint()|getMass()|getCharge()|getSpin()|getColorFlow()|getParents()|getDaucters()|
   
   In the above table, the first row is the variable name, and the second row is the corresponding methed to invoke them in the processor. 
For example, once you declare a new MCParticle, you can use the command like `MC->getPDG()` to get the PDG information of that MCParticle.

   For PandoraPFOs, the information is very similar

   |[id]| com | type | momentum | energy | mass | charge | position ( x,y,z ) | pidUsed | GoodnessOfPID | covariance( px,py,pz,E ) | particles([id]) | tracks ([id]) | clusters ([id]) | particle ids ([id],PDG,(type)) | vertices|
   |----|-----|------|----------|--------|------|--------|--------------------|---------|---------------|--------------------------|-----------------|---------------|-----------------|--------------------------------|---------|

   The method for invoke these variables can be found at [here](http://lcio.desy.de/v02-09/doc/doxygen_api/html/classEVENT_1_1ReconstructedParticle.html), where you can also find other c++ API for lcio.

The MCTruthRecoLink reflects that if you have know a MCParticle, then what reconstructed particles it can be. You can load this information by a LCRelationNavigator.
For example 

```
	LCCollection relation_mcpfo= new LCRelationNavigator( evt->getCollection( _mcpfoRelation ) );
```

Then use

```
		LCObjectVec fromMCobj = relation_mc->getRelatedToObjects(MC[i]);
        // fromMC may contain many reconstructed particles, they all come from this MC[i]
        // a dynamic_cast should be used to turn them to ReconstructedParticle. 

		std::vector<ReconstructedParticle*> fromMC;
		for( unsigned int j = 0; j < frompars.size(); j++ ){
			ReconstructedParticle* recpfo = dynamic_cast< ReconstructedParticle* >( fromMC_obj[j] );
			fromMC.push_back(recpfo);
		}
```
Now the vector "fromMC" contains all ReconstructedParticles that come from  MC[i].

The RecoMCTruthLink is opposite to MCTruthRecoLink, which tells you that for one reconstructed particle, it comes from how many MCParticles.


	











