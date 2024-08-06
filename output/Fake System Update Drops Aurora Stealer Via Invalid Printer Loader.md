# Fake System Update Drops Aurora Stealer Via Invalid Printer Loader

Incident: Fake System Update Drops Aurora Stealer via Invalid Printer Loader

Root cause: Malvertising campaign leading to the download of a steganographically obfuscated malware loader.

Impact: 27,146 potential unique victims, 585 of them downloaded the malware. The financial losses and number of devices and people impacted are not specified in the blog.

Mitigation: Enhance browser security settings, educate users on identifying fake updates, and implement advanced threat detection mechanisms to identify and block malvertising campaigns. 

**Detailed Steps for Mitigation:**
1. **Browser Security Settings:**
   - Ensure that browser security settings are set to the highest level.
   - Use browser extensions that block malicious ads and scripts.
  
2. **User Education:**
   - Conduct regular training sessions to educate users on the signs of fake system updates and social engineering attacks.
   - Provide clear guidelines on what legitimate update notifications look like and how to verify them.
  
3. **Threat Detection:**
   - Deploy endpoint detection and response (EDR) solutions to monitor for and detect unusual activity.
   - Use threat intelligence feeds to stay updated on the latest malvertising campaigns and their indicators of compromise (IoCs).
  
4. **Network Security:**
   - Implement web filtering solutions to block access to known malicious domains.
   - Use reputation-based filtering to block suspicious URLs and IP addresses.
  
5. **Incident Response:**
   - Establish an incident response plan to quickly isolate and remediate infected systems.
   - Regularly update antivirus and anti-malware solutions to detect and block new threats.

Detection Signature:
- **Service:** Web Browser
- **Port:** 80, 443 (HTTP, HTTPS)
- **Severity:** Critical
- **Incident:** Fake System Update Drops Aurora Stealer via Invalid Printer Loader
- **Signature Name:** “Fake System Update Malvertising”
- **Internal checks:**
  - Setting1: Ensure web filtering is in place to block access to known malicious domains. – In network
  - Setting2: Ensure endpoint protection software is updated and capable of detecting Aurora Stealer. – Inside endpoints
  - Setting3: Ensure browser security settings are configured to block pop-ups and malicious scripts. – Inside endpoints
- **External scanning:**
  - Detect malicious domains associated with the campaign.
  - Monitor for unusual traffic patterns indicative of malvertising redirects.

IoCs:
- **Malvertising gate:** qqtube[.]ru, 194.58.112[.]173
- **Fake system update page:** activessd[.]ru, chistauyavoda[.]ru, xxxxxxxxxxxxxx[.]ru, activehdd[.]ru, oled8kultra[.]ru, xhamster-18[.]ru, oled8kultra[.]site, activessd6[.]ru, activedebian[.]ru, shluhapizdec[.]ru, 04042023[.]ru, clickaineasdfer[.]ru, moskovpizda[.]ru, pochelvpizdy[.]ru, evatds[.]ru, click7adilla[.]ru, grhfgetraeg6yrt[.]site, 92.53.96[.]119
- **Invalid Printer samples:** d29f4ffcc9e2164800dcf5605668bdd4298bcd6e75b58bed9c42196b4225d5905a07e02aec263f0c3e3a958f2b3c3d65a55240e5da30bbe77c60dba49d953b2c193cec31ea298103fe55164ff6270a2adf70248b3a4d05127414d6981f72cef4dac1bd40799564288bf55874543196c4ef6265d89e3228864be4d475258b906240b8acc3560ac0e1825755b3b05ef01c46bdbd184f35a15d0dc84ab44fa9906131c425510fe7f353002b7eb9d101408dde0065b160b089095a2178d1904f3434398faa3aab8cce7a12e3e3f698bc29514c5b10a4369cc386421913e31f95cfdc93b9199ca9e1ee0afbe7cf6acccedd39f37f2dd603a3b1ea05084ab29ff79df74c80bd604ae430864c507d723c6a8c66f4f5e9ba246983c833870d05219bd3e5
- **Aurora Stealer C2:** 103.195.103[.]54:443, 94.142.138[.]218:4561
- **Amadey Stealer panel:** 193.233.20[.]29/games/category/Login.php
