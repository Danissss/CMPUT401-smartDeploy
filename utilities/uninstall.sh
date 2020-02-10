#!/bin/bash



#setup for each vm

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


#uninstallfor first vm (master vm)
sudo systemctl stop docker
sudo apt-get purge -y docker-engine docker docker.io docker-ce
sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce
sudo apt-get autoclean

sudo rm -rf /var/lib/docker
sudo rm /etc/apparmor.d/docker
sudo groupdel docker

# test if ip.txt exist
input_ip=$(cat ip.txt)
if [ "$input_ip" == "cat: ip.txt: No such file or directory" ]
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

# test if the key is empty
if [ -z "$KEYNAME" ];
	then
	echo "Please input your key name (more detail see readme)"
	exit 1
fi

COMMAND1=""
COMMAND2=""
COMMAND3=""
COMMAND4=""
COMMAND5=""
COMMAND6=""
COMMAND7=""
for i in $input_ip;
	do
		COMMAND1="$COMMAND1 ssh -i ~/.ssh/$KEYNAME ubuntu@$i \"sudo systemctl stop docker \" |"
		COMMAND2="$COMMAND2 ssh -i ~/.ssh/$KEYNAME ubuntu@$i \"sudo apt-get purge -y docker-engine docker docker.io docker-ce\" |"
		COMMAND3="$COMMAND3 ssh -i ~/.ssh/$KEYNAME ubuntu@$i \"sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce\" |"
		COMMAND4="$COMMAND4 ssh -i ~/.ssh/$KEYNAME ubuntu@$i \"sudo apt-get autoclean\" |"
		COMMAND5="$COMMAND5 ssh -i ~/.ssh/$KEYNAME ubuntu@$i \"sudo rm -rf /var/lib/docker\" |"
		COMMAND6="$COMMAND6 ssh -i ~/.ssh/$KEYNAME ubuntu@$i \"sudo rm /etc/apparmor.d/docker\" |"
		COMMAND7="$COMMAND7 ssh -i ~/.ssh/$KEYNAME ubuntu@$i \"sudo groupdel docker\" |"
	done

COMMAND1Mo1="${COMMAND1% |}"
COMMAND1Mo1="${COMMAND1Mo1# }"
eval "$COMMAND1Mo1"
echo "$COMMAND1Mo1"
COMMAND2Mo1="${COMMAND2% |}"
COMMAND2Mo1="${COMMAND2Mo1# }"
eval "$COMMAND2Mo1"
echo "$COMMAND2Mo1"
COMMAND3Mo1="${COMMAND3% |}"
COMMAND3Mo1="${COMMAND3Mo1# }"
eval "$COMMAND3Mo1"
echo "$COMMAND3Mo1"
COMMAND4Mo1="${COMMAND4% |}"
COMMAND4Mo1="${COMMAND4Mo1# }"
eval "$COMMAND4Mo1"
echo "$COMMAND4Mo1"
COMMAND5Mo1="${COMMAND5% |}"
COMMAND5Mo1="${COMMAND5Mo1# }"
eval "$COMMAND5Mo1"
echo "$COMMAND5Mo1"
COMMAND6Mo1="${COMMAND6% |}"
COMMAND6Mo1="${COMMAND6Mo1# }"
eval "$COMMAND6Mo1"
echo "$COMMAND6Mo1"
COMMAND7Mo1="${COMMAND7% |}"
COMMAND7Mo1="${COMMAND7Mo1# }"
eval "$COMMAND7Mo1"
echo "$COMMAND7Mo1"

echo "unistallation done"

