using System;
namespace None.Commands
{class ipconfig
{public ipconfig(string[] args)
{Console.WriteLine(@"
Windows IP Configuration


Ethernet adapter Ethernet:
   Connection -specific DNS Suffix  . :
   IPv4 Address. . . . . . . . . . . : 192.168.5.250
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.5.1");

}}}