

# DST format

Collections in the ILD DST files:

if processors in the input and output column are marked like this: (?)<...> it is not sure whether they are classified correctly



| collection name               | type of objects          | content                 | written  by	(output)		| needed by		(input)											|	input and outpout *									|
| :---------------------------- | :----------------------- | :---------------------- |:---------------------------- |:------------------------------------------------------------- |:----------------------------------------------------- |
| BuildUpVertex                 | Vertex                   |   -					 |	VertexFinder				| 	-															|														|	
| BuildUpVertex_RP              | ReconstructedParticle    |   -					 |	-							| 	-															|														|
| BuildUpVertex_V0              | Vertex                   |   -					 |	VertexFinder				|	-															|														|
| BuildUpVertex_V0_RP           | ReconstructedParticle    |   -					 |	-							|	-															|														|
| DistilledPFOs                 | ReconstructedParticle    |   -					 | MyDistilledPFOCreator		|	-															|														|
| GammaGammaCandidateEtaPrimes  | ReconstructedParticle    |   -					 | MyEtaPrimeFinder				| MyGammaGammaSolutionFinder									|														|
| GammaGammaCandidateEtas       | ReconstructedParticle    |   -					 | MyEtaFinder					| MyGammaGammaSolutionFinder									|														|
| GammaGammaCandidatePi0s       | ReconstructedParticle    |   -					 | MyPi0Finder					| MyGammaGammaSolutionFinder									|														|
| GammaGammaParticles           | ReconstructedParticle    |   -					 | MyGammaGammaSolutionFinder	| MyDistilledPFOCreator											|														|
| KinkRecoParticles             | ReconstructedParticle    |   -					 |	-							|	-															|														|
| KinkVertices                  | Vertex                   |   -					 |	-							| MyDDMarlinPandora											| 														|
| MCTruthMarlinTrkTracksLink    | LCRelation               |  link Reconstructed Particles to MCParticle					 | MyRecoMCTruthLinker			|	-															| 														|
| MarlinTrkTracks               | Track                    |  best track collection  |	MyFullLDCTracking_MarlinTrk	| MyExtrToSIT; MyRecoMCTruthLinker; MyDDMarlinPandora		| MyCompute_dEdxProcessor; MyKinkFinder; MyV0Finder; 	|
| MarlinTrkTracksMCTruthLink    | LCRelation               |  link Reconstructed Particles to MCParticle					 | MyRecoMCTruthLinker			|	-															| 														|
| PandoraClusters               | Cluster                  |   -					 |	-							| (?)MyComputeShowerShapesProcessor; git diffMyAddClusterProperties; MyRecoMCTruthLinker	| MyDDMarlinPandora 									|
| PandoraPFANewStartVertices    | Vertex                   |   -					 |	-							|	-															|														|
| PandoraPFOs                   | ReconstructedParticle    |  final PFA objects	     |	-							| VertexFinder;MyComputeShowerShapesProcessor; MyPfoAnalysis; MyAddClusterProperties; MyEtaFinder; MyEtaPrimeFinder; MyRecoMCTruthLinker; MyTauFinder; MyAdd4MomCovMatrixCharged; MyPi0Finder; MyLikelihoodPID| MyPFOID												|
| PrimaryVertex                 | Vertex                   |   -					 |	VertexFinder				|  																|														|
| PrimaryVertex_RP              | ReconstructedParticle    |   -					 |	-							|	-															|														|
| ProngRecoParticles            | ReconstructedParticle    |   -					 |	-							|	-															|														|
| ProngVertices                 | Vertex                   |   -					 |	-							| MyDDMarlinPandora															|														|
| V0RecoParticles               | ReconstructedParticle    |   -					 |	-							|	-															|														|
| V0Vertices                    | Vertex                   |   -                     |	MyV0Finder					| MyDDMarlinPandora											| 														|



* this means that the processor uses the given input of a collection and adds sth, changes sth (or does whatever it does)etc.  and gives you the output of this afterwards without changing the name of the collection

there is a processor named "DSTOutput" that keeps whatever you want to keep in your dst file and drops whatever you want to drop, 
so it can't be specified which colleciton it uses as an input or output because this depends on your commands/interests




