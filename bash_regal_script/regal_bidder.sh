#!/bin/bash
# site=$1
# username=$2
# password=$3
# bid_amount=$4

echo "Please enter the site: "
read site
echo "Please enter the username: "
read username
echo "Please enter your password: "
read password
echo "Please enter the maximum bid amount: "
read bid_amount


python regal_bidder_cl_args.py $site $username $password $bid_amount

