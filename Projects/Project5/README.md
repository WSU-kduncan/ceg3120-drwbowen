# MY PROJECT 5

## FILES CREATED AND MODIFIED
- for the /etc/hosts file, I did not create one, but modified the one that already exists on all of the systems. To configure this to I used the info provided from [How to Edit Your Hosts File on Linux, Windows, and macOS](https://linuxize.com/post/how-to-edit-your-hosts-file/), which explained that the /etc/hosts file is used to map specified domain to an ip address. And it is configured like this:
    - IPADRESS DomainName [DomainAlias]
- To be able to ssh between the systems using their provate IPaddress, I first had to add my private key to each of the systems. I then had to create a /.ssh/config file on each system that specified the host, the private IPaddress as the HostName and the location for the private key as the IdentityFile. also had to add each system to the /etc/hosts file as specified earlier. After this was all set up correctly I was able to use the ssh comand followed by the specified host name and I am able to ssh between each of the systems. 
