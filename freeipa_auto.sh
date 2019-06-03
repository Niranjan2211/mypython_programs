#!/bin/bash


###########################################
# This script is for installing freeipa-server|freeipa-client##
# Started on 27th May 2019#################
# Written by J.Niranjan Reddy, DevOps Team#
###########################################
#clear
HOSTIP=$(hostname -i)
HOSTNAME=$(hostname -s)
DOMAIN=$(hostname -d)
REALM=$(echo ${DOMAIN} | tr '[:lower:]' '[:upper:]')
LOOKUPIP=$(host ${HOSTNAME} | awk '{print $4}')

# Checking if script is being executed as not-root user,
# this script will exit if non-root user run this script.
if [ $EUID -ne 0 ]; then
   echo ""
   echo "This script must be run as root" 1>&2
   echo ""
   exit 1
fi
########################################################

if [ "$1" == "ipa-server" ]; then

      echo ""
      echo -e "Checking Pre-flight...."
         if [ "$HOSTIP" == "$LOOKUPIP" ]; then
               echo -e "DNS Resolution looks good.."
            else
               echo -e "\e[1;31mDNS Resolution failed, please fix it then run this script again.\e[0m"
         fi
      
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
