# 华东师范大学健康打卡【请勿滥用】

## 开发说明：疫情打卡已经持续一年多，每天手动打卡非常麻烦，而且会经常忘记，不得不麻烦辅导员和监督助理，千里寻人来打卡。本人身体健康，基本不出差，且常年待在闵行校区，遂开发每天自动打卡，图个方便。如果有出行计划，请停止自动打卡，严格遵守学校打卡规范。

## 技术实现：
            收集微信小程序登录所需的params(open_key, iv, data);
            用requests.get获取MiniToken作为下一步的headers；
            用requests.put发送包含打卡信息的json；
            用Server酱发送微信通知(需要注册并关联微信);
            用Github Action实现每日自动打卡

## 使用说明：
1. 安装Fiddler Everywhere工具（Free），对电脑微信客户端中的打卡小程序进行抓包，获取打卡小程序（https://anti-epidemic.ecnu.edu.cn/clock/mini/wx） 登录时所需的params(open_key, iv, data)。打开关闭重复几次，open_key是不变的，iv和data是变化，获取几组对应的数据（代码中是四组）；

![fiddler](https://user-images.githubusercontent.com/58336082/113386639-432c2280-93bd-11eb-902c-282011928cf2.jpg)
![fiddler2](https://user-images.githubusercontent.com/58336082/113386643-43c4b900-93bd-11eb-87d8-74b9e9f4f4c7.jpg)

2. 使用Fiddler Everywhere工具，对电脑微信客户端中的打卡小程序进行抓包，获取微信打卡的Token。成功打卡后，在打卡页面（https://anti-epidemic.ecnu.edu.cn/clock/mini/record） 查看request的body信息，获得Token；

![fiddler3](https://user-images.githubusercontent.com/58336082/113388742-5b9e3c00-93c1-11eb-811d-c2f3ca58d48a.jpg)


3. 获取Server酱（Free）的sckey，用于微信推送消息（需用Github账号登录，并绑定微信）；

4. 在线修改ECNU.py，填补代码中的open_key, iv, data, number（学号）, token, sckey等；

5. 将github action文件内容复制到github action workflow的main.yml文件中，实现自动打卡（每日8:30）；

## License
本作品采用[知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](http://creativecommons.org/licenses/by-nc-sa/4.0/)进行许可。
