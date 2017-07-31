# KB
Knowledge Base Directory 

This directory contains knowledge bases consisting of ConceptNet, InsectPoison, and a split WordNet with tools for loading them. As well as Poison and Insect articles that will be used for stimulation within the LoggerAgent.cc

Within the LoggerAgent.cc (under opencog/experiments/insect-poison) adjust the Parser path in the initializer to point to the insect_text and poison_text in the KB. Also under the getAtomsTrack() method, adjust the relevant_nodes to the one in the KB.

To Load Wordnet: 
	1.Verify the splitFiles directory has scm files (roughly 186605 blocks)
	2.Verify the shell file is executable (chmod +x loadSplitWordnet.sh)
	3.Run the shell file with more memory allocation to it while the cogserver is started (./loadSplitWordnet.sh ulimit -m 10000000)

To Load ConceptNet and/or InsectPoison:
	1. echo scm | cat <conceptnet4.scm or InsectPoison.scm> | telnet localhost 17001
