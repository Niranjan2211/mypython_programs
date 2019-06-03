#!/bin/bash


###########################################
# This script is for installing freeipa-server|freeipa-client##
# Started on 27th May 2019#################
# Written by J.Niranjan Reddy, DevOps Team#
###########################################
#clear
 





if [ "$1" == "ipa-server" ]; then

      echo ""
      echo -e "Checking Pre-flight...."
      #RPMCHK=$(rpm -qa | grep -w ipa-server)
      rpm -qa | grep -w ipa-server
        if [ "$?" == "0" ]; then
              echo "IPA-server is already installed...exiting."
              echo ""
              exit 1
              
        fi
#######################################################################    
elif [ "$1" == "ipa-client" ]; then
      
      echo ""
      echo -e "Checking Pre-flight...."
      #RPMCHK=$(rpm -qa | grep -w ipa-client)
      rpm -qa | grep -w ipa-client
        if [ "$?" == "0" ]; then
              echo "IPA-client is already installed...exiting."
              exit 1
        fi
    else
         echo ""
         echo "Usage of this script $0 ipa-server|ipa-client"
fi     
echo ""
#######################################################################
