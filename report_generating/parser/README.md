## Usage:
1. run script:
```
$./parser.sh -m {container memory} -c {container cpu} -b {container blockI/O}
```
1.1 get all standard ycsb test report (no multiple threads) from five workload
1.2 put them all together in one file
1.3 commit them to database


2. run test:
```
$python3 UnitTest.py {container memory} {container cpu} {container blockI/O}
```
2.1 return all the data from defined memory, cpu and blockIO



How to remotely connect to the mysql database?
```
$mysql -h 162.246.156.220 -u root -p'password'
```
then select smartdeployer database
```
mysql>use smartdeployer;
```
