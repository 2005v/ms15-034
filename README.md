ms15-034漏洞脚本编写 首先需要请求模块 MS15-034 漏洞的攻击。MS15-034 是一个影响 Microsoft IIS 7.5 和 8.0 的安全漏洞。

此代码将 GET 请求发送到“url”变量中指定的 URL，然后检查响应标头中“服务器”标头的值，以查看它是否在 Microsoft IIS 7.5 或 IIS 8.0 上运行。如果是，代码将发送另一个具有特定标头值的 GET 请求，并检查字符串"请求的范围不满足"的响应内容。如果响应内容中存在此字符串，则假定该网站容易受到 MS15-034 漏洞的攻击。如果该字符串不存在，则假定该网站不易受攻击。


![WDIW63P}MNC3NQ0D7A{E(ZE](https://user-images.githubusercontent.com/101918480/218248343-79863ba3-99d5-470a-a758-3248f5498fe4.png)
