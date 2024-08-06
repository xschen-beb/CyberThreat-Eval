# VMConnect Malicious PyPI Packages Imitate Popular Open Source Modules

Incident: VMConnect: Malicious PyPI Packages Imitate Popular Open Source Modules

Root cause: Malicious packages uploaded to PyPI repository

Impact: The exact number of devices or people impacted is not provided in the blog. Financial losses are also not quantified. However, considering the popularity of the mimicked packages (with tens of thousands of downloads per month), the potential impact could be significant.

Mitigation: 
1. **Enhance Package Review Procedures**:
    - Implement stringent review processes for new packages and updates including automated and manual reviews.
    - Use tools to evaluate the final release packages, not just the source code.
2. **Behavior Analysis Integration**:
    - Integrate behavior analysis tools like ReversingLabs Titanium Platform to detect obfuscation techniques and suspicious behavior in packages.
3. **Secure Development Practices**:
    - Encourage developers to verify the authenticity of packages and their sources before use.
    - Use checksum verification to ensure package integrity.
4. **Continuous Monitoring**:
    - Continuously monitor and scan public repositories for signs of malicious activity.
    - Set up alerts for new package uploads that imitate popular packages.
5. **Community and Vendor Collaboration**:
    - Collaborate with repository maintainers (like PyPI) to quickly report and remove malicious packages.
    - Share IoCs with the broader community to aid in detection and prevention.

Detection Signature:
- **Service**: PyPI (Python Package Index)
- **Port**: Not applicable (web-based service)
- **Severity**: Critical
- **Incident**: VMConnect: Malicious PyPI Packages
- **Signature Name**: “Malicious PyPI Package”
- **Internal Checks**:
    - **Setting1**: Ensure all downloaded packages are verified against known good checksums.
    - **Setting2**: Implement tools to scan and analyze the behavior of package content before deployment.
    - **Setting3**: Establish a review process for package updates and new submissions.
- **External Scanning**:
    - Monitor public repositories for new package submissions that imitate popular packages.
    - Use threat intelligence feeds to identify known malicious packages.

IoCs:
- IP Address: 45.61.139.219
- Domains: ethertestnet.pro, deliworkshopexpress.xyz
- PyPI Packages and SHA1 Hashes:
    - VMConnect 1.1.7: b0095f149951241c6e11e0d1be1f74e8cdfbdbb2
    - VMConnect 1.1.7: 2ff1b3aa2dbff6d87447b250a8d19241e7853ab0
    - osinfopkg 0.0.2: 67226da423ab4a2c97b2d008dec45280aaa5fdf5
    - osinfopkg 0.0.2: 146942c5dbaba55be174b1bfb127410e332caa03
    - osinfopkg 0.0.3: 0eb79e80c51c0e14be3620dfb237f7b53160a292
    - osinfopkg 0.0.3: bc2d48d6d9eeaf0b29625683942e90dfd2b75723
    - osinfopkg 0.0.4: 9a276ca3678898f5596166416f7e709a2064e95c
    - osinfopkg 0.0.4: 658605988c7afd9adf437fb64ff682cb4190f144
    - osinfopkg 1.0.1: 5f03b73d56528ecbc3f24b8e7daec6b3d3370834
    - osinfopkg 1.0.1: 19684554e4905bb3cf354a5d5a0f00d696f38926
    - osinfopkg 1.0.2: e531121b137182453f0d120be860ad882d2dc0a7
    - osinfopkg 1.0.2: b1f2d50be0aca0672475488d77c6f71a1b0633f8
    - osinfopkg 1.0.3: de4e9efeace6ff76dc00a166dca152dc3021d799
    - osinfopkg 1.0.3: 664f0913a5952eeb77373f83e090fab7e94aa45e
    - osinfopkg 1.0.4: bd7ba47f730c2bc33afa67a39d9cbe3768f62426
    - osinfopkg 1.0.4: 0dc723e77a5b97183a90eaecb62c9b7341e483ed
    - ethter 0.9.1b1: 6bf76b01bd17f370cd3f9947135bf250597d1ac1
    - ethter 0.9.1b1: 497df2fd2dba324be04cc57f50a3170b532aa70c
    - ethter 1.10.1b1: d404a55f1f7fbcd8b3156a84ebcf97c57ba24b95
    - ethter 1.10.1b1: 9588affaf9d85e2141b9d76b914d9f89a8292574
    - quantiumbase 0.7.0: dbc14c3ac0528a8aeb6edba8a0b2792dab131102
    - quantiumbase 0.7.0: 0b7b4444f820e9990dfeb5e2080321b5f25a9785
    - quantiumbase 0.8.1: e6494b9a91862191556d77022e5577ddbe749ef4
    - quantiumbase 0.8.1: a1b039f88c385f5c5eec2ef1701251c7341b1fcd
