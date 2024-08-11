Source: [https://www.reversinglabs.com/blog/beware-impostor-http-libraries-lurk-on-pypi](https://www.reversinglabs.com/blog/beware-impostor-http-libraries-lurk-on-pypi)

# Developers Beware Imposter HTTP Libraries Lurk on PyPI

### Incident: Malicious HTTP Libraries on PyPI

**Root cause:** Lack of verification and proper security checks on the PyPI repository allowing the upload of malicious packages.

**Impact:** Hundreds to thousands of developers potentially impacted. The exact number of devices or financial losses are not specified in the document.

**Mitigation:** Implement stricter verification processes for new packages uploaded to PyPI and educate developers on the importance of verifying the authenticity of third-party libraries before use.
  - **Detailed Steps for mitigation:**
    1. **Enhance PyPI Security Measures:**
       - Implement automated static and dynamic analysis tools to scan for malicious code in newly uploaded packages.
       - Require multi-factor authentication (MFA) for developers uploading packages.
       - Introduce a reputation score system for new packages and package maintainers.
    2. **Developer Education:**
       - Conduct training sessions to make developers aware of the risks of typosquatting and how to verify package authenticity.
       - Encourage the use of well-known and actively maintained libraries.
       - Promote the practice of reviewing the code of dependencies whenever possible.
    3. **Security Tools Integration:**
       - Integrate tools like ReversingLabs A1000 for static analysis and threat classification into the CI/CD pipeline.
       - Utilize software composition analysis (SCA) tools to track dependencies and identify potential vulnerabilities.

**Detection Signature:**
   - **Service:** PyPI
   - **Port:** N/A (since this is related to software packages rather than network services)
   - **Severity:** Critical
   - **Incident:** Typosquatting and Malicious Package Distribution
   - **Signature name:** “Malicious PyPI Package Detection”
     - **Internal checks:**
       - Setting1: Verify package names closely resemble popular libraries.
       - Setting2: Ensure package descriptions and functionalities match legitimate packages.
       - Setting3: Check for malicious code patterns in setup.py and other common files.
     - **External scanning:**
       - Monitor for newly uploaded packages that mimic popular libraries.
       - Use threat intelligence feeds to detect known malicious packages.

**IoCs:**
- Malicious PyPI packages identified by ReversingLabs:
  - **Package Name:** aio5
    - **Version:** 0.2.9
    - **SHA1:** 8c80db3ea4ebf67da6839c249270184dc4fcaeab
  - **Package Name:** aio6
    - **Version:** 6.6.6
    - **SHA1:** 92bcbf74010bb056b79968cd64289d100c8a80c7
  - **Package Name:** htps1
    - **Version:** 2.3.1
    - **SHA1:** 2b0822ba5f147dc594c4f9a95669090acab03bc1
  - **Additional IoCs:** 
    - **SHA1:** 7b325940dee4055745dd8d78ab535edc4fca078c
    - **SHA1:** d65524917e4d7d3a14483f4104b5a9a82d63acbf
    - **SHA1:** b997146c966da74b9c3e32f589d2790ced781864
    - **SHA1:** c1fe2bab43d8feb7f6a49fab13dad379cdad4b6e
    - **SHA1:** c2c50d42bea265e2b9033fd53cf5932b933ebc8a
    - **SHA1:** efc8db855e879c72dc172ecd61e7ff0421c1fdbd
    - **SHA1:** c1442f89167024fe9e1b47509ffa9aadc63cdb23
    - **SHA1:** 030728c7a876f34ee97963c7f09e6e0398a1f00a
    - **SHA1:** 7a5d7f9dac73ee3ea9a631ee944cca635b4ff9f2
    - **SHA1:** fa62287b44a159bbfaefb7f44c5df985de3d8fa8
    - **SHA1:** 4b990e7f0bfd04a8619cb583ccabb2bce7a65bb7
    - **SHA1:** feaeac543428558fe6a9bace070939b9ec267b7d
    - **SHA1:** 7fe9ecbb376b77b976825f40a07bee31ae250e9b
    - **SHA1:** 267b170a52a52a2137c77e671dd703a0b56d8b2d
    - **SHA1:** bfb941328af98ad59608bbbf00f99178ae610352
    - **SHA1:** c5b50973ac6c654e7bfd3e5e82b16f763a8ae149
    - **SHA1:** ff12f89964e88d8c00f9f4339ca9539aea46db47
    - **SHA1:** 9ab40a25efe023ea23ce74aeb196181aefa3be15
    - **SHA1:** 9cca5e233bee9f9ab3b41ce7cad8e5f43218d72c
    - **SHA1:** c14af02c6d44645937d23fb122e3e84a612e93ca
    - **SHA1:** a197c2140edac03fb48b1847c4369379c8925ba5
    - **SHA1:** 9821e2f58328338598bbecaf9dd53a881d467978
    - **SHA1:** 06663a6664335f700dd2c9aaf71bd656e9161cd6
    - **SHA1:** faecbfe3d35f5cecfc04b9933b4f3128a5a9cc12
    - **SHA1:** 3dd660983a6ea7727fdbfb310292ba83c443ca03
    - **SHA1:** e315223b801fe90d8eb6caae6c31aa70f0f9aa15
    - **SHA1:** 23dc7d61d9d0d40cde42cc7cc48afee8b3f31110
    - **SHA1:** 91d756cc909e56e4ac97e013ea0951e5bb62c1dc
    - **SHA1:** cceaba4359acefea532073bf235553776a6ecfe5
    - **SHA1:** 28c57661cb9f5528a46cbe848beebdfa02d866b1
    - **SHA1:** 916bebc9d52d9c925edb6c4108ab9dead50a9ece
    - **SHA1:** 2b41cec321dd0be8519612294676f8bc3feaf1b6
    - **SHA1:** 904ed2566728036acc7ee645aaaac0b753f1ceef
    - **SHA1:** 081f21e6398266f41bc179271bc3b95827122490
    - **SHA1:** df70515280dd4abcd7425aa616c1334ec1ab2a85
    - **SHA1:** c5654cd8e7a728b10094db0239d1d80c82de5d2d
    - **SHA1:** 3d5914e823940b3598f74c54cc09b5c39488474e
    - **SHA1:** 944fd9e568ebdb2ea77b8f3f47868f87cab62bf2
