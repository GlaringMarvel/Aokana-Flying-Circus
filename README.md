# Aokana Flying Circus

### 基于War Thunder这款游戏的空战历史脚本
### Based on the aircraft script of the game War Thunder

#### 这是一个Python初学者的个人练习项目  
#### This is a personal practice project for a Python beginner.

Q:Will this project support English?  
A:This project will not support English. All the following instructions will be based on Chinese. I hope you can use a translator yourself. If you come across any sentences that you don't understand, why not ask the GPT for help?

Q:我为什么会做这个项目呢？  
A:事情的起因是这样的，因为工作上的原因我不得不学习Python这门语言，因此我请教了我的几位朋友，询问他们我应该如何开始学习Python。  
出乎意料的是，我得到的答复非常统一：直接去写项目，哪里不会再去学。  
于是乎就有了这么一个脚本的计划

A:项目名称来自游戏《苍之彼方的四重奏》  
Q:谁问你了？

A:你说的对，但是《苍之彼方的四重奏》是一款由……  
Q:Ciallo～(∠・ω< )⌒☆  
A:哪来的柚子厨，去你马的

Q:为什么你会放出这种好东西的源码?  
A:实际上这并不是一个特别复杂的东西，作为一个初学者，我能在一个礼拜以内把主要功能完全做完，起码我觉得这个项目并不困难  
如果你精通python，并且能读一遍我稀烂的代码再帮我优化一下，那我会非常感谢

Q:有考虑过付费吗？  
A:没有，我是个好人

Q:你怎么看待其他卖脚本的商家？  
A:我不好说

Q:我是一位来自b站的正义感爆棚的网友，请问我可以攻击你吗？  
A:我玩原神

Q:原神怎么你了？  
A:你说得对，但是呢，那个，就是……就是那个两个字的游戏，它那个，嗯，他是由那个，好像是三个字的那个什么公司，自主，啊，研发的一款…全新的，开放的，那个叫做什么的冒险，的游戏。这个游戏发生在一个…一个被称作，被称作…三个字的，的一个幻想的世界，然后就是呃呃啊啊啊我又忘了
重要的游戏，绝不能忘记的游戏

Q:下载地址在哪？  
A:找到右边Releases

