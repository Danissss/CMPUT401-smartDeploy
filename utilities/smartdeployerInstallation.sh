#!/bin/bash

sudo chmod u+x *.sh

KEYNAME=$1
OPTION=$2

if [ "$OPTION" == "install" ];
	then
	./setup.sh -k $KEYNAME
elif [ "$OPTION" == "update" ];
	then
	./update.sh -k $KEYNAME
elif [ "$OPTION" == "uninstall" ];
	then
	./uninstall.sh -k $KEYNAME
else
	echo "Couldn't recongnize command"
fi