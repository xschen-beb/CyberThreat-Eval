import re

def convert_star_links_to_markdown(text):
    pattern = re.compile(r"\*([^*]+)\*\s?\((https?://[^\s)]+)\)")

    def replace_func(match):
        link_text = match.group(1).strip()
        link_url  = match.group(2)

        return f"[*{link_text}*]({link_url})"

    new_text = pattern.sub(replace_func, text)
    return new_text


def process_text(text):
    """
    1. 删除文本中 "*Your changes* (link)" 的 "Your changes"，只保留 "(link)"。
    2. 如果出现连续两个或更多链接，比如：
       (https://link1.com). (https://link2.com)
       则将它们合并成 (https://link1.com)(https://link2.com)。
    3. 将“前一句”或“前一个句子”作为这批链接的锚文本：
       [前一个句子.](https://link1.com)(https://link2.com)
    """
    #---------------------------------------------------
    # 第一步：去除 *Your changes*，只保留 (url)
    # 例如：*Your changes* (https://link.com) --> (https://link.com)
    #---------------------------------------------------
    # 匹配模式：\*Your\s+changes\*\s?\((https?://...)\)
    # 注意如果有其他大小写或拼写错误，可再做更多的选项
    pattern_your_changes = re.compile(
        r"\*Your\s+changes\*\s?\((https?://[^\s)]+)\)",
        flags=re.IGNORECASE
    )
    text_step1 = pattern_your_changes.sub(lambda m: f"({m.group(1)})", text)

    #---------------------------------------------------
    # 第二步：合并形如 `(url1). (url2)` 为 `(url1)(url2)`
    # 先把它们替换为 `(url1)(url2)`，去掉中间的点号和空格
    #---------------------------------------------------
    # 正则思路： 匹配 ) . (https://... 
    # 形式如： )(https://...) 可能带空格
    # 为了只合并两个连续链接之间的 “). ”，同时保留句子的结尾，做一个简单替换。
    pattern_consecutive_links = re.compile(
        r"\)\.\s?\("
        r"(https?://[^\s)]+)\)"
    )
    # 这个替换只做一次，处理两两合并。如果有三四个连续链接，需要循环合并，直到不再出现。

    def merge_links(match):
        # match.group(1) 是第二个链接
        return f")({match.group(1)})"

    # 用 while 循环连续合并，直到不再出现这样的 pattern
    text_step2 = text_step1
    while True:
        new_text = pattern_consecutive_links.sub(merge_links, text_step2)
        if new_text == text_step2:
            break
        text_step2 = new_text

    #---------------------------------------------------
    # 第三步：将前一个句子作为锚文本
    # 实际效果：把 "前一个句子. (link)(link2)" 改成 "[前一个句子.](link)(link2)"
    #
    # 实现思路：
    # 1. 找到所有形如 "前一个句子. (https://...)" 的位置
    # 2. 把句子和链接打包成 Markdown 形式
    #
    # 如果链接是多个 (link1)(link2)(link3)，也一并处理。
    #---------------------------------------------------

    # 匹配模式： ([^.]+)\.\s*\((https?://...) 等
    # 这里假设：sentence 在句点 . 结束，后面紧随若干 (链接)
    # 我们用捕获组把句子和链接都捕获出来
    pattern_sentence_link = re.compile(
        r"([^.\n]+)\.\s*\(("
        r"(?:https?://[^\s)]+)\)"
        r"(?:\(https?://[^\s)]+\))*"  # 允许链接重复多次
        r")"
    )

    def sentence_to_markdown(match):
        sentence_text = match.group(1).strip()
        link_part = match.group(2)  # 包含"(url1)(url2)..."等
        # 将 sentence_text + link_part 打包成 [sentence_text.](url1)(url2) 形式
        return f"[{sentence_text}.]{link_part}"

    text_step3 = pattern_sentence_link.sub(sentence_to_markdown, text_step2)

    return text_step3


