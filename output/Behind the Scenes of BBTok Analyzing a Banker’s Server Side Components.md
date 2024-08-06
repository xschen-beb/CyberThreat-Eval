# Behind the Scenes of BBTok Analyzing a Banker’s Server Side Components

### Incident: BBTok Banker Campaign

**Root Cause:** Misconfigured XAMPP-based server

**Impact:** Hundreds of users in Brazil and Mexico; financial losses estimated based on banking trojan activities, but exact figures are not provided in the report.

**Mitigation:** 
1. **Secure server configurations**:
    - Ensure the XAMPP server is not exposed to the public internet unless necessary.
    - Regularly update and patch the XAMPP software and underlying services.
2. **Implement Network Segmentation**:
    - Isolate web servers from critical infrastructure.
3. **Employ Strong Authentication Mechanisms**:
    - Use multi-factor authentication (MFA) to access server management interfaces.
4. **Monitor and Respond**:
    - Continuously monitor server access logs for unusual activity.
    - Implement an incident response plan for quick mitigation of future breaches.
5. **Limit Geolocation Access**:
    - Configure access controls to limit connections to known geolocations only.

**Detailed Steps for Mitigation:**
1. **Update XAMPP**:
    - Regularly update XAMPP to the latest version by downloading from the official website.
    - Apply patches promptly.

2. **Configuration Hardening**:
    - Disable any unnecessary services in the XAMPP configuration.
    - Ensure that sensitive files (like `db.php` and `descarga.php`) are not publicly accessible.
    - Use `.htaccess` to restrict access to sensitive directories.

3. **Authentication and Access Control**:
    - Implement strong passwords and multi-factor authentication for accessing the XAMPP admin panel.
    - Restrict IP addresses that can access the admin panel using firewall rules.

4. **Network Segmentation**:
    - Place the XAMPP server on a segmented network and restrict traffic to and from this segment using firewall rules.

5. **Monitoring and Logging**:
    - Enable detailed logging on the server.
    - Use tools like Fail2Ban to block malicious IPs.
    - Regularly review logs for signs of compromise.

6. **Geolocation Access Control**:
    - Configure the server to block or flag requests from non-targeted geolocations.
    - Use services like Cloudflare for geolocation-based access control.

**Detection Signature:**
- **Service**: XAMPP-based Server
- **Port**: 80, 443 (HTTP, HTTPS)
- **Severity**: Critical
- **Incident**: BBTok Banker Campaign
- **Signature name**: "BBTok Payload Distribution"
- **Internal checks**:
    - **Setting1**: Ensure XAMPP services are not exposed to the internet without proper security measures.
    - **Setting2**: Sensitive scripts (e.g., `descarga.php`) should not be accessible externally.
    - **Setting3**: Enable authentication for accessing sensitive resources.
- **External scanning**:
    - **Port 80, 443 open**: Check for XAMPP service exposure.
    - **Public access to sensitive scripts**: Verify if scripts like `descarga.php` are accessible from the internet.

**IoCs:**
- **IP Addresses**:
    - 216[.]250[.]251[.]196
    - 173[.]249[.]196[.]195
    - 176[.]31[.]159[.]196
    - 147[.]124[.]213[.]152

- **Domains**:
    - danfe[.]is-certified[.]com
    - rendinfo[.]shop
    - odkvsodkv[.]supplier[.]serveftp[.]net

- **Files**:
    - DANFE357702036539112.iso
    - DANFE357666506667634.iso
    - DANFE352023067616112.iso
    - DANFE358567378531506.pdf
    - Brammy.dll
    - Trammy.dll
    - HtmlFactura
    - DPCYKJ4Ojk.iso
    - HtmlFactura-497fc589432931214ed0f7f4de320f3brzi8y1MTdn.iso
    - HtmlFactura-4887f50edb734a49d33639883b60796do52lTREjMh.iso
    - Html-Factura35493606948895934113728188857090JCOY.pdf
    - Kammy.dll
    - Gammy.dll
    - ze.docx
    - xll.xll

- **Hashes**:
    - be36c832a1186fd752dd975d31284bdd2ac3342bd3d32980c6c52271d0d2c84c
    - 095b793d60ce5b15fac035e03d41f1ddd2e462ec4fa00ccf20553af3c09656f6
    - 8e65383a91716b87651d3fa60bc39967927ab01b230086e3c5a2f9a096fc6c57
    - 825a5c221cb8247831745d44b424954c99e9023843c96def6baf84ccb62e9e5f
    - e5e89824f52816d786aaac4ebdb07a898a827004a94bee558800e4a0e29b083a
    - 07028ec2a727330a3710dba8940aa97809f47e75e1fd9485d8fc52a3c018a128
    - 808e0ddccd5ae4b8cbc4747a5ee044356b7aa67354724519d1e54efb2fc4f6ec
    - f83b33acfd9390309eefb4a17b42e89dcdbe759757844a3d9b474d570ddbab86
    - dbeb4960cdb04999c1a5a3360c9112e3bc1de79534d7ac9027b7fdb7798968a6
    - be35b48dfec1cc2fc046423036fa76fc9096123efadac065c80361c45f401d3c
    - 9d91437a3bfd37f68cc3e2e2acfbbbbfffa3a73d8f3f466bc3751f48c6e1b40e
    - d9b2450e4b91739c39981ab34ec7a3aeb33fb3b75deb45020b9c16596a97a219
    - 3b43de8555d8f413a797e19c414a55578882ad7bbcb6ad7604bb1818dd3eedcd
    - fb7a958b99275caa0c04be2a821b2a821bb797c4be6bd049fa09144de349ea41
    - cd22e14f4fa6716cfc9964fdead813d2ffb80d6dd716e2114f987ff36cc5e872
    - 5c59cd977890ed32eb60caca8dc2c9a667cff4edc2b12011854310474d5f405d
    - 5ad42b39f368a25a00d9fe15fa5326101c43bf4c296b64c1556bc49beeee9ae1
    - b198da893972df5b0f2cbcec859c0b6c88bb3cf285477b672b4f40c104bcbd36

This comprehensive analysis should help in understanding, detecting, and mitigating the issues related to the BBTok Banker Campaign.
