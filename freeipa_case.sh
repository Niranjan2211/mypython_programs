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
ONESPACE()
{
echo ""
}

DNSLOOKUP()
           {
              if [ "$HOSTIP" == "$LOOKUPIP" ]; then
                     echo -e "\e[1;32mDNS Resolution looks good...\e[0m"
                 else
                     echo -e "\e[1;31mDNS Resolution failed, please fix it then run this script again.\e[0m"
                     exit 1
              fi
           }

# Checking if script is being executed as not-root user,
# this script will exit if non-root user run this script.
if [ $EUID -ne 0 ]; then
   echo ""
   echo "This script must be run as root" 1>&2
   echo ""
   exit 1
fi
########################################################
VERIFYSRV=$(rpm -qa | grep -i ipa-server | wc -l)
VERIFYCLI=$(rpm -qa | grep -i ipa-client | wc -l)
MYOPTION=$1
case $MYOPTION in
    
     ipa-server)
                 ONESPACE
                 echo -e "Checking Pre-flight...."
                       ONESPACE
                       DNSLOOKUP
                       if [ "$VERIFYSRV" ==  "0" ]; then
                            ONESPACE
                            echo -e "\e[1;32mgood to proceed.\e[0m"
                           else
                               echo -e "\e[1;31mIPA-server already installed...exiting.\e[0m"
                               ONESPACE
                               exit 1
                       fi

                 ;;
      ipa-client)
                 ONESPACE
                 echo -e "Checking Pre-flight...."
                 ONESPACE
                 DNSLOOKUP
                 if [ "$VERIFYCLI" == "0" ]; then
                      ONESPACE
                      echo -e "\e[1;32mgood to proceed.\e[0m"
                   else 
                      echo -e "\e[1;31mIPA-client already installed...exiting.\e[0m"
                      ONESPACE
                      exit 1
                 fi
                   ONESPACE
                 ;;
               *)

                 ONESPACE 
                 echo -e "\e[1;31mUsage of this script $0 ipa-server|ipa-client...\e[0m"
                 ONESPACE
               ;;
esac
#######################################################################