Q:如果别人拿你的项目去卖钱怎么办？  
T:In the event that someone appropriates your project for commercial purposes, what course of action should be taken?  
A:信息差被骗钱很正常，例如AI绘画包天天都有人买。  
如果你不喜欢看到无良商家赚这种钱，那么你可以为我的项目点一颗星星，并且为我的b站视频一键三连来宣传这个项目，让更多的人知道这个免费开源脚本（笑）  
T:It is not uncommon for misinformation to lead to financial deception, as seen in cases where AI painting packages are frequently sold.  
If you disapprove of unscrupulous merchants profiting from such practices, you have the option to support my project by giving it a favorable rating and promoting it through engaging with my Bilibili video, thereby increasing awareness of this free and open-source script. A simple action that could make a substantial difference (laughs).  
[Bilibili视频](https://www.bilibili.com/video/BV1Fj411B7Kf)
#### 之前的视频全都被举报下架了，审核也盯上我了，我近期不会发布明示脚本的视频，有问题可以私聊我
[个人主页](https://space.bilibili.com/350438467)

Q:这个项目还存在哪些问题，没有实现哪些功能？  
A:好多好多，我只能实现简单的一架飞机反复挂机，以及自动研发。并且我还在测试，不清楚有哪些BUG。  
如果你发现了一些问题，请到BiliBili视频底下进行评论，我会尽可能的想办法修复（我尽量吧）
地图目前就适配了几张，你们可以在map文件夹里找到适配的地图，但是够用了。  
#### 注意！脚本只适用于CCPR投弹，你可以在内构预览中将鼠标放到飞行员上，如果显示"连续炸弹投放点"，那么这架飞机是支持的。
![內构预览](https://github.com/GlaringMarvel/Aokana-Flying-Circus/blob/master/Setting/10.png)  
#### 亚音速飞机如su-25，A-10一类我增加了延时入场，具体可以看下面设置

Q:使用这个会被封号吗？  
A:看你怎么用，据我所知你需要避免以下情况：  
1. 全天24小时挂机（你不死谁死？）  
2. 记得同一载具偶尔自己玩一会，避免出现空中目标击杀0，地面目标击杀0的情况，否则很容易被gaijin筛查出来  
3. 你可以每天打会陆战或者挂会海战，这样可以防止人工审核
4. 如果你担心这个开源项目会被官方针对性检测，那么你要知道，空历是可以关闭反作弊后启动的

### 如果你出现下图情况，请立即停止使用任何脚本!因为已经开始人工审核了
![警告](https://github.com/GlaringMarvel/Aokana-Flying-Circus/blob/master/Setting/11.jpg)

Q:会持续更新吗？  
A:不一定会，因为我还有很多其他的东西需要学，脚本就告一段落了，除非有什么bug我会尝试修复一下  
如果有大佬愿意接手这个项目我当然很欢迎

Q:该脚本如何使用？  
A:你先别急，下面会详细介绍

### 请务必完成以下图片中的设置

#### 系统(桌面)分辨率请调整到1080p(1920x1080)

#### V1.1.0版本以后不再进行战局内图像识别,所有影响画面的东西都可以打开了

![窗口画面设置](https://github.com/GlaringMarvel/Aokana-Flying-Circus/blob/master/Setting/00.png)
![Example Image](https://github.com/GlaringMarvel/Aokana-Flying-Circus/blob/master/Setting/01.png)
![Example Image](https://github.com/GlaringMarvel/Aokana-Flying-Circus/blob/master/Setting/02.png)
![Example Image](https://github.com/GlaringMarvel/Aokana-Flying-Circus/blob/master/Setting/03.png)
![Example Image](https://github.com/GlaringMarvel/Aokana-Flying-Circus/blob/master/Setting/05.png)

### 请务必使用我上传的按键设置并进行导入

![按键设置](https://github.com/GlaringMarvel/Aokana-Flying-Circus/blob/master/Setting/09.png)
### 配置文件我放在主目录下了，文件叫 WTsetting.blk

Q:每次都改设置好麻烦啊  
A:你听说过虚拟机吗？  

Q:飞行的视角移动过快或者飞机调整过慢怎么办？  
A:看下面表格

### Map.txt里的一些设置功能
| 参数                    | 值   | 说明                                                                                                                                                 |
|-----------------------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------|
| flight_mode           | 0.5 | 数据请求延时（开局起飞时视角疯狂上抬请改这个为1,单位是秒，控制飞机上下的速度）                                                                                                           |
| decelerate            | -1  | 离战区多少公里开始开启减速板（-1代表不开启减速板。这个距离和飞机的飞行高度和速度有关，自己根据飞机调整，单位是公里）[v1.1.6版本中移动到地图设置中]                                                                     |
| reorienting_direction | 0.5 | 方向调整延时（控制飞机左右调整的速度，单位为秒）                                                                                                                           |
| infrared_decoy        | 10  | 自动热诱循环（飞机距离战区多少公里内开启热诱循环）                                                                                                                          |
| bombing_distance      | 3   | 战区剩余距离判断（这个值比较复杂，与下面的press_time属于联动判断关系，当飞机与战区的距离小于这个值时，会进入下面press_time的判断。单位是公里。如果你上面的延时设置比较大的话，会影响这个距离判断，所以我不建议这个值低于默认的3Km，具体可以根据你的飞机速度来，可以自己尝试） |
| press_time            | 5   | 投弹键剩余按压时间（单位是秒。例如默认值是5，当战区剩余距离小于上面的战区与飞机距离时，在经过5秒后松开投弹键，判断为投弹完毕，开始进入下一个动作。为什么要这么判断？因为8111端口没有提供任何关于挂载的信息……）                                        |
| Harrier               | 0   | 如果是鹞式，请把这个改为1。丢完炸弹以后会自动收油门到节流阀95%左右（勉强救一下）                                                                                                         |
| mode                  | 2   | 飞行模式（模式1：扔完炸弹以后直奔对面机场。模式2：扔完炸弹以后会随机选取一个战区方向开始逛街，到达后切换战区继续逛街。模式3：测试中的自动降落，已经初步完成。模式4：在前三种模式中随机选择一个模式）                                               |
| delay_takeoff         | 0   | 延迟入场（0为关闭，1为开启，适用于SU25与A10等超慢速飞机，具体设置请看下面）                                                                                                         |
| speed_limit           | 0   | 限速（0为关闭，1为开启。适用于SU25这种会飞断的飞机）                                                                                                                      |
| max_speed             | 950 | 最大速度（只有开启限速时才会生效）                                                                                                                                  |
| port8111              | 1   | 8111请求地址，如果你在使用中最快也只能一秒刷新一次，那么把这个值改成2                                                                                                              |
| CCRP启动延时              | 45  | 游戏开始45秒以后才会开启CCRP，你可以自己设置，适当增大或减小                                                                                                                  |

例如：越南  
Vietnam:h1=900,h2=1500,v1=5,v2=15,v3=20

#### 如果你的飞机在默认参数下会起飞撞山，或者投弹前就拍地上了，可以更改以下数值加大爬升率或增加飞行高度

| 参数              | 值    | 说明                                        |
|-----------------|------|-------------------------------------------|
| h1              | 900  | 飞行区间最低高度                                  |
| h2              | 1500 | 飞行区间最高高度                                  |
| v1              | 5    | 爬升率小于该速度大幅向上拉机头                           |
| v2              | 15   | 爬升率大于该速度后小幅度上拉机头                          |
| v3              | 20   | 爬升率大于该速度后小幅度下压机头                          |
| time            | 300  | 从这里开始，以下数值只有开启延时入场才会生效。300意味着300s以后开始转向入场 |
| north_direction | 150  | 上方机场出生以后开局飞的方向                            |
| south_direction | 300  | 下方机场出生以后开局飞的方向                            |

#### 注意！v1等数值是爬升率而不是爬升角度，就是你左边那一排高度变化的快慢，单位是m/s

### 关于飞机航向的说明
![Example Image](https://github.com/GlaringMarvel/Aokana-Flying-Circus/blob/master/Setting/map.png)
![Example Image](https://github.com/GlaringMarvel/Aokana-Flying-Circus/blob/master/Setting/compass.png)  
延迟入场设置如图所示，这是一张经典的南北机场地图（东西机场就一个洛基峡谷），你可以直接把罗盘扔地图上，罗盘上的刻度方向，就代表你想飞的方向（你需要填的值）。  
北方出生改north_direction，南方出生改south_direction。  
你可以设置朝一个方向飞多少秒，然后再入场

#### 自动降落是一个噱头，实际的挂机效率不如你飞对面机场或者等对面打你下来（可它看上去实在是太酷啦！）。我本来打算用PID写，但是我发现这样会花费大量的时间和精力去调试，所以我放弃PID了。
#### 你会发现我的地图并不全面，是因为我没有时间测试每一张地图，我只适配了9.3+的地图，如果你想要添加一张地图，那么请告诉我这张地图上下方机场高度，投弹高度区间（无论哪边起飞在平飞时都不会撞山的高度）

### 如果你出现了战区对不准的情况，大概是你的电脑没法识别到100或50ms以下的键盘输入，解决方案如下
| 参数          | 值    | 说明                  |
|-------------|------|---------------------|
| x_correct_1 | 0.5  | 调整时请注意要微调，不要使数值过大   |
| x_correct_2 | 0.2  | 1和2基本不需要改动，一般只需要改动4 |
| x_correct_3 | 0.05 | 输入单位：秒，请适当增大        |
| x_correct_4 | 0.01 | 输入单位：秒，请适当增大        |

### 其他一些杂项：  
1. win11我没有测试过，暂时不清楚是否支持，但是如果你开一个win10虚拟机应该是没问题的。  
2. 请保证你的网络稳定，如果在加载界面卡太久可能会出现问题。没有能力使用加速器可以只开亚服，我一般是UU加速俄服然后关闭亚服匹配，具体情况和各地运营商有关  
3. 脚本打开以后非常长一串报错以后闪退可能是因为游戏的8111端口出现问题，一般重启游戏就行 
4. 发现问题提问时请截图整个屏幕，附上详细的当时情况说明，最好是录像以及Dos黑窗口显示了啥
5. 比利牛斯山，阿富汗，洛基峡谷过于煞笔，你们看着ban
6. 建议先手动飞一把，该调的设置调好，比如挂载，油量，打开连续投弹，热诱等等……
7. 如果你和我的电脑一样，程序运行速度很慢，那是因为8111端口的请求速度问题，这个我暂时不清楚原理，会降低挂机效率，但是还是能用
8. 还有一些功能正在尝试，之后可能会加进来，比如自动回机场。
9. 本来我想要写一个PID飞控来达到调节飞机飞行状态的目的，但是我发现我实在没有空，越复杂的东西越容易出问题，我没有时间去调整和修补，不如简单粗暴一点。
10. 每一次更新功能都有可能会出现问题，谨慎尝试
11. 其他情况待补充……

### 更新日志：
v 1.0.0:完成了主要功能  
v 1.0.1:修复了其他玩家电脑性能远超我电脑的bug（加上了可以自己设置8111端口请求时间的data.txt）  
v 1.0.2:优化了机库界面的识图判定（可能会有bug），增加了自动热诱功能，增加了对初代CCRP喷气机支持  
v 1.0.3:可以手动选择每一张地图的飞行数据  
v 1.1.0:我将整个判断逻辑推到重构，现在解决了会卡在一些界面的问题，新增了热诱，减速板，前往敌方机场，战局中不再使用图像识别  
v 1.1.1:稳定版（可能），修复了主要的bug，解决鹞式一直加力的问题，可以选择每个地图的固定战区（如果出现问题请改回默认值）  
v 1.1.2:新增了一些测试功能：逛街模式，延迟入场，飞行限速。新增功能可能会有BUG，请谨慎选择。修复了一些小bug。  
v 1.1.3:自动降落初步完成了，以后就剩缝缝补补了  
v 1.1.4:自动降落应该可以使用了，但我不建议开启。修复了部分BUG  
v 1.1.5:终于把我的8111端口请求问题修了，不过对你们没有影响  
v 1.1.6:最终版本（可能），之后所有的更新或修复bug都会全部整理到这个版本中，详情请看右边的releases