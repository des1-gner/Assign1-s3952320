The main script is mazeTester.py.
There are two sample configuration files, sampleConfig01.json and sampleConfig02.json.  These specify the parameters used to run the maze generation.

To run the script, go to the same folder/directory that this README.txt file is located, and execute:

On Windows:
    python mazeTester.py sampleConfig01.json
On *nix, particularly core teaching servers:
    python3 mazeTester.py sampleConfig01.json

On the core teaching servers, matplotlib isn't installed, hence visualisation won't work.  Please run the visualisation on your own machines.

Please avoid modifying the provided files, apart from implementing adjListGraph.py and adjMatGraph.py, and possibly graphMaze.py
If you must modify anything, please check in with the FAQ or teaching team first.