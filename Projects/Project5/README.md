# MY PROJECT 5

## FILES CREATED AND MODIFIED
- for the /etc/hosts file, I did not create one, but modified the one that already exists on all of the systems. To configure this to I used the info provided from [How to Edit Your Hosts File on Linux, Windows, and macOS](https://linuxize.com/post/how-to-edit-your-hosts-file/), which explained that the /etc/hosts file is used to map specified domain to an ip address. And it is configured like this:
    - IPADRESS DomainName [DomainAlias]
- To be able to ssh between the systems using their provate IPaddress, I first had to add my private key to each of the systems. I then had to create a /.ssh/config file on each system that specified the host, the private IPaddress as the HostName and the location for the private key as the IdentityFile. also had to add each system to the /etc/hosts file as specified earlier. After this was all set up correctly I was able to use the ssh comand followed by the specified host name and I am able to ssh between each of the systems. 
## HAPROXY CONFIGURATION
- To install the haproxy package on my proxy system, in the cf-template I added this line "apt-get install -y git python3 python3-pip haproxy && \" to the line in hte instance creation part of the cf-template. then I ssh into the instance once it was created and used the haproxy -v comand to insure that it was installed and to see what version I was running.
## WEB SERVER CONFIGURATION
- to install apache2 on each of the web server systems, I added the line "apt-get install -y git apache2 && \" to each of the instance creation, telling aws to preinstall these packages on the instances when it creates them. I then again ssh into each instance and perform apache2 -v to insure that the package was installed, and what version was installed.
