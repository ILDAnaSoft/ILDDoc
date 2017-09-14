# Processors for reconstructed particles 

|processor name| explaination |
|:------------:|:------------:|
|AIDAProcessor| Creates on directory per processor,Needs to be the first ActiveProcessor |
|LCIOOutputProcessor|output reconstruction information to slcio file|
|InitDD4hep |InitializeDD4hep reads a compact xml file and initializes the DD4hep::LCDD object|
|Statusmonitor|prints out information on running Marlin Job|
|BgOverlay|Opens a second (chain of) lcio file(s) and overlays events|
|SplitCollectionByLayer|split a hit collection based on the layer number of the hits|
|DDPlanarDigiProcessor|creates TrackerHits from SimTrackerHits|
|SpacePointBuilder| combine si-strip measurements into 3D spacepoints |
|DDSpacePointBuilder| SpacePointBuilder combine si-strip measurements into 3D spacepoints|
|TPCDigiProcessor|Produces TPC TrackerHit collection from SimTrackerHit collection|
|ClupatraProcessor|nearest neighbour clustering seeded pattern recognition|
|SiliconTracking_MarlinTrk|Pattern recognition in silicon trackers|  
|ForwardTracking|create fwd tracks in parallel|
|TrackSubsetProcessor|takes tracks from multiple sources and outputs them |
|CellsAutomatonMV|ForwardTracking reconstructs tracks through the FTDs|
|FullLDCTracking_MarlinTrk|Performs full tracking in ILD detector|
|Compute_dEdxProcessor|Energy Loss Error for TPC| 
|ForwardTracking|reconstructs tracks through the FTDs|
|TruthTracker|Creates Track Collection from MC Truth. Can handle composite spacepoints as long as they consist of two TrackerHits|
|V0Finder||
|KinkFinder||
|RealisticCaloDigiSilicon||
|RealisticCaloRecoSilicon||
|BruteForceEcalGapFiller||
|RealisticCaloDigiScinPpd||
|RealisticCaloRecoScinPpd||
|SimpleFCalDigi|Performs simple digitization of sim calo hits|
|SimpleMuonDigi|Performs simple digitization of sim calo hits|
|DDPandoraPFANewProcessor||
|BeamCalClusterReco|akes a list of beamcal background files from the ReadBeamCalprocessor, adds NumberOfBX of them together and puts the signal hits from thelcio nput file on top of that, and then clustering is attempted|
|BCalReco|Filling Histograms with deposited energy from beamstrahlung pairs in BeamCal|
|PFOID|Performs particle identification|
|Add4MomCovMatrixCharged||
|AddClusterProperties||
|ComputeShowerShapesProcessor||    
|GammaGammaSolutionFinder|| 
|DistilledPFOCreator|| 
|LikelihoodPIDProcessor|Performs particle identification|
|RecoMCTruthLinker|links RecontructedParticles to the MCParticle based on number of hits used| 
|ComputeShowerShapesProcessor|Performs Shower profile extraction|
|TaJetClustering|Performs tau jet finding|
|AddClusterProperties||
|LcfiplusProcessor||
|PfoAnalysis|PfoAnalysis analyses output of PandoraPFANew|
|Add4MomCovMatrixCharged|Set the convariance matrix in (P,E) for all charged pfos in PandoraPFOs Collection|
|GammaGammaCandidateFinder||


