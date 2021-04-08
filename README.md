# 华东师范大学健康打卡【请勿滥用】

## 开发说明：疫情打卡已经持续一年多，每天手动打卡非常麻烦，而且会经常忘记，不得不麻烦辅导员和监督助理，千里寻人来打卡。本人身体健康，基本不出差，且常年待在闵行校区，图个方便，遂开发每天自动打卡。如果有外出计划，请自行停止自动打卡，严格遵守学校打卡规范。

## 技术实现：
1. 收集微信小程序登录所需的params(open_key, iv, data);
2. 用requests.get获取MiniToken作为下一步的headers；
3. 用requests.put发送包含打卡信息的json；
4. 用Server酱发送微信通知(需要注册并关联微信);
5. 用Github Action实现每日自动打卡

## 使用说明：
1. 安装Fiddler Everywhere工具（Free），对电脑微信客户端中的打卡小程序进行抓包，获取打卡小程序（https://anti-epidemic.ecnu.edu.cn/clock/mini/wx） 登录时所需的params(open_key, iv, data)。重复打开关闭打卡小程序界面几次，open_key是不变的，iv和data是变化，获取几组对应的value（代码中是四组）；

![fiddler](https://user-images.githubusercontent.com/58336082/113386639-432c2280-93bd-11eb-902c-282011928cf2.jpg)
![fiddler2](https://user-images.githubusercontent.com/58336082/113386643-43c4b900-93bd-11eb-87d8-74b9e9f4f4c7.jpg)

2. 使用Fiddler Everywhere工具，对电脑微信客户端中的打卡小程序进行抓包，获取微信打卡的token。用小程序打卡成功后，查看打卡页面（https://anti-epidemic.ecnu.edu.cn/clock/mini/record） 的request的body信息，获得token；

![fiddler3](https://user-images.githubusercontent.com/58336082/113388742-5b9e3c00-93c1-11eb-811d-c2f3ca58d48a.jpg)


3. 获取Server酱（Free）的SCKEY，用于微信推送消息（需用Github账号登录，并绑定微信）；

4. 复制到自己github的仓库中（请不要在此项目中随意改动）；

5. 修改ECNU.py，根据代码中的说明指示填补open_key, iv, data, number（学号）, token, sckey的值；

6. 将github_action.txt文件内容复制到github action的workflow的yml文件中，实现自动打卡（每日8:00和9:00）；

## License
本作品采用[知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](http://creativecommons.org/licenses/by-nc-sa/4.0/)进行许可。
