# Communicate file between client and server HW
## Installation
1. Clone the repository. 
2. Install a version of python 3.x (preferably 3.10).
3. Install zmq - "pip install pyzmq"
4. Run the application:
- There are two sets of files in the ./bin folder.
- One set of files is for a ZeroMQ client, server connection
- A second set of files for shared memory client, server connection

To Run the application, bring up a terminal (I tested on Windows), navigate to
the bin directory. Start first by running the server for either ZeroMQ or the 
shared-memory client/server. There should be logging to the terminal as the 
application runs. Open a ***second terminal***, navigate to the ./bin directory 
and run the respective client. The output file (i.e. output.stl) will show
up in the ./data directory. 

## Notes:
- There is a configuration file for ZeroMQ to set IPs, and defaults to localhost.
  Theoretically, the client and server could run on separate machines, as long
  as there is no firewall in the way, and connectivity between the hosts.
- The shared memory queue version of the client-server will need to run on the same host.
- Due to size of the code, did not include proper documentation for all classes/functions, such 
  as documenting function inputs and outputs.
- There are many, many ways to distribute and deploy python applications. Examples include raw-python,
  Docker containers, virtual environments, egg files, RPMs, etc. Also, there are many systems to target, 
  which include (but not limited to) Windows, Linux, K8s, etc.. Because of packaging and targeting,
  distribution and running was kept very simplistic.
- Perhaps one more improvement would be to include a single server and client script and a command
  line argument to specify ZeroMQ vs. shared-memory server/client. Also, bash scripts to run on linux, 
  but due to lack of linux, I was unable to test.
- Lots of object-orientation was used, which in some cases may seem like abuse, but would allow for greater
  flexibility.

## Author
[Eric First](https://github.com/cloodve)
