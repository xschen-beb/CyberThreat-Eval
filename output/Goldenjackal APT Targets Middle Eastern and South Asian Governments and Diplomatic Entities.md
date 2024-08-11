Source: [https://securelist.com/goldenjackal-apt-group/109677/](https://securelist.com/goldenjackal-apt-group/109677/)

# Goldenjackal APT Targets Middle Eastern and South Asian Governments and Diplomatic Entities

Incident: GoldenJackal APT Toolset Usage

Root cause: Exploitation of known vulnerabilities in outdated WordPress instances.

Impact: Government and diplomatic entities in the Middle East and South Asia were targeted. Specific details on the number of devices, people impacted, and financial losses are not provided in the blog.

Mitigation: Update and secure WordPress installations and other web applications.
- **Detailed Steps for mitigation:**
  1. Regularly update WordPress core, themes, and plugins to the latest versions.
  2. Implement Web Application Firewalls (WAFs) to filter and monitor HTTP requests.
  3. Conduct regular security audits and vulnerability assessments.
  4. Apply strong authentication mechanisms, such as Multi-Factor Authentication (MFA) for administrative access.
  5. Monitor for unusual activity and review logs frequently to detect any signs of compromise.
  6. Use secure coding practices to protect against injections and other forms of attacks.

Detection Signature:
- **Service:** WordPress
- **Port:** 80/443 (HTTP/HTTPS)
- **Severity:** Critical
- **Incident:** GoldenJackal APT activity
- **Signature name:** “WordPress outdated version”
- **Internal checks:**
  - Setting1: WordPress core, plugins, and themes should be up to date – Web server
  - Setting2: Administrative URLs should be protected by strong authentication – Web server
  - Setting3: No unauthorized changes to WordPress files – File Integrity Monitoring
- **External scanning:**
  - Detect outdated WordPress installations
  - Identify common vulnerabilities and exposures (CVEs) related to WordPress

IoCs:
- **MD5 hashes:**
  - JackalControl: 
    - 5ed498f9ad6e74442b9b6fe289d9feb3
    - a5ad15a9115a60f15b7796bc717a471d
    - c6e5c8bd7c066008178bc1fb19437763
    - 4f041937da7748ebf6d0bbc44f1373c9
    - eab4f3a69b2d30b16df3d780d689794c
    - 8c1070f188ae87fba1148a3d791f2523
  - JackalSteal: 
    - c05999b9390a3d8f4086f6074a592bc2
  - JackalWorm: 
    - 5de309466b2163958c2e12c7b02d8384
  - JackalPerInfo: 
    - a491aefb659d2952002ef20ae98d7465
  - JackalScreenWatcher: 
    - 1072bfeee89e369a9355819ffa39ad20

- **Legitimate compromised websites:**
  - hxxp://abert-online[.]de/meeting/plugins[.]php
  - hxxp://acehigh[.]host/robotx[.]php
  - hxxp://assistance[.]uz/admin/plugins[.]php
  - hxxp://cnom[.]sante[.]gov[.]ml/components/com_avreloaded/views/popup/tmpl/header[.]php
  - hxxp://info[.]merysof[.]am/plugins/search/content/plugins[.]php
  - hxxp://invest[.]zyrardow[.]pl/admin/model/setting/plugins[.]php
  - hxxp://weblines[.]gr/gallery/gallery_input[.]php
  - hxxp://www[.]wetter-bild[.]de/plugins[.]php
  - hxxps://ajapnyakmc[.]com/wp-content/cache/index[.]php
  - hxxps://asusiran[.]com/wp-content/plugins/persian-woocommerce/include/class-cache[.]php
  - hxxps://asusiran[.]com/wp-content/themes/woodmart/inc/modules/cache[.]php
  - hxxps://croma[.]vn/wp-content/themes/croma/template-parts/footer[.]php
  - hxxps://den-photomaster[.]kz/wp-track[.]php
  - hxxps://eyetelligence[.]ai/wp-content/themes/cms/inc/template-parts/footer[.]php
  - hxxps://finasteridehair[.]com/wp-includes/class-wp-network-statistics[.]php
  - hxxps://gradaran[.]be/wp-content/themes/tb-sound/inc/footer[.]php
  - hxxps://mehrganhospital[.]com/wp-includes/class-wp-tax-system[.]php
  - hxxps://meukowcognac[.]com/wp-content/themes/astra/page-flags[.]php
  - hxxps://nassiraq[.]iq/wp-includes/class-wp-header-styles[.]php
  - hxxps://new[.]jmcashback[.]com/wp-track[.]php
  - hxxps://news[.]lmond[.]com/wp-content/themes/newsbook/inc/footer[.]php
  - hxxps://pabalochistan[.]gov[.]pk/new/wp-content/cache/functions[.]php
  - hxxps://pabalochistan[.]gov[.]pk/new/wp-content/themes/dt-the7/inc/cache[.]php
  - hxxps://pabalochistan[.]gov[.]pk/new/wp-content/themes/twentyfifteen/content-manager[.]php
  - hxxps://sbj-i[.]com/wp-content/plugins/wp-persian/includes/class-wp-cache[.]php
  - hxxps://sbj-i[.]com/wp-content/themes/hamyarwp-spacious/cache[.]php
  - hxxps://sokerpower[.]com/wp-includes/class-wp-header-styles[.]php
  - hxxps://technocometsolutions[.]com/wp-content/themes/seofy/templates-sample[.]php
  - hxxps://www[.]djstuff[.]fr/wp-content/themes/twentyfourteen/inc/footer[.]php
  - hxxps://www[.]perlesoie[.]com/wp-content/plugins/contact-form-7/includes/cache[.]php
  - hxxps://www[.]perlesoie[.]com/wp-content/themes/flatsome/inc/classes/class-flatsome-cache[.]php
  - hxxps://tahaherbal[.]ir/wp-includes/class-wp-http-iwr-client.php
  - hxxps://winoptimum[.]com/wp-includes/customize/class-wp-customize-sidebar-refresh.php
  - hxxps://www[.]pak-developers[.]net/internal_data/templates/template.html
  - hxxps://www[.]pak-developers[.]net/internal_data/templates/bottom.jpg
  
No additional IoCs found.
