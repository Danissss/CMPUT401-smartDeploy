#!/bin/bash
# this program automatically run five different workloads provided from ycsb
# the output files are named respectively: workloada.txt, workloadb.txt, workloadc.txt
# workloadd.txt, workloade.txt
# at the end the python script will output a nice table with all information
# cql file will clean all the database for next iteration

# required file:
# ycsb_setup.cql
# output.py
# ycsb_cleanup.cql

# download ycsb
# in the container


POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"

 
case $key in
    -m|--memory)
    MEMORY="$2"
    shift # past argument
    shift # past value
    ;;
    -c|--cpu)
    CPU="$2"
    shift # past argument
    shift # past value
    ;;
    -b|--blkio)
    BLKIO="$2"
    shift # past argument
    shift # past value
    ;;
    -i|--ip)
    IP="$2"
    shift # past argument
    shift # past value
    ;;
    # -l|--lib)
    # LIBPATH="$2"
    # shift # past argument
    # shift # past value
    # ;;
    # --default)
    # DEFAULT=YES
    # shift # past argument
    # ;;
    # *)    # unknown option
    # POSITIONAL+=("$1") # save it in an array for later
    # shift # past argument
    # ;;
esac
done

set -- "${POSITIONAL[@]}" # restore positional parameters

SYSTEM_RESOURCE=${MEMORY}_${CPU}_${BLKIO}
# echo ${SYSTEM_RESOURCE}
# exit 1



# apt-get update
# apt-get install curl
# apt-get install python-pip
# obtain the ycsb
curl -O --location https://github.com/brianfrankcooper/YCSB/releases/download/0.12.0/ycsb-0.12.0.tar.gz
tar xfvz ycsb-0.12.0.tar.gz
rm ycsb-0.12.0.tar.gz

    #install pip and mysql-connector  and  give the general report via python file
pip install --allow-external mysql-connector-python mysql-connector-python


# set_up the ycsb
cqlsh -e "create keyspace if not exists ycsb WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor': 1 };"
cqlsh -e "create table if not exists ycsb.usertable (y_id varchar primary key, field0 varchar, field1 varchar, field2 varchar, field3 varchar, field4 varchar, field5 varchar, field6 varchar, field7 varchar, field8 varchar, field9 varchar) with compression = {'sstable_compression': ''};"


# step 1. get the ip address
# make the output as variable
# OUTPUT="$(ls -1)"
# echo "${OUTPUT}"


# load data
./ycsb-0.12.0/bin/ycsb load cassandra-cql -p hosts=${IP_address} -P ./ycsb-0.12.0/workloads/workloada -s > ../workload_load_outputa.txt
# step 2. generate five report

declare -a arr=("a" "b" "c" "f" "d")
for i in "${arr[@]}"
do
./ycsb-0.12.0/bin/ycsb run  cassandra-cql -p hosts=${IP_address} -P ./ycsb-0.12.0/workloads/workload${i} -s > ../workload_run_output${i}.txt
# or do whatever with individual element of the array
done

#remove all data in table
cqlsh -e "TRUNCATE ycsb.usertable;"
#for rest of workload
# load workloade
./ycsb-0.12.0/bin/ycsb load cassandra-cql -p hosts=${IP_address} -P ./ycsb-0.12.0/workloads/workloade -s > ../workload_load_outpute.txt

./ycsb-0.12.0/bin/ycsb run  cassandra-cql -p hosts=${IP_address} -P ./ycsb-0.12.0/workloads/workloade -s > ../workload_run_outpute.txt


python generateReport.py 
python commitToDatabase.py ${MEMORY} ${CPU} ${BLKIO} None

# clean up the ycsb
cqlsh -e "TRUNCATE ycsb.usertable;"

rm *.txt
echo "finished"
exit 1


