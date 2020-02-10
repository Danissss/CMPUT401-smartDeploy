Description:

This script file automatically install docker and setup numbers of docker containers for user


Software requirement:
Linux programming environment



##Usage:

#make it executable 
```
$chmod u+x smartDeployer.sh
```

run it with default setting: numbers of container: 1; optimization: OFF;
```
$./smartDeployer.sh 

```

#user can define how many docker container they want by using "-c [numbers of container]" <br/>
#example (create 5 containers; optimization OFF):
```
$./smartDeployer.sh -c 5 
```
#note: the number has to be larger than 0 and smaller than 100


#user can enable optimization option by using "-o ON"
#example (create 5 containers; optimization ON):
```
$./smartDeployer.sh -c 5 -o ON
```
#note: input has to be capitalized e.g. "ON" or "OFF"




##Possible issue:

You may have the issue of "sudo unable to resolve host"

Solution:

1. ```$cd /etc/```
2. find and look into file "hostname" to check the host name
3. find and open file "hosts" with terminal editor (e.g. nano, vim, etc.)
4. add "127.0.1.1 [your hostname]" under "127.0.0.1 localhost" (notes: no quotation when you type in)
5. save it 
6. go back to run the script
7. For more information, you can check https://askubuntu.com/questions/59458/error-message-sudo-unable-to-resolve-host-user








