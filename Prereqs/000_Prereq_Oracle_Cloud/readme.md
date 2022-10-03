# Setting up Oracle cloud


y
#### Setup and use SSH on Windows

https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/accessinginstance.htm


To connect to a Linux instance from a Windows system using OpenSSH

If the instance uses a key pair that was generated by Oracle Cloud Infrastructure, use the following procedure.

If this is the first time you are using this key pair, you must set the file permissions so that only you can read the file. Do the following:
  In Windows Explorer, navigate to the private key file, right-click the file, and then click Properties.
  On the Security tab, click Advanced.
  On the Permissions tab, for Permission entries, under Principal, ensure that your user account is listed.
  Click Disable Inheritance, and then select Convert inherited permissions into explicit permissions on this object.
  For Permission entries, select each permission entry that is not your user account and click Remove.
  Ensure that the access permission for your user account is Full control.
  Save your changes.

To connect to the instance, open Windows PowerShell and run the following command

```ssh -i .\ssh-key-2022-09-07.key ubuntu@150.136.53.57``

#### Connecting to Oracle in PowerShell

ssh -i <private_key_file> <username>@<public-ip-address>

ssh -i ssh-key-2022-09-07.key ubuntu@150.136.53.57


