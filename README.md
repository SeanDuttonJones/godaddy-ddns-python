# godaddy-ddns-python
A script that allows you to simulate a static IP address using the Go Daddy API. This is useful when you are running a home network and do not have access to or do not want to pay for a static IP address. 

It compares your current IP address to a Go Daddy domain and updates the domain if there is a discrepancy.

You will need to have a Go Daddy account to create public and private keys. Please note that once you create a "test" key, you will need to create a "production" key, which you will use in this script. 

https://developer.godaddy.com/

## Dependencies
The following packages need to be installed for the script to run:

- requests

## Usage
python ddns.py

This should work on all operating systems.

Note that some people have multiple versions of python installed. If this is the case, you may run python by using "python2" or "python3". In addition, if you are using cron and insert one of the examples below, make sure to change "python" to suit your scenario.

## Cron
Since most web servers are running some flavour of unix, a cron job is a great way to schedule this script to run. In terminal run crontab -e. Chose one of the examples below to insert:

### Every two minutes
*/2 * * * * python {PATH TO DDNS.PY SCRIPT}

### Every five minutes
*/5 * * * * python {PATH TO DDNS.PY SCRIPT}

### Every half hour
*/30 * * * * python {PATH TO DDNS.PY SCRIPT}

### Every hour
0 * * * * python {PATH TO DDNS.PY SCRIPT}

If these examples do not fit your fancy, a crontab generator can be found here: 

https://crontab.guru/

#### Uhh, I am lost... What is cron?

https://en.wikipedia.org/wiki/Cron

## Additional Information
The API used to retrieve your current IP address allows 1000 requests per day. If you plan on having more requests per day, there are paid options. 

https://ipinfo.io/developers
