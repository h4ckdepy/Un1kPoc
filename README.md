# Un1kPoc

作者:depy@rce.ink

环境要求: (docker版本部署-容器待开发 || webman版本源码部署 ) && javafx支持的java环境

## 前言

关于漏洞管理,很久之前我做过一个web页面测试的平台Un1kPoc-web版本。他的原理很简单,就是将数据库保存的漏洞poc有关的url、body等参数放到前端页面展示，然后发送请求的时候重新构造发包即可。

同时他可以让云函数重新发包,实现防溯源的效果。并且它打开即用，超级方便，基本上打开输入漏洞,对应修改url就行了。

但他存在很多弊端,我需要考虑到脚本语言的性能问题,也需要考虑http代理调试的问题,更重要的需要考虑对本地内网环境漏洞测试的问题。

综合思考之后发现web端能够实现的,通过javafx编写的gui本地端也可以实现。并且效果似乎更好，还可以实现http的代理，更方便去调试poc。当然了,对于漏洞数据的保存我还是选择用webapi的方案,只是这次可以将api部署在本地或者是远端服务器罢了。

## 特性

1.快速利用web端中存在的poc,只需要web端能够与本机进行网络通讯即可,并且可以根据模版导入漏洞,后期只需要维护poc部分即可

2.授权模式,可以在一个Team中做好漏洞利用范围划分与时间限制 指定用户使用指定POC,防止0day漏洞泄漏

## 功能列表

主界面

![image](https://user-images.githubusercontent.com/42985524/183280615-e6bac2ed-15cb-4e27-9e86-895a307966c6.png)

漏洞搜索

![image](https://user-images.githubusercontent.com/42985524/183280642-a88d8278-4189-4f76-a033-231f9e2ff3ed.png)

漏洞选择

![image](https://user-images.githubusercontent.com/42985524/183280677-ab37387c-4348-49e7-a89c-adae8c3acd57.png)

漏洞利用

![image](https://user-images.githubusercontent.com/42985524/183280703-0693381a-8948-46bd-ae31-0ccc3115c514.png)

接入Un1kcodes（burpsuite插件un1kfiles相同功能）

![image](https://user-images.githubusercontent.com/42985524/183280940-176d8aca-3110-4341-8216-d39deff615c7.png)

工具sqlite数据库配置

![image](https://user-images.githubusercontent.com/42985524/183280713-07070471-0785-404e-9989-6462f06abb81.png)

![image](https://user-images.githubusercontent.com/42985524/183280724-b33c53b5-294c-4908-8218-b898adea7380.png)

![image](https://user-images.githubusercontent.com/42985524/183280733-4b234497-ed67-4018-af8f-ae851d53af46.png)

Web端 漏洞POC管理&授权

![image](https://user-images.githubusercontent.com/42985524/183280753-ebb3c726-4156-4fd3-b30b-a29bedb8347d.png)

![image](https://user-images.githubusercontent.com/42985524/183280765-ceab3aa6-6074-4cbd-ae29-705a1c1e2479.png)

## Log

更多功能亟待开发 现在在做容器部分 之后将提供web端docker镜像以及web端源代码、编译生成后的jar文件至本仓库
