# Un1kPoc

作者:depy@rce.ink

目前提供Un1kPoc的测试版本供大家测试,直接运行后默认导入的配置信息即可使用本人远端api中存放的一些NdayPoc,您除了代理配置无需修改任何内容。

希望大家能够帮我找到一些工具的异常错误上报issue或者联系我本人邮箱i@rce.ink，感激不尽。

测试周期完毕后 我将开源web端代码供您使用,测试版本需要联通互联网,后续本地环境搭建后只需要可与web端联通即可。

## Log

2022-08-29 更新至版本V2.0.5 

2022-08-29 更新至版本V2.0.1 旧版本已不可使用

## Introduce

日常工作里,我经常会因为找不到漏洞POC而头疼,看着漏洞poc目录里杂七杂八的脚本,我感受到了前所未有的压力。

并且我经常需要使用fofa搜集资产后,处理域名,再写一个python脚本去测试或者修改burpsuite的请求包去测试,这里面浪费的时间确实很多。

在最近的护网里，我发现我和我的同事经常在做一件事。搜集靶标相关资产，找到可以用nday打的资产，找到nday的poc，利用。如果我能够把这个流程简化成搜索漏洞，搜索资产，点击利用，那么就可以微我节省很多时间。所以我才会去花一个月的时间编写这个工具。

## Download & Run

1.确保本机环境可用javafx[在jdk14的环境下 出现找不到主类的错误 更换jdk1.8即可]

2.下载 https://github.com/h4ckdepy/Un1kPoc/releases

3.切换至jar包目录

4.java -jar ...

![image](https://user-images.githubusercontent.com/42985524/187059103-6dfa4191-1df6-4465-91fd-79a833896520.png)

5.首次安装将提示没有生成本地数据库

![image](https://user-images.githubusercontent.com/42985524/187059151-1267d461-46d6-48d4-82a9-6156d596a5e5.png)

确定后 点击Exploit->Setting->NormalSetting 初始化数据库即可

## Example[测试版本 可以从第四步骤开始看]

1.在web端容器维护一个POC-网*防火墙RCE

![image](https://user-images.githubusercontent.com/42985524/187059295-ce4a7c3e-345b-42a9-86c7-7a1c403ca86d.png)

2.配置禁测域名列表

![image](https://user-images.githubusercontent.com/42985524/187059303-1e732e42-43fc-4d6e-8355-cb7d200aa8bc.png)

3.生成授权用户

![image](https://user-images.githubusercontent.com/42985524/187059332-4ec2c4f1-f3f3-4563-9b03-34b3f8bfabb5.png)

4.按照下载使用的方法运行工具 主界面如下

![image](https://user-images.githubusercontent.com/42985524/187059343-404cb826-20bb-4c72-b8b6-723efe903740.png)

5.在配置中配置好自己的授权地址、授权码、邮箱（必填） 在other中配置好fofakey和fofamail（可选）

![image](https://user-images.githubusercontent.com/42985524/187059406-466feb6a-ad83-48c7-9a20-d9dee1782b5e.png)

![image](https://user-images.githubusercontent.com/42985524/187059423-fa1534a2-930c-4c7f-9387-a21f90e729be.png)

6.关闭菜单 出现以下信息 代表已和webapi通讯成功

![image](https://user-images.githubusercontent.com/42985524/187059460-46efea70-e267-4b4b-80d7-bfcf178a4399.png)

7.搜索漏洞并选中

![image](https://user-images.githubusercontent.com/42985524/187059483-326ca2d9-d8be-4439-ae33-4a4f43e7937b.png)

8.修改自动填充好的区域的内容 然后Exploit按钮点击即可

（联动Fofa）

9.配置好fofa相关密钥信息后切换至fofa

![image](https://user-images.githubusercontent.com/42985524/187059545-3405fe23-c6ba-4319-b302-04dea9c49d9b.png)

10.选择任意一条结果右键

![image](https://user-images.githubusercontent.com/42985524/187059558-75d0d555-7fe1-4e66-9c4e-8d1714107623.png)

这里分别对应 打开网站（也可以双击打开^_^）、复制url、该记录的ip进行FOFAC段查询、使用当前选中的bug进行测试

11.点击第四个

![image](https://user-images.githubusercontent.com/42985524/187059596-af250d6c-8767-4645-a659-1b5c4d9da15d.png)

在相应里查看结果 并且此时URL已经修改你选中的那列 
![image](https://user-images.githubusercontent.com/42985524/187059660-611895eb-3c3f-4ef5-a0b4-dd6cac0663fe.png)
![image](https://user-images.githubusercontent.com/42985524/187059644-edf479d3-fd00-4c2d-8f2c-0dc149599d72.png)

所以你只需要做的就是 fofa查询->选中漏洞->一个右一个测试

## 其他功能

1.禁测域名配置

我们把工具给团队成员使用 为了防止测试gov、edu等我们不希望被工具测试的域名 可以去web端添加

成员测试后会弹窗提示

![image](https://user-images.githubusercontent.com/42985524/187059890-bc9240b1-d078-45ec-b1b8-974e3700fc9c.png)

2.Un1kCodes

启发于我的另一个项目un1kfiles 准确描述应该是快速复制相关代码

打开工具后我们在body或者备忘录处右键

![image](https://user-images.githubusercontent.com/42985524/187059964-03f64c2c-c1b2-4c2f-89ea-0f5b87b95bea.png)

![image](https://user-images.githubusercontent.com/42985524/187059981-8ed82bba-8047-4cc2-94e9-9a858ac2157e.png)

点击后相应的代码会复制到你的剪切板 ctrl+v粘贴即可 维护codes可以在web端后台配置

![image](https://user-images.githubusercontent.com/42985524/187060013-b8609b77-0119-47ab-ac41-f5db7435981b.png)

点击后相应的代码会复制到你的剪切板 ctrl+v粘贴即可 维护codes可以在web端后台配置

## Thanks

由于我是第一次开发javafx，在这期间非常感谢Mrkaixin师傅、Ch1ng师傅对我疑问的解答。特别是mdut项目中的一些解决方案，让我少走了很多弯路。
