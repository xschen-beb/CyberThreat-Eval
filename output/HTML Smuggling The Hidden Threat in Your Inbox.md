# HTML Smuggling The Hidden Threat in Your Inbox

Incident: HTML Smuggling: The Hidden Threat in Your Inbox

Root cause: Exploitation of HTML5 features in email attachments

Impact: Multiple malware campaigns detected. Specific numbers for devices, people impacted, and financial losses are not provided.

Mitigation:
1. **Email Security Solutions**:
   - Implement advanced email filtering solutions that can detect and block HTML smuggling attempts.
   - Use sandboxing to analyze attachments in a controlled environment before delivering them to the end-users.

2. **Endpoint Protection**:
   - Ensure endpoint protection solutions are updated to detect and block malicious scripts and payloads dropped by HTML smuggling.

3. **User Training and Awareness**:
   - Conduct regular training sessions to educate users about the risks of opening email attachments and links from unknown sources.
   - Encourage users to report suspicious emails to the IT department.

4. **Browser Security**:
   - Configure browsers to limit the execution of JavaScript from untrusted sources.
   - Use browser security plugins that can detect and block potentially harmful scripts.

Detection Signature:
    Service: Web Browser (Chrome, Firefox, etc.)
    Port: N/A (as this is related to browser activity)
    Severity: Critical
    Incident: HTML Smuggling
    Signature name: “HTML Smuggling Detected”
    Internal checks:
        - Setting1: Monitor for the use of `msSaveOrOpenBlob` function in HTML files.
        - Setting2: Inspect for obfuscated JavaScript code that attempts to decode and save binary blobs.
        - Setting3: Check for unexpected downloads initiated by email attachments.
    External scanning:
        - Monitor network traffic for suspicious external connections initiated by browsers after opening email attachments.
        - Detect and block access to known malicious domains and URLs associated with HTML smuggling.

IoCs:
Qakbot
- Document1611.html: b79ff504eb6ec509b8b6b870dc2f0113825d859b
- Document1611.zip: b5da32a803b31d769d4d330e9c923d8c2dc5da1f
- File577.lnk: d92b31ddf25e30e7cc34239bf45c7ec913b713c4
- enhrP.s_1L.QH0w.js: 0d17a7f60f7f5a6d5e00ed23635dd4998a5df307
- _OIV.dll (Qakbot DLL): 78542b48745136d9e77896ec77c7613c4386ad81
- jackboots.tmp (Qakbot DLL): ed67cb8a6c44871ec6ffb6517d77b5e84f00b399
- PE40.vhd (VHD containing Qakbot): 55781d120a91b71da2c51ed3657a73e819493f38
- Download URL for JS: hxxps://purepowerinc[.]net/nluGZ/082.html
- Download URL for DLL (Qakbot): hxxps://huhuwarcanoefestival[.]com/iSx1Ch/0509.html

IcedID
- alljumping,doc,09.30.22.html: 07251deafd605437a25d51428aade79255036d49
- 3ebdb69f-1430-4414-ace5-a413e8bdb9cd.zip: df3f2f97383d4ae897b3197e8d07f474f651a053
- scandocument-83848d84-c26a-4bc9-95f5-10f288709ff7.iso: cffb01d11245792b5498c051603a279b0ad1930d
- scandocument-83848d84-c26a-4bc9-95f5-10f288709ff7.lnk: 702631c91a8fe86b2e75f4a6b089d00b7762ff1b
- 0e7132bf-c75b-4ff9-ab6a-0db25f7250a4.W6_ (IcedID DLL): 15f8a879534143a4169c6ecd1d56132d1908443d
- d5216149-74d2-4662-a923-3ea963ef2a5a.png: b6b61511ea7a36015f8002922bc20ad1f42234ab

Cobalt Strike
- a5c7f1e3-e33c-4dd8-bd27-f40fba04cb5d.html: ce4611b2d2e326ff7b37acdc10636f0dcd9439ba
- Bill-1208-1113add9551798.iso: 63adbabf3dfde36e745f4c42979260a2e946848c
- Bill-1208.lnk: 0afe54c016f4770ad2a8690ef9a06b1f53804215
- bbftullzytwpbp.log (PS1 stager): 23b950b209cb16b084cad87c006dc7691c60dc40
- fwoebcdndjhrmrn.log (PS1 CobaltStrike): 4b9d2f4b80ef9578711c569524694905012a8080
- vqulmjurow.pdf (Decoy PDF document): fbc916f065157cc5a13f22453c19f7dfecc3c228
- C2 server: hxxp[://]165[.]22[.]48[.]183/common?chunk=false

Xworm
- ERYASZBM279.html: 207b87124f8abe2226251eb84f033e8642418fb1
- US-ERYASZBM279.iso: e318c01fcd1f711fd063e845ca2431012086658f
- us1012401.vbs: 35b9fd8856edd443a4e27727c54dd135e26220bd
- dll2.txt (Initial DLL): efd195d8ef795e123bb1c1faee77459a781c003e
- weslle.txt (Xworm): 8cb57a7e1e929c48716974edf55df2e9456d1443
- Pe.txt (Stager DLL): 7a7e76553dafc2c1b6a0d804aa540ab7a80fd77b
- hxxp://5[.]42[.]199[.]235/dll/dll2.txt
- hxxp://5[.]42[.]199[.]235/pe/Pe.txt
- hxxps://beautiful-elion[.]68-64-160-26[.]plesk[.]page/weslle.txt
