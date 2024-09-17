#### Description
Recently, systems security consultant Daniel Milisic discovered that an Android TV box purchased from Amazon was pre-loaded with persistent, sophisticated malware baked into its firmware. The T95 streaming device uses an Android 10-based ROM signed with test keys and the ADB (Android Debug Bridge) open over Ethernet and WiFi. This is a suspicious configuration as ADB can be used to connect to devices for unrestricted filesystem access, command execution, software installation, data modification, and remote control. 

While analyzing the DNS request in Pi-hole, Milisic discovered that the device was attempting to connect to several IP addresses associated with active malware.  Milisic believes the malware installed on the device is a strain that resembles 'CopyCat,' a sophisticated Android malware first discovered by Check Point in 2017. This malware was previously seen in an adware campaign where it infected 14 million Android devices to make its operators over $1,500,000 in profits.

#### Reference URL(s)
1. https://www.malwarebytes.com/blog/news/2023/01/preinstalled-malware-infested-t95-tv-box-from-amazon
2. https://www.bleepingcomputer.com/news/security/android-tv-box-on-amazon-came-pre-installed-with-malware/
3. https://github.com/DesktopECHO/T95-H616-Malware

#### Publication Date
January 30, 2023

#### Author(s)
Nathan Colliere
Bill Toulas  
Daniel Milisic 