if __name__ == "__main__":
    # input_text = """#### Root cause \n The root cause of the incident was the exploitation of two zero-day vulnerabilities (CVE-2024-12356 and CVE-2024-12686) in BeyondTrust's Remote Support SaaS platform. The threat actors utilized a stolen Remote Support SaaS API key to reset passwords for local application accounts and gain further privileged access to the systems. *BeyondTrust cybersecurity company detected the breach on December 2nd, 2024, and conducted a root cause analysis on December 5th, 2024* (https://www.bleepingcomputer.com/news/security/beyondtrust-says-hackers-breached-remote-support-saas-instances/). *Security Advisory BT24-10 and BT24-11 were issued to address the vulnerabilities* (https://blog.gitguardian.com/what-happened-in-the-u-s-department-of-the-treasury-breach-a-detailed-summary/). *CISA is working closely with the Treasury Department and BeyondTrust to understand and mitigate the impacts* (https://www.cisa.gov/news-events/news/cisa-update-treasury-breach). *The vulnerabilities included a Command Injection Vulnerability (CVE-2024-12356) and a Post-Exploitation Privilege Escalation (CVE-2024-12686)* (https://socradar.io/beyondtrust-security-incident-command-injection/). *BeyondTrust's 20,000 customers across 100 countries were notified* (https://www.darkreading.com/cyberattacks-data-breaches/chinese-state-hackers-breach-us-treasury-department). *The API key was obtained from BeyondTrust, a third-party vendor* (https://www.cpomagazine.com/cyber-security/us-treasury-breached-by-chinese-state-sponsored-hackers-via-stolen-api-key/)."""
    # input_text = """
# The attack potentially impacted all users of the compromised Chrome extensions, with specific mention of targeting Facebook Ads accounts and stealing Facebook access tokens, user passwords, and session tokens. The malicious code added a mouse click listener for Facebook.com to retrieve images, presumably searching for QR codes to bypass captchas and/or 2FA authorization requests *Your changes* (https://www.securityweek.com/several-chrome-extensions-compromised-in-supply-chain-attack/). *Your changes* (https://www.darkreading.com/application-security/chrome-extension-compromises-highlight-software-supply-challenges). The attack affected 2.6 million people. *Your changes* (https://socradar.io/phishing-attack-cyberhaven-chrome-extension/). The retail and hospitality sectors face significant risks, including data breaches and compliance violations *Your changes* (https://rhisac.org/threat-intelligence/cyberhaven-extension-compromise-part-of-broader-campaign-affecting-multiple-chrome-extensions/). 
# """
    # output_text = process_text(input_text)
    # print(output_text)
    import ast
    ttps = """{'T1078': 'Valid Accounts, Confidence: High. Justification: The threat actors used a stolen Remote Support SaaS API key to reset passwords and gain access to the systems.', 'T1190': 'Exploit Public-Facing Application, Confidence: High. Justification: The attackers exploited two zero-day vulnerabilities in the BeyondTrust Remote Support SaaS platform.', 'T1071': 'Application Layer Protocol, Confidence: Medium. Justification: The attackers used the remote support platform to access agency computers and steal documents remotely.', 'T1074': "Data Staged, Confidence: Medium. Justification: The attackers accessed and stole documents from the Treasury Department's computers."}"""
    formatted_ttps = []
    data = ast.literal_eval(ttps)
    print(data)
        # 判断解析后的对象是否为字典
    if isinstance(data, dict):
        for ttp_id, details in data.items():
            # 假设 details 是一个字符串，包含描述、置信度和理由
            # 使用 ',' 和 '.' 作为分隔符
            parts = details.split(', ')  # 首先按 ',' 分割
            if len(parts) == 2:
                description = parts[0].strip()  # 描述
                confidence_part = parts[1].strip()  # 包含置信度和理由的部分
                
                # 进一步分割置信度和理由
                confidence, justification = confidence_part.split('. ', 1)  # 按 '.' 分割
            elif len(parts) == 1:
                description = parts[0].strip()
                confidence = "N/A"
                justification = "N/A"
            else:
                continue  # 如果格式不正确，跳过

            formatted_ttps.append(f"- {ttp_id}: {description}\n  {confidence}.\n  {justification}\n")

        # 将格式化后的 TTPs 添加到输出文本中
        text_output = "\n".join(formatted_ttps) + "\n"
        print(text_output)
