#!/bin/bash

# smartdeployer install script
# version 1.0
# required file:
# 1. all.tar
# 

#default setting
CONTAINTERS=1
OPTIMIZE="OFF"

#docker installation function

function install_docker {

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt-get update

    # install docker
    sudo apt-get install -y docker-ce

    # all setup, docker is running, pull cassandra from docker hub
    sudo docker pull cassandra

}

# return the most suitable parameters
# 1. cp the all.tar (contain the file that benchmark the container)
function find_the_optima {

    #cpu divison factor = 4
    #note: input memory in mb format; e.g 16gb ram = 16000mb ram
    #note: Block IO (relative weight), between 10 and 1000, or 0 to disable (default 0) 
    TOTALBLK=1000
    CPU_division_Factor=$((TOTAL_CPU / 4 ))
    MEMORY_division_Factor=$((TOTALMEMORY / 4))
    BLKIO_division_Factor=$((TOTALBLK / 4))

    sudo docker run -d -P --name "test_container" cassandra
    sudo docker cp all.tar test_container:/all.tar
    sudo docker exec -it test_container tar xvfz all.tar
    # this will get the default container data, and push the info into the database
    # later, just select the most powerful parameters in database
    sudo docker exec -it test_container ./all.sh ${TOTALMEMORY} ${TOTAL_CPU} ${TOTALBLK}

    for ((CPU=$CPU_division_Factor;CPU<=${TOTAL_CPU};CPU+=$CPU_division_Factor))
        do
            for ((MEMORY=$MEMORY_division_Factor;MEMORY<=${TOTALMEMORY};MEMORY+=$MEMORY_division_Factor))
                do
                    for ((BLKIO=$BLKIO_division_Factor;BLKIO<=${TOTALBLK};BLKIO+=$BLKIO_division_Factor))
                        do
                            # this command works
                            # sudo docker update --memory=500m --cpus=1.0 demo
                            sudo docker update --cpus=$CPU -m=MEMORY"m" --blkio-weight=BLKIO "test_container"
                        done
                done
        done

    # after all the loop done, you get all the information in the mysql database
    # run the script that connect to database and get the most value; set them as variable

}



POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"
 
case $key in
    -c|--container)
    CONTAINTERS="$2"
    shift # past argument
    shift # past value
    ;;
    -o|--optimize)
    OPTIMIZE="$2"
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
 
# echo Numbers of Containers  = "${CONTAINTERS}"
# echo Optimization is = "${OPTIMIZE}"

#if user input is less than 0: warning; if user input is greater than 100 (number may fix), warning
#  ${CONTAINERS} will return int, not string
if [ "${CONTAINTERS}" -le 0 ]; then
    echo Containers number has to greater than 0
    exit 1

elif [ "${CONTAINTERS}" -gt 100 ]; then
    echo Containers number is way too big
    exit 1
fi



# optimization option;
# space matters!!!  ["$OPTIMIZE" == "ON"] won't work
if [ "$OPTIMIZE" == "ON" ]; then

    echo "optimize ON"
    install_docker
    find_the_optima
    # get the desired output for cpu memory blockio
    # implment them below docker run command
    for ((container_num=0;container_num<${CONTAINTERS};container_num++))
        do
            sudo docker run -d -P --name "demo"$container_num cassandra
        done
    echo "${CONTAINTERS} containers generated."
    #show all the created containers
    sudo docker stats -a --no-stream
    

    
elif [ "$OPTIMIZE" == "OFF" ]; then
    echo "optimize OFF"
    install_docker
    for ((container_num=0;container_num<${CONTAINTERS};container_num++))
        do
            sudo docker run -d -P --name "demo"$container_num cassandra
        done
        
else
    echo "Please choose ON or OFF for optimize option (Capitalized)"
fi
























