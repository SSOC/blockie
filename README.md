#Description
Blockie is a stratum based mining protocol. It is a replacement for *getwork* based pooling servers by allowing clients to generate work. The stratum protocol is described [here](http://mining.bitcoin.cz/stratum-mining) in full detail.

This is a implementation of the stratum services various cryptocurrency coins. It is compatible with *MPOS*. The end goal is to build on these standards to come up with a more efficient, optimized and stable solution.

The goal is to make a reliable stratum mining server for various cryptocurrency coins. Over time we will develop this to be more feature rich and very stable. If you would like to see a feature please file a feature request. 

**NOTE:** This fork is still in development. Many features may be broken. Please report any broken features or issues.

#Features

* Stratum Mining Protocol
* Block Confirmation
* Job Based Vardiff support
* Solution via SHA256/Scrypt
* SHA256 and Scrypt Algo Support 
* Log Rotation
* Initial low difficulty share confirmation
* Growing cryptocurrency support
* On the fly addition of new *coind* wallets
* MySQL/PostGres/SQLite database support
* Adjustable database commit parameters
* Bypass password check for workers
* Proof Of Work and Proof of Stake Coin Support
* Transaction Messaging Support

#Donations 
Not required, please contribute back by helping with coding or tracking issues.

#Installation
The installation of this *stratum-mining* can be found in the Repo Wiki. 

#Contact
We are available in the #SSOC on irc.freenode.net
Please issue all issues via github.

#Credits

* @Slush0 - Original version by Slush0 (original stratum code)
* @GeneralFault 
* @WadeeWomersley
* @Moopless
* @viperaus
* @TheSeven
* @Ahmed_Bodi
* @Obigal