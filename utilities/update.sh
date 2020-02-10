#!/bin/bash

POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -k|--keyname)
    KEYNAME="$2"
    shift # past argument
    shift # past value
esac
done

set -- "${POSITIONAL[@]}" # restore positional parameters

echo "y"|sudo apt-get install docker-ce

# test if ip.txt exist

input_ip=$(cat ip.txt)
if [ "$input_ip" == "cat: ip.txt: No such file or directory" ];
then
      echo "can't find ip.txt (program exit)"
      exit 1
fi

# test if ip.txt is empty
total_ip=0
ip="ip"
IFS=' ' read -ra ADDR <<< "$input_ip"
for i in "${ADDR[@]}";
do
    ((total_ip++))
    # process "$i"
    done
if [ "${total_ip}" -le 0 ]; then
    echo "installation done"
    exit 1
fi
if [ -z "$KEYNAME" ];
then
    echo "Please input your key name (more detail see README.md)"
    exit 1
fi

# test if the key is empty
COMMAND1=""
for i in $input_ip;
    do
        COMMAND1="$COMMAND1 ssh -i ~/.ssh/$KEYNAME ubuntu@$i \"echo 'Y' |sudo apt-get install docker-ce\" |"
    done

COMMAND1Mo1="${COMMAND1% |}"
COMMAND1Mo1="${COMMAND1Mo1# }"
eval "$COMMAND1Mo1"
echo "$COMMAND1Mo1"


echo "update docker-ce done"
