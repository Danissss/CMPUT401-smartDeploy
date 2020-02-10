# Description:

## Parser:
Parser need to run inside the cassandra docker container([docker_cassandra](https://github.com/docker-library/cassandra])). The program will run 7 workloads from [YCSB](https://github.com/brianfrankcooper/YCSB), and parse and commit the important information from ycsb report into remote mysql server.

## Smartdeployer:
Smardeployer need to run remote server (e.g. [cybera](https://www.cybera.ca/) virtual machine, AWS E2 instance, etc.) with Ubuntu 16.04. User has to configure and provide keypair for each virtual machine (more details see Smartdeployer [ReadMe.md](https://github.com/Zhipeng-Chang/CMPUT-401-Winter-2018/tree/master/Deployer/automatic%20installation%20and%20uninstallation)). This program will help user automatically update, install, update cassandra docker for all given virtual machines.


## Possible issue:

You may have the issue of "sudo unable to resolve host"

Solution:

1. ```$cd /etc/```
2. find and look into file "hostname" to check the host name
3. find and open file "hosts" with terminal editor (e.g. nano, vim, etc.)
4. add "127.0.1.1 [your hostname]" under "127.0.0.1 localhost" (notes: no quotation when you type in)
5. save it 
6. go back to run the script
7. For more information, you can check https://askubuntu.com/questions/59458/error-message-sudo-unable-to-resolve-host-user

Create keypair:
1. create keypair inside directory .ssh 
```
cd ~/.ssh/
touch <your_keypair_name>

```
2. copy the private key and paste into the new created file
