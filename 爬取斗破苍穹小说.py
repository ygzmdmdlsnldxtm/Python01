import re
import requests
list_all = []
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}
html = """<ul class="dirlist three clearfix">
                                                <li><a href="/1/1.html" title="斗破苍穹 第一章 陨落的天才" target="_blank">第一章 陨落的天才</a></li>
                                <li><a href="/1/2.html" title="斗破苍穹 第二章 斗气大陆" target="_blank">第二章 斗气大陆</a></li>
                                <li><a href="/1/3.html" title="斗破苍穹 第三章 客人" target="_blank">第三章 客人</a></li>
                                <li><a href="/1/4.html" title="斗破苍穹 第四章 云岚宗" target="_blank">第四章 云岚宗</a></li>
                                <li><a href="/1/5.html" title="斗破苍穹 第五章 聚气散" target="_blank">第五章 聚气散</a></li>
                                <li><a href="/1/6.html" title="斗破苍穹 第六章 炼药师" target="_blank">第六章 炼药师</a></li>
                                <li><a href="/1/7.html" title="斗破苍穹 第七章 休！" target="_blank">第七章 休！</a></li>
                                <li><a href="/1/8.html" title="斗破苍穹 第八章 神秘的老者" target="_blank">第八章 神秘的老者</a></li>
                                <li><a href="/1/9.html" title="斗破苍穹 第九章 药老！" target="_blank">第九章 药老！</a></li>
                                <li><a href="/1/10.html" title="斗破苍穹 第十章 借钱" target="_blank">第十章 借钱</a></li>
                                <li><a href="/1/11.html" title="斗破苍穹 第十一章 坊市" target="_blank">第十一章 坊市</a></li>
                                <li><a href="/1/12.html" title="斗破苍穹 第十二章 离他远点" target="_blank">第十二章 离他远点</a></li>
                                <li><a href="/1/13.html" title="斗破苍穹 第十三章 黑铁片" target="_blank">第十三章 黑铁片</a></li>
                                <li><a href="/1/14.html" title="斗破苍穹 第十四章 吸掌" target="_blank">第十四章 吸掌</a></li>
                                <li><a href="/1/15.html" title="斗破苍穹 第十五章 修炼" target="_blank">第十五章 修炼</a></li>
                                <li><a href="/1/16.html" title="斗破苍穹 第十六章 萧宁" target="_blank">第十六章 萧宁</a></li>
                                <li><a href="/1/17.html" title="斗破苍穹 第十七章 冲突" target="_blank">第十七章 冲突</a></li>
                                <li><a href="/1/18.html" title="斗破苍穹 第十八章 玄阶高级斗技：八极崩" target="_blank">第十八章 玄阶高级斗技：八极崩</a></li>
                                <li><a href="/1/19.html" title="斗破苍穹 第十九章 残酷训练" target="_blank">第十九章 残酷训练</a></li>
                                <li><a href="/1/20.html" title="斗破苍穹 第二十章 拍卖" target="_blank">第二十章 拍卖</a></li>
                                <li><a href="/1/21.html" title="斗破苍穹 第二十一章 二品炼药师谷尼" target="_blank">第二十一章 二品炼药师谷尼</a></li>
                                <li><a href="/1/22.html" title="斗破苍穹 第二十二章 风卷决" target="_blank">第二十二章 风卷决</a></li>
                                <li><a href="/1/23.html" title="斗破苍穹 第二十三章 争抢" target="_blank">第二十三章 争抢</a></li>
                                <li><a href="/1/24.html" title="斗破苍穹 第二十四章 一切待续" target="_blank">第二十四章 一切待续</a></li>
                                <li><a href="/1/25.html" title="斗破苍穹 第二十五章 钱由我出" target="_blank">第二十五章 钱由我出</a></li>
                                <li><a href="/1/26.html" title="斗破苍穹 第二十六章 苦修" target="_blank">第二十六章 苦修</a></li>
                                <li><a href="/1/27.html" title="斗破苍穹 第二十七章 冲击第七段" target="_blank">第二十七章 冲击第七段</a></li>
                                <li><a href="/1/28.html" title="斗破苍穹 第二十八章 强化“吸掌”" target="_blank">第二十八章 强化“吸掌”</a></li>
                                <li><a href="/1/29.html" title="斗破苍穹 第二十九章 重要的日子" target="_blank">第二十九章 重要的日子</a></li>
                                <li><a href="/1/30.html" title="斗破苍穹 第三十章 辱人者，人恒辱之" target="_blank">第三十章 辱人者，人恒辱之</a></li>
                                <li><a href="/1/31.html" title="斗破苍穹 第三十一章 一星斗者" target="_blank">第三十一章 一星斗者</a></li>
                                <li><a href="/1/32.html" title="斗破苍穹 第三十二章 挑战" target="_blank">第三十二章 挑战</a></li>
                                <li><a href="/1/33.html" title="斗破苍穹 第三十三章 证实" target="_blank">第三十三章 证实</a></li>
                                <li><a href="/1/34.html" title="斗破苍穹 第三十四章 翻身" target="_blank">第三十四章 翻身</a></li>
                                <li><a href="/1/35.html" title="斗破苍穹 第三十五章 罪恶感" target="_blank">第三十五章 罪恶感</a></li>
                                <li><a href="/1/36.html" title="斗破苍穹 第三十六章 滑稽的突破" target="_blank">第三十六章 滑稽的突破</a></li>
                                <li><a href="/1/37.html" title="斗破苍穹 第三十七章 萧玉" target="_blank">第三十七章 萧玉</a></li>
                                <li><a href="/1/38.html" title="斗破苍穹 第三十八章 这小家伙，不简单呐" target="_blank">第三十八章 这小家伙，不简单呐</a></li>
                                <li><a href="/1/39.html" title="斗破苍穹 第三十九章 仪式复测" target="_blank">第三十九章 仪式复测</a></li>
                                <li><a href="/1/40.html" title="斗破苍穹 第四十章 震撼" target="_blank">第四十章 震撼</a></li>
                                <li><a href="/1/41.html" title="斗破苍穹 第四十一章 增气散" target="_blank">第四十一章 增气散</a></li>
                                <li><a href="/1/42.html" title="斗破苍穹 第四十二章 你输了" target="_blank">第四十二章 你输了</a></li>
                                <li><a href="/1/43.html" title="斗破苍穹 第四十三章 强横的萧炎" target="_blank">第四十三章 强横的萧炎</a></li>
                                <li><a href="/1/44.html" title="斗破苍穹 第四十四章 陪你试试" target="_blank">第四十四章 陪你试试</a></li>
                                <li><a href="/1/45.html" title="斗破苍穹 第四十五章 落幕" target="_blank">第四十五章 落幕</a></li>
                                <li><a href="/1/46.html" title="斗破苍穹 第四十六章 暴怒的萧炎" target="_blank">第四十六章 暴怒的萧炎</a></li>
                                <li><a href="/1/47.html" title="斗破苍穹 第四十七章 亵渎" target="_blank">第四十七章 亵渎</a></li>
                                <li><a href="/1/48.html" title="斗破苍穹 第四十八章 斗气阁" target="_blank">第四十八章 斗气阁</a></li>
                                <li><a href="/1/49.html" title="斗破苍穹 第四十九章 选择功法" target="_blank">第四十九章 选择功法</a></li>
                                <li><a href="/1/50.html" title="斗破苍穹 第五十章 帮？" target="_blank">第五十章 帮？</a></li>
                                <li><a href="/1/51.html" title="斗破苍穹 第五十一章 安心" target="_blank">第五十一章 安心</a></li>
                                <li><a href="/1/52.html" title="斗破苍穹 第五十二章 突破" target="_blank">第五十二章 突破</a></li>
                                <li><a href="/1/53.html" title="斗破苍穹 第五十三章 第九段" target="_blank">第五十三章 第九段</a></li>
                                <li><a href="/1/54.html" title="斗破苍穹 第五十四章 筹钱" target="_blank">第五十四章 筹钱</a></li>
                                <li><a href="/1/55.html" title="斗破苍穹 第五十五章 不小心" target="_blank">第五十五章 不小心</a></li>
                                <li><a href="/1/56.html" title="斗破苍穹 第五十六章 迦南学院" target="_blank">第五十六章 迦南学院</a></li>
                                <li><a href="/1/57.html" title="斗破苍穹 第五十七章 广告" target="_blank">第五十七章 广告</a></li>
                                <li><a href="/1/58.html" title="斗破苍穹 第五十八章 高价" target="_blank">第五十八章 高价</a></li>
                                <li><a href="/1/59.html" title="斗破苍穹 第五十九章 拍卖结束" target="_blank">第五十九章 拍卖结束</a></li>
                                <li><a href="/1/60.html" title="斗破苍穹 第六十章 药材到手" target="_blank">第六十章 药材到手</a></li>
                                <li><a href="/1/61.html" title="斗破苍穹 第六十一章 装" target="_blank">第六十一章 装</a></li>
                                <li><a href="/1/62.html" title="斗破苍穹 第六十二章 打" target="_blank">第六十二章 打</a></li>
                                <li><a href="/1/63.html" title="斗破苍穹 第六十三章 异火榜" target="_blank">第六十三章 异火榜</a></li>
                                <li><a href="/1/64.html" title="斗破苍穹 第六十四章 炼制聚气散" target="_blank">第六十四章 炼制聚气散</a></li>
                                <li><a href="/1/65.html" title="斗破苍穹 第六十五章 晋级斗者" target="_blank">第六十五章 晋级斗者</a></li>
                                <li><a href="/1/66.html" title="斗破苍穹 第六十六章 焚决" target="_blank">第六十六章 焚决</a></li>
                                <li><a href="/1/67.html" title="斗破苍穹 第六十七章 选择" target="_blank">第六十七章 选择</a></li>
                                <li><a href="/1/68.html" title="斗破苍穹 第六十八章 陨落心炎" target="_blank">第六十八章 陨落心炎</a></li>
                                <li><a href="/1/69.html" title="斗破苍穹 第六十九章 气愤的薰儿" target="_blank">第六十九章 气愤的薰儿</a></li>
                                <li><a href="/1/70.html" title="斗破苍穹 第七十章 探查" target="_blank">第七十章 探查</a></li>
                                <li><a href="/1/71.html" title="斗破苍穹 地七十一章 萧家形势" target="_blank">地七十一章 萧家形势</a></li>
                                <li><a href="/1/72.html" title="斗破苍穹 第七十一章 萧家形势" target="_blank">第七十一章 萧家形势</a></li>
                                <li><a href="/1/73.html" title="斗破苍穹 第七十二章 初学炼药" target="_blank">第七十二章 初学炼药</a></li>
                                <li><a href="/1/74.html" title="斗破苍穹 第七十三章 第一次炼药" target="_blank">第七十三章 第一次炼药</a></li>
                                <li><a href="/1/75.html" title="斗破苍穹 第七十四章 不请自来" target="_blank">第七十四章 不请自来</a></li>
                                <li><a href="/1/76.html" title="斗破苍穹 第七十五章 大手笔" target="_blank">第七十五章 大手笔</a></li>
                                <li><a href="/1/77.html" title="斗破苍穹 第七十六章 合作" target="_blank">第七十六章 合作</a></li>
                                <li><a href="/1/78.html" title="斗破苍穹 第七十七章 断其药路" target="_blank">第七十七章 断其药路</a></li>
                                <li><a href="/1/79.html" title="斗破苍穹 第七十八章 炼啊炼的就突破了" target="_blank">第七十八章 炼啊炼的就突破了</a></li>
                                <li><a href="/1/80.html" title="斗破苍穹 第七十九章 萧家的反击" target="_blank">第七十九章 萧家的反击</a></li>
                                <li><a href="/1/81.html" title="斗破苍穹 第八十章 炼药师柳席" target="_blank">第八十章 炼药师柳席</a></li>
                                <li><a href="/1/82.html" title="斗破苍穹 第八十一章 察觉" target="_blank">第八十一章 察觉</a></li>
                                <li><a href="/1/83.html" title="斗破苍穹 第八十二章 坦白" target="_blank">第八十二章 坦白</a></li>
                                <li><a href="/1/84.html" title="斗破苍穹 第八十三章 小坊主" target="_blank">第八十三章 小坊主</a></li>
                                <li><a href="/1/85.html" title="斗破苍穹 第八十四章 废掉" target="_blank">第八十四章 废掉</a></li>
                                <li><a href="/1/86.html" title="斗破苍穹 第八十五章 接受" target="_blank">第八十五章 接受</a></li>
                                <li><a href="/1/87.html" title="斗破苍穹 第八十六章 挑战" target="_blank">第八十六章 挑战</a></li>
                                <li><a href="/1/88.html" title="斗破苍穹 第八十七 下杀手" target="_blank">第八十七 下杀手</a></li>
                                <li><a href="/1/89.html" title="斗破苍穹 第八十八章 落幕" target="_blank">第八十八章 落幕</a></li>
                                <li><a href="/1/90.html" title="斗破苍穹 第八十九章 月黑风高" target="_blank">第八十九章 月黑风高</a></li>
                                <li><a href="/1/91.html" title="斗破苍穹 第九十章 料理后事" target="_blank">第九十章 料理后事</a></li>
                                <li><a href="/1/92.html" title="斗破苍穹 第九十一章 夜中相遇" target="_blank">第九十一章 夜中相遇</a></li>
                                <li><a href="/1/93.html" title="斗破苍穹 第九十二章 抢" target="_blank">第九十二章 抢</a></li>
                                <li><a href="/1/94.html" title="斗破苍穹 第九十三章 半路毁药" target="_blank">第九十三章 半路毁药</a></li>
                                <li><a href="/1/95.html" title="斗破苍穹 第九十五章 眼光挺差" target="_blank">第九十五章 眼光挺差</a></li>
                                <li><a href="/1/96.html" title="斗破苍穹 第九十六章 加列家族的境地" target="_blank">第九十六章 加列家族的境地</a></li>
                                <li><a href="/1/97.html" title="斗破苍穹 第九十七章 承诺" target="_blank">第九十七章 承诺</a></li>
                                <li><a href="/1/98.html" title="斗破苍穹 第九十八章 雪妮" target="_blank">第九十八章 雪妮</a></li>
                                <li><a href="/1/99.html" title="斗破苍穹 第九十九章 刁难" target="_blank">第九十九章 刁难</a></li>
                                <li><a href="/1/100.html" title="斗破苍穹 第一百零章 威胁" target="_blank">第一百零章 威胁</a></li>
                                <li><a href="/1/101.html" title="斗破苍穹 第一百零一章 潜力值的分级" target="_blank">第一百零一章 潜力值的分级</a></li>
                                <li><a href="/1/102.html" title="斗破苍穹 第一百零二章 最恐怖的一个" target="_blank">第一百零二章 最恐怖的一个</a></li>
                                <li><a href="/1/103.html" title="斗破苍穹 第一百零三章 假期" target="_blank">第一百零三章 假期</a></li>
                                <li><a href="/1/104.html" title="斗破苍穹 第一百零四章 初战大斗师" target="_blank">第一百零四章 初战大斗师</a></li>
                                <li><a href="/1/105.html" title="斗破苍穹 第一百零五章 离去之前" target="_blank">第一百零五章 离去之前</a></li>
                                <li><a href="/1/106.html" title="斗破苍穹 第一百零六章 离开" target="_blank">第一百零六章 离开</a></li>
                                <li><a href="/1/107.html" title="斗破苍穹 第一百零七章 云岚宗" target="_blank">第一百零七章 云岚宗</a></li>
                                <li><a href="/1/108.html" title="斗破苍穹 第一百零八章 八极崩的暗劲" target="_blank">第一百零八章 八极崩的暗劲</a></li>
                                <li><a href="/1/109.html" title="斗破苍穹 第一百零九章 血莲精" target="_blank">第一百零九章 血莲精</a></li>
                                <li><a href="/1/110.html" title="斗破苍穹 第一百一十章 小医仙" target="_blank">第一百一十章 小医仙</a></li>
                                <li><a href="/1/111.html" title="斗破苍穹 第一百一十一章 加入队伍" target="_blank">第一百一十一章 加入队伍</a></li>
                                <li><a href="/1/112.html" title="斗破苍穹 第一百一十二章 进入魔兽山脉" target="_blank">第一百一十二章 进入魔兽山脉</a></li>
                                <li><a href="/1/113.html" title="斗破苍穹 第一百一十三章 山洞" target="_blank">第一百一十三章 山洞</a></li>
                                <li><a href="/1/114.html" title="斗破苍穹 第一百一十四章 探宝" target="_blank">第一百一十四章 探宝</a></li>
                                <li><a href="/1/115.html" title="斗破苍穹 第一百一十五章 洞口遇险" target="_blank">第一百一十五章 洞口遇险</a></li>
                                <li><a href="/1/116.html" title="斗破苍穹 第一百一十六章 冰灵焰草" target="_blank">第一百一十六章 冰灵焰草</a></li>
                                <li><a href="/1/117.html" title="斗破苍穹 第一百一十七章 飞行斗技：鹰之翼" target="_blank">第一百一十七章 飞行斗技：鹰之翼</a></li>
                                <li><a href="/1/118.html" title="斗破苍穹 第一百一十八章 生死逃亡" target="_blank">第一百一十八章 生死逃亡</a></li>
                                <li><a href="/1/119.html" title="斗破苍穹 第一百一十九章 紫云翼" target="_blank">第一百一十九章 紫云翼</a></li>
                                <li><a href="/1/120.html" title="斗破苍穹 第一百二十章 净莲妖火" target="_blank">第一百二十章 净莲妖火</a></li>
                                <li><a href="/1/121.html" title="斗破苍穹 第一百二十一章 晋级六星！" target="_blank">第一百二十一章 晋级六星！</a></li>
                                <li><a href="/1/122.html" title="斗破苍穹 第一百二十二章 地阶斗技：焰分噬浪尺！" target="_blank">第一百二十二章 地阶斗技：焰分噬浪尺！</a></li>
                                <li><a href="/1/123.html" title="斗破苍穹 第一百二十三章 报复开始" target="_blank">第一百二十三章 报复开始</a></li>
                                <li><a href="/1/124.html" title="斗破苍穹 第一百二十四章 杀戮" target="_blank">第一百二十四章 杀戮</a></li>
                                <li><a href="/1/125.html" title="斗破苍穹 第一百二十五章 八星斗者赫蒙" target="_blank">第一百二十五章 八星斗者赫蒙</a></li>
                                <li><a href="/1/126.html" title="斗破苍穹 第一百二十六章 击杀" target="_blank">第一百二十六章 击杀</a></li>
                                <li><a href="/1/127.html" title="斗破苍穹 第一百二十七章 大围剿" target="_blank">第一百二十七章 大围剿</a></li>
                                <li><a href="/1/128.html" title="斗破苍穹 第一百二十八章 追杀" target="_blank">第一百二十八章 追杀</a></li>
                                <li><a href="/1/129.html" title="斗破苍穹 第一百二十九章 独战斗师" target="_blank">第一百二十九章 独战斗师</a></li>
                                <li><a href="/1/130.html" title="斗破苍穹 第一百三十章 突破七星" target="_blank">第一百三十章 突破七星</a></li>
                                <li><a href="/1/131.html" title="斗破苍穹 第一百三十一章 神秘女人与六阶魔兽紫晶翼狮王" target="_blank">第一百三十一章 神秘女人与六阶魔兽紫晶翼狮王</a></li>
                                <li><a href="/1/132.html" title="斗破苍穹 第一百三十二章 斗皇级别的战斗" target="_blank">第一百三十二章 斗皇级别的战斗</a></li>
                                <li><a href="/1/133.html" title="斗破苍穹 第一百三十三章 正确的疗伤" target="_blank">第一百三十三章 正确的疗伤</a></li>
                                <li><a href="/1/134.html" title="斗破苍穹 第一百三十四章 山洞同居" target="_blank">第一百三十四章 山洞同居</a></li>
                                <li><a href="/1/135.html" title="斗破苍穹 第一百三十五章 不小心惹得祸" target="_blank">第一百三十五章 不小心惹得祸</a></li>
                                <li><a href="/1/136.html" title="斗破苍穹 第一百三十六章 救人成功" target="_blank">第一百三十六章 救人成功</a></li>
                                <li><a href="/1/137.html" title="斗破苍穹 第一百三十七章 破解封印" target="_blank">第一百三十七章 破解封印</a></li>
                                <li><a href="/1/138.html" title="斗破苍穹 第一百三十八章 联手行动" target="_blank">第一百三十八章 联手行动</a></li>
                                <li><a href="/1/139.html" title="斗破苍穹 第一百三十九章 伴生紫晶源" target="_blank">第一百三十九章 伴生紫晶源</a></li>
                                <li><a href="/1/140.html" title="斗破苍穹 第一百四十章 紫灵晶到手" target="_blank">第一百四十章 紫灵晶到手</a></li>
                                <li><a href="/1/141.html" title="斗破苍穹 第一百四十一章 生死时速" target="_blank">第一百四十一章 生死时速</a></li>
                                <li><a href="/1/142.html" title="斗破苍穹 第一百四十二章 吸收紫色能量" target="_blank">第一百四十二章 吸收紫色能量</a></li>
                                <li><a href="/1/143.html" title="斗破苍穹 第一百四十三章 九星斗者" target="_blank">第一百四十三章 九星斗者</a></li>
                                <li><a href="/1/144.html" title="斗破苍穹 第一百四十四章 甘慕" target="_blank">第一百四十四章 甘慕</a></li>
                                <li><a href="/1/145.html" title="斗破苍穹 第一百四十五章 击杀九星斗者" target="_blank">第一百四十五章 击杀九星斗者</a></li>
                                <li><a href="/1/146.html" title="斗破苍穹 第一百四十六章 再见小医仙" target="_blank">第一百四十六章 再见小医仙</a></li>
                                <li><a href="/1/147.html" title="斗破苍穹 第一百四十七章 闯狼头" target="_blank">第一百四十七章 闯狼头</a></li>
                                <li><a href="/1/148.html" title="斗破苍穹 第一百四十八章 踢场" target="_blank">第一百四十八章 踢场</a></li>
                                <li><a href="/1/149.html" title="斗破苍穹 第一百四十九章 击杀二星斗师" target="_blank">第一百四十九章 击杀二星斗师</a></li>
                                <li><a href="/1/150.html" title="斗破苍穹 第一百五十章 小山谷" target="_blank">第一百五十章 小山谷</a></li>
                                <li><a href="/1/151.html" title="斗破苍穹 第一百五十一章 紫焰" target="_blank">第一百五十一章 紫焰</a></li>
                                <li><a href="/1/152.html" title="斗破苍穹 第一百五十二章 炼化火种" target="_blank">第一百五十二章 炼化火种</a></li>
                                <li><a href="/1/153.html" title="斗破苍穹 第一百五十三章 奇怪的言行" target="_blank">第一百五十三章 奇怪的言行</a></li>
                                <li><a href="/1/154.html" title="斗破苍穹 第一百五十四章 厄难毒体" target="_blank">第一百五十四章 厄难毒体</a></li>
                                <li><a href="/1/155.html" title="斗破苍穹 第一百五十五章 可怕的体质" target="_blank">第一百五十五章 可怕的体质</a></li>
                                <li><a href="/1/156.html" title="斗破苍穹 第一百五十六章 吞噬紫火之前的准备" target="_blank">第一百五十六章 吞噬紫火之前的准备</a></li>
                                <li><a href="/1/157.html" title="斗破苍穹 第一百五十七章 魔核到手" target="_blank">第一百五十七章 魔核到手</a></li>
                                <li><a href="/1/158.html" title="斗破苍穹 第一百五十八章 炼丹！功法进化！" target="_blank">第一百五十八章 炼丹！功法进化！</a></li>
                                <li><a href="/1/159.html" title="斗破苍穹 第一百五十九章 晋阶斗师！" target="_blank">第一百五十九章 晋阶斗师！</a></li>
                                <li><a href="/1/160.html" title="斗破苍穹 第一百六十章 斗师与斗者的差距" target="_blank">第一百六十章 斗师与斗者的差距</a></li>
                                <li><a href="/1/161.html" title="斗破苍穹 第一百六十一章 离别" target="_blank">第一百六十一章 离别</a></li>
                                <li><a href="/1/162.html" title="斗破苍穹 第一百六十二章 炼化异火的三种必备之物" target="_blank">第一百六十二章 炼化异火的三种必备之物</a></li>
                                <li><a href="/1/163.html" title="斗破苍穹 第一百六十三章 奥托大师" target="_blank">第一百六十三章 奥托大师</a></li>
                                <li><a href="/1/164.html" title="斗破苍穹 第一百六十四章 炼药师公会" target="_blank">第一百六十四章 炼药师公会</a></li>
                                <li><a href="/1/165.html" title="斗破苍穹 第一百六十五章 一品炼药师的考核" target="_blank">第一百六十五章 一品炼药师的考核</a></li>
                                <li><a href="/1/166.html" title="斗破苍穹 第一百六十六章 通过考核" target="_blank">第一百六十六章 通过考核</a></li>
                                <li><a href="/1/167.html" title="斗破苍穹 第一百六十七章 最年轻的二品炼药师" target="_blank">第一百六十七章 最年轻的二品炼药师</a></li>
                                <li><a href="/1/168.html" title="斗破苍穹 第一百六十八章 炼药师的极品待遇" target="_blank">第一百六十八章 炼药师的极品待遇</a></li>
                                <li><a href="/1/169.html" title="斗破苍穹 第一百六十九章 古特" target="_blank">第一百六十九章 古特</a></li>
                                <li><a href="/1/170.html" title="斗破苍穹 第一百七十章 交换" target="_blank">第一百七十章 交换</a></li>
                                <li><a href="/1/171.html" title="斗破苍穹 第一百七十一章 冰灵寒泉到手" target="_blank">第一百七十一章 冰灵寒泉到手</a></li>
                                <li><a href="/1/172.html" title="斗破苍穹 第一百七十二章 炼药师大会" target="_blank">第一百七十二章 炼药师大会</a></li>
                                <li><a href="/1/173.html" title="斗破苍穹 第一百七十三章 飞行途中" target="_blank">第一百七十三章 飞行途中</a></li>
                                <li><a href="/1/174.html" title="斗破苍穹 第一百七十四章 五品丹药所引发的空中血案" target="_blank">第一百七十四章 五品丹药所引发的空中血案</a></li>
                                <li><a href="/1/175.html" title="斗破苍穹 第一百七十五章 抵达" target="_blank">第一百七十五章 抵达</a></li>
                                <li><a href="/1/176.html" title="斗破苍穹 第一百七十六章 神秘的残破图片？" target="_blank">第一百七十六章 神秘的残破图片？</a></li>
                                <li><a href="/1/177.html" title="斗破苍穹 第一百七十七章 神秘的老人" target="_blank">第一百七十七章 神秘的老人</a></li>
                                <li><a href="/1/178.html" title="斗破苍穹 第一百七十八章 交手" target="_blank">第一百七十八章 交手</a></li>
                                <li><a href="/1/179.html" title="斗破苍穹 第一百七十九章 药老出手" target="_blank">第一百七十九章 药老出手</a></li>
                                <li><a href="/1/180.html" title="斗破苍穹 第一百八十章 曾经的十大强者，冰皇！" target="_blank">第一百八十章 曾经的十大强者，冰皇！</a></li>
                                <li><a href="/1/181.html" title="斗破苍穹 第一百八十一章 沙漠之行" target="_blank">第一百八十一章 沙漠之行</a></li>
                                <li><a href="/1/182.html" title="斗破苍穹 第一百八十二章 沙漠苦修" target="_blank">第一百八十二章 沙漠苦修</a></li>
                                <li><a href="/1/183.html" title="斗破苍穹 第一百八十三章 巧遇" target="_blank">第一百八十三章 巧遇</a></li>
                                <li><a href="/1/184.html" title="斗破苍穹 第一百八十四章 初遇蛇人,斗师初显威" target="_blank">第一百八十四章 初遇蛇人,斗师初显威</a></li>
                                <li><a href="/1/185.html" title="斗破苍穹 第一百八十五章 兄弟" target="_blank">第一百八十五章 兄弟</a></li>
                                <li><a href="/1/186.html" title="斗破苍穹 第一百八十六章 青鳞" target="_blank">第一百八十六章 青鳞</a></li>
                                <li><a href="/1/187.html" title="斗破苍穹 第一百八十七章 测验" target="_blank">第一百八十七章 测验</a></li>
                                <li><a href="/1/188.html" title="斗破苍穹 第一百八十八章 兄弟间的比试" target="_blank">第一百八十八章 兄弟间的比试</a></li>
                                <li><a href="/1/189.html" title="斗破苍穹 第一百八十九章 青鳞的发现" target="_blank">第一百八十九章 青鳞的发现</a></li>
                                <li><a href="/1/190.html" title="斗破苍穹 第一百九十章 探测地形" target="_blank">第一百九十章 探测地形</a></li>
                                <li><a href="/1/191.html" title="斗破苍穹 第一百九十一章 解决麻烦" target="_blank">第一百九十一章 解决麻烦</a></li>
                                <li><a href="/1/192.html" title="斗破苍穹 第一百九十二章 通道" target="_blank">第一百九十二章 通道</a></li>
                                <li><a href="/1/193.html" title="斗破苍穹 第一百九十三章 探测" target="_blank">第一百九十三章 探测</a></li>
                                <li><a href="/1/194.html" title="斗破苍穹 第一百九十四章 岩浆中的神秘生物" target="_blank">第一百九十四章 岩浆中的神秘生物</a></li>
                                <li><a href="/1/195.html" title="斗破苍穹 第一百九十五章 遇袭" target="_blank">第一百九十五章 遇袭</a></li>
                                <li><a href="/1/196.html" title="斗破苍穹 第一百九十六章 双头火灵蛇" target="_blank">第一百九十六章 双头火灵蛇</a></li>
                                <li><a href="/1/197.html" title="斗破苍穹 第一百九十七章 药老出手" target="_blank">第一百九十七章 药老出手</a></li>
                                <li><a href="/1/198.html" title="斗破苍穹 第一百九十八章 碧蛇三花瞳" target="_blank">第一百九十八章 碧蛇三花瞳</a></li>
                                <li><a href="/1/199.html" title="斗破苍穹 第一百九十九章 地穴之底" target="_blank">第一百九十九章 地穴之底</a></li>
                                <li><a href="/1/200.html" title="斗破苍穹 第两百章 青莲地心火" target="_blank">第两百章 青莲地心火</a></li>
                                <li><a href="/1/201.html" title="斗破苍穹 第两百零一章 略有收获" target="_blank">第两百零一章 略有收获</a></li>
                                <li><a href="/1/202.html" title="斗破苍穹 第两百零二章 晋级！启程！" target="_blank">第两百零二章 晋级！启程！</a></li>
                                <li><a href="/1/203.html" title="斗破苍穹 第两百零三章 沙漠深处" target="_blank">第两百零三章 沙漠深处</a></li>
                                <li><a href="/1/204.html" title="斗破苍穹 第两百零四章 蛇女月媚" target="_blank">第两百零四章 蛇女月媚</a></li>
                                <li><a href="/1/205.html" title="斗破苍穹 第两百零五章 恐怖的阵容！" target="_blank">第两百零五章 恐怖的阵容！</a></li>
                                <li><a href="/1/206.html" title="斗破苍穹 第两百零六章 强者间的战斗" target="_blank">第两百零六章 强者间的战斗</a></li>
                                <li><a href="/1/207.html" title="斗破苍穹 第两百零七章 神秘黑袍人" target="_blank">第两百零七章 神秘黑袍人</a></li>
                                <li><a href="/1/208.html" title="斗破苍穹 第两百零八章 夜闯部落" target="_blank">第两百零八章 夜闯部落</a></li>
                                <li><a href="/1/209.html" title="斗破苍穹 第两百零九章 沙漠中心的城市" target="_blank">第两百零九章 沙漠中心的城市</a></li>
                                <li><a href="/1/210.html" title="斗破苍穹 第两百一十章 美杜莎女王" target="_blank">第两百一十章 美杜莎女王</a></li>
                                <li><a href="/1/211.html" title="斗破苍穹 第两百一十一章 丹王古河的大手笔！" target="_blank">第两百一十一章 丹王古河的大手笔！</a></li>
                                <li><a href="/1/212.html" title="斗破苍穹 第两百一十二章 谈判失败" target="_blank">第两百一十二章 谈判失败</a></li>
                                <li><a href="/1/213.html" title="斗破苍穹 第两百一十三章 争分夺秒" target="_blank">第两百一十三章 争分夺秒</a></li>
                                <li><a href="/1/214.html" title="斗破苍穹 第两百一十四章 再见青莲地心火！" target="_blank">第两百一十四章 再见青莲地心火！</a></li>
                                <li><a href="/1/215.html" title="斗破苍穹 第两百一十五章 进化开始" target="_blank">第两百一十五章 进化开始</a></li>
                                <li><a href="/1/216.html" title="斗破苍穹 第两百一十六章 进化成功？" target="_blank">第两百一十六章 进化成功？</a></li>
                                <li><a href="/1/217.html" title="斗破苍穹 第两百一十七章 七彩吞天蟒" target="_blank">第两百一十七章 七彩吞天蟒</a></li>
                                <li><a href="/1/218.html" title="斗破苍穹 第两百一十八章 收服青莲地心火！" target="_blank">第两百一十八章 收服青莲地心火！</a></li>
                                <li><a href="/1/219.html" title="斗破苍穹 第两百一十九章 混乱的局面" target="_blank">第两百一十九章 混乱的局面</a></li>
                                <li><a href="/1/220.html" title="斗破苍穹 第两百二十章 携宝而逃" target="_blank">第两百二十章 携宝而逃</a></li>
                                <li><a href="/1/221.html" title="斗破苍穹 第两百二十一章 千里逃亡" target="_blank">第两百二十一章 千里逃亡</a></li>
                                <li><a href="/1/222.html" title="斗破苍穹 第两百二十二章 云芝？" target="_blank">第两百二十二章 云芝？</a></li>
                                <li><a href="/1/223.html" title="斗破苍穹 第两百二十三章 短促的相见" target="_blank">第两百二十三章 短促的相见</a></li>
                                <li><a href="/1/224.html" title="斗破苍穹 第两百二十四章 五蛇毒刹印" target="_blank">第两百二十四章 五蛇毒刹印</a></li>
                                <li><a href="/1/225.html" title="斗破苍穹 第两百二十五章 能耐" target="_blank">第两百二十五章 能耐</a></li>
                                <li><a href="/1/226.html" title="斗破苍穹 第二百二十六章 开花结果时" target="_blank">第二百二十六章 开花结果时</a></li>
                                <li><a href="/1/227.html" title="斗破苍穹 第二百二十七章 异火的吞噬，启动！" target="_blank">第二百二十七章 异火的吞噬，启动！</a></li>
                                <li><a href="/1/228.html" title="斗破苍穹 第二百二十八章 抽离火种" target="_blank">第二百二十八章 抽离火种</a></li>
                                <li><a href="/1/229.html" title="斗破苍穹 第两百二十九章 异火锻体" target="_blank">第两百二十九章 异火锻体</a></li>
                                <li><a href="/1/230.html" title="斗破苍穹 第两百三十章  成功" target="_blank">第两百三十章  成功</a></li>
                                <li><a href="/1/231.html" title="斗破苍穹 第二百三十一章 修补与强化" target="_blank">第二百三十一章 修补与强化</a></li>
                                <li><a href="/1/232.html" title="斗破苍穹 第两百三十二章 萧炎的第一种本源异火：青莲地心火！" target="_blank">第两百三十二章 萧炎的第一种本源异火：青莲地心火！</a></li>
                                <li><a href="/1/233.html" title="斗破苍穹 第两百三十三章 进化功法！" target="_blank">第两百三十三章 进化功法！</a></li>
                                <li><a href="/1/234.html" title="斗破苍穹 第两百三十四章 煎熬之痛" target="_blank">第两百三十四章 煎熬之痛</a></li>
                                <li><a href="/1/235.html" title="斗破苍穹 第两百三十五章 焚决进化！" target="_blank">第两百三十五章 焚决进化！</a></li>
                                <li><a href="/1/236.html" title="斗破苍穹 第两百三十六章 再见冰皇" target="_blank">第两百三十六章 再见冰皇</a></li>
                                <li><a href="/1/237.html" title="斗破苍穹 第两百三十七章 谈话" target="_blank">第两百三十七章 谈话</a></li>
                                <li><a href="/1/238.html" title="斗破苍穹 第两百三十八章 天鼎榜" target="_blank">第两百三十八章 天鼎榜</a></li>
                                <li><a href="/1/239.html" title="斗破苍穹 第两百三十九章 深藏不露" target="_blank">第两百三十九章 深藏不露</a></li>
                                <li><a href="/1/240.html" title="斗破苍穹 第两百四十章 破解封印" target="_blank">第两百四十章 破解封印</a></li>
                                <li><a href="/1/241.html" title="斗破苍穹 第两百四十一章 残图到手，聘请保镖" target="_blank">第两百四十一章 残图到手，聘请保镖</a></li>
                                <li><a href="/1/242.html" title="斗破苍穹 地两百四十二章 石漠城的变故" target="_blank">地两百四十二章 石漠城的变故</a></li>
                                <li><a href="/1/243.html" title="斗破苍穹 地两百四十三章 击杀大斗师！" target="_blank">地两百四十三章 击杀大斗师！</a></li>
                                <li><a href="/1/244.html" title="斗破苍穹 第两百四十四章 直闯" target="_blank">第两百四十四章 直闯</a></li>
                                <li><a href="/1/245.html" title="斗破苍穹 第两百四十五章 震慑" target="_blank">第两百四十五章 震慑</a></li>
                                <li><a href="/1/246.html" title="斗破苍穹 第两百四十六章 墨家" target="_blank">第两百四十六章 墨家</a></li>
                                <li><a href="/1/247.html" title="斗破苍穹 第两百四十七章 吞并" target="_blank">第两百四十七章 吞并</a></li>
                                <li><a href="/1/248.html" title="斗破苍穹 第两百四十八章 盐城" target="_blank">第两百四十八章 盐城</a></li>
                                <li><a href="/1/249.html" title="斗破苍穹 第两百四十九章 纳兰！" target="_blank">第两百四十九章 纳兰！</a></li>
                                <li><a href="/1/250.html" title="斗破苍穹 第两百五十章 休整" target="_blank">第两百五十章 休整</a></li>
                                <li><a href="/1/251.html" title="斗破苍穹 第两百五十一章 长久打手" target="_blank">第两百五十一章 长久打手</a></li>
                                <li><a href="/1/252.html" title="斗破苍穹 第两百五十二章 纳兰嫣然" target="_blank">第两百五十二章 纳兰嫣然</a></li>
                                <li><a href="/1/253.html" title="斗破苍穹 第两百五十三章 搜寻以及墨家的野心" target="_blank">第两百五十三章 搜寻以及墨家的野心</a></li>
                                <li><a href="/1/254.html" title="斗破苍穹 第两百五十四章 墨盟" target="_blank">第两百五十四章 墨盟</a></li>
                                <li><a href="/1/255.html" title="斗破苍穹 第两百五十五章 砸场" target="_blank">第两百五十五章 砸场</a></li>
                                <li><a href="/1/256.html" title="斗破苍穹 第两百五十六章 狠辣手段" target="_blank">第两百五十六章 狠辣手段</a></li>
                                <li><a href="/1/257.html" title="斗破苍穹 第两百五十七章 斩杀墨承" target="_blank">第两百五十七章 斩杀墨承</a></li>
                                <li><a href="/1/258.html" title="斗破苍穹 第两百五十八章 神秘的青衣女人" target="_blank">第两百五十八章 神秘的青衣女人</a></li>
                                <li><a href="/1/259.html" title="斗破苍穹 第两百五十九章 三名斗皇强者的战斗！" target="_blank">第两百五十九章 三名斗皇强者的战斗！</a></li>
                                <li><a href="/1/260.html" title="斗破苍穹 第两百六十章 八翼黑蛇皇" target="_blank">第两百六十章 八翼黑蛇皇</a></li>
                                <li><a href="/1/261.html" title="斗破苍穹 第两百六十一章 天空大战" target="_blank">第两百六十一章 天空大战</a></li>
                                <li><a href="/1/262.html" title="斗破苍穹 第两百六十二章 异火相融，佛怒火莲！" target="_blank">第两百六十二章 异火相融，佛怒火莲！</a></li>
                                <li><a href="/1/263.html" title="斗破苍穹 第两百六十三章 恐怖的破坏力" target="_blank">第两百六十三章 恐怖的破坏力</a></li>
                                <li><a href="/1/264.html" title="斗破苍穹 第两百六十四章 药老沉睡" target="_blank">第两百六十四章 药老沉睡</a></li>
                                <li><a href="/1/265.html" title="斗破苍穹 第两百六十五章 依靠自己" target="_blank">第两百六十五章 依靠自己</a></li>
                                <li><a href="/1/266.html" title="斗破苍穹 第两百六十六章 休养与控火能力" target="_blank">第两百六十六章 休养与控火能力</a></li>
                                <li><a href="/1/267.html" title="斗破苍穹 第两百六十七章 美杜莎女王再现？" target="_blank">第两百六十七章 美杜莎女王再现？</a></li>
                                <li><a href="/1/268.html" title="斗破苍穹 第两百六十八章 较量" target="_blank">第两百六十八章 较量</a></li>
                                <li><a href="/1/269.html" title="斗破苍穹 第两百六十九章 暴涨的契合度" target="_blank">第两百六十九章 暴涨的契合度</a></li>
                                <li><a href="/1/270.html" title="斗破苍穹 第两百七十章 紫火丹" target="_blank">第两百七十章 紫火丹</a></li>
                                <li><a href="/1/271.html" title="斗破苍穹 第两百七十一章 山寨版的佛怒火莲" target="_blank">第两百七十一章 山寨版的佛怒火莲</a></li>
                                <li><a href="/1/272.html" title="斗破苍穹 第两百七十二章 解决隐患，离开之前" target="_blank">第两百七十二章 解决隐患，离开之前</a></li>
                                <li><a href="/1/273.html" title="斗破苍穹 第两百七十三章 抵达帝都" target="_blank">第两百七十三章 抵达帝都</a></li>
                                <li><a href="/1/274.html" title="斗破苍穹 第两百七十四 章 米特尔拍卖场，故人" target="_blank">第两百七十四 章 米特尔拍卖场，故人</a></li>
                                <li><a href="/1/275.html" title="斗破苍穹 第两百七十五章 恶毒" target="_blank">第两百七十五章 恶毒</a></li>
                                <li><a href="/1/276.html" title="斗破苍穹 第两百七十六章  寻药" target="_blank">第两百七十六章  寻药</a></li>
                                <li><a href="/1/277.html" title="斗破苍穹 第两百七十七章 阻拦" target="_blank">第两百七十七章 阻拦</a></li>
                                <li><a href="/1/278.html" title="斗破苍穹 第两百七十八章 贱骨头" target="_blank">第两百七十八章 贱骨头</a></li>
                                <li><a href="/1/279.html" title="斗破苍穹 第两百七十九章 七幻青灵涎" target="_blank">第两百七十九章 七幻青灵涎</a></li>
                                <li><a href="/1/280.html" title="斗破苍穹 第两百八十章 薰儿" target="_blank">第两百八十章 薰儿</a></li>
                                <li><a href="/1/281.html" title="斗破苍穹 第两百八十一章 隐藏在暗中的保护" target="_blank">第两百八十一章 隐藏在暗中的保护</a></li>
                                <li><a href="/1/282.html" title="斗破苍穹 第两百八十二章 我试试" target="_blank">第两百八十二章 我试试</a></li>
                                <li><a href="/1/283.html" title="斗破苍穹 第两百八十三章 倔着骨，咬着牙，忍着辱" target="_blank">第两百八十三章 倔着骨，咬着牙，忍着辱</a></li>
                                <li><a href="/1/284.html" title="斗破苍穹 第两百八十四章 驱毒" target="_blank">第两百八十四章 驱毒</a></li>
                                <li><a href="/1/285.html" title="斗破苍穹 第两百八十五章 意外之喜，黑指" target="_blank">第两百八十五章 意外之喜，黑指</a></li>
                                <li><a href="/1/286.html" title="斗破苍穹 第两百八十六章 淘宝" target="_blank">第两百八十六章 淘宝</a></li>
                                <li><a href="/1/287.html" title="斗破苍穹 第两百八十七章 冠军的福利" target="_blank">第两百八十七章 冠军的福利</a></li>
                                <li><a href="/1/288.html" title="斗破苍穹 第两百八十八章 参加" target="_blank">第两百八十八章 参加</a></li>
                                <li><a href="/1/289.html" title="斗破苍穹 第两百八十九章 柳翎" target="_blank">第两百八十九章 柳翎</a></li>
                                <li><a href="/1/290.html" title="斗破苍穹 第两百九十章 潜在对手" target="_blank">第两百九十章 潜在对手</a></li>
                                <li><a href="/1/291.html" title="斗破苍穹 第两百九十一章 晋级七星，最后的测验" target="_blank">第两百九十一章 晋级七星，最后的测验</a></li>
                                <li><a href="/1/292.html" title="斗破苍穹 第两百九十二章 提炼" target="_blank">第两百九十二章 提炼</a></li>
                                <li><a href="/1/293.html" title="斗破苍穹 第两百九十三章  测验" target="_blank">第两百九十三章  测验</a></li>
                                <li><a href="/1/294.html" title="斗破苍穹 第两百九十四章 结束" target="_blank">第两百九十四章 结束</a></li>
                                <li><a href="/1/295.html" title="斗破苍穹 第两百九十六章 黑马" target="_blank">第两百九十六章 黑马</a></li>
                                <li><a href="/1/296.html" title="斗破苍穹 第两百九十七章 聚会，木战" target="_blank">第两百九十七章 聚会，木战</a></li>
                                <li><a href="/1/297.html" title="斗破苍穹 第两百九十八章 短暂的对决" target="_blank">第两百九十八章 短暂的对决</a></li>
                                <li><a href="/1/298.html" title="斗破苍穹 第两百九十九章 纳兰嫣然的出手" target="_blank">第两百九十九章 纳兰嫣然的出手</a></li>
                                <li><a href="/1/299.html" title="斗破苍穹 第三百章 收场" target="_blank">第三百章 收场</a></li>
                                <li><a href="/1/300.html" title="斗破苍穹 第三百零一章 突如其来的斗皇气势" target="_blank">第三百零一章 突如其来的斗皇气势</a></li>
                                <li><a href="/1/301.html" title="斗破苍穹 第三百零二章 麻袍加老" target="_blank">第三百零二章 麻袍加老</a></li>
                                <li><a href="/1/302.html" title="斗破苍穹 第三百零三章 加老的实力" target="_blank">第三百零三章 加老的实力</a></li>
                                <li><a href="/1/303.html" title="斗破苍穹 第三百零四章 法犸，夭夜，大会开始！【三更合一，包括了五百票的加更！】" target="_blank">第三百零四章 法犸，夭夜，大会开始！【三更合一，包括了五百票的加更！】</a></li>
                                <li><a href="/1/304.html" title="斗破苍穹 第三百零五章 第一轮，开始！" target="_blank">第三百零五章 第一轮，开始！</a></li>
                                <li><a href="/1/305.html" title="斗破苍穹 第三百零六章 惊心动魄【五千，今日九千字到！】" target="_blank">第三百零六章 惊心动魄【五千，今日九千字到！】</a></li>
                                <li><a href="/1/306.html" title="斗破苍穹 第三百零七章 测验，神秘的灰袍人！【两更合一！】" target="_blank">第三百零七章 测验，神秘的灰袍人！【两更合一！】</a></li>
                                <li><a href="/1/307.html" title="斗破苍穹 第三百零八章 过于简单的第二轮【这算是第一千票的加更吧。】" target="_blank">第三百零八章 过于简单的第二轮【这算是第一千票的加更吧。】</a></li>
                                <li><a href="/1/308.html" title="斗破苍穹 第三百零九章 问题所在" target="_blank">第三百零九章 问题所在</a></li>
                                <li><a href="/1/309.html" title="斗破苍穹 第三百一十章  力挽狂澜,大会暂休【二合一！】" target="_blank">第三百一十章  力挽狂澜,大会暂休【二合一！】</a></li>
                                <li><a href="/1/310.html" title="斗破苍穹 第三百一十章 力挽狂澜,大会暂休" target="_blank">第三百一十章 力挽狂澜,大会暂休</a></li>
                                <li><a href="/1/311.html" title="斗破苍穹 第三百一十一章  诡秘的黑袍人" target="_blank">第三百一十一章  诡秘的黑袍人</a></li>
                                <li><a href="/1/312.html" title="斗破苍穹 第三百一十二章  真相" target="_blank">第三百一十二章  真相</a></li>
                                <li><a href="/1/313.html" title="斗破苍穹 第三百一十三章 炎利" target="_blank">第三百一十三章 炎利</a></li>
                                <li><a href="/1/314.html" title="斗破苍穹 第三百一十四章 天降横财" target="_blank">第三百一十四章 天降横财</a></li>
                                <li><a href="/1/315.html" title="斗破苍穹 第三百一十五章 三纹青灵丹【第四更！】" target="_blank">第三百一十五章 三纹青灵丹【第四更！】</a></li>
                                <li><a href="/1/316.html" title="斗破苍穹 第三百一十六章 最后一轮：开始！" target="_blank">第三百一十六章 最后一轮：开始！</a></li>
                                <li><a href="/1/317.html" title="斗破苍穹 第三百一十七章 各显神通" target="_blank">第三百一十七章 各显神通</a></li>
                                <li><a href="/1/318.html" title="斗破苍穹 第三百一十八章 失败" target="_blank">第三百一十八章 失败</a></li>
                                <li><a href="/1/319.html" title="斗破苍穹 第三百一十九章 冠军，我要了！" target="_blank">第三百一十九章 冠军，我要了！</a></li>
                                <li><a href="/1/320.html" title="斗破苍穹 第三百二十章  再度崛起" target="_blank">第三百二十章  再度崛起</a></li>
                                <li><a href="/1/321.html" title="斗破苍穹 第三百二十一章  紫心破障丹" target="_blank">第三百二十一章  紫心破障丹</a></li>
                                <li><a href="/1/322.html" title="斗破苍穹 第三百二十二章 炸炉" target="_blank">第三百二十二章 炸炉</a></li>
                                <li><a href="/1/323.html" title="斗破苍穹 第三百二十三章 最后的胜利者！【迟来的第三更！抱歉！】" target="_blank">第三百二十三章 最后的胜利者！【迟来的第三更！抱歉！】</a></li>
                                <li><a href="/1/324.html" title="斗破苍穹 第三百二十四章  评价" target="_blank">第三百二十四章  评价</a></li>
                                <li><a href="/1/325.html" title="斗破苍穹 第三百二十五章  大会结束！" target="_blank">第三百二十五章  大会结束！</a></li>
                                <li><a href="/1/326.html" title="斗破苍穹 第三百二十六章  领取奖励" target="_blank">第三百二十六章  领取奖励</a></li>
                                <li><a href="/1/327.html" title="斗破苍穹 第三百二十七章 七幻青灵涎到手【第三更！】" target="_blank">第三百二十七章 七幻青灵涎到手【第三更！】</a></li>
                                <li><a href="/1/328.html" title="斗破苍穹 第三百二十八章  药老苏醒？" target="_blank">第三百二十八章  药老苏醒？</a></li>
                                <li><a href="/1/329.html" title="斗破苍穹 第三百二十九章 夜谈" target="_blank">第三百二十九章 夜谈</a></li>
                                <li><a href="/1/330.html" title="斗破苍穹 第三百三十章 服用三纹青灵丹" target="_blank">第三百三十章 服用三纹青灵丹</a></li>
                                <li><a href="/1/331.html" title="斗破苍穹 第三百三十一章  晋阶大斗师！" target="_blank">第三百三十一章  晋阶大斗师！</a></li>
                                <li><a href="/1/332.html" title="斗破苍穹 第三百三十二章  托付" target="_blank">第三百三十二章  托付</a></li>
                                <li><a href="/1/333.html" title="斗破苍穹 第三百三十三章  萧家，萧炎！" target="_blank">第三百三十三章  萧家，萧炎！</a></li>
                                <li><a href="/1/334.html" title="斗破苍穹 第三百三十四章 三年之约！" target="_blank">第三百三十四章 三年之约！</a></li>
                                <li><a href="/1/335.html" title="斗破苍穹 第三百三十五章 纳兰嫣然，败？" target="_blank">第三百三十五章 纳兰嫣然，败？</a></li>
                                <li><a href="/1/336.html" title="斗破苍穹 第三百三十六章 双方的真实实力" target="_blank">第三百三十六章 双方的真实实力</a></li>
                                <li><a href="/1/337.html" title="斗破苍穹 第三百三十七章  白热化的战斗！" target="_blank">第三百三十七章  白热化的战斗！</a></li>
                                <li><a href="/1/338.html" title="斗破苍穹 第三百三十八章  风之极：落日耀" target="_blank">第三百三十八章  风之极：落日耀</a></li>
                                <li><a href="/1/339.html" title="斗破苍穹 第三百三十九章  暴露" target="_blank">第三百三十九章  暴露</a></li>
                                <li><a href="/1/340.html" title="斗破苍穹 第三百四十章 小型佛怒火莲！" target="_blank">第三百四十章 小型佛怒火莲！</a></li>
                                <li><a href="/1/341.html" title="斗破苍穹 第三百四十一章  结束！" target="_blank">第三百四十一章  结束！</a></li>
                                <li><a href="/1/342.html" title="斗破苍穹 第三百四十二章  风波再起" target="_blank">第三百四十二章  风波再起</a></li>
                                <li><a href="/1/343.html" title="斗破苍穹 第三百四十三章  逃不掉的麻烦" target="_blank">第三百四十三章  逃不掉的麻烦</a></li>
                                <li><a href="/1/344.html" title="斗破苍穹 第三百四十四章  一触即发【第一更，求保底月票！】" target="_blank">第三百四十四章  一触即发【第一更，求保底月票！】</a></li>
                                <li><a href="/1/345.html" title="斗破苍穹 第三百四十五章 三名斗王强者【第二更，求月票！】" target="_blank">第三百四十五章 三名斗王强者【第二更，求月票！】</a></li>
                                <li><a href="/1/346.html" title="斗破苍穹 第三百四十六章  大战！【第三更到，呐喊一声，月票~~~！】" target="_blank">第三百四十六章  大战！【第三更到，呐喊一声，月票~~~！】</a></li>
                                <li><a href="/1/347.html" title="斗破苍穹 第三百四十七章  七彩吞天蟒出场！" target="_blank">第三百四十七章  七彩吞天蟒出场！</a></li>
                                <li><a href="/1/348.html" title="斗破苍穹 第三百四十八章  悲剧的云棱" target="_blank">第三百四十八章  悲剧的云棱</a></li>
                                <li><a href="/1/349.html" title="斗破苍穹 第三百四十九章 云烟覆日阵" target="_blank">第三百四十九章 云烟覆日阵</a></li>
                                <li><a href="/1/350.html" title="斗破苍穹 第三百五十章 神秘斗皇出场！" target="_blank">第三百五十章 神秘斗皇出场！</a></li>
                                <li><a href="/1/351.html" title="斗破苍穹 第三百五十一章  斗皇，凌影" target="_blank">第三百五十一章  斗皇，凌影</a></li>
                                <li><a href="/1/352.html" title="斗破苍穹 第三百五十二章  云岚宗的底牌！" target="_blank">第三百五十二章  云岚宗的底牌！</a></li>
                                <li><a href="/1/353.html" title="斗破苍穹 第三百五十三章  云岚宗上任宗主，斗宗云山！" target="_blank">第三百五十三章  云岚宗上任宗主，斗宗云山！</a></li>
                                <li><a href="/1/354.html" title="斗破苍穹 第三百五十四章  下山" target="_blank">第三百五十四章  下山</a></li>
                                <li><a href="/1/355.html" title="斗破苍穹 第三百五十五章 分别与交易" target="_blank">第三百五十五章 分别与交易</a></li>
                                <li><a href="/1/356.html" title="斗破苍穹 第三百五十六章  回家之途" target="_blank">第三百五十六章  回家之途</a></li>
                                <li><a href="/1/357.html" title="斗破苍穹 第三百五十七章  萧家变故" target="_blank">第三百五十七章  萧家变故</a></li>
                                <li><a href="/1/358.html" title="斗破苍穹 第三百五十八章 一个不留" target="_blank">第三百五十八章 一个不留</a></li>
                                <li><a href="/1/359.html" title="斗破苍穹 第三百五十九章 他必须死！" target="_blank">第三百五十九章 他必须死！</a></li>
                                <li><a href="/1/360.html" title="斗破苍穹 第三百六十章  安顿萧家" target="_blank">第三百六十章  安顿萧家</a></li>
                                <li><a href="/1/361.html" title="斗破苍穹 第三百六十一章  再上云岚宗！【拉下推荐票！谢谢！】" target="_blank">第三百六十一章  再上云岚宗！【拉下推荐票！谢谢！】</a></li>
                                <li><a href="/1/362.html" title="斗破苍穹 第三百六十二章  药岩，云芝" target="_blank">第三百六十二章  药岩，云芝</a></li>
                                <li><a href="/1/363.html" title="斗破苍穹 第三百六十三章 击杀云棱！【拉推荐票！】" target="_blank">第三百六十三章 击杀云棱！【拉推荐票！】</a></li>
                                <li><a href="/1/364.html" title="斗破苍穹 第三百六十四章  生死之局！" target="_blank">第三百六十四章  生死之局！</a></li>
                                <li><a href="/1/365.html" title="斗破苍穹 第三百六十五章  生死门" target="_blank">第三百六十五章  生死门</a></li>
                                <li><a href="/1/366.html" title="斗破苍穹 第三百三十六章  斗宗强者间的大战！" target="_blank">第三百三十六章  斗宗强者间的大战！</a></li>
                                <li><a href="/1/367.html" title="斗破苍穹 第三百三十七章 大逃亡开始" target="_blank">第三百三十七章 大逃亡开始</a></li>
                                <li><a href="/1/368.html" title="斗破苍穹 第三百三十八章  养伤" target="_blank">第三百三十八章  养伤</a></li>
                                <li><a href="/1/369.html" title="斗破苍穹 第三百三十九章 节节攀升！晋级！" target="_blank">第三百三十九章 节节攀升！晋级！</a></li>
                                <li><a href="/1/370.html" title="斗破苍穹 第三百四十章 天火三玄变！" target="_blank">第三百四十章 天火三玄变！</a></li>
                                <li><a href="/1/371.html" title="斗破苍穹 第三百四十一章  秘法的妙处" target="_blank">第三百四十一章  秘法的妙处</a></li>
                                <li><a href="/1/372.html" title="斗破苍穹 第三百四十二章 血腥报复！" target="_blank">第三百四十二章 血腥报复！</a></li>
                                <li><a href="/1/373.html" title="斗破苍穹 第三百四十三章 魔兽山脉中的围杀" target="_blank">第三百四十三章 魔兽山脉中的围杀</a></li>
                                <li><a href="/1/374.html" title="斗破苍穹 第三百四十四章  突如其来的援兵" target="_blank">第三百四十四章  突如其来的援兵</a></li>
                                <li><a href="/1/375.html" title="斗破苍穹 第三百四十五章  逃脱" target="_blank">第三百四十五章  逃脱</a></li>
                                <li><a href="/1/376.html" title="斗破苍穹 第三百四十六章 大岭城" target="_blank">第三百四十六章 大岭城</a></li>
                                <li><a href="/1/377.html" title="斗破苍穹 第三百四十七章  离开前的准备" target="_blank">第三百四十七章  离开前的准备</a></li>
                                <li><a href="/1/378.html" title="斗破苍穹 第三百四十八章  黑角域" target="_blank">第三百四十八章  黑角域</a></li>
                                <li><a href="/1/379.html" title="斗破苍穹 第三百四十九章  暴露" target="_blank">第三百四十九章  暴露</a></li>
                                <li><a href="/1/380.html" title="斗破苍穹 第三百五十章  离开加玛帝国！" target="_blank">第三百五十章  离开加玛帝国！</a></li>
                                <li><a href="/1/381.html" title="斗破苍穹 第三百五十一章  神秘势力，魂殿？" target="_blank">第三百五十一章  神秘势力，魂殿？</a></li>
                                <li><a href="/1/382.html" title="斗破苍穹 第三百五十二章  迦南学院，萧家有女初长成" target="_blank">第三百五十二章  迦南学院，萧家有女初长成</a></li>
                                <li><a href="/1/383.html" title="斗破苍穹 第三百五十三章  黑域大平原" target="_blank">第三百五十三章  黑域大平原</a></li>
                                <li><a href="/1/384.html" title="斗破苍穹 第三百五十四章  不需要慈悲的混乱地域" target="_blank">第三百五十四章  不需要慈悲的混乱地域</a></li>
                                <li><a href="/1/385.html" title="斗破苍穹 第三百五十五章 黑榜，黑风暴【第三更！】" target="_blank">第三百五十五章 黑榜，黑风暴【第三更！】</a></li>
                                <li><a href="/1/386.html" title="斗破苍穹 第三百五十六章  黑印城" target="_blank">第三百五十六章  黑印城</a></li>
                                <li><a href="/1/387.html" title="斗破苍穹 第三百五十七章  经济窘迫的萧炎" target="_blank">第三百五十七章  经济窘迫的萧炎</a></li>
                                <li><a href="/1/388.html" title="斗破苍穹 第三百五十八章  炼丹脱贫" target="_blank">第三百五十八章  炼丹脱贫</a></li>
                                <li><a href="/1/389.html" title="斗破苍穹 第三百五十九章  黑印拍卖场" target="_blank">第三百五十九章  黑印拍卖场</a></li>
                                <li><a href="/1/390.html" title="斗破苍穹 第三百六十章 拍卖会开始" target="_blank">第三百六十章 拍卖会开始</a></li>
                                <li><a href="/1/391.html" title="斗破苍穹 第三百六十一章 飞行斗技：雷蝠天翼" target="_blank">第三百六十一章 飞行斗技：雷蝠天翼</a></li>
                                <li><a href="/1/392.html" title="斗破苍穹 第三百六十二章  雷蝠天翼的争夺以及残破地图" target="_blank">第三百六十二章  雷蝠天翼的争夺以及残破地图</a></li>
                                <li><a href="/1/393.html" title="斗破苍穹 第三百六十三章 横生变故【第三更到，求月票！】" target="_blank">第三百六十三章 横生变故【第三更到，求月票！】</a></li>
                                <li><a href="/1/394.html" title="斗破苍穹 第三百六十四章 地阶身法斗技：三千雷动" target="_blank">第三百六十四章 地阶身法斗技：三千雷动</a></li>
                                <li><a href="/1/395.html" title="斗破苍穹 第三百六十五章 重头戏！" target="_blank">第三百六十五章 重头戏！</a></li>
                                <li><a href="/1/396.html" title="斗破苍穹 第三百六十六章 七品丹药：阴阳玄龙丹！" target="_blank">第三百六十六章 七品丹药：阴阳玄龙丹！</a></li>
                                <li><a href="/1/397.html" title="斗破苍穹 第三百六十七章 尾随【第三更！】" target="_blank">第三百六十七章 尾随【第三更！】</a></li>
                                <li><a href="/1/398.html" title="斗破苍穹 第三百六十八章 埋伏截杀" target="_blank">第三百六十八章 埋伏截杀</a></li>
                                <li><a href="/1/399.html" title="斗破苍穹 第三百六十九章 大路激战" target="_blank">第三百六十九章 大路激战</a></li>
                                <li><a href="/1/400.html" title="斗破苍穹 第三百七十章  鹬蚌相争，萧炎得利！【第三更！】" target="_blank">第三百七十章  鹬蚌相争，萧炎得利！【第三更！】</a></li>
                                <li><a href="/1/401.html" title="斗破苍穹 第三百七十一章  天火三玄变第一重：青莲变！" target="_blank">第三百七十一章  天火三玄变第一重：青莲变！</a></li>
                                <li><a href="/1/402.html" title="斗破苍穹 第三百七十二章  收获！" target="_blank">第三百七十二章  收获！</a></li>
                                <li><a href="/1/403.html" title="斗破苍穹 第三百七十三章 吞服阴阳玄龙丹！" target="_blank">第三百七十三章 吞服阴阳玄龙丹！</a></li>
                                <li><a href="/1/404.html" title="斗破苍穹 第三百七十四章  和平镇" target="_blank">第三百七十四章  和平镇</a></li>
                                <li><a href="/1/405.html" title="斗破苍穹 第三百七十五章 迦南学院执法队" target="_blank">第三百七十五章 迦南学院执法队</a></li>
                                <li><a href="/1/406.html" title="斗破苍穹 第三百七十六章 关键时刻！【七千字，月中求月票！】" target="_blank">第三百七十六章 关键时刻！【七千字，月中求月票！】</a></li>
                                <li><a href="/1/407.html" title="斗破苍穹 第三百三十七章 一招" target="_blank">第三百三十七章 一招</a></li>
                                <li><a href="/1/408.html" title="斗破苍穹 第三百三十八章  杀鸡儆猴" target="_blank">第三百三十八章  杀鸡儆猴</a></li>
                                <li><a href="/1/409.html" title="斗破苍穹 第三百三十九章  黑夜中的对碰" target="_blank">第三百三十九章  黑夜中的对碰</a></li>
                                <li><a href="/1/410.html" title="斗破苍穹 第三百四十章 初次交锋" target="_blank">第三百四十章 初次交锋</a></li>
                                <li><a href="/1/411.html" title="斗破苍穹 第三百三十八章 扑朔迷离" target="_blank">第三百三十八章 扑朔迷离</a></li>
                                <li><a href="/1/412.html" title="斗破苍穹 第三百三十九章  劲敌" target="_blank">第三百三十九章  劲敌</a></li>
                                <li><a href="/1/413.html" title="斗破苍穹 第三百八十三章 对战陆牧" target="_blank">第三百八十三章 对战陆牧</a></li>
                                <li><a href="/1/414.html" title="斗破苍穹 第三百八十四章  玩火" target="_blank">第三百八十四章  玩火</a></li>
                                <li><a href="/1/415.html" title="斗破苍穹 第三百八十六章 丹火之技" target="_blank">第三百八十六章 丹火之技</a></li>
                                <li><a href="/1/416.html" title="斗破苍穹 第三百八十七章  执法队：吴昊" target="_blank">第三百八十七章  执法队：吴昊</a></li>
                                <li><a href="/1/417.html" title="斗破苍穹 第三百八十八章 挑战" target="_blank">第三百八十八章 挑战</a></li>
                                <li><a href="/1/418.html" title="斗破苍穹 第三百八十九章 家传玉片" target="_blank">第三百八十九章 家传玉片</a></li>
                                <li><a href="/1/419.html" title="斗破苍穹 第三百九十章  最后的选拔赛" target="_blank">第三百九十章  最后的选拔赛</a></li>
                                <li><a href="/1/420.html" title="斗破苍穹 第三百九十一章 　大混战" target="_blank">第三百九十一章 　大混战</a></li>
                                <li><a href="/1/421.html" title="斗破苍穹 第三百九十二章 　撼雷地弧爆【第三更！】" target="_blank">第三百九十二章 　撼雷地弧爆【第三更！】</a></li>
                                <li><a href="/1/422.html" title="斗破苍穹 第三百九十三章  战斗中晋级！【第四更！】" target="_blank">第三百九十三章  战斗中晋级！【第四更！】</a></li>
                                <li><a href="/1/423.html" title="斗破苍穹 第三百九十四章  薰儿的实力【第五更，已经到极限了，没办法了。】" target="_blank">第三百九十四章  薰儿的实力【第五更，已经到极限了，没办法了。】</a></li>
                                <li><a href="/1/424.html" title="斗破苍穹 第三百九十五章 　以一敌三" target="_blank">第三百九十五章 　以一敌三</a></li>
                                <li><a href="/1/425.html" title="斗破苍穹 第三百九十七章 毫不留情" target="_blank">第三百九十七章 毫不留情</a></li>
                                <li><a href="/1/426.html" title="斗破苍穹 第三百九十八章 比赛落幕【第一更！】" target="_blank">第三百九十八章 比赛落幕【第一更！】</a></li>
                                <li><a href="/1/427.html" title="斗破苍穹 第三百九十九章  大赛后的安宁【第二更！】" target="_blank">第三百九十九章  大赛后的安宁【第二更！】</a></li>
                                <li><a href="/1/428.html" title="斗破苍穹 第四百章 神秘的藏书阁【第三更！】" target="_blank">第四百章 神秘的藏书阁【第三更！】</a></li>
                                <li><a href="/1/429.html" title="斗破苍穹 第四百零一章   神秘的守阁人" target="_blank">第四百零一章   神秘的守阁人</a></li>
                                <li><a href="/1/430.html" title="斗破苍穹 第四百零二章  争抢【第二更！】" target="_blank">第四百零二章  争抢【第二更！】</a></li>
                                <li><a href="/1/431.html" title="斗破苍穹 第四百零三章  声波斗技【第三更!】" target="_blank">第四百零三章  声波斗技【第三更!】</a></li>
                                <li><a href="/1/432.html" title="斗破苍穹 第四百零四章   狮虎碎金吟" target="_blank">第四百零四章   狮虎碎金吟</a></li>
                                <li><a href="/1/433.html" title="斗破苍穹 第四百零五章  修炼" target="_blank">第四百零五章  修炼</a></li>
                                <li><a href="/1/434.html" title="斗破苍穹 第四百零六章  虎啸震山林" target="_blank">第四百零六章  虎啸震山林</a></li>
                                <li><a href="/1/435.html" title="斗破苍穹 第四百零七章 内院的位置" target="_blank">第四百零七章 内院的位置</a></li>
                                <li><a href="/1/436.html" title="斗破苍穹 第四百零八章  火能猎捕赛" target="_blank">第四百零八章  火能猎捕赛</a></li>
                                <li><a href="/1/437.html" title="斗破苍穹 第四百零九章  队长【第三更】" target="_blank">第四百零九章  队长【第三更】</a></li>
                                <li><a href="/1/438.html" title="斗破苍穹 第四百一十章  反抢【第一更！】" target="_blank">第四百一十章  反抢【第一更！】</a></li>
                                <li><a href="/1/439.html" title="斗破苍穹 第四百一十一章  火能的作用【第二更！】" target="_blank">第四百一十一章  火能的作用【第二更！】</a></li>
                                <li><a href="/1/440.html" title="斗破苍穹 第四百一十二章   猎人与猎物的位置调换【第三更！】" target="_blank">第四百一十二章   猎人与猎物的位置调换【第三更！】</a></li>
                                <li><a href="/1/441.html" title="斗破苍穹 第四百一十三章  飞速成长的配合【第四更！求保底月票！】" target="_blank">第四百一十三章  飞速成长的配合【第四更！求保底月票！】</a></li>
                                <li><a href="/1/442.html" title="斗破苍穹 第四百一十四章   形成整体之后的战斗力【第一更！】" target="_blank">第四百一十四章   形成整体之后的战斗力【第一更！】</a></li>
                                <li><a href="/1/443.html" title="斗破苍穹 第四百一十五章   大反击【第二更！】" target="_blank">第四百一十五章   大反击【第二更！】</a></li>
                                <li><a href="/1/444.html" title="斗破苍穹 第四百一十六章 强者对战【第三更！】" target="_blank">第四百一十六章 强者对战【第三更！】</a></li>
                                <li><a href="/1/445.html" title="斗破苍穹 第四百一十七章  大战起【求声月票！】" target="_blank">第四百一十七章  大战起【求声月票！】</a></li>
                                <li><a href="/1/446.html" title="斗破苍穹 第四百一十八章  胜局暂现" target="_blank">第四百一十八章  胜局暂现</a></li>
                                <li><a href="/1/447.html" title="斗破苍穹 第四百一十九章  鹬蚌相争，渔翁后随" target="_blank">第四百一十九章  鹬蚌相争，渔翁后随</a></li>
                                <li><a href="/1/448.html" title="斗破苍穹 第四百二十章  变故" target="_blank">第四百二十章  变故</a></li>
                                <li><a href="/1/449.html" title="斗破苍穹 第四百二十一章  斗黑煞队" target="_blank">第四百二十一章  斗黑煞队</a></li>
                                <li><a href="/1/450.html" title="斗破苍穹 第四百二十二章   争分夺秒【第三更！】" target="_blank">第四百二十二章   争分夺秒【第三更！】</a></li>
                                <li><a href="/1/451.html" title="斗破苍穹 第四百二十二章 争分夺秒" target="_blank">第四百二十二章 争分夺秒</a></li>
                                <li><a href="/1/452.html" title="斗破苍穹 第四百二十三章  扭转局面" target="_blank">第四百二十三章  扭转局面</a></li>
                                <li><a href="/1/453.html" title="斗破苍穹 第四百二十四章 　悲愤的沙铁" target="_blank">第四百二十四章 　悲愤的沙铁</a></li>
                                <li><a href="/1/454.html" title="斗破苍穹 第四百二十五章   分赃，养伤" target="_blank">第四百二十五章   分赃，养伤</a></li>
                                <li><a href="/1/455.html" title="斗破苍穹 第四百二十六章  白煞队" target="_blank">第四百二十六章  白煞队</a></li>
                                <li><a href="/1/456.html" title="斗破苍穹 第四百二十七章   最后的大战！" target="_blank">第四百二十七章   最后的大战！</a></li>
                                <li><a href="/1/457.html" title="斗破苍穹 第四百二十八章  赢！" target="_blank">第四百二十八章  赢！</a></li>
                                <li><a href="/1/458.html" title="斗破苍穹 第四百二十九章 奖励" target="_blank">第四百二十九章 奖励</a></li>
                                <li><a href="/1/459.html" title="斗破苍穹 第四百三十章  安顿" target="_blank">第四百三十章  安顿</a></li>
                                <li><a href="/1/460.html" title="斗破苍穹 第四百三十一章  新生纳贡费【第一更！】" target="_blank">第四百三十一章  新生纳贡费【第一更！】</a></li>
                                <li><a href="/1/461.html" title="斗破苍穹 第四百三十二章  震慑与客气【第二更！】" target="_blank">第四百三十二章  震慑与客气【第二更！】</a></li>
                                <li><a href="/1/462.html" title="斗破苍穹 第四百三十三章  磐门！【抱歉，这是昨天第三更，我囧！】" target="_blank">第四百三十三章  磐门！【抱歉，这是昨天第三更，我囧！】</a></li>
                                <li><a href="/1/463.html" title="斗破苍穹 第四百三十四章 神秘黑塔？" target="_blank">第四百三十四章 神秘黑塔？</a></li>
                                <li><a href="/1/464.html" title="斗破苍穹 第四百三十五章  修炼加速器" target="_blank">第四百三十五章  修炼加速器</a></li>
                                <li><a href="/1/465.html" title="斗破苍穹 第四百三十六章  震动" target="_blank">第四百三十六章  震动</a></li>
                                <li><a href="/1/466.html" title="斗破苍穹 第四百三十七章 　初见" target="_blank">第四百三十七章 　初见</a></li>
                                <li><a href="/1/467.html" title="斗破苍穹 第四百三十八章   黑洞" target="_blank">第四百三十八章   黑洞</a></li>
                                <li><a href="/1/468.html" title="斗破苍穹 第四百三十九章  神秘的无形火蟒" target="_blank">第四百三十九章  神秘的无形火蟒</a></li>
                                <li><a href="/1/469.html" title="斗破苍穹 第四百四十章  麻烦事" target="_blank">第四百四十章  麻烦事</a></li>
                                <li><a href="/1/470.html" title="斗破苍穹 第四百四十一章 赌注" target="_blank">第四百四十一章 赌注</a></li>
                                <li><a href="/1/471.html" title="斗破苍穹 第四百四十二章 战付敖" target="_blank">第四百四十二章 战付敖</a></li>
                                <li><a href="/1/472.html" title="斗破苍穹 第四百四十三章 白帮的实力" target="_blank">第四百四十三章 白帮的实力</a></li>
                                <li><a href="/1/473.html" title="斗破苍穹 第四百四十四章  相遇" target="_blank">第四百四十四章  相遇</a></li>
                                <li><a href="/1/474.html" title="斗破苍穹 第四百四十五章 暗中交锋" target="_blank">第四百四十五章 暗中交锋</a></li>
                                <li><a href="/1/475.html" title="斗破苍穹 第四百四十六章  中级修炼室" target="_blank">第四百四十六章  中级修炼室</a></li>
                                <li><a href="/1/476.html" title="斗破苍穹 第四百四十七章  淬炼" target="_blank">第四百四十七章  淬炼</a></li>
                                <li><a href="/1/477.html" title="斗破苍穹 第四百四十八章  第二层" target="_blank">第四百四十八章  第二层</a></li>
                                <li><a href="/1/478.html" title="斗破苍穹 第四百四十九章 探查与会谈" target="_blank">第四百四十九章 探查与会谈</a></li>
                                <li><a href="/1/479.html" title="斗破苍穹 第四百五十章 七星大斗师" target="_blank">第四百五十章 七星大斗师</a></li>
                                <li><a href="/1/480.html" title="斗破苍穹 第四百五十一章  磐门的变化【补上的第三更，抱歉】" target="_blank">第四百五十一章  磐门的变化【补上的第三更，抱歉】</a></li>
                                <li><a href="/1/481.html" title="斗破苍穹 第四百五十二章  陀舍古帝玉？" target="_blank">第四百五十二章  陀舍古帝玉？</a></li>
                                <li><a href="/1/482.html" title="斗破苍穹 第四百五十三章  陀舍古帝" target="_blank">第四百五十三章  陀舍古帝</a></li>
                                <li><a href="/1/483.html" title="斗破苍穹 第四百五十四章 　青木仙藤" target="_blank">第四百五十四章 　青木仙藤</a></li>
                                <li><a href="/1/484.html" title="斗破苍穹 第四百五十五章  古怪的家伙" target="_blank">第四百五十五章  古怪的家伙</a></li>
                                <li><a href="/1/485.html" title="斗破苍穹 第四百五十六章 交易" target="_blank">第四百五十六章 交易</a></li>
                                <li><a href="/1/486.html" title="斗破苍穹 第四百五十七章  青芝火灵膏，速灵风丹" target="_blank">第四百五十七章  青芝火灵膏，速灵风丹</a></li>
                                <li><a href="/1/487.html" title="斗破苍穹 第四百五十八章  闭关【第三更！】" target="_blank">第四百五十八章  闭关【第三更！】</a></li>
                                <li><a href="/1/488.html" title="斗破苍穹 第四百五十九章  找上门的麻烦【第一更！】" target="_blank">第四百五十九章  找上门的麻烦【第一更！】</a></li>
                                <li><a href="/1/489.html" title="斗破苍穹 第四百五十九章 找上门的麻烦" target="_blank">第四百五十九章 找上门的麻烦</a></li>
                                <li><a href="/1/490.html" title="斗破苍穹 第四百六十章  柳菲【第二更！】" target="_blank">第四百六十章  柳菲【第二更！】</a></li>
                                <li><a href="/1/491.html" title="斗破苍穹 第四百六十一章  赫长老【第三更！】" target="_blank">第四百六十一章  赫长老【第三更！】</a></li>
                                <li><a href="/1/492.html" title="斗破苍穹 第四百六十二章  修炼进展【第一更！】" target="_blank">第四百六十二章  修炼进展【第一更！】</a></li>
                                <li><a href="/1/493.html" title="斗破苍穹 第四百六十三章  再次突破！【第二更！】" target="_blank">第四百六十三章  再次突破！【第二更！】</a></li>
                                <li><a href="/1/494.html" title="斗破苍穹 第四百六十四章  霸枪柳擎" target="_blank">第四百六十四章  霸枪柳擎</a></li>
                                <li><a href="/1/495.html" title="斗破苍穹 第四百六十五章 赚取火能【第一更！】" target="_blank">第四百六十五章 赚取火能【第一更！】</a></li>
                                <li><a href="/1/496.html" title="斗破苍穹 第四百六十六章  大批炼制【第二更！】" target="_blank">第四百六十六章  大批炼制【第二更！】</a></li>
                                <li><a href="/1/497.html" title="斗破苍穹 第四百六十七章  丰硕的收获！【第三更！】" target="_blank">第四百六十七章  丰硕的收获！【第三更！】</a></li>
                                <li><a href="/1/498.html" title="斗破苍穹 第四百六十八章  冲突【第一更！】" target="_blank">第四百六十八章  冲突【第一更！】</a></li>
                                <li><a href="/1/499.html" title="斗破苍穹 第四百六十九章 药帮韩闲【第二更！】" target="_blank">第四百六十九章 药帮韩闲【第二更！】</a></li>
                                <li><a href="/1/500.html" title="斗破苍穹 四百七十章  比试【第三更！】" target="_blank">四百七十章  比试【第三更！】</a></li>
                                <li><a href="/1/501.html" title="斗破苍穹 第四百七十一章  比试题目:龙力丹【第一更！】" target="_blank">第四百七十一章  比试题目:龙力丹【第一更！】</a></li>
                                <li><a href="/1/502.html" title="斗破苍穹 第四百七十二章  幻金火【第二更！】" target="_blank">第四百七十二章  幻金火【第二更！】</a></li>
                                <li><a href="/1/503.html" title="斗破苍穹 第四百七十三章   半成品【第三更！】" target="_blank">第四百七十三章   半成品【第三更！】</a></li>
                                <li><a href="/1/504.html" title="斗破苍穹 第四百七十四章  幸不辱命" target="_blank">第四百七十四章  幸不辱命</a></li>
                                <li><a href="/1/505.html" title="斗破苍穹 第四百七十五章  胜利" target="_blank">第四百七十五章  胜利</a></li>
                                <li><a href="/1/506.html" title="斗破苍穹 第四百七十六章   招纳" target="_blank">第四百七十六章   招纳</a></li>
                                <li><a href="/1/507.html" title="斗破苍穹 第四百七十七章  修炼，三千雷动" target="_blank">第四百七十七章  修炼，三千雷动</a></li>
                                <li><a href="/1/508.html" title="斗破苍穹 第四百七十八章   风雷之力" target="_blank">第四百七十八章   风雷之力</a></li>
                                <li><a href="/1/509.html" title="斗破苍穹 第四百七十九章  炼化成功" target="_blank">第四百七十九章  炼化成功</a></li>
                                <li><a href="/1/510.html" title="斗破苍穹 第四百八十章  雷闪" target="_blank">第四百八十章  雷闪</a></li>
                                <li><a href="/1/511.html" title="斗破苍穹 第四百八十一章 　领悟，尺法【祝福大家虎年吉祥！】" target="_blank">第四百八十一章 　领悟，尺法【祝福大家虎年吉祥！】</a></li>
                                <li><a href="/1/512.html" title="斗破苍穹 第四百八十二章  地心淬体乳" target="_blank">第四百八十二章  地心淬体乳</a></li>
                                <li><a href="/1/513.html" title="斗破苍穹 第四百八十三章   强榜高手" target="_blank">第四百八十三章   强榜高手</a></li>
                                <li><a href="/1/514.html" title="斗破苍穹 第四百八十四章  狂暴血脉" target="_blank">第四百八十四章  狂暴血脉</a></li>
                                <li><a href="/1/515.html" title="斗破苍穹 第四百八十五章 邀请" target="_blank">第四百八十五章 邀请</a></li>
                                <li><a href="/1/516.html" title="斗破苍穹 第四百八十六章  蟒猿相斗" target="_blank">第四百八十六章  蟒猿相斗</a></li>
                                <li><a href="/1/517.html" title="斗破苍穹 第四百八十七章 寻宝" target="_blank">第四百八十七章 寻宝</a></li>
                                <li><a href="/1/518.html" title="斗破苍穹 第四百八十八章  真假地心乳" target="_blank">第四百八十八章  真假地心乳</a></li>
                                <li><a href="/1/519.html" title="斗破苍穹 第四百八十九章  美杜莎女王再现" target="_blank">第四百八十九章  美杜莎女王再现</a></li>
                                <li><a href="/1/520.html" title="斗破苍穹 第四百九十章  约定" target="_blank">第四百九十章  约定</a></li>
                                <li><a href="/1/521.html" title="斗破苍穹 第四百九十一章   调配药液" target="_blank">第四百九十一章   调配药液</a></li>
                                <li><a href="/1/522.html" title="斗破苍穹 第四百九十二章  九星大斗师" target="_blank">第四百九十二章  九星大斗师</a></li>
                                <li><a href="/1/523.html" title="斗破苍穹 第四百九十三章  晋阶斗灵【第三更】" target="_blank">第四百九十三章  晋阶斗灵【第三更】</a></li>
                                <li><a href="/1/524.html" title="斗破苍穹 第四百九十四章  回院" target="_blank">第四百九十四章  回院</a></li>
                                <li><a href="/1/525.html" title="斗破苍穹 第四百九十五章  出场" target="_blank">第四百九十五章  出场</a></li>
                                <li><a href="/1/526.html" title="斗破苍穹 第四百九十六章 　激战" target="_blank">第四百九十六章 　激战</a></li>
                                <li><a href="/1/527.html" title="斗破苍穹 更新换月票，斗破读者进来瞧瞧，拼了。" target="_blank">更新换月票，斗破读者进来瞧瞧，拼了。</a></li>
                                <li><a href="/1/528.html" title="斗破苍穹 第四百九十七章  对战六星斗灵" target="_blank">第四百九十七章  对战六星斗灵</a></li>
                                <li><a href="/1/529.html" title="斗破苍穹 第四百九十八章 　拼药【第二更！】" target="_blank">第四百九十八章 　拼药【第二更！】</a></li>
                                <li><a href="/1/530.html" title="斗破苍穹 第四百九十九章  强力一击 【第三更！】" target="_blank">第四百九十九章  强力一击 【第三更！】</a></li>
                                <li><a href="/1/531.html" title="斗破苍穹 第五百章  败敌【第四更！】" target="_blank">第五百章  败敌【第四更！】</a></li>
                                <li><a href="/1/532.html" title="斗破苍穹 第五百零一章  一耳光【第五更！】" target="_blank">第五百零一章  一耳光【第五更！】</a></li>
                                <li><a href="/1/533.html" title="斗破苍穹 第五百零二章  强榜排名【第一更！】" target="_blank">第五百零二章  强榜排名【第一更！】</a></li>
                                <li><a href="/1/534.html" title="斗破苍穹 第五百零三章 神秘的强榜第一【第二更！】" target="_blank">第五百零三章 神秘的强榜第一【第二更！】</a></li>
                                <li><a href="/1/535.html" title="斗破苍穹 第五百零四章 冰火龙须果" target="_blank">第五百零四章 冰火龙须果</a></li>
                                <li><a href="/1/536.html" title="斗破苍穹 第五百零五章  神秘白衣小女孩【第二更！】" target="_blank">第五百零五章  神秘白衣小女孩【第二更！】</a></li>
                                <li><a href="/1/537.html" title="斗破苍穹 第五百零六章  不是人【第三更！】" target="_blank">第五百零六章  不是人【第三更！】</a></li>
                                <li><a href="/1/538.html" title="斗破苍穹 第五百零七章   最后一种材料【第四更！】" target="_blank">第五百零七章   最后一种材料【第四更！】</a></li>
                                <li><a href="/1/539.html" title="斗破苍穹 四章已更，最后二十三小时求月票！" target="_blank">四章已更，最后二十三小时求月票！</a></li>
                                <li><a href="/1/540.html" title="斗破苍穹 第五百零八章  交换【第一更！】" target="_blank">第五百零八章  交换【第一更！】</a></li>
                                <li><a href="/1/541.html" title="斗破苍穹 第五百零九章  到手【第二更！】" target="_blank">第五百零九章  到手【第二更！】</a></li>
                                <li><a href="/1/542.html" title="斗破苍穹 第五百一十章   炼制地灵丹【第三更！】" target="_blank">第五百一十章   炼制地灵丹【第三更！】</a></li>
                                <li><a href="/1/543.html" title="斗破苍穹 三章已更，月初拜求诸位弟兄手中保底月票！" target="_blank">三章已更，月初拜求诸位弟兄手中保底月票！</a></li>
                                <li><a href="/1/544.html" title="斗破苍穹 第五百一十一章   动静【第一更！】" target="_blank">第五百一十一章   动静【第一更！】</a></li>
                                <li><a href="/1/545.html" title="斗破苍穹 第五百一十二章   药皇，韩枫！【第二更！】" target="_blank">第五百一十二章   药皇，韩枫！【第二更！】</a></li>
                                <li><a href="/1/546.html" title="斗破苍穹 第五百一十三章  丹成【第三更！求保底月票！】" target="_blank">第五百一十三章  丹成【第三更！求保底月票！】</a></li>
                                <li><a href="/1/547.html" title="斗破苍穹 第五百一十四章  探宝的天赋【第一更！】" target="_blank">第五百一十四章  探宝的天赋【第一更！】</a></li>
                                <li><a href="/1/548.html" title="斗破苍穹 第五百一十五章  急事？【第二更！】" target="_blank">第五百一十五章  急事？【第二更！】</a></li>
                                <li><a href="/1/549.html" title="斗破苍穹 第五百一十六章  回外院【第三更！】" target="_blank">第五百一十六章  回外院【第三更！】</a></li>
                                <li><a href="/1/550.html" title="斗破苍穹 第五百一十七章 族中变故" target="_blank">第五百一十七章 族中变故</a></li>
                                <li><a href="/1/551.html" title="斗破苍穹 第五百一十八章  魂殿参与" target="_blank">第五百一十八章  魂殿参与</a></li>
                                <li><a href="/1/552.html" title="斗破苍穹 第五百一十九章  萧厉的打算" target="_blank">第五百一十九章  萧厉的打算</a></li>
                                <li><a href="/1/553.html" title="斗破苍穹 第五百二十章   摆擂接战【今日恢复更新，抱歉！】" target="_blank">第五百二十章   摆擂接战【今日恢复更新，抱歉！】</a></li>
                                <li><a href="/1/554.html" title="斗破苍穹 第五百二十一章 姚盛" target="_blank">第五百二十一章 姚盛</a></li>
                                <li><a href="/1/555.html" title="斗破苍穹 第五百二十二章  初步交锋" target="_blank">第五百二十二章  初步交锋</a></li>
                                <li><a href="/1/556.html" title="斗破苍穹 第五百二十三章  一号修炼室" target="_blank">第五百二十三章  一号修炼室</a></li>
                                <li><a href="/1/557.html" title="斗破苍穹 第五百二十四章  塔中暴动" target="_blank">第五百二十四章  塔中暴动</a></li>
                                <li><a href="/1/558.html" title="斗破苍穹 第五百二十五章  陨落心炎提前的暴动" target="_blank">第五百二十五章  陨落心炎提前的暴动</a></li>
                                <li><a href="/1/559.html" title="斗破苍穹 第五百二十六章  大长老苏千" target="_blank">第五百二十六章  大长老苏千</a></li>
                                <li><a href="/1/560.html" title="斗破苍穹 第五百二十七章  冤家路窄" target="_blank">第五百二十七章  冤家路窄</a></li>
                                <li><a href="/1/561.html" title="斗破苍穹 第五百二十八章  针锋相对" target="_blank">第五百二十八章  针锋相对</a></li>
                                <li><a href="/1/562.html" title="斗破苍穹 第五百二十九章  定对手" target="_blank">第五百二十九章  定对手</a></li>
                                <li><a href="/1/563.html" title="斗破苍穹 第五百三十章  大赛开始" target="_blank">第五百三十章  大赛开始</a></li>
                                <li><a href="/1/564.html" title="斗破苍穹 第五百三十一章  贝崌" target="_blank">第五百三十一章  贝崌</a></li>
                                <li><a href="/1/565.html" title="斗破苍穹 第五百三十二章   尺法" target="_blank">第五百三十二章   尺法</a></li>
                                <li><a href="/1/566.html" title="斗破苍穹 第五百三十三章  血地八裂" target="_blank">第五百三十三章  血地八裂</a></li>
                                <li><a href="/1/567.html" title="斗破苍穹 第五百三十四章  青火盔甲" target="_blank">第五百三十四章  青火盔甲</a></li>
                                <li><a href="/1/568.html" title="斗破苍穹 第五百三十五章  柳擎的出场" target="_blank">第五百三十五章  柳擎的出场</a></li>
                                <li><a href="/1/569.html" title="斗破苍穹 第五百三十六章   大裂劈棺爪" target="_blank">第五百三十六章   大裂劈棺爪</a></li>
                                <li><a href="/1/570.html" title="斗破苍穹 第五百三十七章   第二轮" target="_blank">第五百三十七章   第二轮</a></li>
                                <li><a href="/1/571.html" title="斗破苍穹 第五百三十八章 　对战姚盛" target="_blank">第五百三十八章 　对战姚盛</a></li>
                                <li><a href="/1/572.html" title="斗破苍穹 第五百三十九章  破解“黑水界”" target="_blank">第五百三十九章  破解“黑水界”</a></li>
                                <li><a href="/1/573.html" title="斗破苍穹 第五百四十章  胜！" target="_blank">第五百四十章  胜！</a></li>
                                <li><a href="/1/574.html" title="斗破苍穹 第五百四十一章  耀眼" target="_blank">第五百四十一章  耀眼</a></li>
                                <li><a href="/1/575.html" title="斗破苍穹 第五百四十二章  一缠一罡" target="_blank">第五百四十二章  一缠一罡</a></li>
                                <li><a href="/1/576.html" title="斗破苍穹 第五百四十三章  卷轴【第一更！】" target="_blank">第五百四十三章  卷轴【第一更！】</a></li>
                                <li><a href="/1/577.html" title="斗破苍穹 第五百四十四章   争夺前十【第二更！】" target="_blank">第五百四十四章   争夺前十【第二更！】</a></li>
                                <li><a href="/1/578.html" title="斗破苍穹 第五百四十五章  新人黑马与老牌强者的交锋！【第三更！】" target="_blank">第五百四十五章  新人黑马与老牌强者的交锋！【第三更！】</a></li>
                                <li><a href="/1/579.html" title="斗破苍穹 第五百四十六章   沸腾【第四更！】" target="_blank">第五百四十六章   沸腾【第四更！】</a></li>
                                <li><a href="/1/580.html" title="斗破苍穹 第五百四十七章   八极崩与大裂劈棺爪的碰撞！" target="_blank">第五百四十七章   八极崩与大裂劈棺爪的碰撞！</a></li>
                                <li><a href="/1/581.html" title="斗破苍穹 第五百四十八章   爆！" target="_blank">第五百四十八章   爆！</a></li>
                                <li><a href="/1/582.html" title="斗破苍穹 第五百四十九章 一招" target="_blank">第五百四十九章 一招</a></li>
                                <li><a href="/1/583.html" title="斗破苍穹 第五百五十章  大裂岩与焰分噬浪尺的对碰！" target="_blank">第五百五十章  大裂岩与焰分噬浪尺的对碰！</a></li>
                                <li><a href="/1/584.html" title="斗破苍穹 第五百五十一章  还有口气" target="_blank">第五百五十一章  还有口气</a></li>
                                <li><a href="/1/585.html" title="斗破苍穹 第五百五十二章  落幕" target="_blank">第五百五十二章  落幕</a></li>
                                <li><a href="/1/586.html" title="斗破苍穹 第五百五十三章 养伤" target="_blank">第五百五十三章 养伤</a></li>
                                <li><a href="/1/587.html" title="斗破苍穹 第五百五十四章  实力晋升 【第一更！求月票！】" target="_blank">第五百五十四章  实力晋升 【第一更！求月票！】</a></li>
                                <li><a href="/1/588.html" title="斗破苍穹 第五百五十五章   黑湮军副统领，翎泉【第二更！】" target="_blank">第五百五十五章   黑湮军副统领，翎泉【第二更！】</a></li>
                                <li><a href="/1/589.html" title="斗破苍穹 第五百五十六章  分离【第三更！】" target="_blank">第五百五十六章  分离【第三更！】</a></li>
                                <li><a href="/1/590.html" title="斗破苍穹 第五百五十七章  进入天焚炼气塔底层" target="_blank">第五百五十七章  进入天焚炼气塔底层</a></li>
                                <li><a href="/1/591.html" title="斗破苍穹 第五百五十八章  本源心炎" target="_blank">第五百五十八章  本源心炎</a></li>
                                <li><a href="/1/592.html" title="斗破苍穹 第五百五十九章  锻体之痛" target="_blank">第五百五十九章  锻体之痛</a></li>
                                <li><a href="/1/593.html" title="斗破苍穹 第五百六十章  陨落心炎，爆发！" target="_blank">第五百六十章  陨落心炎，爆发！</a></li>
                                <li><a href="/1/594.html" title="斗破苍穹 第五百六十一章   冲破封印！【第一更！】" target="_blank">第五百六十一章   冲破封印！【第一更！】</a></li>
                                <li><a href="/1/595.html" title="斗破苍穹 第五百六十二章  破塔！【第二更！】" target="_blank">第五百六十二章  破塔！【第二更！】</a></li>
                                <li><a href="/1/596.html" title="斗破苍穹 第五百六十三章  千层封阵！【第三更！】" target="_blank">第五百六十三章  千层封阵！【第三更！】</a></li>
                                <li><a href="/1/597.html" title="斗破苍穹 第五百六十四章  呼朋唤友【第四更！】" target="_blank">第五百六十四章  呼朋唤友【第四更！】</a></li>
                                <li><a href="/1/598.html" title="斗破苍穹 第五百六十五章   联手封印！" target="_blank">第五百六十五章   联手封印！</a></li>
                                <li><a href="/1/599.html" title="斗破苍穹 第五百五十六章  残卷焚决【第二更！】" target="_blank">第五百五十六章  残卷焚决【第二更！】</a></li>
                                <li><a href="/1/600.html" title="斗破苍穹 第五百六十七章  混乱大战  【第三更！】" target="_blank">第五百六十七章  混乱大战  【第三更！】</a></li>
                                <li><a href="/1/601.html" title="斗破苍穹 第五百六十八章  对战范痨【昨天的第四更，抱歉！】" target="_blank">第五百六十八章  对战范痨【昨天的第四更，抱歉！】</a></li>
                                <li><a href="/1/602.html" title="斗破苍穹 第五百六十九章  援手" target="_blank">第五百六十九章  援手</a></li>
                                <li><a href="/1/603.html" title="斗破苍穹 第五百七十章  青火漫天！" target="_blank">第五百七十章  青火漫天！</a></li>
                                <li><a href="/1/604.html" title="斗破苍穹 第五百七十一章  海心焰【周初求推荐票！】" target="_blank">第五百七十一章  海心焰【周初求推荐票！】</a></li>
                                <li><a href="/1/605.html" title="斗破苍穹 第五百七十二章  惊天大爆炸" target="_blank">第五百七十二章  惊天大爆炸</a></li>
                                <li><a href="/1/606.html" title="斗破苍穹 第五百七十三章  同样的心思" target="_blank">第五百七十三章  同样的心思</a></li>
                                <li><a href="/1/607.html" title="斗破苍穹 第五百七十四章   赶尽杀绝" target="_blank">第五百七十四章   赶尽杀绝</a></li>
                                <li><a href="/1/608.html" title="斗破苍穹 第五百七十五章  封印无效" target="_blank">第五百七十五章  封印无效</a></li>
                                <li><a href="/1/609.html" title="斗破苍穹 第五百七十六章   陨落心炎：修炼作弊器！" target="_blank">第五百七十六章   陨落心炎：修炼作弊器！</a></li>
                                <li><a href="/1/610.html" title="斗破苍穹 第五百七十七章  斗火！" target="_blank">第五百七十七章  斗火！</a></li>
                                <li><a href="/1/611.html" title="斗破苍穹 第五百七十八章  现形" target="_blank">第五百七十八章  现形</a></li>
                                <li><a href="/1/612.html" title="斗破苍穹 第五百七十九章  本体" target="_blank">第五百七十九章  本体</a></li>
                                <li><a href="/1/613.html" title="斗破苍穹 第五百八十章  交锋" target="_blank">第五百八十章  交锋</a></li>
                                <li><a href="/1/614.html" title="斗破苍穹 第五百八十一章  恐惧" target="_blank">第五百八十一章  恐惧</a></li>
                                <li><a href="/1/615.html" title="斗破苍穹 第五百八十二章  大型佛怒火莲" target="_blank">第五百八十二章  大型佛怒火莲</a></li>
                                <li><a href="/1/616.html" title="斗破苍穹 第五百八十三章  吞噬，封印！" target="_blank">第五百八十三章  吞噬，封印！</a></li>
                                <li><a href="/1/617.html" title="斗破苍穹 第五百八十四章  绝境" target="_blank">第五百八十四章  绝境</a></li>
                                <li><a href="/1/618.html" title="斗破苍穹 第五百八十五章 蛇现" target="_blank">第五百八十五章 蛇现</a></li>
                                <li><a href="/1/619.html" title="斗破苍穹 第五百八十六章   生死之段" target="_blank">第五百八十六章   生死之段</a></li>
                                <li><a href="/1/620.html" title="斗破苍穹 第五百八十七章  缓慢的蜕变" target="_blank">第五百八十七章  缓慢的蜕变</a></li>
                                <li><a href="/1/621.html" title="斗破苍穹 第五百八十八章  晋阶斗王！" target="_blank">第五百八十八章  晋阶斗王！</a></li>
                                <li><a href="/1/622.html" title="斗破苍穹 第五百八十九章  局面反转，抓捕陨落心炎！【第一更！】" target="_blank">第五百八十九章  局面反转，抓捕陨落心炎！【第一更！】</a></li>
                                <li><a href="/1/623.html" title="斗破苍穹 第五百九十章  侵蚀，炼化，融合！【第二更！】" target="_blank">第五百九十章  侵蚀，炼化，融合！【第二更！】</a></li>
                                <li><a href="/1/624.html" title="斗破苍穹 第五百九十一章  融合成功！【第三更！】" target="_blank">第五百九十一章  融合成功！【第三更！】</a></li>
                                <li><a href="/1/625.html" title="斗破苍穹 第五百九十二章   异火相融后遗症【第四更！】" target="_blank">第五百九十二章   异火相融后遗症【第四更！】</a></li>
                                <li><a href="/1/626.html" title="斗破苍穹 第五百九十三章  破封！【第五更！】" target="_blank">第五百九十三章  破封！【第五更！】</a></li>
                                <li><a href="/1/627.html" title="斗破苍穹 第五百九十四章  破塔而出！【第六更！】" target="_blank">第五百九十四章  破塔而出！【第六更！】</a></li>
                                <li><a href="/1/628.html" title="斗破苍穹 第五百九十五章  试手" target="_blank">第五百九十五章  试手</a></li>
                                <li><a href="/1/629.html" title="斗破苍穹 第五百九十六章  灾星" target="_blank">第五百九十六章  灾星</a></li>
                                <li><a href="/1/630.html" title="斗破苍穹 第五百九十七章  解决麻烦" target="_blank">第五百九十七章  解决麻烦</a></li>
                                <li><a href="/1/631.html" title="斗破苍穹 第五百九十八章  召集人手" target="_blank">第五百九十八章  召集人手</a></li>
                                <li><a href="/1/632.html" title="斗破苍穹 第五百九十九章 　生死之刻" target="_blank">第五百九十九章 　生死之刻</a></li>
                                <li><a href="/1/633.html" title="斗破苍穹 第六百章  喝退" target="_blank">第六百章  喝退</a></li>
                                <li><a href="/1/634.html" title="斗破苍穹 第六百零一章  援兵【第一更！】" target="_blank">第六百零一章  援兵【第一更！】</a></li>
                                <li><a href="/1/635.html" title="斗破苍穹 第六百零二章  击杀范痨 【第二更！】" target="_blank">第六百零二章  击杀范痨 【第二更！】</a></li>
                                <li><a href="/1/636.html" title="斗破苍穹 第六百零三章  大开杀戒【第三更！】" target="_blank">第六百零三章  大开杀戒【第三更！】</a></li>
                                <li><a href="/1/637.html" title="斗破苍穹 第六百零四章 噬生丹" target="_blank">第六百零四章 噬生丹</a></li>
                                <li><a href="/1/638.html" title="斗破苍穹 第六百零五章  药方" target="_blank">第六百零五章  药方</a></li>
                                <li><a href="/1/639.html" title="斗破苍穹 第六百零六章 大战来临" target="_blank">第六百零六章 大战来临</a></li>
                                <li><a href="/1/640.html" title="斗破苍穹 第六百零七章  强强对碰" target="_blank">第六百零七章  强强对碰</a></li>
                                <li><a href="/1/641.html" title="斗破苍穹 第六百零八章  交锋【第一更！】" target="_blank">第六百零八章  交锋【第一更！】</a></li>
                                <li><a href="/1/642.html" title="斗破苍穹 第六百零九章  火莲瓶【第二更！】" target="_blank">第六百零九章  火莲瓶【第二更！】</a></li>
                                <li><a href="/1/643.html" title="斗破苍穹 第六百一十章  同门之战 【第三更！】" target="_blank">第六百一十章  同门之战 【第三更！】</a></li>
                                <li><a href="/1/644.html" title="斗破苍穹 第六百一十一章   半只脚踏入斗宗的韩枫【第四更到！】" target="_blank">第六百一十一章   半只脚踏入斗宗的韩枫【第四更到！】</a></li>
                                <li><a href="/1/645.html" title="斗破苍穹 第六百一十二章  翡翠火莲" target="_blank">第六百一十二章  翡翠火莲</a></li>
                                <li><a href="/1/646.html" title="斗破苍穹 第六百一十三章  你的命，是我的！" target="_blank">第六百一十三章  你的命，是我的！</a></li>
                                <li><a href="/1/647.html" title="斗破苍穹 第六百一十四章  魂殿再现" target="_blank">第六百一十四章  魂殿再现</a></li>
                                <li><a href="/1/648.html" title="斗破苍穹 第六百一十五章  幽海纳戒" target="_blank">第六百一十五章  幽海纳戒</a></li>
                                <li><a href="/1/649.html" title="斗破苍穹 第六百一十六章  闭关疗伤" target="_blank">第六百一十六章  闭关疗伤</a></li>
                                <li><a href="/1/650.html" title="斗破苍穹 第六百一十七章 帝印决【第二更！】" target="_blank">第六百一十七章 帝印决【第二更！】</a></li>
                                <li><a href="/1/651.html" title="斗破苍穹 第六百一十八章  打算【第三更！】" target="_blank">第六百一十八章  打算【第三更！】</a></li>
                                <li><a href="/1/652.html" title="斗破苍穹 第六百一十九章  交易 【第四更！】" target="_blank">第六百一十九章  交易 【第四更！】</a></li>
                                <li><a href="/1/653.html" title="斗破苍穹 第六百二十章  修炼开山印！ 【第五更！】" target="_blank">第六百二十章  修炼开山印！ 【第五更！】</a></li>
                                <li><a href="/1/654.html" title="斗破苍穹 第六百二十一章  萧门" target="_blank">第六百二十一章  萧门</a></li>
                                <li><a href="/1/655.html" title="斗破苍穹 第六百二十二章   三大势力" target="_blank">第六百二十二章   三大势力</a></li>
                                <li><a href="/1/656.html" title="斗破苍穹 第六百二十三章  震慑" target="_blank">第六百二十三章  震慑</a></li>
                                <li><a href="/1/657.html" title="斗破苍穹 第六百二十四章  拉取帮手" target="_blank">第六百二十四章  拉取帮手</a></li>
                                <li><a href="/1/658.html" title="斗破苍穹 第六百二十五章  收罗药材 【第一更！】" target="_blank">第六百二十五章  收罗药材 【第一更！】</a></li>
                                <li><a href="/1/659.html" title="斗破苍穹 第六百二十六章  炼制复紫灵丹 【第二更！】" target="_blank">第六百二十六章  炼制复紫灵丹 【第二更！】</a></li>
                                <li><a href="/1/660.html" title="斗破苍穹 第六百二十七章  丹药拍卖会 【第三更！】" target="_blank">第六百二十七章  丹药拍卖会 【第三更！】</a></li>
                                <li><a href="/1/661.html" title="斗破苍穹 第六百二十八章 震慑" target="_blank">第六百二十八章 震慑</a></li>
                                <li><a href="/1/662.html" title="斗破苍穹 第六百二十九章  拍卖结束" target="_blank">第六百二十九章  拍卖结束</a></li>
                                <li><a href="/1/663.html" title="斗破苍穹 第六百三十章  修复药液" target="_blank">第六百三十章  修复药液</a></li>
                                <li><a href="/1/664.html" title="斗破苍穹 第六百三十一章  药老苏醒！" target="_blank">第六百三十一章  药老苏醒！</a></li>
                                <li><a href="/1/665.html" title="斗破苍穹 第六百三十二章  师徒相见" target="_blank">第六百三十二章  师徒相见</a></li>
                                <li><a href="/1/666.html" title="斗破苍穹 第六百三十三章  炼制躯体的材料" target="_blank">第六百三十三章  炼制躯体的材料</a></li>
                                <li><a href="/1/667.html" title="斗破苍穹 第六百三十四章  寻解之法" target="_blank">第六百三十四章  寻解之法</a></li>
                                <li><a href="/1/668.html" title="斗破苍穹 第六百三十五章  恢复" target="_blank">第六百三十五章  恢复</a></li>
                                <li><a href="/1/669.html" title="斗破苍穹 第六百三十六章  姚氏三兄弟" target="_blank">第六百三十六章  姚氏三兄弟</a></li>
                                <li><a href="/1/670.html" title="斗破苍穹 第六百三十七章  照看" target="_blank">第六百三十七章  照看</a></li>
                                <li><a href="/1/671.html" title="斗破苍穹 第六百三十八章  安置磐门" target="_blank">第六百三十八章  安置磐门</a></li>
                                <li><a href="/1/672.html" title="斗破苍穹 第六百三十九章  十招" target="_blank">第六百三十九章  十招</a></li>
                                <li><a href="/1/673.html" title="斗破苍穹 第六百四十章  安宁" target="_blank">第六百四十章  安宁</a></li>
                                <li><a href="/1/674.html" title="斗破苍穹 第六百四十一章  万事皆备" target="_blank">第六百四十一章  万事皆备</a></li>
                                <li><a href="/1/675.html" title="斗破苍穹 第六百四十二章  离开内院" target="_blank">第六百四十二章  离开内院</a></li>
                                <li><a href="/1/676.html" title="斗破苍穹 第六百四十三章 启程：回归加玛！" target="_blank">第六百四十三章 启程：回归加玛！</a></li>
                                <li><a href="/1/677.html" title="斗破苍穹 第六百四十四章  云岚宗的动静" target="_blank">第六百四十四章  云岚宗的动静</a></li>
                                <li><a href="/1/678.html" title="斗破苍穹 第六百四十五章  万里之遥" target="_blank">第六百四十五章  万里之遥</a></li>
                                <li><a href="/1/679.html" title="斗破苍穹 第六百四十六章  镇鬼关！故人！" target="_blank">第六百四十六章  镇鬼关！故人！</a></li>
                                <li><a href="/1/680.html" title="斗破苍穹 第六百四十七章  木铁 【第一更！】" target="_blank">第六百四十七章  木铁 【第一更！】</a></li>
                                <li><a href="/1/681.html" title="斗破苍穹 第六百四十八章  斩杀 【第二更！】" target="_blank">第六百四十八章  斩杀 【第二更！】</a></li>
                                <li><a href="/1/682.html" title="斗破苍穹 第六百四十九章  加玛情势 【第三更！】" target="_blank">第六百四十九章  加玛情势 【第三更！】</a></li>
                                <li><a href="/1/683.html" title="斗破苍穹 第六百五十章  宗内议事" target="_blank">第六百五十章  宗内议事</a></li>
                                <li><a href="/1/684.html" title="斗破苍穹 第六百五十一章  米特尔之难" target="_blank">第六百五十一章  米特尔之难</a></li>
                                <li><a href="/1/685.html" title="斗破苍穹 第六百五十二章  血洗" target="_blank">第六百五十二章  血洗</a></li>
                                <li><a href="/1/686.html" title="斗破苍穹 第六百五十三章  血战" target="_blank">第六百五十三章  血战</a></li>
                                <li><a href="/1/687.html" title="斗破苍穹 第六百五十四章  赶至帝都！" target="_blank">第六百五十四章  赶至帝都！</a></li>
                                <li><a href="/1/688.html" title="斗破苍穹 第六百五十五章  讨债！" target="_blank">第六百五十五章  讨债！</a></li>
                                <li><a href="/1/689.html" title="斗破苍穹 第六百五十六章 　其人之道还治其人之身" target="_blank">第六百五十六章 　其人之道还治其人之身</a></li>
                                <li><a href="/1/690.html" title="斗破苍穹 第六百五十七章  大开杀戒" target="_blank">第六百五十七章  大开杀戒</a></li>
                                <li><a href="/1/691.html" title="斗破苍穹 第六百五十八章   横扫" target="_blank">第六百五十八章   横扫</a></li>
                                <li><a href="/1/692.html" title="斗破苍穹 第六百五十九章  云岚宗的震惊" target="_blank">第六百五十九章  云岚宗的震惊</a></li>
                                <li><a href="/1/693.html" title="斗破苍穹 第六百六十章  局势" target="_blank">第六百六十章  局势</a></li>
                                <li><a href="/1/694.html" title="斗破苍穹 第六百六十一章  势 【第一更！】" target="_blank">第六百六十一章  势 【第一更！】</a></li>
                                <li><a href="/1/695.html" title="斗破苍穹 第六百六十二章   商讨 【第二更！】" target="_blank">第六百六十二章   商讨 【第二更！】</a></li>
                                <li><a href="/1/696.html" title="斗破苍穹 第六百六十三章  安顿萧家 【第三更！】" target="_blank">第六百六十三章  安顿萧家 【第三更！】</a></li>
                                <li><a href="/1/697.html" title="斗破苍穹 第六百六十四章   女人间的针锋相对" target="_blank">第六百六十四章   女人间的针锋相对</a></li>
                                <li><a href="/1/698.html" title="斗破苍穹 第六百六十五章  雪魅" target="_blank">第六百六十五章  雪魅</a></li>
                                <li><a href="/1/699.html" title="斗破苍穹 第六百六十六章  傅岩" target="_blank">第六百六十六章  傅岩</a></li>
                                <li><a href="/1/700.html" title="斗破苍穹 第六百六十七章   见面" target="_blank">第六百六十七章   见面</a></li>
                                <li><a href="/1/701.html" title="斗破苍穹 第六百六十八章   现身" target="_blank">第六百六十八章   现身</a></li>
                                <li><a href="/1/702.html" title="斗破苍穹 第六百六十九章   婚礼" target="_blank">第六百六十九章   婚礼</a></li>
                                <li><a href="/1/703.html" title="斗破苍穹 第六百七十章  混元塑骨丹" target="_blank">第六百七十章  混元塑骨丹</a></li>
                                <li><a href="/1/704.html" title="斗破苍穹 第六百七十一章   萧家新府邸" target="_blank">第六百七十一章   萧家新府邸</a></li>
                                <li><a href="/1/705.html" title="斗破苍穹 第六百七十二章  夜谈" target="_blank">第六百七十二章  夜谈</a></li>
                                <li><a href="/1/706.html" title="斗破苍穹 第六百七十三章  幽海蛟兽 【第二更！】" target="_blank">第六百七十三章  幽海蛟兽 【第二更！】</a></li>
                                <li><a href="/1/707.html" title="斗破苍穹 第六百七十四章  治疗 【第三更！】" target="_blank">第六百七十四章  治疗 【第三更！】</a></li>
                                <li><a href="/1/708.html" title="斗破苍穹 第六百七十五章  大战来临！ 【第四更！】" target="_blank">第六百七十五章  大战来临！ 【第四更！】</a></li>
                                <li><a href="/1/709.html" title="斗破苍穹 第六百七十六章  大婚之日 【第五更！】" target="_blank">第六百七十六章  大婚之日 【第五更！】</a></li>
                                <li><a href="/1/710.html" title="斗破苍穹 第六百七十七章  十招之战 【第六更！】" target="_blank">第六百七十七章  十招之战 【第六更！】</a></li>
                                <li><a href="/1/711.html" title="斗破苍穹 第六百七十八章  战古河" target="_blank">第六百七十八章  战古河</a></li>
                                <li><a href="/1/712.html" title="斗破苍穹 第六百七十九章  败！" target="_blank">第六百七十九章  败！</a></li>
                                <li><a href="/1/713.html" title="斗破苍穹 第六百八十章  杀无赦！" target="_blank">第六百八十章  杀无赦！</a></li>
                                <li><a href="/1/714.html" title="斗破苍穹 第六百八十一章   决战，云岚宗！" target="_blank">第六百八十一章   决战，云岚宗！</a></li>
                                <li><a href="/1/715.html" title="斗破苍穹 第六百八十二章  决战云山！" target="_blank">第六百八十二章  决战云山！</a></li>
                                <li><a href="/1/716.html" title="斗破苍穹 第六百八十三章  大悲撕风手！" target="_blank">第六百八十三章  大悲撕风手！</a></li>
                                <li><a href="/1/717.html" title="斗破苍穹 第六百八十四章  鹜护法 【第一更！】" target="_blank">第六百八十四章  鹜护法 【第一更！】</a></li>
                                <li><a href="/1/718.html" title="斗破苍穹 第六百八十五章  风刹湮罡 【第二更！】" target="_blank">第六百八十五章  风刹湮罡 【第二更！】</a></li>
                                <li><a href="/1/719.html" title="斗破苍穹 第六百八十六章  底牌，三色火莲！ 【第三更！】" target="_blank">第六百八十六章  底牌，三色火莲！ 【第三更！】</a></li>
                                <li><a href="/1/720.html" title="斗破苍穹 第六百八十七章  火莲爆发" target="_blank">第六百八十七章  火莲爆发</a></li>
                                <li><a href="/1/721.html" title="斗破苍穹 第六百八十八章   杀？" target="_blank">第六百八十八章   杀？</a></li>
                                <li><a href="/1/722.html" title="斗破苍穹 第六百八十九章  击杀云山！！" target="_blank">第六百八十九章  击杀云山！！</a></li>
                                <li><a href="/1/723.html" title="斗破苍穹 第六百九十章  变故" target="_blank">第六百九十章  变故</a></li>
                                <li><a href="/1/724.html" title="斗破苍穹 第六百九十一章   纳兰嫣然再现" target="_blank">第六百九十一章   纳兰嫣然再现</a></li>
                                <li><a href="/1/725.html" title="斗破苍穹 第六百九十二章  药老战鹜护法" target="_blank">第六百九十二章  药老战鹜护法</a></li>
                                <li><a href="/1/726.html" title="斗破苍穹 第六百九十三章  斗宗大战 【第一更！】" target="_blank">第六百九十三章  斗宗大战 【第一更！】</a></li>
                                <li><a href="/1/727.html" title="斗破苍穹 第六百九十四章   被捕 【第二更！】" target="_blank">第六百九十四章   被捕 【第二更！】</a></li>
                                <li><a href="/1/728.html" title="斗破苍穹 第六百九十五章  痛苦 【第三更！】" target="_blank">第六百九十五章  痛苦 【第三更！】</a></li>
                                <li><a href="/1/729.html" title="斗破苍穹 第六百九十六章  处理云岚宗" target="_blank">第六百九十六章  处理云岚宗</a></li>
                                <li><a href="/1/730.html" title="斗破苍穹 第六百九十七章  云岚宗结局" target="_blank">第六百九十七章  云岚宗结局</a></li>
                                <li><a href="/1/731.html" title="斗破苍穹 第六百九十八章   落幕" target="_blank">第六百九十八章   落幕</a></li>
                                <li><a href="/1/732.html" title="斗破苍穹 第六百九十九章   形势" target="_blank">第六百九十九章   形势</a></li>
                                <li><a href="/1/733.html" title="斗破苍穹 第七百章  宗门大会 【第一更！】" target="_blank">第七百章  宗门大会 【第一更！】</a></li>
                                <li><a href="/1/734.html" title="斗破苍穹 第七百零一章  毒宗 【第二更！】" target="_blank">第七百零一章  毒宗 【第二更！】</a></li>
                                <li><a href="/1/735.html" title="斗破苍穹 第七百零二章  药老所留 【第三更！】" target="_blank">第七百零二章  药老所留 【第三更！】</a></li>
                                <li><a href="/1/736.html" title="斗破苍穹 第七百零三章   势力雏形" target="_blank">第七百零三章   势力雏形</a></li>
                                <li><a href="/1/737.html" title="斗破苍穹 第七百零四章  离别" target="_blank">第七百零四章  离别</a></li>
                                <li><a href="/1/738.html" title="斗破苍穹 第七百零五章  痊愈" target="_blank">第七百零五章  痊愈</a></li>
                                <li><a href="/1/739.html" title="斗破苍穹 第七百零六章  联盟" target="_blank">第七百零六章  联盟</a></li>
                                <li><a href="/1/740.html" title="斗破苍穹 第七百零七章  炎盟 【第一更！】" target="_blank">第七百零七章  炎盟 【第一更！】</a></li>
                                <li><a href="/1/741.html" title="斗破苍穹 第七百零八章   事成 【第二更！】" target="_blank">第七百零八章   事成 【第二更！】</a></li>
                                <li><a href="/1/742.html" title="斗破苍穹 第七百零九章  炼制 【第三更！】" target="_blank">第七百零九章  炼制 【第三更！】</a></li>
                                <li><a href="/1/743.html" title="斗破苍穹 第七百一十章  闭关之念" target="_blank">第七百一十章  闭关之念</a></li>
                                <li><a href="/1/744.html" title="斗破苍穹 第七百一十一章  青山" target="_blank">第七百一十一章  青山</a></li>
                                <li><a href="/1/745.html" title="斗破苍穹 第七百一十二章   遇故" target="_blank">第七百一十二章   遇故</a></li>
                                <li><a href="/1/746.html" title="斗破苍穹 第七百一十三章  古怪的山谷 【第一更！】" target="_blank">第七百一十三章  古怪的山谷 【第一更！】</a></li>
                                <li><a href="/1/747.html" title="斗破苍穹 第七百一十四章  神秘黑影 【第二更！】" target="_blank">第七百一十四章  神秘黑影 【第二更！】</a></li>
                                <li><a href="/1/748.html" title="斗破苍穹 第七百一十五章  小医仙？ 【第三更！】" target="_blank">第七百一十五章  小医仙？ 【第三更！】</a></li>
                                <li><a href="/1/749.html" title="斗破苍穹 第七百一十六章  紫研晋阶" target="_blank">第七百一十六章  紫研晋阶</a></li>
                                <li><a href="/1/750.html" title="斗破苍穹 第七百一十七章  丹成" target="_blank">第七百一十七章  丹成</a></li>
                                <li><a href="/1/751.html" title="斗破苍穹 第七百一十八章  赫家" target="_blank">第七百一十八章  赫家</a></li>
                                <li><a href="/1/752.html" title="斗破苍穹 第七百一十九章   援手【第一更！】" target="_blank">第七百一十九章   援手【第一更！】</a></li>
                                <li><a href="/1/753.html" title="斗破苍穹 第七百二十章   赫乾 【第二更！】" target="_blank">第七百二十章   赫乾 【第二更！】</a></li>
                                <li><a href="/1/754.html" title="斗破苍穹 第七百二十一章  闭死关 【第三更！】" target="_blank">第七百二十一章  闭死关 【第三更！】</a></li>
                                <li><a href="/1/755.html" title="斗破苍穹 第七百二十二章  变动 【第四更！】" target="_blank">第七百二十二章  变动 【第四更！】</a></li>
                                <li><a href="/1/756.html" title="斗破苍穹 第七百二十三章   灵魂窥测" target="_blank">第七百二十三章   灵魂窥测</a></li>
                                <li><a href="/1/757.html" title="斗破苍穹 第七百二十四章  晋阶斗皇！" target="_blank">第七百二十四章  晋阶斗皇！</a></li>
                                <li><a href="/1/758.html" title="斗破苍穹 第七百二十五章   出谷" target="_blank">第七百二十五章   出谷</a></li>
                                <li><a href="/1/759.html" title="斗破苍穹 第七百二十六章   大乱" target="_blank">第七百二十六章   大乱</a></li>
                                <li><a href="/1/760.html" title="斗破苍穹 第七百二十七章  毒宗，金雁宗，慕兰谷" target="_blank">第七百二十七章  毒宗，金雁宗，慕兰谷</a></li>
                                <li><a href="/1/761.html" title="斗破苍穹 第七百二十八章   援救" target="_blank">第七百二十八章   援救</a></li>
                                <li><a href="/1/762.html" title="斗破苍穹 第七百二十九章   蛇人月媚" target="_blank">第七百二十九章   蛇人月媚</a></li>
                                <li><a href="/1/763.html" title="斗破苍穹 第七百三十章  情势 【第一更！】" target="_blank">第七百三十章  情势 【第一更！】</a></li>
                                <li><a href="/1/764.html" title="斗破苍穹 第七百三十一章  大战！ 【第二更！】" target="_blank">第七百三十一章  大战！ 【第二更！】</a></li>
                                <li><a href="/1/765.html" title="斗破苍穹 第七百三十二章  三兽蛮荒决 【第三更！】" target="_blank">第七百三十二章  三兽蛮荒决 【第三更！】</a></li>
                                <li><a href="/1/766.html" title="斗破苍穹 第七百三十三章   迎战慕兰三老 【第四更！求保底月票！" target="_blank">第七百三十三章   迎战慕兰三老 【第四更！求保底月票！</a></li>
                                <li><a href="/1/767.html" title="斗破苍穹 第七百三十四章  激战！【第一更！】" target="_blank">第七百三十四章  激战！【第一更！】</a></li>
                                <li><a href="/1/768.html" title="斗破苍穹 第七百三十五章  三千雷 【第二更！！】" target="_blank">第七百三十五章  三千雷 【第二更！！】</a></li>
                                <li><a href="/1/769.html" title="斗破苍穹 第七百三十六章  骗局 【第三更！】" target="_blank">第七百三十六章  骗局 【第三更！】</a></li>
                                <li><a href="/1/770.html" title="斗破苍穹 第七百三十七章  鹰啼 【第四更！】" target="_blank">第七百三十七章  鹰啼 【第四更！】</a></li>
                                <li><a href="/1/771.html" title="斗破苍穹 第七百三十八章  毒宗宗主！ 【第一更！】" target="_blank">第七百三十八章  毒宗宗主！ 【第一更！】</a></li>
                                <li><a href="/1/772.html" title="斗破苍穹 第七百三十九章  身法较技 【第二更！】" target="_blank">第七百三十九章  身法较技 【第二更！】</a></li>
                                <li><a href="/1/773.html" title="斗破苍穹 第七百四十四章  爆！ 【第三更！】" target="_blank">第七百四十四章  爆！ 【第三更！】</a></li>
                                <li><a href="/1/774.html" title="斗破苍穹 第七百四十五章  威望！ 【第四更！】" target="_blank">第七百四十五章  威望！ 【第四更！】</a></li>
                                <li><a href="/1/775.html" title="斗破苍穹 第七百四十六章  物是人非 【第一更！】" target="_blank">第七百四十六章  物是人非 【第一更！】</a></li>
                                <li><a href="/1/776.html" title="斗破苍穹 第七百四十七章  大战休止 【第二更！】" target="_blank">第七百四十七章  大战休止 【第二更！】</a></li>
                                <li><a href="/1/777.html" title="斗破苍穹 第七百四十八章  夜见 【第三更！】" target="_blank">第七百四十八章  夜见 【第三更！】</a></li>
                                <li><a href="/1/778.html" title="斗破苍穹 第七百四十九章  毒丹之法 【第一更！】" target="_blank">第七百四十九章  毒丹之法 【第一更！】</a></li>
                                <li><a href="/1/779.html" title="斗破苍穹 第七百五十章  蛇人族强者 【第二更！】" target="_blank">第七百五十章  蛇人族强者 【第二更！】</a></li>
                                <li><a href="/1/780.html" title="斗破苍穹 第七百五十一章  四大长老 【第三更！】" target="_blank">第七百五十一章  四大长老 【第三更！】</a></li>
                                <li><a href="/1/781.html" title="斗破苍穹 第七百五十二章   秘法三等 【第一更！】" target="_blank">第七百五十二章   秘法三等 【第一更！】</a></li>
                                <li><a href="/1/782.html" title="斗破苍穹 第七百五十三章  挑衅 【第二更！】" target="_blank">第七百五十三章  挑衅 【第二更！】</a></li>
                                <li><a href="/1/783.html" title="斗破苍穹 第七百五十四章  调养 【第三更！】" target="_blank">第七百五十四章  调养 【第三更！】</a></li>
                                <li><a href="/1/784.html" title="斗破苍穹 第七百五十五章  行动 【第一更！】" target="_blank">第七百五十五章  行动 【第一更！】</a></li>
                                <li><a href="/1/785.html" title="斗破苍穹 第七百五十六章   暗杀！ 【第二更！】" target="_blank">第七百五十六章   暗杀！ 【第二更！】</a></li>
                                <li><a href="/1/786.html" title="斗破苍穹 第七百五十七章   以寡敌众  【第三更！】" target="_blank">第七百五十七章   以寡敌众  【第三更！】</a></li>
                                <li><a href="/1/787.html" title="斗破苍穹 第七百五十八章 收获颇丰【第一更！】" target="_blank">第七百五十八章 收获颇丰【第一更！】</a></li>
                                <li><a href="/1/788.html" title="斗破苍穹 第七百五十九章  天雁九行翼 【第二更！】" target="_blank">第七百五十九章  天雁九行翼 【第二更！】</a></li>
                                <li><a href="/1/789.html" title="斗破苍穹 第七百六十章  云山之上，薰儿！ 【第三更！】" target="_blank">第七百六十章  云山之上，薰儿！ 【第三更！】</a></li>
                                <li><a href="/1/790.html" title="斗破苍穹 第七百六十一章  丹塔 【第一更！】" target="_blank">第七百六十一章  丹塔 【第一更！】</a></li>
                                <li><a href="/1/791.html" title="斗破苍穹 第七百六十二章   招揽古河 【第二更！】" target="_blank">第七百六十二章   招揽古河 【第二更！】</a></li>
                                <li><a href="/1/792.html" title="斗破苍穹 第七百六十三章  大统领 【第三更！】" target="_blank">第七百六十三章  大统领 【第三更！】</a></li>
                                <li><a href="/1/793.html" title="斗破苍穹 第七百六十四章  邀请帮手 【第一更！】" target="_blank">第七百六十四章  邀请帮手 【第一更！】</a></li>
                                <li><a href="/1/794.html" title="斗破苍穹 第七百六十五章 赶往出云！【第二更！】" target="_blank">第七百六十五章 赶往出云！【第二更！】</a></li>
                                <li><a href="/1/795.html" title="斗破苍穹 第七百六十六章   万蝎门 【第三更！】" target="_blank">第七百六十六章   万蝎门 【第三更！】</a></li>
                                <li><a href="/1/796.html" title="斗破苍穹 第七百六十七章  蜈崖 【第一更！】" target="_blank">第七百六十七章  蜈崖 【第一更！】</a></li>
                                <li><a href="/1/797.html" title="斗破苍穹 第七百六十八章  凶险 【第二更！】" target="_blank">第七百六十八章  凶险 【第二更！】</a></li>
                                <li><a href="/1/798.html" title="斗破苍穹 第七百六十九章   蝎毕岩 【第三更！】" target="_blank">第七百六十九章   蝎毕岩 【第三更！】</a></li>
                                <li><a href="/1/799.html" title="斗破苍穹 第七百七十章   门派大战 【第一更！】" target="_blank">第七百七十章   门派大战 【第一更！】</a></li>
                                <li><a href="/1/800.html" title="斗破苍穹 第七百七十一章  斩杀 【第二更！】" target="_blank">第七百七十一章  斩杀 【第二更！】</a></li>
                                <li><a href="/1/801.html" title="斗破苍穹 第七百七十二章  四翼天魔蝎 【第三更！】" target="_blank">第七百七十二章  四翼天魔蝎 【第三更！】</a></li>
                                <li><a href="/1/802.html" title="斗破苍穹 第七百七十三章 现身 【第一更！】" target="_blank">第七百七十三章 现身 【第一更！】</a></li>
                                <li><a href="/1/803.html" title="斗破苍穹 第七百七十四章   铁护法 【第二更！】" target="_blank">第七百七十四章   铁护法 【第二更！】</a></li>
                                <li><a href="/1/804.html" title="斗破苍穹 第七百七十五章  斗宗大爆发 【第三更！】" target="_blank">第七百七十五章  斗宗大爆发 【第三更！】</a></li>
                                <li><a href="/1/805.html" title="斗破苍穹 第七百七十六章   偷袭 【第一更！】" target="_blank">第七百七十六章   偷袭 【第一更！】</a></li>
                                <li><a href="/1/806.html" title="斗破苍穹 第七百七十七章    蝎山身亡 【第二更！】" target="_blank">第七百七十七章    蝎山身亡 【第二更！】</a></li>
                                <li><a href="/1/807.html" title="斗破苍穹 第七百七十八章   魂袋 【第三更！】" target="_blank">第七百七十八章   魂袋 【第三更！】</a></li>
                                <li><a href="/1/808.html" title="斗破苍穹 第七百七十九章  翻海印！【第一更！】" target="_blank">第七百七十九章  翻海印！【第一更！】</a></li>
                                <li><a href="/1/809.html" title="斗破苍穹 第七百八十章   狼狈的铁护法 【第二更！】" target="_blank">第七百八十章   狼狈的铁护法 【第二更！】</a></li>
                                <li><a href="/1/810.html" title="斗破苍穹 第七百八十一章   擒获！ 【第三更！】" target="_blank">第七百八十一章   擒获！ 【第三更！】</a></li>
                                <li><a href="/1/811.html" title="斗破苍穹 第七百八十二章   拼死一击 【第一更！】" target="_blank">第七百八十二章   拼死一击 【第一更！】</a></li>
                                <li><a href="/1/812.html" title="斗破苍穹 第七百八十三章  魔毒斑 【第二更！】" target="_blank">第七百八十三章  魔毒斑 【第二更！】</a></li>
                                <li><a href="/1/813.html" title="斗破苍穹 第七百八十四章  石池 【第三更！】" target="_blank">第七百八十四章  石池 【第三更！】</a></li>
                                <li><a href="/1/814.html" title="斗破苍穹 第七百八十五章   封印魔毒斑 【第一更！】" target="_blank">第七百八十五章   封印魔毒斑 【第一更！】</a></li>
                                <li><a href="/1/815.html" title="斗破苍穹 第七百八十六章  二星斗皇 【第二更！】" target="_blank">第七百八十六章  二星斗皇 【第二更！】</a></li>
                                <li><a href="/1/816.html" title="斗破苍穹 第七百八十七章    榜上第三！ 【第三更！】" target="_blank">第七百八十七章    榜上第三！ 【第三更！】</a></li>
                                <li><a href="/1/817.html" title="斗破苍穹 第七百八十八章  打算【第一更！】" target="_blank">第七百八十八章  打算【第一更！】</a></li>
                                <li><a href="/1/818.html" title="斗破苍穹 第七百八十九章  魂殿情报 【第二更！】" target="_blank">第七百八十九章  魂殿情报 【第二更！】</a></li>
                                <li><a href="/1/819.html" title="斗破苍穹 第七百九十章  赶往黑角域 【第三更！】" target="_blank">第七百九十章  赶往黑角域 【第三更！】</a></li>
                                <li><a href="/1/820.html" title="斗破苍穹 第七百九十一章   路遇 【第一更！】" target="_blank">第七百九十一章   路遇 【第一更！】</a></li>
                                <li><a href="/1/821.html" title="斗破苍穹 第七百九十二章   魔炎谷 【第二更！】" target="_blank">第七百九十二章   魔炎谷 【第二更！】</a></li>
                                <li><a href="/1/822.html" title="斗破苍穹 第七百九十三章   血剑吴昊 【第三更！】" target="_blank">第七百九十三章   血剑吴昊 【第三更！】</a></li>
                                <li><a href="/1/823.html" title="斗破苍穹 第七百九十四章   鹰爪老人 【第一更！】" target="_blank">第七百九十四章   鹰爪老人 【第一更！】</a></li>
                                <li><a href="/1/824.html" title="斗破苍穹 第七百九十四章 鹰爪老人" target="_blank">第七百九十四章 鹰爪老人</a></li>
                                <li><a href="/1/825.html" title="斗破苍穹 第七百九十五章   萧门，萧炎 【第二更！】" target="_blank">第七百九十五章   萧门，萧炎 【第二更！】</a></li>
                                <li><a href="/1/826.html" title="斗破苍穹 第七百九十六章    一个不留 【第三更！】" target="_blank">第七百九十六章    一个不留 【第三更！】</a></li>
                                <li><a href="/1/827.html" title="斗破苍穹 第七百九十七章  风起云涌 【第一更！】" target="_blank">第七百九十七章  风起云涌 【第一更！】</a></li>
                                <li><a href="/1/828.html" title="斗破苍穹 第七百九十八章  进城 【第二更！】" target="_blank">第七百九十八章  进城 【第二更！】</a></li>
                                <li><a href="/1/829.html" title="斗破苍穹 第七百九十九章 千药坊 【第三更！】" target="_blank">第七百九十九章 千药坊 【第三更！】</a></li>
                                <li><a href="/1/830.html" title="斗破苍穹 第八百章  换丹集会 【第一更！】" target="_blank">第八百章  换丹集会 【第一更！】</a></li>
                                <li><a href="/1/831.html" title="斗破苍穹 第八百零一章  红脸老者 【第二更！】" target="_blank">第八百零一章  红脸老者 【第二更！】</a></li>
                                <li><a href="/1/832.html" title="斗破苍穹 第八百零二章  竞价 【第一更！】" target="_blank">第八百零二章  竞价 【第一更！】</a></li>
                                <li><a href="/1/833.html" title="斗破苍穹 第八百零三章  得手 【第二更！】" target="_blank">第八百零三章  得手 【第二更！】</a></li>
                                <li><a href="/1/834.html" title="斗破苍穹 第八百零四章  菩提心 【第三更！】" target="_blank">第八百零四章  菩提心 【第三更！】</a></li>
                                <li><a href="/1/835.html" title="斗破苍穹 第八百零五章 黒皇阁【第一更！】" target="_blank">第八百零五章 黒皇阁【第一更！】</a></li>
                                <li><a href="/1/836.html" title="斗破苍穹 第八百零五章 黑皇阁" target="_blank">第八百零五章 黑皇阁</a></li>
                                <li><a href="/1/837.html" title="斗破苍穹 第八百零六章 找上门的麻烦 【第二更！】" target="_blank">第八百零六章 找上门的麻烦 【第二更！】</a></li>
                                <li><a href="/1/838.html" title="斗破苍穹 第八百零七章  白衣人  【第三更！】" target="_blank">第八百零七章  白衣人  【第三更！】</a></li>
                                <li><a href="/1/839.html" title="斗破苍穹 第八百零八章  莫崖 【第一更！】" target="_blank">第八百零八章  莫崖 【第一更！】</a></li>
                                <li><a href="/1/840.html" title="斗破苍穹 第八百零九章   强者云集 【第二更！】" target="_blank">第八百零九章   强者云集 【第二更！】</a></li>
                                <li><a href="/1/841.html" title="斗破苍穹 第八百一十章  二女暗手 【第三更！】" target="_blank">第八百一十章  二女暗手 【第三更！】</a></li>
                                <li><a href="/1/842.html" title="斗破苍穹 第八百一十一章  破宗丹【第一更】" target="_blank">第八百一十一章  破宗丹【第一更】</a></li>
                                <li><a href="/1/843.html" title="斗破苍穹 第八百一十二章  动静【第二更！】" target="_blank">第八百一十二章  动静【第二更！】</a></li>
                                <li><a href="/1/844.html" title="斗破苍穹 第八百一十三章   莫天行【第三更！】" target="_blank">第八百一十三章   莫天行【第三更！】</a></li>
                                <li><a href="/1/845.html" title="斗破苍穹 第八百一十四章   拍卖开始【第四更！】" target="_blank">第八百一十四章   拍卖开始【第四更！】</a></li>
                                <li><a href="/1/846.html" title="斗破苍穹 第八百一十五章  好戏开锣 【第一更！】" target="_blank">第八百一十五章  好戏开锣 【第一更！】</a></li>
                                <li><a href="/1/847.html" title="斗破苍穹 第八百一十六章   拍卖！【第二更！】" target="_blank">第八百一十六章   拍卖！【第二更！】</a></li>
                                <li><a href="/1/848.html" title="斗破苍穹 第八百一十七章 六合游身尺 【第三更！】" target="_blank">第八百一十七章 六合游身尺 【第三更！】</a></li>
                                <li><a href="/1/849.html" title="斗破苍穹 第八百一十八章 魔兽干尸【第一更！】" target="_blank">第八百一十八章 魔兽干尸【第一更！】</a></li>
                                <li><a href="/1/850.html" title="斗破苍穹 第八百一十九章  拍卖干尸【第二更！】" target="_blank">第八百一十九章  拍卖干尸【第二更！】</a></li>
                                <li><a href="/1/851.html" title="斗破苍穹 第八百二十章   以物换物【第三更！】" target="_blank">第八百二十章   以物换物【第三更！】</a></li>
                                <li><a href="/1/852.html" title="斗破苍穹 第八百二十一章  菩提化体涎【第一更！】" target="_blank">第八百二十一章  菩提化体涎【第一更！】</a></li>
                                <li><a href="/1/853.html" title="斗破苍穹 第八百二十二章   各显本钱【第二更！】" target="_blank">第八百二十二章   各显本钱【第二更！】</a></li>
                                <li><a href="/1/854.html" title="斗破苍穹 第八百二十三章   最终胜者 【第三更！】" target="_blank">第八百二十三章   最终胜者 【第三更！】</a></li>
                                <li><a href="/1/855.html" title="斗破苍穹 第八百二十四章   鹰山老人【第一更！】" target="_blank">第八百二十四章   鹰山老人【第一更！】</a></li>
                                <li><a href="/1/856.html" title="斗破苍穹 第八百二十四章 鹰山老人" target="_blank">第八百二十四章 鹰山老人</a></li>
                                <li><a href="/1/857.html" title="斗破苍穹 第八百二十五章   见面【第二更！】" target="_blank">第八百二十五章   见面【第二更！】</a></li>
                                <li><a href="/1/858.html" title="斗破苍穹 第八百二十六章    相谈 【第三更！】" target="_blank">第八百二十六章    相谈 【第三更！】</a></li>
                                <li><a href="/1/859.html" title="斗破苍穹 第八百二十七章   商议定计【第一更！】" target="_blank">第八百二十七章   商议定计【第一更！】</a></li>
                                <li><a href="/1/860.html" title="斗破苍穹 第八百二十八章  分尸【第二更！】" target="_blank">第八百二十八章  分尸【第二更！】</a></li>
                                <li><a href="/1/861.html" title="斗破苍穹 第八百二十九章   青红血液 【第三更！】" target="_blank">第八百二十九章   青红血液 【第三更！】</a></li>
                                <li><a href="/1/862.html" title="斗破苍穹 第八百三十章 七阶魔核" target="_blank">第八百三十章 七阶魔核</a></li>
                                <li><a href="/1/863.html" title="斗破苍穹 第八百三十一章    心火种子" target="_blank">第八百三十一章    心火种子</a></li>
                                <li><a href="/1/864.html" title="斗破苍穹 第八百三十二章  尾随" target="_blank">第八百三十二章  尾随</a></li>
                                <li><a href="/1/865.html" title="斗破苍穹 第八百三十三章   探测" target="_blank">第八百三十三章   探测</a></li>
                                <li><a href="/1/866.html" title="斗破苍穹 第八百三十四章    灵魂分身" target="_blank">第八百三十四章    灵魂分身</a></li>
                                <li><a href="/1/867.html" title="斗破苍穹 第八百三十五章   果然是你" target="_blank">第八百三十五章   果然是你</a></li>
                                <li><a href="/1/868.html" title="斗破苍穹 第八百三十六章   同门再见" target="_blank">第八百三十六章   同门再见</a></li>
                                <li><a href="/1/869.html" title="斗破苍穹 第八百三十七章   五大斗宗" target="_blank">第八百三十七章   五大斗宗</a></li>
                                <li><a href="/1/870.html" title="斗破苍穹 第八百三十八章  局势转变" target="_blank">第八百三十八章  局势转变</a></li>
                                <li><a href="/1/871.html" title="斗破苍穹 第八百三十九章  大战起" target="_blank">第八百三十九章  大战起</a></li>
                                <li><a href="/1/872.html" title="斗破苍穹 第八百四十章   化生火" target="_blank">第八百四十章   化生火</a></li>
                                <li><a href="/1/873.html" title="斗破苍穹 第八百四十一章   收服" target="_blank">第八百四十一章   收服</a></li>
                                <li><a href="/1/874.html" title="斗破苍穹 第八百四十二章  击杀" target="_blank">第八百四十二章  击杀</a></li>
                                <li><a href="/1/875.html" title="斗破苍穹 第八百四十三章  暴走的紫研" target="_blank">第八百四十三章  暴走的紫研</a></li>
                                <li><a href="/1/876.html" title="斗破苍穹 第八百四十四章   喝退" target="_blank">第八百四十四章   喝退</a></li>
                                <li><a href="/1/877.html" title="斗破苍穹 第八百四十五章   离去" target="_blank">第八百四十五章   离去</a></li>
                                <li><a href="/1/878.html" title="斗破苍穹 第八百四十六章   变故" target="_blank">第八百四十六章   变故</a></li>
                                <li><a href="/1/879.html" title="斗破苍穹 第八百四十七章   消除隐患" target="_blank">第八百四十七章   消除隐患</a></li>
                                <li><a href="/1/880.html" title="斗破苍穹 第八百四十八章  抵达和平镇" target="_blank">第八百四十八章  抵达和平镇</a></li>
                                <li><a href="/1/881.html" title="斗破苍穹 第八百四十九章  欣蓝" target="_blank">第八百四十九章  欣蓝</a></li>
                                <li><a href="/1/882.html" title="斗破苍穹 第八百五十章   见面" target="_blank">第八百五十章   见面</a></li>
                                <li><a href="/1/883.html" title="斗破苍穹 第八百五十一章  办法" target="_blank">第八百五十一章  办法</a></li>
                                <li><a href="/1/884.html" title="斗破苍穹 第八百五十二章   异火消息" target="_blank">第八百五十二章   异火消息</a></li>
                                <li><a href="/1/885.html" title="斗破苍穹 第八百五十三章    九龙天罡火" target="_blank">第八百五十三章    九龙天罡火</a></li>
                                <li><a href="/1/886.html" title="斗破苍穹 第八百五十四章  三千焱炎火" target="_blank">第八百五十四章  三千焱炎火</a></li>
                                <li><a href="/1/887.html" title="斗破苍穹 第八百五十五章  炼制" target="_blank">第八百五十五章  炼制</a></li>
                                <li><a href="/1/888.html" title="斗破苍穹 第八百五十六章  意外收获" target="_blank">第八百五十六章  意外收获</a></li>
                                <li><a href="/1/889.html" title="斗破苍穹 第八百五十七章   霸道的骨翼" target="_blank">第八百五十七章   霸道的骨翼</a></li>
                                <li><a href="/1/890.html" title="斗破苍穹 收到起点的锦书，试用了下，效果很不错" target="_blank">收到起点的锦书，试用了下，效果很不错</a></li>
                                <li><a href="/1/891.html" title="斗破苍穹 第八百五十八章   一劳永逸" target="_blank">第八百五十八章   一劳永逸</a></li>
                                <li><a href="/1/892.html" title="斗破苍穹 第八百五十九章  到来" target="_blank">第八百五十九章  到来</a></li>
                                <li><a href="/1/893.html" title="斗破苍穹 第八百六十章  地魔老鬼" target="_blank">第八百六十章  地魔老鬼</a></li>
                                <li><a href="/1/894.html" title="斗破苍穹 第八百六十一章   动手" target="_blank">第八百六十一章   动手</a></li>
                                <li><a href="/1/895.html" title="斗破苍穹 第八百六十二章   对战地魔老鬼" target="_blank">第八百六十二章   对战地魔老鬼</a></li>
                                <li><a href="/1/896.html" title="斗破苍穹 第八百六十三章  惊心动魄" target="_blank">第八百六十三章  惊心动魄</a></li>
                                <li><a href="/1/897.html" title="斗破苍穹 第八百六十四章    疯狂" target="_blank">第八百六十四章    疯狂</a></li>
                                <li><a href="/1/898.html" title="斗破苍穹 第八百六十五章  毁灭火莲" target="_blank">第八百六十五章  毁灭火莲</a></li>
                                <li><a href="/1/899.html" title="斗破苍穹 第八百六十六章  大破坏！" target="_blank">第八百六十六章  大破坏！</a></li>
                                <li><a href="/1/900.html" title="斗破苍穹 第八百六十七章    千百二老" target="_blank">第八百六十七章    千百二老</a></li>
                                <li><a href="/1/901.html" title="斗破苍穹 第八百六十八章   希冀" target="_blank">第八百六十八章   希冀</a></li>
                                <li><a href="/1/902.html" title="斗破苍穹 第八百六十九章   失败" target="_blank">第八百六十九章   失败</a></li>
                                <li><a href="/1/903.html" title="斗破苍穹 第八百七十章   五星斗皇" target="_blank">第八百七十章   五星斗皇</a></li>
                                <li><a href="/1/904.html" title="斗破苍穹 第八百七十一章   修炼之所" target="_blank">第八百七十一章   修炼之所</a></li>
                                <li><a href="/1/905.html" title="斗破苍穹 第八百七十二章   再进塔底" target="_blank">第八百七十二章   再进塔底</a></li>
                                <li><a href="/1/906.html" title="斗破苍穹 第八百七十三章   召唤" target="_blank">第八百七十三章   召唤</a></li>
                                <li><a href="/1/907.html" title="斗破苍穹 第八百七十四章   尺法小成" target="_blank">第八百七十四章   尺法小成</a></li>
                                <li><a href="/1/908.html" title="斗破苍穹 第八百七十五章   神秘骨骸" target="_blank">第八百七十五章   神秘骨骸</a></li>
                                <li><a href="/1/909.html" title="斗破苍穹 第八百七十六章  岩浆生物" target="_blank">第八百七十六章  岩浆生物</a></li>
                                <li><a href="/1/910.html" title="斗破苍穹 第八百七十七章   火焰蜥蜴族" target="_blank">第八百七十七章   火焰蜥蜴族</a></li>
                                <li><a href="/1/911.html" title="斗破苍穹 第八百七十八章   天火尊者 【第一更！】" target="_blank">第八百七十八章   天火尊者 【第一更！】</a></li>
                                <li><a href="/1/912.html" title="斗破苍穹 第八百七十九章  五轮离火法 【第二更！】" target="_blank">第八百七十九章  五轮离火法 【第二更！】</a></li>
                                <li><a href="/1/913.html" title="斗破苍穹 第八百八十章  神秘存在 【第三更！】" target="_blank">第八百八十章  神秘存在 【第三更！】</a></li>
                                <li><a href="/1/914.html" title="斗破苍穹 第八百八十一章 陀舍古帝玉的动静【第一更！】" target="_blank">第八百八十一章 陀舍古帝玉的动静【第一更！】</a></li>
                                <li><a href="/1/915.html" title="斗破苍穹 第八百八十二章   再次晋级 【第二更！】" target="_blank">第八百八十二章   再次晋级 【第二更！】</a></li>
                                <li><a href="/1/916.html" title="斗破苍穹 第八百八十三章   情报 【第三更！】" target="_blank">第八百八十三章   情报 【第三更！】</a></li>
                                <li><a href="/1/917.html" title="斗破苍穹 第八百八十三章 情报" target="_blank">第八百八十三章 情报</a></li>
                                <li><a href="/1/918.html" title="斗破苍穹 第八百八十四章   商议 【第一更！】" target="_blank">第八百八十四章   商议 【第一更！】</a></li>
                                <li><a href="/1/919.html" title="斗破苍穹 第八百八十五章   招集 【第二更！】" target="_blank">第八百八十五章   招集 【第二更！】</a></li>
                                <li><a href="/1/920.html" title="斗破苍穹 第八百八十六章    联盟 【第三更！】" target="_blank">第八百八十六章    联盟 【第三更！】</a></li>
                                <li><a href="/1/921.html" title="斗破苍穹 第八百八十七章   速度所造成的威慑 【第一更！】" target="_blank">第八百八十七章   速度所造成的威慑 【第一更！】</a></li>
                                <li><a href="/1/922.html" title="斗破苍穹 第八百八十八章   轩护法 【第二更！】" target="_blank">第八百八十八章   轩护法 【第二更！】</a></li>
                                <li><a href="/1/923.html" title="斗破苍穹 第八百八十八章 轩护法" target="_blank">第八百八十八章 轩护法</a></li>
                                <li><a href="/1/924.html" title="斗破苍穹 第八百八十九章   火灵显威 【第三更！】" target="_blank">第八百八十九章   火灵显威 【第三更！】</a></li>
                                <li><a href="/1/925.html" title="斗破苍穹 第八百九十章   凶魂凝聚" target="_blank">第八百九十章   凶魂凝聚</a></li>
                                <li><a href="/1/926.html" title="斗破苍穹 第八百九十一章   迎战" target="_blank">第八百九十一章   迎战</a></li>
                                <li><a href="/1/927.html" title="斗破苍穹 第八百九十二章    收取凶魂" target="_blank">第八百九十二章    收取凶魂</a></li>
                                <li><a href="/1/928.html" title="斗破苍穹 第八百九十三章   击杀" target="_blank">第八百九十三章   击杀</a></li>
                                <li><a href="/1/929.html" title="斗破苍穹 第八百九十四章 再度交手" target="_blank">第八百九十四章 再度交手</a></li>
                                <li><a href="/1/930.html" title="斗破苍穹 第八百九十五章    火莲，杀！" target="_blank">第八百九十五章    火莲，杀！</a></li>
                                <li><a href="/1/931.html" title="斗破苍穹 第八百九十六章   最后胜者" target="_blank">第八百九十六章   最后胜者</a></li>
                                <li><a href="/1/932.html" title="斗破苍穹 第八百九十七章    寻宝" target="_blank">第八百九十七章    寻宝</a></li>
                                <li><a href="/1/933.html" title="斗破苍穹 第八百九十八章   石洞库房" target="_blank">第八百九十八章   石洞库房</a></li>
                                <li><a href="/1/934.html" title="斗破苍穹 第八百九十九章    天妖傀" target="_blank">第八百九十九章    天妖傀</a></li>
                                <li><a href="/1/935.html" title="斗破苍穹 第九百章   养魂涎" target="_blank">第九百章   养魂涎</a></li>
                                <li><a href="/1/936.html" title="斗破苍穹 第九百零一章   厄难毒体提前爆发" target="_blank">第九百零一章   厄难毒体提前爆发</a></li>
                                <li><a href="/1/937.html" title="斗破苍穹 第九百零二章   封印 【第一更！】" target="_blank">第九百零二章   封印 【第一更！】</a></li>
                                <li><a href="/1/938.html" title="斗破苍穹 第九百零三章   炼化凶魂 【第二更！】" target="_blank">第九百零三章   炼化凶魂 【第二更！】</a></li>
                                <li><a href="/1/939.html" title="斗破苍穹 第九百零四章  炼制天妖傀 【第三更！】" target="_blank">第九百零四章  炼制天妖傀 【第三更！】</a></li>
                                <li><a href="/1/940.html" title="斗破苍穹 第九百零五章   淬炼 【第四更！】" target="_blank">第九百零五章   淬炼 【第四更！】</a></li>
                                <li><a href="/1/941.html" title="斗破苍穹 第九百零六章   炼制成功！" target="_blank">第九百零六章   炼制成功！</a></li>
                                <li><a href="/1/942.html" title="斗破苍穹 第九百零七章    大动静" target="_blank">第九百零七章    大动静</a></li>
                                <li><a href="/1/943.html" title="斗破苍穹 第九百零八章   炼制天魂融血丹" target="_blank">第九百零八章   炼制天魂融血丹</a></li>
                                <li><a href="/1/944.html" title="斗破苍穹 第九百零九章   血脉中的威压" target="_blank">第九百零九章   血脉中的威压</a></li>
                                <li><a href="/1/945.html" title="斗破苍穹 第九百一十章     丹成" target="_blank">第九百一十章     丹成</a></li>
                                <li><a href="/1/946.html" title="斗破苍穹 第九百一十一章   丹雷【第二更！】" target="_blank">第九百一十一章   丹雷【第二更！】</a></li>
                                <li><a href="/1/947.html" title="斗破苍穹 第九百一十二章    地妖傀显威【第三更！】" target="_blank">第九百一十二章    地妖傀显威【第三更！】</a></li>
                                <li><a href="/1/948.html" title="斗破苍穹 第九百一十三章   再度突破！" target="_blank">第九百一十三章   再度突破！</a></li>
                                <li><a href="/1/949.html" title="斗破苍穹 第九百一十四章   离开" target="_blank">第九百一十四章   离开</a></li>
                                <li><a href="/1/950.html" title="斗破苍穹 第九百一十五章  一殿一塔，二宗三谷，四方阁" target="_blank">第九百一十五章  一殿一塔，二宗三谷，四方阁</a></li>
                                <li><a href="/1/951.html" title="斗破苍穹 第九百一十六章   关闭" target="_blank">第九百一十六章   关闭</a></li>
                                <li><a href="/1/952.html" title="斗破苍穹 第九百一十七章    红衣少女" target="_blank">第九百一十七章    红衣少女</a></li>
                                <li><a href="/1/953.html" title="斗破苍穹 第九百一十八章   六阶" target="_blank">第九百一十八章   六阶</a></li>
                                <li><a href="/1/954.html" title="斗破苍穹 第九百一十九章   修复【第一更！】" target="_blank">第九百一十九章   修复【第一更！】</a></li>
                                <li><a href="/1/955.html" title="斗破苍穹 第九百二十章    空间风暴【第二更！】" target="_blank">第九百二十章    空间风暴【第二更！】</a></li>
                                <li><a href="/1/956.html" title="斗破苍穹 第九百二十一章   通道惊魂 【第三更！】" target="_blank">第九百二十一章   通道惊魂 【第三更！】</a></li>
                                <li><a href="/1/957.html" title="斗破苍穹 第九百一十九章 修复" target="_blank">第九百一十九章 修复</a></li>
                                <li><a href="/1/958.html" title="斗破苍穹 第九百二十章 空间风暴" target="_blank">第九百二十章 空间风暴</a></li>
                                <li><a href="/1/959.html" title="斗破苍穹 第九百二十一章 通道惊魂" target="_blank">第九百二十一章 通道惊魂</a></li>
                                <li><a href="/1/960.html" title="斗破苍穹 第九百二十二章   韩冲" target="_blank">第九百二十二章   韩冲</a></li>
                                <li><a href="/1/961.html" title="斗破苍穹 第九百二十三章   韩家，韩雪" target="_blank">第九百二十三章   韩家，韩雪</a></li>
                                <li><a href="/1/962.html" title="斗破苍穹 第九百二十四章   妖蛇夏莽" target="_blank">第九百二十四章   妖蛇夏莽</a></li>
                                <li><a href="/1/963.html" title="斗破苍穹 第九百二十五章     万蛇峡" target="_blank">第九百二十五章     万蛇峡</a></li>
                                <li><a href="/1/964.html" title="斗破苍穹 第九百二十六章   神秘强者" target="_blank">第九百二十六章   神秘强者</a></li>
                                <li><a href="/1/965.html" title="斗破苍穹 第九百二十七章   空间之力" target="_blank">第九百二十七章   空间之力</a></li>
                                <li><a href="/1/966.html" title="斗破苍穹 第九百二十八章    洪家【第一更！】" target="_blank">第九百二十八章    洪家【第一更！】</a></li>
                                <li><a href="/1/967.html" title="斗破苍穹 第九百二十九章    出手 【第二更！】" target="_blank">第九百二十九章    出手 【第二更！】</a></li>
                                <li><a href="/1/968.html" title="斗破苍穹 第九百三十章   天北城【第三更！】" target="_blank">第九百三十章   天北城【第三更！】</a></li>
                                <li><a href="/1/969.html" title="斗破苍穹 第九百三十一章  熟人{第四更！}" target="_blank">第九百三十一章  熟人{第四更！}</a></li>
                                <li><a href="/1/970.html" title="斗破苍穹 第九百三十二章    试探" target="_blank">第九百三十二章    试探</a></li>
                                <li><a href="/1/971.html" title="斗破苍穹 第九百三十三章   九转风游步" target="_blank">第九百三十三章   九转风游步</a></li>
                                <li><a href="/1/972.html" title="斗破苍穹 第九百三十四章   诸乾【第一更！】" target="_blank">第九百三十四章   诸乾【第一更！】</a></li>
                                <li><a href="/1/973.html" title="斗破苍穹 第九百三十五章   药老的关押之处【第二更！】" target="_blank">第九百三十五章   药老的关押之处【第二更！】</a></li>
                                <li><a href="/1/974.html" title="斗破苍穹 第九百三十六章    天石台【第三更！】" target="_blank">第九百三十六章    天石台【第三更！】</a></li>
                                <li><a href="/1/975.html" title="斗破苍穹 第九百三十七章   交手【第一更！】" target="_blank">第九百三十七章   交手【第一更！】</a></li>
                                <li><a href="/1/976.html" title="斗破苍穹 第九百三十八章   雷神降临【第二更！】" target="_blank">第九百三十八章   雷神降临【第二更！】</a></li>
                                <li><a href="/1/977.html" title="斗破苍穹 第九百三十九章    灭雷锤！【第三更！】" target="_blank">第九百三十九章    灭雷锤！【第三更！】</a></li>
                                <li><a href="/1/978.html" title="斗破苍穹 第九百四十章   变故【第一更！】" target="_blank">第九百四十章   变故【第一更！】</a></li>
                                <li><a href="/1/979.html" title="斗破苍穹 第九百四十一章   不够资格【第二更！】" target="_blank">第九百四十一章   不够资格【第二更！】</a></li>
                                <li><a href="/1/980.html" title="斗破苍穹 第九百四十二章    妖傀现身【第三更！】" target="_blank">第九百四十二章    妖傀现身【第三更！】</a></li>
                                <li><a href="/1/981.html" title="斗破苍穹 第九百四十三章    洪家围剿【第一更！】" target="_blank">第九百四十三章    洪家围剿【第一更！】</a></li>
                                <li><a href="/1/982.html" title="斗破苍穹 第九百四十四章   杀伐果断【第二更！】" target="_blank">第九百四十四章   杀伐果断【第二更！】</a></li>
                                <li><a href="/1/983.html" title="斗破苍穹 第九百四十五章   疯狂的举动【第三更！】" target="_blank">第九百四十五章   疯狂的举动【第三更！】</a></li>
                                <li><a href="/1/984.html" title="斗破苍穹 第九百四十六章   三千雷幻身【第一更！】" target="_blank">第九百四十六章   三千雷幻身【第一更！】</a></li>
                                <li><a href="/1/985.html" title="斗破苍穹 第九百四十七章    残卷【第二更！】" target="_blank">第九百四十七章    残卷【第二更！】</a></li>
                                <li><a href="/1/986.html" title="斗破苍穹 第九百四十八章   滔天气势【第三更！】" target="_blank">第九百四十八章   滔天气势【第三更！】</a></li>
                                <li><a href="/1/987.html" title="斗破苍穹 第九百四十九章   击杀沈云【第一更！】" target="_blank">第九百四十九章   击杀沈云【第一更！】</a></li>
                                <li><a href="/1/988.html" title="斗破苍穹 第九百五十章   斗宗强者的自爆【第二更！】" target="_blank">第九百五十章   斗宗强者的自爆【第二更！】</a></li>
                                <li><a href="/1/989.html" title="斗破苍穹 第九百五十一章   栖凤山【第三更！】" target="_blank">第九百五十一章   栖凤山【第三更！】</a></li>
                                <li><a href="/1/990.html" title="斗破苍穹 第九百五十二章   九星斗皇【第四更！】" target="_blank">第九百五十二章   九星斗皇【第四更！】</a></li>
                                <li><a href="/1/991.html" title="斗破苍穹 第九百五十三章   龙潭虎穴【第一更！】" target="_blank">第九百五十三章   龙潭虎穴【第一更！】</a></li>
                                <li><a href="/1/992.html" title="斗破苍穹 第九百五十四章    九天雷狱阵【第二更！】" target="_blank">第九百五十四章    九天雷狱阵【第二更！】</a></li>
                                <li><a href="/1/993.html" title="斗破苍穹 第九百五十五章   雷神之怒【第三更！】" target="_blank">第九百五十五章   雷神之怒【第三更！】</a></li>
                                <li><a href="/1/994.html" title="斗破苍穹 第九百五十六章    火莲之威【第一更！】" target="_blank">第九百五十六章    火莲之威【第一更！】</a></li>
                                <li><a href="/1/995.html" title="斗破苍穹 第九百五十七章   斩杀洪天啸【第二更！】" target="_blank">第九百五十七章   斩杀洪天啸【第二更！】</a></li>
                                <li><a href="/1/996.html" title="斗破苍穹 第九百五十八章   灵魂残印【第三更！】" target="_blank">第九百五十八章   灵魂残印【第三更！】</a></li>
                                <li><a href="/1/997.html" title="斗破苍穹 第九百五十九章   天山血潭【第一更！】" target="_blank">第九百五十九章   天山血潭【第一更！】</a></li>
                                <li><a href="/1/998.html" title="斗破苍穹 第九百六十章    天雷子【第二更！】" target="_blank">第九百六十章    天雷子【第二更！】</a></li>
                                <li><a href="/1/999.html" title="斗破苍穹 第九百六十一章     追杀【第三更！】" target="_blank">第九百六十一章     追杀【第三更！】</a></li>
                                <li><a href="/1/1000.html" title="斗破苍穹 第九百三十四章 诸乾" target="_blank">第九百三十四章 诸乾</a></li>
                                <li><a href="/1/1001.html" title="斗破苍穹 第九百三十五章  药老的关押之处" target="_blank">第九百三十五章  药老的关押之处</a></li>
                                <li><a href="/1/1002.html" title="斗破苍穹 第九百三十六章 天石台" target="_blank">第九百三十六章 天石台</a></li>
                                <li><a href="/1/1003.html" title="斗破苍穹 第九百三十七章 交手" target="_blank">第九百三十七章 交手</a></li>
                                <li><a href="/1/1004.html" title="斗破苍穹 第九百三十八章 雷神降临" target="_blank">第九百三十八章 雷神降临</a></li>
                                <li><a href="/1/1005.html" title="斗破苍穹 第九百三十九章 灭雷锤！" target="_blank">第九百三十九章 灭雷锤！</a></li>
                                <li><a href="/1/1006.html" title="斗破苍穹 第九百四十章 变故" target="_blank">第九百四十章 变故</a></li>
                                <li><a href="/1/1007.html" title="斗破苍穹 第九百四十一章 不够资格" target="_blank">第九百四十一章 不够资格</a></li>
                                <li><a href="/1/1008.html" title="斗破苍穹 第九百四十二章 妖傀现身" target="_blank">第九百四十二章 妖傀现身</a></li>
                                <li><a href="/1/1009.html" title="斗破苍穹 第九百四十三章 洪家围剿" target="_blank">第九百四十三章 洪家围剿</a></li>
                                <li><a href="/1/1010.html" title="斗破苍穹 第九百四十四章 杀伐果断" target="_blank">第九百四十四章 杀伐果断</a></li>
                                <li><a href="/1/1011.html" title="斗破苍穹 第九百四十五章 疯狂的举动" target="_blank">第九百四十五章 疯狂的举动</a></li>
                                <li><a href="/1/1012.html" title="斗破苍穹 第九百四十六章 三千雷幻身" target="_blank">第九百四十六章 三千雷幻身</a></li>
                                <li><a href="/1/1013.html" title="斗破苍穹 第九百四十七章 残卷" target="_blank">第九百四十七章 残卷</a></li>
                                <li><a href="/1/1014.html" title="斗破苍穹 第九百四十八章 滔天气势" target="_blank">第九百四十八章 滔天气势</a></li>
                                <li><a href="/1/1015.html" title="斗破苍穹 第九百四十九章 击杀沈云" target="_blank">第九百四十九章 击杀沈云</a></li>
                                <li><a href="/1/1016.html" title="斗破苍穹 第九百五十章 斗宗强者的自爆" target="_blank">第九百五十章 斗宗强者的自爆</a></li>
                                <li><a href="/1/1017.html" title="斗破苍穹 第九百五十一章 栖凤山" target="_blank">第九百五十一章 栖凤山</a></li>
                                <li><a href="/1/1018.html" title="斗破苍穹 第九百五十二章 九星斗皇" target="_blank">第九百五十二章 九星斗皇</a></li>
                                <li><a href="/1/1019.html" title="斗破苍穹 第九百五十三章 龙潭虎穴" target="_blank">第九百五十三章 龙潭虎穴</a></li>
                                <li><a href="/1/1020.html" title="斗破苍穹 第九百五十四章 九天雷狱阵" target="_blank">第九百五十四章 九天雷狱阵</a></li>
                                <li><a href="/1/1021.html" title="斗破苍穹 第九百五十五章 雷神之怒" target="_blank">第九百五十五章 雷神之怒</a></li>
                                <li><a href="/1/1022.html" title="斗破苍穹 第九百五十六章 火莲之威" target="_blank">第九百五十六章 火莲之威</a></li>
                                <li><a href="/1/1023.html" title="斗破苍穹 第九百五十七章 斩杀洪天啸" target="_blank">第九百五十七章 斩杀洪天啸</a></li>
                                <li><a href="/1/1024.html" title="斗破苍穹 第九百五十八章 灵魂残印" target="_blank">第九百五十八章 灵魂残印</a></li>
                                <li><a href="/1/1025.html" title="斗破苍穹 第九百五十九章 天山血潭" target="_blank">第九百五十九章 天山血潭</a></li>
                                <li><a href="/1/1026.html" title="斗破苍穹 第九百六十章 天雷子" target="_blank">第九百六十章 天雷子</a></li>
                                <li><a href="/1/1027.html" title="斗破苍穹 第九百六十一章 追杀" target="_blank">第九百六十一章 追杀</a></li>
                                <li><a href="/1/1028.html" title="斗破苍穹 第九百六十二章    破解" target="_blank">第九百六十二章    破解</a></li>
                                <li><a href="/1/1029.html" title="斗破苍穹 第九百六十三章   森林苦修" target="_blank">第九百六十三章   森林苦修</a></li>
                                <li><a href="/1/1030.html" title="斗破苍穹 第九百六十四章    七阶苍狼王【第三更！】" target="_blank">第九百六十四章    七阶苍狼王【第三更！】</a></li>
                                <li><a href="/1/1031.html" title="斗破苍穹 第九百六十四章 七阶苍狼王" target="_blank">第九百六十四章 七阶苍狼王</a></li>
                                <li><a href="/1/1032.html" title="斗破苍穹 第九百六十五章    魔兽界三大族群" target="_blank">第九百六十五章    魔兽界三大族群</a></li>
                                <li><a href="/1/1033.html" title="斗破苍穹 第九百六十六章    锤炼分身" target="_blank">第九百六十六章    锤炼分身</a></li>
                                <li><a href="/1/1034.html" title="斗破苍穹 第九百六十七章   抵达天目山脉" target="_blank">第九百六十七章   抵达天目山脉</a></li>
                                <li><a href="/1/1035.html" title="斗破苍穹 第九百六十八章   凤小姐" target="_blank">第九百六十八章   凤小姐</a></li>
                                <li><a href="/1/1036.html" title="斗破苍穹 第九百六十九章    初步交手【第一更！】" target="_blank">第九百六十九章    初步交手【第一更！】</a></li>
                                <li><a href="/1/1037.html" title="斗破苍穹 第九百七十章    黑衣男子平【第二更！】" target="_blank">第九百七十章    黑衣男子平【第二更！】</a></li>
                                <li><a href="/1/1038.html" title="斗破苍穹 第九百七十一章    故人【第三更！】" target="_blank">第九百七十一章    故人【第三更！】</a></li>
                                <li><a href="/1/1039.html" title="斗破苍穹 第九百七十二章     再见纳兰嫣然" target="_blank">第九百七十二章     再见纳兰嫣然</a></li>
                                <li><a href="/1/1040.html" title="斗破苍穹 第九百六十九章 初步交手" target="_blank">第九百六十九章 初步交手</a></li>
                                <li><a href="/1/1041.html" title="斗破苍穹 第九百七十章 黑衣男子" target="_blank">第九百七十章 黑衣男子</a></li>
                                <li><a href="/1/1042.html" title="斗破苍穹 第九百七十一章 故人" target="_blank">第九百七十一章 故人</a></li>
                                <li><a href="/1/1043.html" title="斗破苍穹 第九百七十三章    王尘" target="_blank">第九百七十三章    王尘</a></li>
                                <li><a href="/1/1044.html" title="斗破苍穹 第九百七十四章    迷阵" target="_blank">第九百七十四章    迷阵</a></li>
                                <li><a href="/1/1045.html" title="斗破苍穹 第九百七十五章    白狐引起的血案" target="_blank">第九百七十五章    白狐引起的血案</a></li>
                                <li><a href="/1/1046.html" title="斗破苍穹 第九百七十六章   天山台" target="_blank">第九百七十六章   天山台</a></li>
                                <li><a href="/1/1047.html" title="斗破苍穹 第九百七十七章   鼠潮音波阵" target="_blank">第九百七十七章   鼠潮音波阵</a></li>
                                <li><a href="/1/1048.html" title="斗破苍穹 第九百七十八章   闯关" target="_blank">第九百七十八章   闯关</a></li>
                                <li><a href="/1/1049.html" title="斗破苍穹 第九百七十九章   慕青鸾" target="_blank">第九百七十九章   慕青鸾</a></li>
                                <li><a href="/1/1050.html" title="斗破苍穹 第九百八十章    声波对碰！" target="_blank">第九百八十章    声波对碰！</a></li>
                                <li><a href="/1/1051.html" title="斗破苍穹 第九百八十一章    风尊者去向" target="_blank">第九百八十一章    风尊者去向</a></li>
                                <li><a href="/1/1052.html" title="斗破苍穹 第九百八十二章    交易" target="_blank">第九百八十二章    交易</a></li>
                                <li><a href="/1/1053.html" title="斗破苍穹 第九百八十三章   血潭之底" target="_blank">第九百八十三章   血潭之底</a></li>
                                <li><a href="/1/1054.html" title="斗破苍穹 第九百八十四章   进入血潭" target="_blank">第九百八十四章   进入血潭</a></li>
                                <li><a href="/1/1055.html" title="斗破苍穹 第九百八十五章    血潭潜修！" target="_blank">第九百八十五章    血潭潜修！</a></li>
                                <li><a href="/1/1056.html" title="斗破苍穹 第九百八十六章   淬炼灵魂之效" target="_blank">第九百八十六章   淬炼灵魂之效</a></li>
                                <li><a href="/1/1057.html" title="斗破苍穹 第九百八十七章    突破！斗宗！【求月票，求订阅！】" target="_blank">第九百八十七章    突破！斗宗！【求月票，求订阅！】</a></li>
                                <li><a href="/1/1058.html" title="斗破苍穹 第九百八十七章 突破！斗宗！" target="_blank">第九百八十七章 突破！斗宗！</a></li>
                                <li><a href="/1/1059.html" title="斗破苍穹 第九百八十八章    再见药老！" target="_blank">第九百八十八章    再见药老！</a></li>
                                <li><a href="/1/1060.html" title="斗破苍穹 第九百八十九章   一星斗宗" target="_blank">第九百八十九章   一星斗宗</a></li>
                                <li><a href="/1/1061.html" title="斗破苍穹 第九百九十章    古界" target="_blank">第九百九十章    古界</a></li>
                                <li><a href="/1/1062.html" title="斗破苍穹 第九百九十一章    炼" target="_blank">第九百九十一章    炼</a></li>
                                <li><a href="/1/1063.html" title="斗破苍穹 第九百九十一章 炼化魔毒斑" target="_blank">第九百九十一章 炼化魔毒斑</a></li>
                                <li><a href="/1/1064.html" title="斗破苍穹 第九百九十二章   风雷山脉" target="_blank">第九百九十二章   风雷山脉</a></li>
                                <li><a href="/1/1065.html" title="斗破苍穹 第九百九十三章   雷山" target="_blank">第九百九十三章   雷山</a></li>
                                <li><a href="/1/1066.html" title="斗破苍穹 第九百九十四章    四大尊者" target="_blank">第九百九十四章    四大尊者</a></li>
                                <li><a href="/1/1067.html" title="斗破苍穹 第九百九十五章  大会开始" target="_blank">第九百九十五章  大会开始</a></li>
                                <li><a href="/1/1068.html" title="斗破苍穹 第九百九十六章    混乱筛选" target="_blank">第九百九十六章    混乱筛选</a></li>
                                <li><a href="/1/1069.html" title="斗破苍穹 第九百九十七章    来吧" target="_blank">第九百九十七章    来吧</a></li>
                                <li><a href="/1/1070.html" title="斗破苍穹 第九百九十八章    战王尘" target="_blank">第九百九十八章    战王尘</a></li>
                                <li><a href="/1/1071.html" title="斗破苍穹 第九百九十九章    六合火" target="_blank">第九百九十九章    六合火</a></li>
                                <li><a href="/1/1072.html" title="斗破苍穹 第一千章   识破身份" target="_blank">第一千章   识破身份</a></li>
                                <li><a href="/1/1073.html" title="斗破苍穹 第一千零一章      奉陪便是" target="_blank">第一千零一章      奉陪便是</a></li>
                                <li><a href="/1/1074.html" title="斗破苍穹 第一千零二章   年轻一辈的巅峰一战" target="_blank">第一千零二章   年轻一辈的巅峰一战</a></li>
                                <li><a href="/1/1075.html" title="斗破苍穹 第一千零三章   风杀指" target="_blank">第一千零三章   风杀指</a></li>
                                <li><a href="/1/1076.html" title="斗破苍穹 第一千零四章   妖凰圣像" target="_blank">第一千零四章   妖凰圣像</a></li>
                                <li><a href="/1/1077.html" title="斗破苍穹 第一千零五章   圣像之力" target="_blank">第一千零五章   圣像之力</a></li>
                                <li><a href="/1/1078.html" title="斗破苍穹 第一千零六章  妖凰钟" target="_blank">第一千零六章  妖凰钟</a></li>
                                <li><a href="/1/1079.html" title="斗破苍穹 第一千零七章    胜负" target="_blank">第一千零七章    胜负</a></li>
                                <li><a href="/1/1080.html" title="斗破苍穹 第一千零八章   古凰血精" target="_blank">第一千零八章   古凰血精</a></li>
                                <li><a href="/1/1081.html" title="斗破苍穹 第一千零九章   大会落幕" target="_blank">第一千零九章   大会落幕</a></li>
                                <li><a href="/1/1082.html" title="斗破苍穹 第一千零十一章   吸收【第一更！】" target="_blank">第一千零十一章   吸收【第一更！】</a></li>
                                <li><a href="/1/1083.html" title="斗破苍穹 第一千零十一章 吸收" target="_blank">第一千零十一章 吸收</a></li>
                                <li><a href="/1/1084.html" title="斗破苍穹 第一千零一十二章   骨翼变异" target="_blank">第一千零一十二章   骨翼变异</a></li>
                                <li><a href="/1/1085.html" title="斗破苍穹 第一千零一十三章   当年旧事" target="_blank">第一千零一十三章   当年旧事</a></li>
                                <li><a href="/1/1086.html" title="斗破苍穹 第一千零一十四章   前往丹域" target="_blank">第一千零一十四章   前往丹域</a></li>
                                <li><a href="/1/1087.html" title="斗破苍穹 第一千零一十五章   修炼弄焰决" target="_blank">第一千零一十五章   修炼弄焰决</a></li>
                                <li><a href="/1/1088.html" title="斗破苍穹 第一千零一十六章   锤炼兽火" target="_blank">第一千零一十六章   锤炼兽火</a></li>
                                <li><a href="/1/1089.html" title="斗破苍穹 第一千零一十七章   火种" target="_blank">第一千零一十七章   火种</a></li>
                                <li><a href="/1/1090.html" title="斗破苍穹 第一千零一十八章   中域，天黄城" target="_blank">第一千零一十八章   中域，天黄城</a></li>
                                <li><a href="/1/1091.html" title="斗破苍穹 第一千零一十九章   虫洞争夺" target="_blank">第一千零一十九章   虫洞争夺</a></li>
                                <li><a href="/1/1092.html" title="斗破苍穹 第一千零二十章    故友相见 【第一更！】" target="_blank">第一千零二十章    故友相见 【第一更！】</a></li>
                                <li><a href="/1/1093.html" title="斗破苍穹 第一千零二十一章   一招【第二更！】" target="_blank">第一千零二十一章   一招【第二更！】</a></li>
                                <li><a href="/1/1094.html" title="斗破苍穹 第一千零二十二章   前往焚炎谷【第三更！】" target="_blank">第一千零二十二章   前往焚炎谷【第三更！】</a></li>
                                <li><a href="/1/1095.html" title="斗破苍穹 第一千零二十三章   炙火山脉【第一更！】" target="_blank">第一千零二十三章   炙火山脉【第一更！】</a></li>
                                <li><a href="/1/1096.html" title="斗破苍穹 第一千零二十四章   唐震，九龙雷罡火！【第二更！】" target="_blank">第一千零二十四章   唐震，九龙雷罡火！【第二更！】</a></li>
                                <li><a href="/1/1097.html" title="斗破苍穹 第一千零二十五章    异火测试【第三更！】" target="_blank">第一千零二十五章    异火测试【第三更！】</a></li>
                                <li><a href="/1/1098.html" title="斗破苍穹 第一千零二十六章   报酬【第一更！】" target="_blank">第一千零二十六章   报酬【第一更！】</a></li>
                                <li><a href="/1/1099.html" title="斗破苍穹 第一千零二十七章    争取【第二更！】" target="_blank">第一千零二十七章    争取【第二更！】</a></li>
                                <li><a href="/1/1100.html" title="斗破苍穹 第一千零二十八章   火菩丹【第三更！】" target="_blank">第一千零二十八章   火菩丹【第三更！】</a></li>
                                <li><a href="/1/1101.html" title="斗破苍穹 第一千零二十九章   融合【第一更！】" target="_blank">第一千零二十九章   融合【第一更！】</a></li>
                                <li><a href="/1/1102.html" title="斗破苍穹 第一千零三十章   变故【第二更！】" target="_blank">第一千零三十章   变故【第二更！】</a></li>
                                <li><a href="/1/1103.html" title="斗破苍穹 第一千零三十一章    力挽狂澜【第三更！】" target="_blank">第一千零三十一章    力挽狂澜【第三更！】</a></li>
                                <li><a href="/1/1104.html" title="斗破苍穹 第一千零二十章 故友相见" target="_blank">第一千零二十章 故友相见</a></li>
                                <li><a href="/1/1105.html" title="斗破苍穹 第一千零二十一章 一招" target="_blank">第一千零二十一章 一招</a></li>
                                <li><a href="/1/1106.html" title="斗破苍穹 第一千零二十二章 前往焚炎谷" target="_blank">第一千零二十二章 前往焚炎谷</a></li>
                                <li><a href="/1/1107.html" title="斗破苍穹 第一千零二十三章 炙火山脉" target="_blank">第一千零二十三章 炙火山脉</a></li>
                                <li><a href="/1/1108.html" title="斗破苍穹 第一千零二十四章 唐震，九龙雷罡火！" target="_blank">第一千零二十四章 唐震，九龙雷罡火！</a></li>
                                <li><a href="/1/1109.html" title="斗破苍穹 第一千零二十五章 异火测试" target="_blank">第一千零二十五章 异火测试</a></li>
                                <li><a href="/1/1110.html" title="斗破苍穹 第一千零二十六章 报酬" target="_blank">第一千零二十六章 报酬</a></li>
                                <li><a href="/1/1111.html" title="斗破苍穹 第一千零二十七章 争取" target="_blank">第一千零二十七章 争取</a></li>
                                <li><a href="/1/1112.html" title="斗破苍穹 第一千零二十八章 火菩丹" target="_blank">第一千零二十八章 火菩丹</a></li>
                                <li><a href="/1/1113.html" title="斗破苍穹 第一千零二十九章 融合" target="_blank">第一千零二十九章 融合</a></li>
                                <li><a href="/1/1114.html" title="斗破苍穹 第一千零三十章 变故" target="_blank">第一千零三十章 变故</a></li>
                                <li><a href="/1/1115.html" title="斗破苍穹 第一千零三十一章 力挽狂澜" target="_blank">第一千零三十一章 力挽狂澜</a></li>
                                <li><a href="/1/1116.html" title="斗破苍穹 第一千零三十二章   再见丹雷" target="_blank">第一千零三十二章   再见丹雷</a></li>
                                <li><a href="/1/1117.html" title="斗破苍穹 第一千零三十三章    炼丹成功【第一更！】" target="_blank">第一千零三十三章    炼丹成功【第一更！】</a></li>
                                <li><a href="/1/1118.html" title="斗破苍穹 第一千零三十四章    阴阳命魂丹【第二更！】" target="_blank">第一千零三十四章    阴阳命魂丹【第二更！】</a></li>
                                <li><a href="/1/1119.html" title="斗破苍穹 第一千零三十五章   受阻【第三更！】" target="_blank">第一千零三十五章   受阻【第三更！】</a></li>
                                <li><a href="/1/1120.html" title="斗破苍穹 第一千零三十三章 炼丹成功" target="_blank">第一千零三十三章 炼丹成功</a></li>
                                <li><a href="/1/1121.html" title="斗破苍穹 第一千零三十四章 阴阳命魂丹" target="_blank">第一千零三十四章 阴阳命魂丹</a></li>
                                <li><a href="/1/1122.html" title="斗破苍穹 第一千零三十五章 受阻" target="_blank">第一千零三十五章 受阻</a></li>
                                <li><a href="/1/1123.html" title="斗破苍穹 第一千零三十六章   考验" target="_blank">第一千零三十六章   考验</a></li>
                                <li><a href="/1/1124.html" title="斗破苍穹 第一千零三十七章   对战吴辰" target="_blank">第一千零三十七章   对战吴辰</a></li>
                                <li><a href="/1/1125.html" title="斗破苍穹 第一千零三十八章    暗藏一手" target="_blank">第一千零三十八章    暗藏一手</a></li>
                                <li><a href="/1/1126.html" title="斗破苍穹 第一千零三十九章   到手" target="_blank">第一千零三十九章   到手</a></li>
                                <li><a href="/1/1127.html" title="斗破苍穹 第一千零四十章   传承秘法" target="_blank">第一千零四十章   传承秘法</a></li>
                                <li><a href="/1/1128.html" title="斗破苍穹 第一千零四十一章   萧玄" target="_blank">第一千零四十一章   萧玄</a></li>
                                <li><a href="/1/1129.html" title="斗破苍穹 第一千零四十二章    小医仙消息" target="_blank">第一千零四十二章    小医仙消息</a></li>
                                <li><a href="/1/1130.html" title="斗破苍穹 第一千零四十三章   赶至中域" target="_blank">第一千零四十三章   赶至中域</a></li>
                                <li><a href="/1/1131.html" title="斗破苍穹 第一千零四十四章   叶城【第三更！】" target="_blank">第一千零四十四章   叶城【第三更！】</a></li>
                                <li><a href="/1/1132.html" title="斗破苍穹 第一千零四十五章   叶家【第一更！】" target="_blank">第一千零四十五章   叶家【第一更！】</a></li>
                                <li><a href="/1/1133.html" title="斗破苍穹 第一千零四十六章   去向【第二更！】" target="_blank">第一千零四十六章   去向【第二更！】</a></li>
                                <li><a href="/1/1134.html" title="斗破苍穹 第一千零四十七章    落神涧【第三更！】" target="_blank">第一千零四十七章    落神涧【第三更！】</a></li>
                                <li><a href="/1/1135.html" title="斗破苍穹 第一千零四十四章 叶城" target="_blank">第一千零四十四章 叶城</a></li>
                                <li><a href="/1/1136.html" title="斗破苍穹 第一千零四十五章 叶家" target="_blank">第一千零四十五章 叶家</a></li>
                                <li><a href="/1/1137.html" title="斗破苍穹 第一千零四十六章 去向" target="_blank">第一千零四十六章 去向</a></li>
                                <li><a href="/1/1138.html" title="斗破苍穹 第一千零四十七章 落神涧" target="_blank">第一千零四十七章 落神涧</a></li>
                                <li><a href="/1/1139.html" title="斗破苍穹 第一千零四十八章   冰河谷的剿杀" target="_blank">第一千零四十八章   冰河谷的剿杀</a></li>
                                <li><a href="/1/1140.html" title="斗破苍穹 第一千零四十九章   逆转局面" target="_blank">第一千零四十九章   逆转局面</a></li>
                                <li><a href="/1/1141.html" title="斗破苍穹 第一千零五十章   不堪一击" target="_blank">第一千零五十章   不堪一击</a></li>
                                <li><a href="/1/1142.html" title="斗破苍穹 第一千零五十一章   一个不留" target="_blank">第一千零五十一章   一个不留</a></li>
                                <li><a href="/1/1143.html" title="斗破苍穹 第一千零五十二章   疗伤" target="_blank">第一千零五十二章   疗伤</a></li>
                                <li><a href="/1/1144.html" title="斗破苍穹 第一千零五十三章    天毒蝎龙兽踪迹" target="_blank">第一千零五十三章    天毒蝎龙兽踪迹</a></li>
                                <li><a href="/1/1145.html" title="斗破苍穹 第一千零五十四章   晋级" target="_blank">第一千零五十四章   晋级</a></li>
                                <li><a href="/1/1146.html" title="斗破苍穹 第一千零五十五章   天毒蝎龙兽" target="_blank">第一千零五十五章   天毒蝎龙兽</a></li>
                                <li><a href="/1/1147.html" title="斗破苍穹 第一千零五十六章   蝎龙族" target="_blank">第一千零五十六章   蝎龙族</a></li>
                                <li><a href="/1/1148.html" title="斗破苍穹 第一千零五十七章   剿杀天毒蝎龙兽" target="_blank">第一千零五十七章   剿杀天毒蝎龙兽</a></li>
                                <li><a href="/1/1149.html" title="斗破苍穹 第一千零五十八章   击杀！" target="_blank">第一千零五十八章   击杀！</a></li>
                                <li><a href="/1/1150.html" title="斗破苍穹 第一千零五十九章   到手" target="_blank">第一千零五十九章   到手</a></li>
                                <li><a href="/1/1151.html" title="斗破苍穹 第一千零六十章   炼制阴阳命魂丹" target="_blank">第一千零六十章   炼制阴阳命魂丹</a></li>
                                <li><a href="/1/1152.html" title="斗破苍穹 第一千零六十一章   炼制躯体" target="_blank">第一千零六十一章   炼制躯体</a></li>
                                <li><a href="/1/1153.html" title="斗破苍穹 第一千零六十二章   斗宗巅峰" target="_blank">第一千零六十二章   斗宗巅峰</a></li>
                                <li><a href="/1/1154.html" title="斗破苍穹 第一千零六十三章   以卵击石" target="_blank">第一千零六十三章   以卵击石</a></li>
                                <li><a href="/1/1155.html" title="斗破苍穹 第一千零六十四章  阳火" target="_blank">第一千零六十四章  阳火</a></li>
                                <li><a href="/1/1156.html" title="斗破苍穹 第一千零六十五章   黑火宗" target="_blank">第一千零六十五章   黑火宗</a></li>
                                <li><a href="/1/1157.html" title="斗破苍穹 第一千零六十六章  阳火古坛【第一更！】" target="_blank">第一千零六十六章  阳火古坛【第一更！】</a></li>
                                <li><a href="/1/1158.html" title="斗破苍穹 第一千零六十七章    毒丹之法，开启！【第二更！】" target="_blank">第一千零六十七章    毒丹之法，开启！【第二更！】</a></li>
                                <li><a href="/1/1159.html" title="斗破苍穹 第一千零六十八章   谁动你，我便杀谁！【第三更！】" target="_blank">第一千零六十八章   谁动你，我便杀谁！【第三更！】</a></li>
                                <li><a href="/1/1160.html" title="斗破苍穹 第一千零六十九章  地心珠【第一更！】" target="_blank">第一千零六十九章  地心珠【第一更！】</a></li>
                                <li><a href="/1/1161.html" title="斗破苍穹 第一千零七十章　　夺取【第二更！】" target="_blank">第一千零七十章　　夺取【第二更！】</a></li>
                                <li><a href="/1/1162.html" title="斗破苍穹 第一千零七十一章   大战将至【第三更！】" target="_blank">第一千零七十一章   大战将至【第三更！】</a></li>
                                <li><a href="/1/1163.html" title="斗破苍穹 第一千零七十二章  三变！【第一更！】" target="_blank">第一千零七十二章  三变！【第一更！】</a></li>
                                <li><a href="/1/1164.html" title="斗破苍穹 第一千零七十三章   恐怖的增幅【第二更！】" target="_blank">第一千零七十三章   恐怖的增幅【第二更！】</a></li>
                                <li><a href="/1/1165.html" title="斗破苍穹 第一千零七十四章   摧枯拉朽【第三更！】" target="_blank">第一千零七十四章   摧枯拉朽【第三更！】</a></li>
                                <li><a href="/1/1166.html" title="斗破苍穹 第一千零七十五章   离火焚天【求月票！】" target="_blank">第一千零七十五章   离火焚天【求月票！】</a></li>
                                <li><a href="/1/1167.html" title="斗破苍穹 第一千零七十六章   恐怖对轰【第二更！】" target="_blank">第一千零七十六章   恐怖对轰【第二更！】</a></li>
                                <li><a href="/1/1168.html" title="斗破苍穹 第一千零七十七章   震撼之战【第三更！】" target="_blank">第一千零七十七章   震撼之战【第三更！】</a></li>
                                <li><a href="/1/1169.html" title="斗破苍穹 第一千零七十八章   青海【第一更！】" target="_blank">第一千零七十八章   青海【第一更！】</a></li>
                                <li><a href="/1/1170.html" title="斗破苍穹 第一千零七十九章   寒冰王座【第三更！】" target="_blank">第一千零七十九章   寒冰王座【第三更！】</a></li>
                                <li><a href="/1/1171.html" title="斗破苍穹 第一千零八十章  冰尊者【第三更，刚才写错了。】" target="_blank">第一千零八十章  冰尊者【第三更，刚才写错了。】</a></li>
                                <li><a href="/1/1172.html" title="斗破苍穹 第一千零六十六章 阳火古坛" target="_blank">第一千零六十六章 阳火古坛</a></li>
                                <li><a href="/1/1173.html" title="斗破苍穹 第一千零六十七章 毒丹之法，开启！" target="_blank">第一千零六十七章 毒丹之法，开启！</a></li>
                                <li><a href="/1/1174.html" title="斗破苍穹 第一千零六十八章 谁动你，我便杀谁！" target="_blank">第一千零六十八章 谁动你，我便杀谁！</a></li>
                                <li><a href="/1/1175.html" title="斗破苍穹 第一千零六十九章 地心珠" target="_blank">第一千零六十九章 地心珠</a></li>
                                <li><a href="/1/1176.html" title="斗破苍穹 第一千零七十章 夺取" target="_blank">第一千零七十章 夺取</a></li>
                                <li><a href="/1/1177.html" title="斗破苍穹 第一千零七十一章 大战将至" target="_blank">第一千零七十一章 大战将至</a></li>
                                <li><a href="/1/1178.html" title="斗破苍穹 第一千零七十二章 三变！" target="_blank">第一千零七十二章 三变！</a></li>
                                <li><a href="/1/1179.html" title="斗破苍穹 第一千零七十三章 恐怖的增幅" target="_blank">第一千零七十三章 恐怖的增幅</a></li>
                                <li><a href="/1/1180.html" title="斗破苍穹 第一千零七十四章 摧枯拉朽" target="_blank">第一千零七十四章 摧枯拉朽</a></li>
                                <li><a href="/1/1181.html" title="斗破苍穹 第一千零七十五章 离火焚天" target="_blank">第一千零七十五章 离火焚天</a></li>
                                <li><a href="/1/1182.html" title="斗破苍穹 第一千零七十六章 恐怖对轰" target="_blank">第一千零七十六章 恐怖对轰</a></li>
                                <li><a href="/1/1183.html" title="斗破苍穹 第一千零七十七章 震撼之战" target="_blank">第一千零七十七章 震撼之战</a></li>
                                <li><a href="/1/1184.html" title="斗破苍穹 第一千零七十八章 青海" target="_blank">第一千零七十八章 青海</a></li>
                                <li><a href="/1/1185.html" title="斗破苍穹 第一千零七十九章 寒冰王座" target="_blank">第一千零七十九章 寒冰王座</a></li>
                                <li><a href="/1/1186.html" title="斗破苍穹 第一千零八十章 冰尊者" target="_blank">第一千零八十章 冰尊者</a></li>
                                <li><a href="/1/1187.html" title="斗破苍穹 第一千零八十一章   再见薰儿！" target="_blank">第一千零八十一章   再见薰儿！</a></li>
                                <li><a href="/1/1188.html" title="斗破苍穹 第一千零八十二章   金色火焰" target="_blank">第一千零八十二章   金色火焰</a></li>
                                <li><a href="/1/1189.html" title="斗破苍穹 第一千零八十三章   击溃【第三更！】" target="_blank">第一千零八十三章   击溃【第三更！】</a></li>
                                <li><a href="/1/1190.html" title="斗破苍穹 第一千零八十四章   退敌【第一更！】" target="_blank">第一千零八十四章   退敌【第一更！】</a></li>
                                <li><a href="/1/1191.html" title="斗破苍穹 第一千零八十五章   封印【第二更！】" target="_blank">第一千零八十五章   封印【第二更！】</a></li>
                                <li><a href="/1/1192.html" title="斗破苍穹 第一千零八十六章   打算【第三更！】" target="_blank">第一千零八十六章   打算【第三更！】</a></li>
                                <li><a href="/1/1193.html" title="斗破苍穹 第一千零八十七章  古玉之谜【第一更！】" target="_blank">第一千零八十七章  古玉之谜【第一更！】</a></li>
                                <li><a href="/1/1194.html" title="斗破苍穹 第一千零八十八章  情迷【第二更！】" target="_blank">第一千零八十八章  情迷【第二更！】</a></li>
                                <li><a href="/1/1195.html" title="斗破苍穹 第一千零八十九章  解决魔毒斑【第三更！】" target="_blank">第一千零八十九章  解决魔毒斑【第三更！】</a></li>
                                <li><a href="/1/1196.html" title="斗破苍穹 第一千零九十章   突破【第一更！】" target="_blank">第一千零九十章   突破【第一更！】</a></li>
                                <li><a href="/1/1197.html" title="斗破苍穹 第一千零九十一章   翎泉统领【第二更！】" target="_blank">第一千零九十一章   翎泉统领【第二更！】</a></li>
                                <li><a href="/1/1198.html" title="斗破苍穹 第一千零九十二章   血玉令【第三更！】" target="_blank">第一千零九十二章   血玉令【第三更！】</a></li>
                                <li><a href="/1/1199.html" title="斗破苍穹 第一千零九十三章   不堪一击！【第四更！】" target="_blank">第一千零九十三章   不堪一击！【第四更！】</a></li>
                                <li><a href="/1/1200.html" title="斗破苍穹 第一千零九十四章    还债【第一更！】" target="_blank">第一千零九十四章    还债【第一更！】</a></li>
                                <li><a href="/1/1201.html" title="斗破苍穹 第一千零九十五章   离开【第二更！】" target="_blank">第一千零九十五章   离开【第二更！】</a></li>
                                <li><a href="/1/1202.html" title="斗破苍穹 第一千零九十六章   长老席【第三更！】" target="_blank">第一千零九十六章   长老席【第三更！】</a></li>
                                <li><a href="/1/1203.html" title="斗破苍穹 第一千零九十七章   苦修炼丹【第一更！】" target="_blank">第一千零九十七章   苦修炼丹【第一更！】</a></li>
                                <li><a href="/1/1204.html" title="斗破苍穹 第一千零九十八章   曹家【第二更！】" target="_blank">第一千零九十八章   曹家【第二更！】</a></li>
                                <li><a href="/1/1205.html" title="斗破苍穹 第一千零九十九章   打赌【第三更！】" target="_blank">第一千零九十九章   打赌【第三更！】</a></li>
                                <li><a href="/1/1206.html" title="斗破苍穹 第一千一百章  玩火【第四更！承喏完成！】" target="_blank">第一千一百章  玩火【第四更！承喏完成！】</a></li>
                                <li><a href="/1/1207.html" title="斗破苍穹 第一千一百零一章  曹家妖女【第一更！】" target="_blank">第一千一百零一章  曹家妖女【第一更！】</a></li>
                                <li><a href="/1/1208.html" title="斗破苍穹 第一千一百零二章   压力【第二更！】" target="_blank">第一千一百零二章   压力【第二更！】</a></li>
                                <li><a href="/1/1209.html" title="斗破苍穹 第一千一百零三章   灵魂境界【第三更！】" target="_blank">第一千一百零三章   灵魂境界【第三更！】</a></li>
                                <li><a href="/1/1210.html" title="斗破苍穹 第一千零八十三章 击溃" target="_blank">第一千零八十三章 击溃</a></li>
                                <li><a href="/1/1211.html" title="斗破苍穹 第一千零八十四章 退敌" target="_blank">第一千零八十四章 退敌</a></li>
                                <li><a href="/1/1212.html" title="斗破苍穹 第一千零八十五章 封印" target="_blank">第一千零八十五章 封印</a></li>
                                <li><a href="/1/1213.html" title="斗破苍穹 第一千零八十六章 打算" target="_blank">第一千零八十六章 打算</a></li>
                                <li><a href="/1/1214.html" title="斗破苍穹 第一千零八十七章 古玉之谜" target="_blank">第一千零八十七章 古玉之谜</a></li>
                                <li><a href="/1/1215.html" title="斗破苍穹 第一千零九十章 突破" target="_blank">第一千零九十章 突破</a></li>
                                <li><a href="/1/1216.html" title="斗破苍穹 第一千零九十一章 翎泉统领" target="_blank">第一千零九十一章 翎泉统领</a></li>
                                <li><a href="/1/1217.html" title="斗破苍穹 第一千零九十二章 血玉令" target="_blank">第一千零九十二章 血玉令</a></li>
                                <li><a href="/1/1218.html" title="斗破苍穹 第一千零九十三章 不堪一击！" target="_blank">第一千零九十三章 不堪一击！</a></li>
                                <li><a href="/1/1219.html" title="斗破苍穹 第一千零九十四章 还债" target="_blank">第一千零九十四章 还债</a></li>
                                <li><a href="/1/1220.html" title="斗破苍穹 第一千零九十五章 离开" target="_blank">第一千零九十五章 离开</a></li>
                                <li><a href="/1/1221.html" title="斗破苍穹 第一千零九十六章 长老席" target="_blank">第一千零九十六章 长老席</a></li>
                                <li><a href="/1/1222.html" title="斗破苍穹 第一千零九十七章 苦修炼丹" target="_blank">第一千零九十七章 苦修炼丹</a></li>
                                <li><a href="/1/1223.html" title="斗破苍穹 第一千零九十八章 曹家" target="_blank">第一千零九十八章 曹家</a></li>
                                <li><a href="/1/1224.html" title="斗破苍穹 第一千零九十九章 打赌" target="_blank">第一千零九十九章 打赌</a></li>
                                <li><a href="/1/1225.html" title="斗破苍穹 第一千一百章 玩火" target="_blank">第一千一百章 玩火</a></li>
                                <li><a href="/1/1226.html" title="斗破苍穹 第一千一百零一章 曹家妖女" target="_blank">第一千一百零一章 曹家妖女</a></li>
                                <li><a href="/1/1227.html" title="斗破苍穹 第一千一百零二章 压力" target="_blank">第一千一百零二章 压力</a></li>
                                <li><a href="/1/1228.html" title="斗破苍穹 第一千一百零三章 灵魂境界" target="_blank">第一千一百零三章 灵魂境界</a></li>
                                <li><a href="/1/1229.html" title="斗破苍穹 第一千一百零四章    赶往圣丹城！" target="_blank">第一千一百零四章    赶往圣丹城！</a></li>
                                <li><a href="/1/1230.html" title="斗破苍穹 第一千一百零五章   丹家【第二更！】" target="_blank">第一千一百零五章   丹家【第二更！】</a></li>
                                <li><a href="/1/1231.html" title="斗破苍穹 第一千一百零六章   星空夜遇【第三更！】" target="_blank">第一千一百零六章   星空夜遇【第三更！】</a></li>
                                <li><a href="/1/1232.html" title="斗破苍穹 第一千一百零五章 丹家" target="_blank">第一千一百零五章 丹家</a></li>
                                <li><a href="/1/1233.html" title="斗破苍穹 第一千一百零六章 星空夜遇" target="_blank">第一千一百零六章 星空夜遇</a></li>
                                <li><a href="/1/1234.html" title="斗破苍穹 第一千一百零七章   分塔" target="_blank">第一千一百零七章   分塔</a></li>
                                <li><a href="/1/1235.html" title="斗破苍穹 第一千一百零八章   测试" target="_blank">第一千一百零八章   测试</a></li>
                                <li><a href="/1/1236.html" title="斗破苍穹 第一千一百零九章   七品中级炼药师" target="_blank">第一千一百零九章   七品中级炼药师</a></li>
                                <li><a href="/1/1237.html" title="斗破苍穹 第一千一百一十章   教训" target="_blank">第一千一百一十章   教训</a></li>
                                <li><a href="/1/1238.html" title="斗破苍穹 第一千一百一十一章   炼药师交易会" target="_blank">第一千一百一十一章   炼药师交易会</a></li>
                                <li><a href="/1/1239.html" title="斗破苍穹 第一千一百一十二章   血精妖果" target="_blank">第一千一百一十二章   血精妖果</a></li>
                                <li><a href="/1/1240.html" title="斗破苍穹 第一千一百一十三章   铜片" target="_blank">第一千一百一十三章   铜片</a></li>
                                <li><a href="/1/1241.html" title="斗破苍穹 第一千一百一十四章    交换" target="_blank">第一千一百一十四章    交换</a></li>
                                <li><a href="/1/1242.html" title="斗破苍穹 第一千一百一十五章   玄冥宗" target="_blank">第一千一百一十五章   玄冥宗</a></li>
                                <li><a href="/1/1243.html" title="斗破苍穹 第一千一百一十六章   孕灵粉尘" target="_blank">第一千一百一十六章   孕灵粉尘</a></li>
                                <li><a href="/1/1244.html" title="斗破苍穹 第一千一百一十七章   无名口诀" target="_blank">第一千一百一十七章   无名口诀</a></li>
                                <li><a href="/1/1245.html" title="斗破苍穹 第一千一百一十八章   吸纳" target="_blank">第一千一百一十八章   吸纳</a></li>
                                <li><a href="/1/1246.html" title="斗破苍穹 第一千一百一十九章   五大家族齐聚" target="_blank">第一千一百一十九章   五大家族齐聚</a></li>
                                <li><a href="/1/1247.html" title="斗破苍穹 第一千一百二十章   考核开始！" target="_blank">第一千一百二十章   考核开始！</a></li>
                                <li><a href="/1/1248.html" title="斗破苍穹 第一千一百二十一章  灵魂测试" target="_blank">第一千一百二十一章  灵魂测试</a></li>
                                <li><a href="/1/1249.html" title="斗破苍穹 第一千一百二十二章   艳惊四座" target="_blank">第一千一百二十二章   艳惊四座</a></li>
                                <li><a href="/1/1250.html" title="斗破苍穹 第一千一百二十三章   灵魂操控" target="_blank">第一千一百二十三章   灵魂操控</a></li>
                                <li><a href="/1/1251.html" title="斗破苍穹 第一千一百二十四章   灵魂交手" target="_blank">第一千一百二十四章   灵魂交手</a></li>
                                <li><a href="/1/1252.html" title="斗破苍穹 第一千一百二十五章   偷学" target="_blank">第一千一百二十五章   偷学</a></li>
                                <li><a href="/1/1253.html" title="斗破苍穹 第一千一百二十六章   获胜" target="_blank">第一千一百二十六章   获胜</a></li>
                                <li><a href="/1/1254.html" title="斗破苍穹 第一千一百二十七章    不速之客" target="_blank">第一千一百二十七章    不速之客</a></li>
                                <li><a href="/1/1255.html" title="斗破苍穹 第一千一百二十八章   神秘黑袍人" target="_blank">第一千一百二十八章   神秘黑袍人</a></li>
                                <li><a href="/1/1256.html" title="斗破苍穹 第一千一百二十九章   慕骨老人" target="_blank">第一千一百二十九章   慕骨老人</a></li>
                                <li><a href="/1/1257.html" title="斗破苍穹 第一千一百三十章   玄空子" target="_blank">第一千一百三十章   玄空子</a></li>
                                <li><a href="/1/1258.html" title="斗破苍穹 第一千一百三十一章   宋清" target="_blank">第一千一百三十一章   宋清</a></li>
                                <li><a href="/1/1259.html" title="斗破苍穹 第一千一百三十二章  魂手印" target="_blank">第一千一百三十二章  魂手印</a></li>
                                <li><a href="/1/1260.html" title="斗破苍穹 第一千一百三十三章   丹会开始！" target="_blank">第一千一百三十三章   丹会开始！</a></li>
                                <li><a href="/1/1261.html" title="斗破苍穹 第一千一百三十四章  两大关卡" target="_blank">第一千一百三十四章  两大关卡</a></li>
                                <li><a href="/1/1262.html" title="斗破苍穹 第一千一百三十五章   过关" target="_blank">第一千一百三十五章   过关</a></li>
                                <li><a href="/1/1263.html" title="斗破苍穹 第一千一百三十六章   丹界入口" target="_blank">第一千一百三十六章   丹界入口</a></li>
                                <li><a href="/1/1264.html" title="斗破苍穹 第一千一百三十七章  千年地黄精" target="_blank">第一千一百三十七章  千年地黄精</a></li>
                                <li><a href="/1/1265.html" title="斗破苍穹 第一千一百三十八章   地心魂髓" target="_blank">第一千一百三十八章   地心魂髓</a></li>
                                <li><a href="/1/1266.html" title="斗破苍穹 第一千一百三十九章   黄衣老者" target="_blank">第一千一百三十九章   黄衣老者</a></li>
                                <li><a href="/1/1267.html" title="斗破苍穹 第一千一百四十章   万药山脉" target="_blank">第一千一百四十章   万药山脉</a></li>
                                <li><a href="/1/1268.html" title="斗破苍穹 第一千一百四十一章   再遇" target="_blank">第一千一百四十一章   再遇</a></li>
                                <li><a href="/1/1269.html" title="斗破苍穹 第一千一百四十二章   动手" target="_blank">第一千一百四十二章   动手</a></li>
                                <li><a href="/1/1270.html" title="斗破苍穹 第一千一百四十三章  下杀手" target="_blank">第一千一百四十三章  下杀手</a></li>
                                <li><a href="/1/1271.html" title="斗破苍穹 第一千一百四十四章   离去" target="_blank">第一千一百四十四章   离去</a></li>
                                <li><a href="/1/1272.html" title="斗破苍穹 第一千一百四十五章   丹灵浆" target="_blank">第一千一百四十五章   丹灵浆</a></li>
                                <li><a href="/1/1273.html" title="斗破苍穹 第一千一百四十六章  下药" target="_blank">第一千一百四十六章  下药</a></li>
                                <li><a href="/1/1274.html" title="斗破苍穹 第一千一百四十七章   杀戮" target="_blank">第一千一百四十七章   杀戮</a></li>
                                <li><a href="/1/1275.html" title="斗破苍穹 第一千一百四十八章   联手" target="_blank">第一千一百四十八章   联手</a></li>
                                <li><a href="/1/1276.html" title="斗破苍穹 第一千一百四十九章    逃命" target="_blank">第一千一百四十九章    逃命</a></li>
                                <li><a href="/1/1277.html" title="斗破苍穹 第一千一百五十章    紫研，熊战" target="_blank">第一千一百五十章    紫研，熊战</a></li>
                                <li><a href="/1/1278.html" title="斗破苍穹 第一千一百五十一章   震退【第一更！】" target="_blank">第一千一百五十一章   震退【第一更！】</a></li>
                                <li><a href="/1/1279.html" title="斗破苍穹 第一千一百五十二章   药材广场【第二更！】" target="_blank">第一千一百五十二章   药材广场【第二更！】</a></li>
                                <li><a href="/1/1280.html" title="斗破苍穹 第一千一百五十三章   调和地心魂髓【第三更！】" target="_blank">第一千一百五十三章   调和地心魂髓【第三更！】</a></li>
                                <li><a href="/1/1281.html" title="斗破苍穹 第一千一百五十四章   晋入八品！【第一更！】" target="_blank">第一千一百五十四章   晋入八品！【第一更！】</a></li>
                                <li><a href="/1/1282.html" title="斗破苍穹 第一千一百五十五章    赶往出口【第二更！】" target="_blank">第一千一百五十五章    赶往出口【第二更！】</a></li>
                                <li><a href="/1/1283.html" title="斗破苍穹 第一千一百五十六章   离开丹界【第三更！】" target="_blank">第一千一百五十六章   离开丹界【第三更！】</a></li>
                                <li><a href="/1/1284.html" title="斗破苍穹 第一千一百五十七章   重头戏【第一更！】" target="_blank">第一千一百五十七章   重头戏【第一更！】</a></li>
                                <li><a href="/1/1285.html" title="斗破苍穹 第一千一百五十八章   血妖焰火【第二更！】" target="_blank">第一千一百五十八章   血妖焰火【第二更！】</a></li>
                                <li><a href="/1/1286.html" title="斗破苍穹 第一千一百五十九章   炼丹开始【第三更！】" target="_blank">第一千一百五十九章   炼丹开始【第三更！】</a></li>
                                <li><a href="/1/1287.html" title="斗破苍穹 第一千一百六十章   丹雷屡现【第一更！】" target="_blank">第一千一百六十章   丹雷屡现【第一更！】</a></li>
                                <li><a href="/1/1288.html" title="斗破苍穹 第一千一百六十一章   强者迭出【第二更！】" target="_blank">第一千一百六十一章   强者迭出【第二更！】</a></li>
                                <li><a href="/1/1289.html" title="斗破苍穹 第一千一百六十二章   八品丹药！【第三更！】" target="_blank">第一千一百六十二章   八品丹药！【第三更！】</a></li>
                                <li><a href="/1/1290.html" title="斗破苍穹 第一千一百六十三章   三色丹雷【第一更！】" target="_blank">第一千一百六十三章   三色丹雷【第一更！】</a></li>
                                <li><a href="/1/1291.html" title="斗破苍穹 第一千一百六十四章   放手一搏【第二更！】" target="_blank">第一千一百六十四章   放手一搏【第二更！】</a></li>
                                <li><a href="/1/1292.html" title="斗破苍穹 第一千一百六十五章   升灵【第三更！】" target="_blank">第一千一百六十五章   升灵【第三更！】</a></li>
                                <li><a href="/1/1293.html" title="斗破苍穹 第一千一百六十六章  五色丹雷！【第四更！】" target="_blank">第一千一百六十六章  五色丹雷！【第四更！】</a></li>
                                <li><a href="/1/1294.html" title="斗破苍穹 第一千一百六十七章   迎接丹雷【第五更！】" target="_blank">第一千一百六十七章   迎接丹雷【第五更！】</a></li>
                                <li><a href="/1/1295.html" title="斗破苍穹 第一千一百六十八章  进化，天妖傀！【第六更！】" target="_blank">第一千一百六十八章  进化，天妖傀！【第六更！】</a></li>
                                <li><a href="/1/1296.html" title="斗破苍穹 第一千一百六十九章   丹会落幕【第七更！】" target="_blank">第一千一百六十九章   丹会落幕【第七更！】</a></li>
                                <li><a href="/1/1297.html" title="斗破苍穹 第一千一百七十章   玄衣，天雷子【第八更！】" target="_blank">第一千一百七十章   玄衣，天雷子【第八更！】</a></li>
                                <li><a href="/1/1298.html" title="斗破苍穹 第一千一百七十一章  两女对恃【第九更！】" target="_blank">第一千一百七十一章  两女对恃【第九更！】</a></li>
                                <li><a href="/1/1299.html" title="斗破苍穹 第一千一百七十二章 龙印【第十更！】" target="_blank">第一千一百七十二章 龙印【第十更！】</a></li>
                                <li><a href="/1/1300.html" title="斗破苍穹 第一千一百七十三章   星域，三千焱炎火！【第一更！】" target="_blank">第一千一百七十三章   星域，三千焱炎火！【第一更！】</a></li>
                                <li><a href="/1/1301.html" title="斗破苍穹 第一千一百七十四章   凶悍的三千焱炎火【第二更！】" target="_blank">第一千一百七十四章   凶悍的三千焱炎火【第二更！】</a></li>
                                <li><a href="/1/1302.html" title="斗破苍穹 第一千一百七十五章   破封【第三更！】" target="_blank">第一千一百七十五章   破封【第三更！】</a></li>
                                <li><a href="/1/1303.html" title="斗破苍穹 第一千一百七十六章 魂殿援手 【第一更！】" target="_blank">第一千一百七十六章 魂殿援手 【第一更！】</a></li>
                                <li><a href="/1/1304.html" title="斗破苍穹 第一千一百七十七章   激战【第二更！】" target="_blank">第一千一百七十七章   激战【第二更！】</a></li>
                                <li><a href="/1/1305.html" title="斗破苍穹 第一千一百七十八章  动手【第三更！】" target="_blank">第一千一百七十八章  动手【第三更！】</a></li>
                                <li><a href="/1/1306.html" title="斗破苍穹 第一千一百七十九章   符印 【第四更！】" target="_blank">第一千一百七十九章   符印 【第四更！】</a></li>
                                <li><a href="/1/1307.html" title="斗破苍穹 第一千一百八十章   灵魂交战【第一更！】" target="_blank">第一千一百八十章   灵魂交战【第一更！】</a></li>
                                <li><a href="/1/1308.html" title="斗破苍穹 第一千一百八十一章   爆发【第二更！】" target="_blank">第一千一百八十一章   爆发【第二更！】</a></li>
                                <li><a href="/1/1309.html" title="斗破苍穹 第一千一百八十二章   僵持【第三更！】" target="_blank">第一千一百八十二章   僵持【第三更！】</a></li>
                                <li><a href="/1/1310.html" title="斗破苍穹 第一千一百八十三章    降服【第一更！】" target="_blank">第一千一百八十三章    降服【第一更！】</a></li>
                                <li><a href="/1/1311.html" title="斗破苍穹 第一千一百八十四章   吞噬异火，九星斗宗！【第二更！】" target="_blank">第一千一百八十四章   吞噬异火，九星斗宗！【第二更！】</a></li>
                                <li><a href="/1/1312.html" title="斗破苍穹 第一千一百八十五章   火雷子【第三更！】" target="_blank">第一千一百八十五章   火雷子【第三更！】</a></li>
                                <li><a href="/1/1313.html" title="斗破苍穹 第一千一百八十六章   情报【第一更！】" target="_blank">第一千一百八十六章   情报【第一更！】</a></li>
                                <li><a href="/1/1314.html" title="斗破苍穹 第一千一百八十七章 茯苓青丹【第二更！】" target="_blank">第一千一百八十七章 茯苓青丹【第二更！】</a></li>
                                <li><a href="/1/1315.html" title="斗破苍穹 第一千一百八十八章  易尘【第三更！】" target="_blank">第一千一百八十八章  易尘【第三更！】</a></li>
                                <li><a href="/1/1316.html" title="斗破苍穹 第一千一百八十九章   交手【第一更！】" target="_blank">第一千一百八十九章   交手【第一更！】</a></li>
                                <li><a href="/1/1317.html" title="斗破苍穹 第一千一百九十章  承让【第二更！】" target="_blank">第一千一百九十章  承让【第二更！】</a></li>
                                <li><a href="/1/1318.html" title="斗破苍穹 第一千一百九十一章   情报到手【第三更！】" target="_blank">第一千一百九十一章   情报到手【第三更！】</a></li>
                                <li><a href="/1/1319.html" title="斗破苍穹 第一千一百九十二章  亡魂山脉【第一更！】" target="_blank">第一千一百九十二章  亡魂山脉【第一更！】</a></li>
                                <li><a href="/1/1320.html" title="斗破苍穹 第一千一百九十三章  万事具备【第二更！】" target="_blank">第一千一百九十三章  万事具备【第二更！】</a></li>
                                <li><a href="/1/1321.html" title="斗破苍穹 第一千一百九十四章   营救行动【第三更！】" target="_blank">第一千一百九十四章   营救行动【第三更！】</a></li>
                                <li><a href="/1/1322.html" title="斗破苍穹 第一千一百九十五章   噬石魔蚁【第一更！】" target="_blank">第一千一百九十五章   噬石魔蚁【第一更！】</a></li>
                                <li><a href="/1/1323.html" title="斗破苍穹 第一千一百九十六章   巨殿【第二更！】" target="_blank">第一千一百九十六章   巨殿【第二更！】</a></li>
                                <li><a href="/1/1324.html" title="斗破苍穹 第一千一百九十七章   大战【第三更！】" target="_blank">第一千一百九十七章   大战【第三更！】</a></li>
                                <li><a href="/1/1325.html" title="斗破苍穹 第一千一百九十八章   杀戮【第一更！】" target="_blank">第一千一百九十八章   杀戮【第一更！】</a></li>
                                <li><a href="/1/1326.html" title="斗破苍穹 第一千一百九十九章   摘星老鬼【第二更！】" target="_blank">第一千一百九十九章   摘星老鬼【第二更！】</a></li>
                                <li><a href="/1/1327.html" title="斗破苍穹 第一千两百章    戏耍【第三更！】" target="_blank">第一千两百章    戏耍【第三更！】</a></li>
                                <li><a href="/1/1328.html" title="斗破苍穹 第一千一百五十一章 震退" target="_blank">第一千一百五十一章 震退</a></li>
                                <li><a href="/1/1329.html" title="斗破苍穹 第一千一百五十二章 药材广场" target="_blank">第一千一百五十二章 药材广场</a></li>
                                <li><a href="/1/1330.html" title="斗破苍穹 第一千一百五十三章 调和地心魂髓" target="_blank">第一千一百五十三章 调和地心魂髓</a></li>
                                <li><a href="/1/1331.html" title="斗破苍穹 第一千一百五十四章 晋入八品！" target="_blank">第一千一百五十四章 晋入八品！</a></li>
                                <li><a href="/1/1332.html" title="斗破苍穹 第一千一百五十五章 赶往出口" target="_blank">第一千一百五十五章 赶往出口</a></li>
                                <li><a href="/1/1333.html" title="斗破苍穹 第一千一百五十六章 离开丹界" target="_blank">第一千一百五十六章 离开丹界</a></li>
                                <li><a href="/1/1334.html" title="斗破苍穹 第一千一百五十七章 重头戏" target="_blank">第一千一百五十七章 重头戏</a></li>
                                <li><a href="/1/1335.html" title="斗破苍穹 第一千一百五十八章 血妖焰火" target="_blank">第一千一百五十八章 血妖焰火</a></li>
                                <li><a href="/1/1336.html" title="斗破苍穹 第一千一百五十九章 炼丹开始" target="_blank">第一千一百五十九章 炼丹开始</a></li>
                                <li><a href="/1/1337.html" title="斗破苍穹 第一千一百六十章 丹雷屡现" target="_blank">第一千一百六十章 丹雷屡现</a></li>
                                <li><a href="/1/1338.html" title="斗破苍穹 第一千一百六十一章 强者迭出" target="_blank">第一千一百六十一章 强者迭出</a></li>
                                <li><a href="/1/1339.html" title="斗破苍穹 第一千一百六十二章 八品丹药！" target="_blank">第一千一百六十二章 八品丹药！</a></li>
                                <li><a href="/1/1340.html" title="斗破苍穹 第一千一百六十三章 三色丹雷" target="_blank">第一千一百六十三章 三色丹雷</a></li>
                                <li><a href="/1/1341.html" title="斗破苍穹 第一千一百六十四章 放手一搏" target="_blank">第一千一百六十四章 放手一搏</a></li>
                                <li><a href="/1/1342.html" title="斗破苍穹 第一千一百六十五章 升灵" target="_blank">第一千一百六十五章 升灵</a></li>
                                <li><a href="/1/1343.html" title="斗破苍穹 第一千一百六十六章 五色丹雷！" target="_blank">第一千一百六十六章 五色丹雷！</a></li>
                                <li><a href="/1/1344.html" title="斗破苍穹 第一千一百六十七章 迎接丹雷" target="_blank">第一千一百六十七章 迎接丹雷</a></li>
                                <li><a href="/1/1345.html" title="斗破苍穹 第一千一百六十八章 进化，天妖傀！" target="_blank">第一千一百六十八章 进化，天妖傀！</a></li>
                                <li><a href="/1/1346.html" title="斗破苍穹 第一千一百六十九章 丹会落幕" target="_blank">第一千一百六十九章 丹会落幕</a></li>
                                <li><a href="/1/1347.html" title="斗破苍穹 第一千一百七十章 玄衣，天雷子" target="_blank">第一千一百七十章 玄衣，天雷子</a></li>
                                <li><a href="/1/1348.html" title="斗破苍穹 第一千一百七十一章 两女对恃" target="_blank">第一千一百七十一章 两女对恃</a></li>
                                <li><a href="/1/1349.html" title="斗破苍穹 第一千一百七十二章 龙印" target="_blank">第一千一百七十二章 龙印</a></li>
                                <li><a href="/1/1350.html" title="斗破苍穹 第一千一百七十三章 星域，三千焱炎火！" target="_blank">第一千一百七十三章 星域，三千焱炎火！</a></li>
                                <li><a href="/1/1351.html" title="斗破苍穹 第一千一百七十四章 凶悍的三千焱炎火" target="_blank">第一千一百七十四章 凶悍的三千焱炎火</a></li>
                                <li><a href="/1/1352.html" title="斗破苍穹 第一千一百七十五章 破封" target="_blank">第一千一百七十五章 破封</a></li>
                                <li><a href="/1/1353.html" title="斗破苍穹 第一千一百七十六章 魂殿援手" target="_blank">第一千一百七十六章 魂殿援手</a></li>
                                <li><a href="/1/1354.html" title="斗破苍穹 第一千一百七十七章 激战" target="_blank">第一千一百七十七章 激战</a></li>
                                <li><a href="/1/1355.html" title="斗破苍穹 第一千一百七十八章 动手" target="_blank">第一千一百七十八章 动手</a></li>
                                <li><a href="/1/1356.html" title="斗破苍穹 第一千一百七十九章 符印" target="_blank">第一千一百七十九章 符印</a></li>
                                <li><a href="/1/1357.html" title="斗破苍穹 第一千一百八十章 灵魂交战" target="_blank">第一千一百八十章 灵魂交战</a></li>
                                <li><a href="/1/1358.html" title="斗破苍穹 第一千一百八十一章 爆发" target="_blank">第一千一百八十一章 爆发</a></li>
                                <li><a href="/1/1359.html" title="斗破苍穹 第一千一百八十二章 僵持" target="_blank">第一千一百八十二章 僵持</a></li>
                                <li><a href="/1/1360.html" title="斗破苍穹 第一千一百八十三章 降服" target="_blank">第一千一百八十三章 降服</a></li>
                                <li><a href="/1/1361.html" title="斗破苍穹 第一千一百八十四章 吞噬异火，九星斗宗！" target="_blank">第一千一百八十四章 吞噬异火，九星斗宗！</a></li>
                                <li><a href="/1/1362.html" title="斗破苍穹 第一千一百八十五章 火雷子" target="_blank">第一千一百八十五章 火雷子</a></li>
                                <li><a href="/1/1363.html" title="斗破苍穹 第一千一百八十六章 情报" target="_blank">第一千一百八十六章 情报</a></li>
                                <li><a href="/1/1364.html" title="斗破苍穹 第一千一百八十七章 茯苓青丹" target="_blank">第一千一百八十七章 茯苓青丹</a></li>
                                <li><a href="/1/1365.html" title="斗破苍穹 第一千一百八十八章 易尘" target="_blank">第一千一百八十八章 易尘</a></li>
                                <li><a href="/1/1366.html" title="斗破苍穹 第一千一百八十九章 交手" target="_blank">第一千一百八十九章 交手</a></li>
                                <li><a href="/1/1367.html" title="斗破苍穹 第一千一百九十章 承让" target="_blank">第一千一百九十章 承让</a></li>
                                <li><a href="/1/1368.html" title="斗破苍穹 第一千一百九十一章 情报到手" target="_blank">第一千一百九十一章 情报到手</a></li>
                                <li><a href="/1/1369.html" title="斗破苍穹 第一千一百九十二章 亡魂山脉" target="_blank">第一千一百九十二章 亡魂山脉</a></li>
                                <li><a href="/1/1370.html" title="斗破苍穹 第一千一百九十三章 万事具备" target="_blank">第一千一百九十三章 万事具备</a></li>
                                <li><a href="/1/1371.html" title="斗破苍穹 第一千一百九十四章 营救行动" target="_blank">第一千一百九十四章 营救行动</a></li>
                                <li><a href="/1/1372.html" title="斗破苍穹 第一千一百九十五章 噬石魔蚁" target="_blank">第一千一百九十五章 噬石魔蚁</a></li>
                                <li><a href="/1/1373.html" title="斗破苍穹 第一千一百九十六章 巨殿" target="_blank">第一千一百九十六章 巨殿</a></li>
                                <li><a href="/1/1374.html" title="斗破苍穹 第一千一百九十七章 大战" target="_blank">第一千一百九十七章 大战</a></li>
                                <li><a href="/1/1375.html" title="斗破苍穹 第一千一百九十八章 杀戮" target="_blank">第一千一百九十八章 杀戮</a></li>
                                <li><a href="/1/1376.html" title="斗破苍穹 第一千一百九十九章 摘星老鬼" target="_blank">第一千一百九十九章 摘星老鬼</a></li>
                                <li><a href="/1/1377.html" title="斗破苍穹 第一千两百章 戏耍" target="_blank">第一千两百章 戏耍</a></li>
                                <li><a href="/1/1378.html" title="斗破苍穹 第一千两百零一章   局势" target="_blank">第一千两百零一章   局势</a></li>
                                <li><a href="/1/1379.html" title="斗破苍穹 第一千两百零二章   拖延" target="_blank">第一千两百零二章   拖延</a></li>
                                <li><a href="/1/1380.html" title="斗破苍穹 第一千两百零三章   两败俱伤" target="_blank">第一千两百零三章   两败俱伤</a></li>
                                <li><a href="/1/1381.html" title="斗破苍穹 第一千两百零四章  神秘之人" target="_blank">第一千两百零四章  神秘之人</a></li>
                                <li><a href="/1/1382.html" title="斗破苍穹 第一千两百零五章   重伤" target="_blank">第一千两百零五章   重伤</a></li>
                                <li><a href="/1/1383.html" title="斗破苍穹 第一千两百零六章    星陨阁" target="_blank">第一千两百零六章    星陨阁</a></li>
                                <li><a href="/1/1384.html" title="斗破苍穹 第一千两百零七章 时间飞逝" target="_blank">第一千两百零七章 时间飞逝</a></li>
                                <li><a href="/1/1385.html" title="斗破苍穹 第一千两百零八章  晋阶，斗尊！" target="_blank">第一千两百零八章  晋阶，斗尊！</a></li>
                                <li><a href="/1/1386.html" title="斗破苍穹 第一千两百零九章   苏醒" target="_blank">第一千两百零九章   苏醒</a></li>
                                <li><a href="/1/1387.html" title="斗破苍穹 第一千两百一十章   远古遗迹" target="_blank">第一千两百一十章   远古遗迹</a></li>
                                <li><a href="/1/1388.html" title="斗破苍穹 第一千两百一十一章 兽域" target="_blank">第一千两百一十一章 兽域</a></li>
                                <li><a href="/1/1389.html" title="斗破苍穹 第一千两百一十二章  骸骨山脉" target="_blank">第一千两百一十二章  骸骨山脉</a></li>
                                <li><a href="/1/1390.html" title="斗破苍穹 第一千两百一十三章   找场子" target="_blank">第一千两百一十三章   找场子</a></li>
                                <li><a href="/1/1391.html" title="斗破苍穹 第一千两百一十四章   滚下去" target="_blank">第一千两百一十四章   滚下去</a></li>
                                <li><a href="/1/1392.html" title="斗破苍穹 第一千两百一十五章   空间封印" target="_blank">第一千两百一十五章   空间封印</a></li>
                                <li><a href="/1/1393.html" title="斗破苍穹 第一千两百一十六章   黑影人" target="_blank">第一千两百一十六章   黑影人</a></li>
                                <li><a href="/1/1394.html" title="斗破苍穹 第一千两百一十七章  遗迹开启" target="_blank">第一千两百一十七章  遗迹开启</a></li>
                                <li><a href="/1/1395.html" title="斗破苍穹 第一千两百一十八章   对头同现" target="_blank">第一千两百一十八章   对头同现</a></li>
                                <li><a href="/1/1396.html" title="斗破苍穹 第一千两百一十九章   进入遗迹" target="_blank">第一千两百一十九章   进入遗迹</a></li>
                                <li><a href="/1/1397.html" title="斗破苍穹 第一千两百二十章  另有玄机的火道" target="_blank">第一千两百二十章  另有玄机的火道</a></li>
                                <li><a href="/1/1398.html" title="斗破苍穹 第一千两百二十一章   收服" target="_blank">第一千两百二十一章   收服</a></li>
                                <li><a href="/1/1399.html" title="斗破苍穹 第一千两百二十二章   远古森林" target="_blank">第一千两百二十二章   远古森林</a></li>
                                <li><a href="/1/1400.html" title="斗破苍穹 第一千两百二十三章   魂婴妖树" target="_blank">第一千两百二十三章   魂婴妖树</a></li>
                                <li><a href="/1/1401.html" title="斗破苍穹 第一千两百二十四章  龙凰本源果" target="_blank">第一千两百二十四章  龙凰本源果</a></li>
                                <li><a href="/1/1402.html" title="斗破苍穹 第一千两百二十五章   凰轩【第一更！】" target="_blank">第一千两百二十五章   凰轩【第一更！】</a></li>
                                <li><a href="/1/1403.html" title="斗破苍穹 第一千两百二十六章   天凰祖魂【第二更！】" target="_blank">第一千两百二十六章   天凰祖魂【第二更！】</a></li>
                                <li><a href="/1/1404.html" title="斗破苍穹 第一千两百二十七章  祖魂比拼【第三更！】" target="_blank">第一千两百二十七章  祖魂比拼【第三更！】</a></li>
                                <li><a href="/1/1405.html" title="斗破苍穹 第一千两百二十五章 凰轩" target="_blank">第一千两百二十五章 凰轩</a></li>
                                <li><a href="/1/1406.html" title="斗破苍穹 第一千两百二十六章 天凰祖魂" target="_blank">第一千两百二十六章 天凰祖魂</a></li>
                                <li><a href="/1/1407.html" title="斗破苍穹 第一千两百二十七章 祖魂比拼" target="_blank">第一千两百二十七章 祖魂比拼</a></li>
                                <li><a href="/1/1408.html" title="斗破苍穹 恭喜斗破成为起点第一本高订达到五万的书。" target="_blank">恭喜斗破成为起点第一本高订达到五万的书。</a></li>
                                <li><a href="/1/1409.html" title="斗破苍穹 第一千两百二十八章  远古丹药" target="_blank">第一千两百二十八章  远古丹药</a></li>
                                <li><a href="/1/1410.html" title="斗破苍穹 第一千两百二十九章   勾引丹兽" target="_blank">第一千两百二十九章   勾引丹兽</a></li>
                                <li><a href="/1/1411.html" title="斗破苍穹 第一千两百三十章 青鳞？" target="_blank">第一千两百三十章 青鳞？</a></li>
                                <li><a href="/1/1412.html" title="斗破苍穹 第一千两百三十一章  故人相见" target="_blank">第一千两百三十一章  故人相见</a></li>
                                <li><a href="/1/1413.html" title="斗破苍穹 第一千两百三十二章  恐怖的碧蛇三花瞳" target="_blank">第一千两百三十二章  恐怖的碧蛇三花瞳</a></li>
                                <li><a href="/1/1414.html" title="斗破苍穹 第一千两百三十三章   主殿" target="_blank">第一千两百三十三章   主殿</a></li>
                                <li><a href="/1/1415.html" title="斗破苍穹 第一千两百三十四章   封印消失" target="_blank">第一千两百三十四章   封印消失</a></li>
                                <li><a href="/1/1416.html" title="斗破苍穹 第一千两百三十五章   混乱" target="_blank">第一千两百三十五章   混乱</a></li>
                                <li><a href="/1/1417.html" title="斗破苍穹 第一千两百三十六章  争夺远古卷轴" target="_blank">第一千两百三十六章  争夺远古卷轴</a></li>
                                <li><a href="/1/1418.html" title="斗破苍穹 第一千两百三十七章  斩杀" target="_blank">第一千两百三十七章  斩杀</a></li>
                                <li><a href="/1/1419.html" title="斗破苍穹 第一千两百三十八章  斗圣骨骸" target="_blank">第一千两百三十八章  斗圣骨骸</a></li>
                                <li><a href="/1/1420.html" title="斗破苍穹 第一千两百三十九章   联手" target="_blank">第一千两百三十九章   联手</a></li>
                                <li><a href="/1/1421.html" title="斗破苍穹 第一千两百四十章   大天造化掌" target="_blank">第一千两百四十章   大天造化掌</a></li>
                                <li><a href="/1/1422.html" title="斗破苍穹 第一千两百四十一章   争抢骸骨" target="_blank">第一千两百四十一章   争抢骸骨</a></li>
                                <li><a href="/1/1423.html" title="斗破苍穹 第一千两百四十二章   收集骨骸" target="_blank">第一千两百四十二章   收集骨骸</a></li>
                                <li><a href="/1/1424.html" title="斗破苍穹 第一千两百四十三章   各方插手" target="_blank">第一千两百四十三章   各方插手</a></li>
                                <li><a href="/1/1425.html" title="斗破苍穹 第一千两百四十四章   四印叠加【第一更！】" target="_blank">第一千两百四十四章   四印叠加【第一更！】</a></li>
                                <li><a href="/1/1426.html" title="斗破苍穹 第一千两百四十五章   血战【第二更！】" target="_blank">第一千两百四十五章   血战【第二更！】</a></li>
                                <li><a href="/1/1427.html" title="斗破苍穹 第一千两百四十六章   援手【第三更！】" target="_blank">第一千两百四十六章   援手【第三更！】</a></li>
                                <li><a href="/1/1428.html" title="斗破苍穹 第一千两百四十七章   黑擎【第一更！】" target="_blank">第一千两百四十七章   黑擎【第一更！】</a></li>
                                <li><a href="/1/1429.html" title="斗破苍穹 第一千两百四十八章  分别【第二更！】" target="_blank">第一千两百四十八章  分别【第二更！】</a></li>
                                <li><a href="/1/1430.html" title="斗破苍穹 第一千两百四十九章  神秘纹身【第三更！】" target="_blank">第一千两百四十九章  神秘纹身【第三更！】</a></li>
                                <li><a href="/1/1431.html" title="斗破苍穹 第一千两百五十章   远古天蛇【第一更！】" target="_blank">第一千两百五十章   远古天蛇【第一更！】</a></li>
                                <li><a href="/1/1432.html" title="斗破苍穹 第一千两百五十一章  天阶斗技【第二更！】" target="_blank">第一千两百五十一章  天阶斗技【第二更！】</a></li>
                                <li><a href="/1/1433.html" title="斗破苍穹 第一千两百五十二章   造化圣者【第三更！】" target="_blank">第一千两百五十二章   造化圣者【第三更！】</a></li>
                                <li><a href="/1/1434.html" title="斗破苍穹 第一千两百五十三章    完美躯体【第一更！】" target="_blank">第一千两百五十三章    完美躯体【第一更！】</a></li>
                                <li><a href="/1/1435.html" title="斗破苍穹 第一千两百五十四章   斗圣骨髓【第二更！】" target="_blank">第一千两百五十四章   斗圣骨髓【第二更！】</a></li>
                                <li><a href="/1/1436.html" title="斗破苍穹 第一千两百五十五章   大敌来临【第三更！】" target="_blank">第一千两百五十五章   大敌来临【第三更！】</a></li>
                                <li><a href="/1/1437.html" title="斗破苍穹 第一千两百四十四章 四印叠加" target="_blank">第一千两百四十四章 四印叠加</a></li>
                                <li><a href="/1/1438.html" title="斗破苍穹 第一千两百四十五章 血战" target="_blank">第一千两百四十五章 血战</a></li>
                                <li><a href="/1/1439.html" title="斗破苍穹 第一千两百四十六章 援手" target="_blank">第一千两百四十六章 援手</a></li>
                                <li><a href="/1/1440.html" title="斗破苍穹 第一千两百四十七章 黑擎" target="_blank">第一千两百四十七章 黑擎</a></li>
                                <li><a href="/1/1441.html" title="斗破苍穹 第一千两百四十八章 分别" target="_blank">第一千两百四十八章 分别</a></li>
                                <li><a href="/1/1442.html" title="斗破苍穹 第一千两百四十九章 神秘纹身" target="_blank">第一千两百四十九章 神秘纹身</a></li>
                                <li><a href="/1/1443.html" title="斗破苍穹 第一千两百五十章 远古天蛇" target="_blank">第一千两百五十章 远古天蛇</a></li>
                                <li><a href="/1/1444.html" title="斗破苍穹 第一千两百五十一章 天阶斗技" target="_blank">第一千两百五十一章 天阶斗技</a></li>
                                <li><a href="/1/1445.html" title="斗破苍穹 第一千两百五十二章 造化圣者" target="_blank">第一千两百五十二章 造化圣者</a></li>
                                <li><a href="/1/1446.html" title="斗破苍穹 第一千两百五十三章 完美躯体" target="_blank">第一千两百五十三章 完美躯体</a></li>
                                <li><a href="/1/1447.html" title="斗破苍穹 第一千两百五十四章 斗圣骨髓" target="_blank">第一千两百五十四章 斗圣骨髓</a></li>
                                <li><a href="/1/1448.html" title="斗破苍穹 第一千两百五十五章 大敌来临" target="_blank">第一千两百五十五章 大敌来临</a></li>
                                <li><a href="/1/1449.html" title="斗破苍穹 第一千两百五十六章   混战" target="_blank">第一千两百五十六章   混战</a></li>
                                <li><a href="/1/1450.html" title="斗破苍穹 第一千两百五十七章   施展" target="_blank">第一千两百五十七章   施展</a></li>
                                <li><a href="/1/1451.html" title="斗破苍穹 第一千两百五十八章  凄惨下场" target="_blank">第一千两百五十八章  凄惨下场</a></li>
                                <li><a href="/1/1452.html" title="斗破苍穹 第一千两百五十九章   大展神威" target="_blank">第一千两百五十九章   大展神威</a></li>
                                <li><a href="/1/1453.html" title="斗破苍穹 第一千两百六十章   半圣" target="_blank">第一千两百六十章   半圣</a></li>
                                <li><a href="/1/1454.html" title="斗破苍穹 第一千两百六十一章   药圣，药尘！" target="_blank">第一千两百六十一章   药圣，药尘！</a></li>
                                <li><a href="/1/1455.html" title="斗破苍穹 第一千两百六十二章    熟人再见" target="_blank">第一千两百六十二章    熟人再见</a></li>
                                <li><a href="/1/1456.html" title="斗破苍穹 第一千两百六十三章 际遇" target="_blank">第一千两百六十三章 际遇</a></li>
                                <li><a href="/1/1457.html" title="斗破苍穹 第一千两百六十四章   赶往花宗" target="_blank">第一千两百六十四章   赶往花宗</a></li>
                                <li><a href="/1/1458.html" title="斗破苍穹 第一千两百六十五章   再见云韵" target="_blank">第一千两百六十五章   再见云韵</a></li>
                                <li><a href="/1/1459.html" title="斗破苍穹 第一千两百六十六章    妖花邪君" target="_blank">第一千两百六十六章    妖花邪君</a></li>
                                <li><a href="/1/1460.html" title="斗破苍穹 第一千两百六十七章   气化天地" target="_blank">第一千两百六十七章   气化天地</a></li>
                                <li><a href="/1/1461.html" title="斗破苍穹 第一千两百六十八章   宗主之位" target="_blank">第一千两百六十八章   宗主之位</a></li>
                                <li><a href="/1/1462.html" title="斗破苍穹 第一千两百六十九章   炼化" target="_blank">第一千两百六十九章   炼化</a></li>
                                <li><a href="/1/1463.html" title="斗破苍穹 第一千两百七十章   天地异象" target="_blank">第一千两百七十章   天地异象</a></li>
                                <li><a href="/1/1464.html" title="斗破苍穹 第一千两百七十一章   准天阶功法" target="_blank">第一千两百七十一章   准天阶功法</a></li>
                                <li><a href="/1/1465.html" title="斗破苍穹 第一千两百七十二章  撕裂封印" target="_blank">第一千两百七十二章  撕裂封印</a></li>
                                <li><a href="/1/1466.html" title="斗破苍穹 第一千两百七十三章   堵截" target="_blank">第一千两百七十三章   堵截</a></li>
                                <li><a href="/1/1467.html" title="斗破苍穹 第一千两百七十四章 　　激战" target="_blank">第一千两百七十四章 　　激战</a></li>
                                <li><a href="/1/1468.html" title="斗破苍穹 第一千两百七十五章    功法显威" target="_blank">第一千两百七十五章    功法显威</a></li>
                                <li><a href="/1/1469.html" title="斗破苍穹 第一千两百七十六章 以一敌三" target="_blank">第一千两百七十六章 以一敌三</a></li>
                                <li><a href="/1/1470.html" title="斗破苍穹 第一千两百七十七章   轰飞" target="_blank">第一千两百七十七章   轰飞</a></li>
                                <li><a href="/1/1471.html" title="斗破苍穹 第一千两百七十八章   古龙岛" target="_blank">第一千两百七十八章   古龙岛</a></li>
                                <li><a href="/1/1472.html" title="斗破苍穹 第一千两百七十九章   分裂的太虚古龙一族" target="_blank">第一千两百七十九章   分裂的太虚古龙一族</a></li>
                                <li><a href="/1/1473.html" title="斗破苍穹 第一千两百八十章  动手" target="_blank">第一千两百八十章  动手</a></li>
                                <li><a href="/1/1474.html" title="斗破苍穹 第一千两百八十一章   炼化龙凰晶层" target="_blank">第一千两百八十一章   炼化龙凰晶层</a></li>
                                <li><a href="/1/1475.html" title="斗破苍穹 第一千两百八十二章   混乱" target="_blank">第一千两百八十二章   混乱</a></li>
                                <li><a href="/1/1476.html" title="斗破苍穹 第一千两百八十三章   苏醒" target="_blank">第一千两百八十三章   苏醒</a></li>
                                <li><a href="/1/1477.html" title="斗破苍穹 第一千两百八十五章   龙皇，紫研" target="_blank">第一千两百八十五章   龙皇，紫研</a></li>
                                <li><a href="/1/1478.html" title="斗破苍穹 第一千两百八十五章   龙凰古甲" target="_blank">第一千两百八十五章   龙凰古甲</a></li>
                                <li><a href="/1/1479.html" title="斗破苍穹 第一千两百八十六章   虚空雷池" target="_blank">第一千两百八十六章   虚空雷池</a></li>
                                <li><a href="/1/1480.html" title="斗破苍穹 第一千两百八十七章   晋级五星" target="_blank">第一千两百八十七章   晋级五星</a></li>
                                <li><a href="/1/1481.html" title="斗破苍穹 第一千两百八十八章   邙姓老者" target="_blank">第一千两百八十八章   邙姓老者</a></li>
                                <li><a href="/1/1482.html" title="斗破苍穹 第一千两百八十九章  离开龙岛" target="_blank">第一千两百八十九章  离开龙岛</a></li>
                                <li><a href="/1/1483.html" title="斗破苍穹 第一千两百九十章   远古八族" target="_blank">第一千两百九十章   远古八族</a></li>
                                <li><a href="/1/1484.html" title="斗破苍穹 第一千两百九十一章   玉贴" target="_blank">第一千两百九十一章   玉贴</a></li>
                                <li><a href="/1/1485.html" title="斗破苍穹 第一千两百九十二章  太一魂决" target="_blank">第一千两百九十二章  太一魂决</a></li>
                                <li><a href="/1/1486.html" title="斗破苍穹 第一千两百九十三章  赶往东域" target="_blank">第一千两百九十三章  赶往东域</a></li>
                                <li><a href="/1/1487.html" title="斗破苍穹 第一千两百九十四章   冤家路窄" target="_blank">第一千两百九十四章   冤家路窄</a></li>
                                <li><a href="/1/1488.html" title="斗破苍穹 第一千两百九十五章   喜欢" target="_blank">第一千两百九十五章   喜欢</a></li>
                                <li><a href="/1/1489.html" title="斗破苍穹 第一千两百九十六章   八大统领而，四大都统" target="_blank">第一千两百九十六章   八大统领而，四大都统</a></li>
                                <li><a href="/1/1490.html" title="斗破苍穹 第一千两百九十六章 八大统领，四大都统" target="_blank">第一千两百九十六章 八大统领，四大都统</a></li>
                                <li><a href="/1/1491.html" title="斗破苍穹 第一千两百九十七章   三统领杨皓" target="_blank">第一千两百九十七章   三统领杨皓</a></li>
                                <li><a href="/1/1492.html" title="斗破苍穹 第一千两百九十八章   炎族" target="_blank">第一千两百九十八章   炎族</a></li>
                                <li><a href="/1/1493.html" title="斗破苍穹 第一千两百九十九章   魂崖" target="_blank">第一千两百九十九章   魂崖</a></li>
                                <li><a href="/1/1494.html" title="斗破苍穹 第一千三百章   古界开启" target="_blank">第一千三百章   古界开启</a></li>
                                <li><a href="/1/1495.html" title="斗破苍穹 第一千三百零一章  天墓 【第一更！】" target="_blank">第一千三百零一章  天墓 【第一更！】</a></li>
                                <li><a href="/1/1496.html" title="斗破苍穹 第一千三百零二章   古真【第二更！】" target="_blank">第一千三百零二章   古真【第二更！】</a></li>
                                <li><a href="/1/1497.html" title="斗破苍穹 第一千三百零三章   下马威【第三更！】" target="_blank">第一千三百零三章   下马威【第三更！】</a></li>
                                <li><a href="/1/1498.html" title="斗破苍穹 第一千三百零四章   修罗都统【第一更！】" target="_blank">第一千三百零四章   修罗都统【第一更！】</a></li>
                                <li><a href="/1/1499.html" title="斗破苍穹 第一千三百零五章   邙天尺【第二更！】" target="_blank">第一千三百零五章   邙天尺【第二更！】</a></li>
                                <li><a href="/1/1500.html" title="斗破苍穹 第一千三百零六章   仪式开始【第三更！】" target="_blank">第一千三百零六章   仪式开始【第三更！】</a></li>
                                <li><a href="/1/1501.html" title="斗破苍穹 第一千三百零七章   血脉等级，族纹！【第一更！】" target="_blank">第一千三百零七章   血脉等级，族纹！【第一更！】</a></li>
                                <li><a href="/1/1502.html" title="斗破苍穹 第一千三百零八章  挑战【第二更！】" target="_blank">第一千三百零八章  挑战【第二更！】</a></li>
                                <li><a href="/1/1503.html" title="斗破苍穹 第一千三百零九章   劲敌！【第三更！】" target="_blank">第一千三百零九章   劲敌！【第三更！】</a></li>
                                <li><a href="/1/1504.html" title="斗破苍穹 第一千三百一十章   巅峰交手【第一更！】" target="_blank">第一千三百一十章   巅峰交手【第一更！】</a></li>
                                <li><a href="/1/1505.html" title="斗破苍穹 第一千三百一十一章   大寂灭指【第二更！】" target="_blank">第一千三百一十一章   大寂灭指【第二更！】</a></li>
                                <li><a href="/1/1506.html" title="斗破苍穹 第一千三百一十二章   落幕！【第三更！】" target="_blank">第一千三百一十二章   落幕！【第三更！】</a></li>
                                <li><a href="/1/1507.html" title="斗破苍穹 第一千三百一十三章  胜！【第一更！】" target="_blank">第一千三百一十三章  胜！【第一更！】</a></li>
                                <li><a href="/1/1508.html" title="斗破苍穹 第一千三百一十四章  神品血脉【第二更！】" target="_blank">第一千三百一十四章  神品血脉【第二更！】</a></li>
                                <li><a href="/1/1509.html" title="斗破苍穹 第一千三百一十五章   七彩族纹【第三更！】" target="_blank">第一千三百一十五章   七彩族纹【第三更！】</a></li>
                                <li><a href="/1/1510.html" title="斗破苍穹 第一千三百一十六章   相见【第一更！】" target="_blank">第一千三百一十六章   相见【第一更！】</a></li>
                                <li><a href="/1/1511.html" title="斗破苍穹 第一千三百一十七章   交谈【第二更！】" target="_blank">第一千三百一十七章   交谈【第二更！】</a></li>
                                <li><a href="/1/1512.html" title="斗破苍穹 第一千三百一十八章   天墓开启【第三更！】" target="_blank">第一千三百一十八章   天墓开启【第三更！】</a></li>
                                <li><a href="/1/1513.html" title="斗破苍穹 第一千三百一十九章   进入天墓【第一更！】" target="_blank">第一千三百一十九章   进入天墓【第一更！】</a></li>
                                <li><a href="/1/1514.html" title="斗破苍穹 第一千三百二十章   枯燥的修行【第二更！】" target="_blank">第一千三百二十章   枯燥的修行【第二更！】</a></li>
                                <li><a href="/1/1515.html" title="斗破苍穹 第一千三百二十一章  魂崖，魂厉【第三更！】" target="_blank">第一千三百二十一章  魂崖，魂厉【第三更！】</a></li>
                                <li><a href="/1/1516.html" title="斗破苍穹 第一千三百零一章 天墓" target="_blank">第一千三百零一章 天墓</a></li>
                                <li><a href="/1/1517.html" title="斗破苍穹 第一千三百零二章 古真" target="_blank">第一千三百零二章 古真</a></li>
                                <li><a href="/1/1518.html" title="斗破苍穹 第一千三百零三章 下马威" target="_blank">第一千三百零三章 下马威</a></li>
                                <li><a href="/1/1519.html" title="斗破苍穹 第一千三百零四章 修罗都统" target="_blank">第一千三百零四章 修罗都统</a></li>
                                <li><a href="/1/1520.html" title="斗破苍穹 第一千三百零五章 邙天尺" target="_blank">第一千三百零五章 邙天尺</a></li>
                                <li><a href="/1/1521.html" title="斗破苍穹 第一千三百零六章 仪式开始" target="_blank">第一千三百零六章 仪式开始</a></li>
                                <li><a href="/1/1522.html" title="斗破苍穹 第一千三百零七章 血脉等级，族纹！" target="_blank">第一千三百零七章 血脉等级，族纹！</a></li>
                                <li><a href="/1/1523.html" title="斗破苍穹 第一千三百零八章 挑战" target="_blank">第一千三百零八章 挑战</a></li>
                                <li><a href="/1/1524.html" title="斗破苍穹 第一千三百零九章 劲敌！" target="_blank">第一千三百零九章 劲敌！</a></li>
                                <li><a href="/1/1525.html" title="斗破苍穹 第一千三百一十章 巅峰交手" target="_blank">第一千三百一十章 巅峰交手</a></li>
                                <li><a href="/1/1526.html" title="斗破苍穹 第一千三百一十一章 大寂灭指" target="_blank">第一千三百一十一章 大寂灭指</a></li>
                                <li><a href="/1/1527.html" title="斗破苍穹 第一千三百一十二章 落幕！" target="_blank">第一千三百一十二章 落幕！</a></li>
                                <li><a href="/1/1528.html" title="斗破苍穹 第一千三百一十三章 胜！" target="_blank">第一千三百一十三章 胜！</a></li>
                                <li><a href="/1/1529.html" title="斗破苍穹 第一千三百一十四章 神品血脉" target="_blank">第一千三百一十四章 神品血脉</a></li>
                                <li><a href="/1/1530.html" title="斗破苍穹 第一千三百一十五章 七彩族纹" target="_blank">第一千三百一十五章 七彩族纹</a></li>
                                <li><a href="/1/1531.html" title="斗破苍穹 第一千三百一十六章 相见" target="_blank">第一千三百一十六章 相见</a></li>
                                <li><a href="/1/1532.html" title="斗破苍穹 第一千三百一十七章 交谈" target="_blank">第一千三百一十七章 交谈</a></li>
                                <li><a href="/1/1533.html" title="斗破苍穹 第一千三百一十八章 天墓开启" target="_blank">第一千三百一十八章 天墓开启</a></li>
                                <li><a href="/1/1534.html" title="斗破苍穹 第一千三百一十九章 进入天墓" target="_blank">第一千三百一十九章 进入天墓</a></li>
                                <li><a href="/1/1535.html" title="斗破苍穹 第一千三百二十章 枯燥的修行" target="_blank">第一千三百二十章 枯燥的修行</a></li>
                                <li><a href="/1/1536.html" title="斗破苍穹 第一千三百二十一章 魂崖，魂厉" target="_blank">第一千三百二十一章 魂崖，魂厉</a></li>
                                <li><a href="/1/1537.html" title="斗破苍穹 第一千三百二十二章   晋级六星" target="_blank">第一千三百二十二章   晋级六星</a></li>
                                <li><a href="/1/1538.html" title="斗破苍穹 第一千三百二十三章   追逃" target="_blank">第一千三百二十三章   追逃</a></li>
                                <li><a href="/1/1539.html" title="斗破苍穹 第一千三百二十四章  九星能量体" target="_blank">第一千三百二十四章  九星能量体</a></li>
                                <li><a href="/1/1540.html" title="斗破苍穹 第一千三百二十五章   紫色的天妖傀" target="_blank">第一千三百二十五章   紫色的天妖傀</a></li>
                                <li><a href="/1/1541.html" title="斗破苍穹 第一千三百二十六章  大风暴" target="_blank">第一千三百二十六章  大风暴</a></li>
                                <li><a href="/1/1542.html" title="斗破苍穹 第一千三百二十七章   聚集" target="_blank">第一千三百二十七章   聚集</a></li>
                                <li><a href="/1/1543.html" title="斗破苍穹 第一千三百二十八章    远古噬虫" target="_blank">第一千三百二十八章    远古噬虫</a></li>
                                <li><a href="/1/1544.html" title="斗破苍穹 第一千三百二十九章   收取报酬" target="_blank">第一千三百二十九章   收取报酬</a></li>
                                <li><a href="/1/1545.html" title="斗破苍穹 第一千三百三十章   开辟晶壁" target="_blank">第一千三百三十章   开辟晶壁</a></li>
                                <li><a href="/1/1546.html" title="斗破苍穹 第一千三百三十一章   第三层" target="_blank">第一千三百三十一章   第三层</a></li>
                                <li><a href="/1/1547.html" title="斗破苍穹 第一千三百三十二章   半圣能量体" target="_blank">第一千三百三十二章   半圣能量体</a></li>
                                <li><a href="/1/1548.html" title="斗破苍穹 第一千三百三十三章   血刀圣者" target="_blank">第一千三百三十三章   血刀圣者</a></li>
                                <li><a href="/1/1549.html" title="斗破苍穹 第一千三百三十四章 两名斗圣" target="_blank">第一千三百三十四章 两名斗圣</a></li>
                                <li><a href="/1/1550.html" title="斗破苍穹 第一千三百三十四章 现身" target="_blank">第一千三百三十四章 现身</a></li>
                                <li><a href="/1/1551.html" title="斗破苍穹 第一千三百三十六章   萧玄！" target="_blank">第一千三百三十六章   萧玄！</a></li>
                                <li><a href="/1/1552.html" title="斗破苍穹 第一千三百三十七章   血脉传承" target="_blank">第一千三百三十七章   血脉传承</a></li>
                                <li><a href="/1/1553.html" title="斗破苍穹 第一千三百三十八章   换血【第一更！】" target="_blank">第一千三百三十八章   换血【第一更！】</a></li>
                                <li><a href="/1/1554.html" title="斗破苍穹 第一千三百三十九章   血脉融合【第二更！】" target="_blank">第一千三百三十九章   血脉融合【第二更！】</a></li>
                                <li><a href="/1/1555.html" title="斗破苍穹 第一千三百四十章   一年半【第三更！】" target="_blank">第一千三百四十章   一年半【第三更！】</a></li>
                                <li><a href="/1/1556.html" title="斗破苍穹 第一千三百四十一章   八星斗尊巅峰！【第一更！】" target="_blank">第一千三百四十一章   八星斗尊巅峰！【第一更！】</a></li>
                                <li><a href="/1/1557.html" title="斗破苍穹 第一千三百四十二章   激活族纹【第二更！】" target="_blank">第一千三百四十二章   激活族纹【第二更！】</a></li>
                                <li><a href="/1/1558.html" title="斗破苍穹 第一千三百四十三章  最后的历练【第三更！】" target="_blank">第一千三百四十三章  最后的历练【第三更！】</a></li>
                                <li><a href="/1/1559.html" title="斗破苍穹 第一千三百三十八章 换血" target="_blank">第一千三百三十八章 换血</a></li>
                                <li><a href="/1/1560.html" title="斗破苍穹 第一千三百三十九章 血脉融合" target="_blank">第一千三百三十九章 血脉融合</a></li>
                                <li><a href="/1/1561.html" title="斗破苍穹 第一千三百四十章 一年半" target="_blank">第一千三百四十章 一年半</a></li>
                                <li><a href="/1/1562.html" title="斗破苍穹 第一千三百四十一章 八星斗尊巅峰！" target="_blank">第一千三百四十一章 八星斗尊巅峰！</a></li>
                                <li><a href="/1/1563.html" title="斗破苍穹 第一千三百四十二章 激活族纹" target="_blank">第一千三百四十二章 激活族纹</a></li>
                                <li><a href="/1/1564.html" title="斗破苍穹 第一千三百四十三章 最后的历练" target="_blank">第一千三百四十三章 最后的历练</a></li>
                                <li><a href="/1/1565.html" title="斗破苍穹 斗破点击破亿，拜谢所有支持斗破的兄弟姐妹！" target="_blank">斗破点击破亿，拜谢所有支持斗破的兄弟姐妹！</a></li>
                                <li><a href="/1/1566.html" title="斗破苍穹 第一千三百四十五章   斩杀" target="_blank">第一千三百四十五章   斩杀</a></li>
                                <li><a href="/1/1567.html" title="斗破苍穹 第一千三百四十五  离开天墓" target="_blank">第一千三百四十五  离开天墓</a></li>
                                <li><a href="/1/1568.html" title="斗破苍穹 第一千三百四十六章   魂林" target="_blank">第一千三百四十六章   魂林</a></li>
                                <li><a href="/1/1569.html" title="斗破苍穹 第一千三百四十七章  摊牌" target="_blank">第一千三百四十七章  摊牌</a></li>
                                <li><a href="/1/1570.html" title="斗破苍穹 第一千三百四十八章   离开古界" target="_blank">第一千三百四十八章   离开古界</a></li>
                                <li><a href="/1/1571.html" title="斗破苍穹 第一千三百四十九章   焕然一新的星陨阁" target="_blank">第一千三百四十九章   焕然一新的星陨阁</a></li>
                                <li><a href="/1/1572.html" title="斗破苍穹 第一千三百五十章  西北大陆的动荡【第一更！】" target="_blank">第一千三百五十章  西北大陆的动荡【第一更！】</a></li>
                                <li><a href="/1/1573.html" title="斗破苍穹 第一千三百五十一章   收徒幽泉【第二更！】" target="_blank">第一千三百五十一章   收徒幽泉【第二更！】</a></li>
                                <li><a href="/1/1574.html" title="斗破苍穹 第一千三百五十二章   邀集帮手【第三更！】" target="_blank">第一千三百五十二章   邀集帮手【第三更！】</a></li>
                                <li><a href="/1/1575.html" title="斗破苍穹 第一千三百五十章 西北大陆的动荡" target="_blank">第一千三百五十章 西北大陆的动荡</a></li>
                                <li><a href="/1/1576.html" title="斗破苍穹 第一千三百五十一章 收徒幽泉" target="_blank">第一千三百五十一章 收徒幽泉</a></li>
                                <li><a href="/1/1577.html" title="斗破苍穹 第一千三百五十二章 邀集帮手" target="_blank">第一千三百五十二章 邀集帮手</a></li>
                                <li><a href="/1/1578.html" title="斗破苍穹 第一千三百五十三章  玄黄要塞" target="_blank">第一千三百五十三章  玄黄要塞</a></li>
                                <li><a href="/1/1579.html" title="斗破苍穹 第一千三百五十四章  小萧潇" target="_blank">第一千三百五十四章  小萧潇</a></li>
                                <li><a href="/1/1580.html" title="斗破苍穹 第一千三百五十五章   大战始【第一更！】" target="_blank">第一千三百五十五章   大战始【第一更！】</a></li>
                                <li><a href="/1/1581.html" title="斗破苍穹 第一千三百五十六章  惨烈【第二更！】" target="_blank">第一千三百五十六章  惨烈【第二更！】</a></li>
                                <li><a href="/1/1582.html" title="斗破苍穹 第一千三百五十七章   一掌击杀！【第三更！】" target="_blank">第一千三百五十七章   一掌击杀！【第三更！】</a></li>
                                <li><a href="/1/1583.html" title="斗破苍穹 第一千三百五十八章   今非昔比【第一更！】" target="_blank">第一千三百五十八章   今非昔比【第一更！】</a></li>
                                <li><a href="/1/1584.html" title="斗破苍穹 第一千三百五十九章  四天尊，血河！【第二更！】" target="_blank">第一千三百五十九章  四天尊，血河！【第二更！】</a></li>
                                <li><a href="/1/1585.html" title="斗破苍穹 第一千三百六十章  噬血术【第三更！】" target="_blank">第一千三百六十章  噬血术【第三更！】</a></li>
                                <li><a href="/1/1586.html" title="斗破苍穹 第一千三百五十五章 大战始" target="_blank">第一千三百五十五章 大战始</a></li>
                                <li><a href="/1/1587.html" title="斗破苍穹 第一千三百五十六章 惨烈" target="_blank">第一千三百五十六章 惨烈</a></li>
                                <li><a href="/1/1588.html" title="斗破苍穹 第一千三百五十七章 一掌击杀！" target="_blank">第一千三百五十七章 一掌击杀！</a></li>
                                <li><a href="/1/1589.html" title="斗破苍穹 第一千三百五十八章 今非昔比" target="_blank">第一千三百五十八章 今非昔比</a></li>
                                <li><a href="/1/1590.html" title="斗破苍穹 第一千三百五十九章 四天尊，血河！" target="_blank">第一千三百五十九章 四天尊，血河！</a></li>
                                <li><a href="/1/1591.html" title="斗破苍穹 第一千三百六十章 噬血术" target="_blank">第一千三百六十章 噬血术</a></li>
                                <li><a href="/1/1592.html" title="斗破苍穹 第一千三百六十一章   九转成圣" target="_blank">第一千三百六十一章   九转成圣</a></li>
                                <li><a href="/1/1593.html" title="斗破苍穹 第一千三百六十二章  落幕" target="_blank">第一千三百六十二章  落幕</a></li>
                                <li><a href="/1/1594.html" title="斗破苍穹 第一千三百六十三章    毒瘤【第一更！】" target="_blank">第一千三百六十三章    毒瘤【第一更！】</a></li>
                                <li><a href="/1/1595.html" title="斗破苍穹 第一千三百六十四章   炼丹【第二更！】" target="_blank">第一千三百六十四章   炼丹【第二更！】</a></li>
                                <li><a href="/1/1596.html" title="斗破苍穹 第一千三百六十五章  严惩【第三更！】" target="_blank">第一千三百六十五章  严惩【第三更！】</a></li>
                                <li><a href="/1/1597.html" title="斗破苍穹 第一千三百六十六章   解决【第四更！】" target="_blank">第一千三百六十六章   解决【第四更！】</a></li>
                                <li><a href="/1/1598.html" title="斗破苍穹 第一千三百六十三章 毒瘤" target="_blank">第一千三百六十三章 毒瘤</a></li>
                                <li><a href="/1/1599.html" title="斗破苍穹 第一千三百六十四章 炼丹" target="_blank">第一千三百六十四章 炼丹</a></li>
                                <li><a href="/1/1600.html" title="斗破苍穹 第一千三百六十五章 严惩" target="_blank">第一千三百六十五章 严惩</a></li>
                                <li><a href="/1/1601.html" title="斗破苍穹 第一千三百六十六章 解决" target="_blank">第一千三百六十六章 解决</a></li>
                                <li><a href="/1/1602.html" title="斗破苍穹 第一千三百六十七章  动身之前" target="_blank">第一千三百六十七章  动身之前</a></li>
                                <li><a href="/1/1603.html" title="斗破苍穹 第一千三百六十八章  回星陨阁" target="_blank">第一千三百六十八章  回星陨阁</a></li>
                                <li><a href="/1/1604.html" title="斗破苍穹 第一千三百六十九章  空间交易会" target="_blank">第一千三百六十九章  空间交易会</a></li>
                                <li><a href="/1/1605.html" title="斗破苍穹 第一千三百七十章   八彩原石" target="_blank">第一千三百七十章   八彩原石</a></li>
                                <li><a href="/1/1606.html" title="斗破苍穹 第一千三百七十一章   古殿【第一更！】" target="_blank">第一千三百七十一章   古殿【第一更！】</a></li>
                                <li><a href="/1/1607.html" title="斗破苍穹 第一千三百七十二章   最后一张残图【第二更！】" target="_blank">第一千三百七十二章   最后一张残图【第二更！】</a></li>
                                <li><a href="/1/1608.html" title="斗破苍穹 第一千三百七十三章   情报【第三更！】" target="_blank">第一千三百七十三章   情报【第三更！】</a></li>
                                <li><a href="/1/1609.html" title="斗破苍穹 第一千三百七十四章   莽荒古域【第一更！】" target="_blank">第一千三百七十四章   莽荒古域【第一更！】</a></li>
                                <li><a href="/1/1610.html" title="斗破苍穹 第一千三百七十五章   蝎魔三鬼【第二更！】" target="_blank">第一千三百七十五章   蝎魔三鬼【第二更！】</a></li>
                                <li><a href="/1/1611.html" title="斗破苍穹 第一千三百七十六章   四色半的佛怒火莲！【第三更！】" target="_blank">第一千三百七十六章   四色半的佛怒火莲！【第三更！】</a></li>
                                <li><a href="/1/1612.html" title="斗破苍穹 第一千三百七十七章   古图到手【第一更！】" target="_blank">第一千三百七十七章   古图到手【第一更！】</a></li>
                                <li><a href="/1/1613.html" title="斗破苍穹 第一千三百七十八章   古图之谜【第二更！】" target="_blank">第一千三百七十八章   古图之谜【第二更！】</a></li>
                                <li><a href="/1/1614.html" title="斗破苍穹 第一千三百七十九章   净莲妖圣【第三更！】" target="_blank">第一千三百七十九章   净莲妖圣【第三更！】</a></li>
                                <li><a href="/1/1615.html" title="斗破苍穹 第一千三百八十章    修炼金刚琉璃身【第一更！疯狂，从现在开始！】" target="_blank">第一千三百八十章    修炼金刚琉璃身【第一更！疯狂，从现在开始！】</a></li>
                                <li><a href="/1/1616.html" title="斗破苍穹 第一千三百八十一章   莽荒镇【第二更！】" target="_blank">第一千三百八十一章   莽荒镇【第二更！】</a></li>
                                <li><a href="/1/1617.html" title="斗破苍穹 第一千三百八十二章   进入莽荒古域【第三更！】" target="_blank">第一千三百八十二章   进入莽荒古域【第三更！】</a></li>
                                <li><a href="/1/1618.html" title="斗破苍穹 第一千三百八十三章 　深入【第四更！】" target="_blank">第一千三百八十三章 　深入【第四更！】</a></li>
                                <li><a href="/1/1619.html" title="斗破苍穹 第一千三百八十四章   再遇云韵【第五更！】" target="_blank">第一千三百八十四章   再遇云韵【第五更！】</a></li>
                                <li><a href="/1/1620.html" title="斗破苍穹 第一千三百八十五章   斩杀天冥宗【第六更！】" target="_blank">第一千三百八十五章   斩杀天冥宗【第六更！】</a></li>
                                <li><a href="/1/1621.html" title="斗破苍穹 第一千三百八十六章   远古天魔蟒【第七更！】" target="_blank">第一千三百八十六章   远古天魔蟒【第七更！】</a></li>
                                <li><a href="/1/1622.html" title="斗破苍穹 第一千三百八十七章 围剿天魔蟒【第八更！】" target="_blank">第一千三百八十七章 围剿天魔蟒【第八更！】</a></li>
                                <li><a href="/1/1623.html" title="斗破苍穹 第一千三百八十八章   天魔血池【第九更！】" target="_blank">第一千三百八十八章   天魔血池【第九更！】</a></li>
                                <li><a href="/1/1624.html" title="斗破苍穹 第一千三百八十九章   九星斗尊！【第十更！】" target="_blank">第一千三百八十九章   九星斗尊！【第十更！】</a></li>
                                <li><a href="/1/1625.html" title="斗破苍穹 第一千三百九十章  古域台【第十一更！！】" target="_blank">第一千三百九十章  古域台【第十一更！！】</a></li>
                                <li><a href="/1/1626.html" title="斗破苍穹 第一千三百九十一章  下马威【第一更！】" target="_blank">第一千三百九十一章  下马威【第一更！】</a></li>
                                <li><a href="/1/1627.html" title="斗破苍穹 第一千三百九十二章  两女相见【第二更！】" target="_blank">第一千三百九十二章  两女相见【第二更！】</a></li>
                                <li><a href="/1/1628.html" title="斗破苍穹 第一千三百九十三章   魂玉，兽潮【第三更！】" target="_blank">第一千三百九十三章   魂玉，兽潮【第三更！】</a></li>
                                <li><a href="/1/1629.html" title="斗破苍穹 第一千三百七十一章 古殿" target="_blank">第一千三百七十一章 古殿</a></li>
                                <li><a href="/1/1630.html" title="斗破苍穹 第一千三百七十二章 最后一张残图" target="_blank">第一千三百七十二章 最后一张残图</a></li>
                                <li><a href="/1/1631.html" title="斗破苍穹 第一千三百七十三章 情报" target="_blank">第一千三百七十三章 情报</a></li>
                                <li><a href="/1/1632.html" title="斗破苍穹 第一千三百七十四章 莽荒古域" target="_blank">第一千三百七十四章 莽荒古域</a></li>
                                <li><a href="/1/1633.html" title="斗破苍穹 第一千三百七十六章 四色半的佛怒火莲！" target="_blank">第一千三百七十六章 四色半的佛怒火莲！</a></li>
                                <li><a href="/1/1634.html" title="斗破苍穹 第一千三百七十七章 古图到手" target="_blank">第一千三百七十七章 古图到手</a></li>
                                <li><a href="/1/1635.html" title="斗破苍穹 第一千三百七十八章 古图之谜" target="_blank">第一千三百七十八章 古图之谜</a></li>
                                <li><a href="/1/1636.html" title="斗破苍穹 第一千三百七十九章 净莲妖圣" target="_blank">第一千三百七十九章 净莲妖圣</a></li>
                                <li><a href="/1/1637.html" title="斗破苍穹 第一千三百八十章 修炼金刚琉璃身" target="_blank">第一千三百八十章 修炼金刚琉璃身</a></li>
                                <li><a href="/1/1638.html" title="斗破苍穹 第一千三百八十一章 莽荒镇" target="_blank">第一千三百八十一章 莽荒镇</a></li>
                                <li><a href="/1/1639.html" title="斗破苍穹 第一千三百八十二章 进入莽荒古域" target="_blank">第一千三百八十二章 进入莽荒古域</a></li>
                                <li><a href="/1/1640.html" title="斗破苍穹 第一千三百八十三章 深入" target="_blank">第一千三百八十三章 深入</a></li>
                                <li><a href="/1/1641.html" title="斗破苍穹 第一千三百八十四章 再遇云韵" target="_blank">第一千三百八十四章 再遇云韵</a></li>
                                <li><a href="/1/1642.html" title="斗破苍穹 第一千三百八十五章 斩杀天冥宗" target="_blank">第一千三百八十五章 斩杀天冥宗</a></li>
                                <li><a href="/1/1643.html" title="斗破苍穹 第一千三百八十六章 远古天魔蟒" target="_blank">第一千三百八十六章 远古天魔蟒</a></li>
                                <li><a href="/1/1644.html" title="斗破苍穹 第一千三百八十七章 围剿天魔蟒" target="_blank">第一千三百八十七章 围剿天魔蟒</a></li>
                                <li><a href="/1/1645.html" title="斗破苍穹 第一千三百八十八章 天魔血池" target="_blank">第一千三百八十八章 天魔血池</a></li>
                                <li><a href="/1/1646.html" title="斗破苍穹 第一千三百八十九章 九星斗尊！" target="_blank">第一千三百八十九章 九星斗尊！</a></li>
                                <li><a href="/1/1647.html" title="斗破苍穹 第一千三百九十章 古域台" target="_blank">第一千三百九十章 古域台</a></li>
                                <li><a href="/1/1648.html" title="斗破苍穹 第一千三百九十一章 下马威" target="_blank">第一千三百九十一章 下马威</a></li>
                                <li><a href="/1/1649.html" title="斗破苍穹 第一千三百九十二章 两女相见" target="_blank">第一千三百九十二章 两女相见</a></li>
                                <li><a href="/1/1650.html" title="斗破苍穹 第一千三百九十三章 魂玉，兽潮" target="_blank">第一千三百九十三章 魂玉，兽潮</a></li>
                                <li><a href="/1/1651.html" title="斗破苍穹 第一千三百九十四章   冲击兽潮" target="_blank">第一千三百九十四章   冲击兽潮</a></li>
                                <li><a href="/1/1652.html" title="斗破苍穹 第一千三百九十五章  突破！" target="_blank">第一千三百九十五章  突破！</a></li>
                                <li><a href="/1/1653.html" title="斗破苍穹 第一千三百九十六章   五位半圣！【第一更！】" target="_blank">第一千三百九十六章   五位半圣！【第一更！】</a></li>
                                <li><a href="/1/1654.html" title="斗破苍穹 第一千三百九十七章   轰杀半圣傀儡【第二更！】" target="_blank">第一千三百九十七章   轰杀半圣傀儡【第二更！】</a></li>
                                <li><a href="/1/1655.html" title="斗破苍穹 第一千三百九十八章   进入古树【第三更！】" target="_blank">第一千三百九十八章   进入古树【第三更！】</a></li>
                                <li><a href="/1/1656.html" title="斗破苍穹 第一千三百九十九章   幻境【第一更！】" target="_blank">第一千三百九十九章   幻境【第一更！】</a></li>
                                <li><a href="/1/1657.html" title="斗破苍穹 第一千四百章   斗帝的负面情绪【第二更！】" target="_blank">第一千四百章   斗帝的负面情绪【第二更！】</a></li>
                                <li><a href="/1/1658.html" title="斗破苍穹 第一千四百零一章   菩提三宝【第三更！】" target="_blank">第一千四百零一章   菩提三宝【第三更！】</a></li>
                                <li><a href="/1/1659.html" title="斗破苍穹 第一千三百九十六章 五位半圣！" target="_blank">第一千三百九十六章 五位半圣！</a></li>
                                <li><a href="/1/1660.html" title="斗破苍穹 第一千三百九十七章 轰杀半圣傀儡" target="_blank">第一千三百九十七章 轰杀半圣傀儡</a></li>
                                <li><a href="/1/1661.html" title="斗破苍穹 第一千三百九十八章 进入古树" target="_blank">第一千三百九十八章 进入古树</a></li>
                                <li><a href="/1/1662.html" title="斗破苍穹 第一千三百九十九章 幻境" target="_blank">第一千三百九十九章 幻境</a></li>
                                <li><a href="/1/1663.html" title="斗破苍穹 第一千四百章 斗帝的负面情绪" target="_blank">第一千四百章 斗帝的负面情绪</a></li>
                                <li><a href="/1/1664.html" title="斗破苍穹 第一千四百零一章 菩提三宝" target="_blank">第一千四百零一章 菩提三宝</a></li>
                                <li><a href="/1/1665.html" title="斗破苍穹 第一千四百零二章   苏醒" target="_blank">第一千四百零二章   苏醒</a></li>
                                <li><a href="/1/1666.html" title="斗破苍穹 第一千四百零三章   百世轮回，九转巅峰！" target="_blank">第一千四百零三章   百世轮回，九转巅峰！</a></li>
                                <li><a href="/1/1667.html" title="斗破苍穹 第一千四百零四章 绝对压制【第一更！】" target="_blank">第一千四百零四章 绝对压制【第一更！】</a></li>
                                <li><a href="/1/1668.html" title="斗破苍穹 第一千四百零五章  空间破裂【第二更！】" target="_blank">第一千四百零五章  空间破裂【第二更！】</a></li>
                                <li><a href="/1/1669.html" title="斗破苍穹 第一千四百零六章  二天尊，骨幽圣者【第三更！】" target="_blank">第一千四百零六章  二天尊，骨幽圣者【第三更！】</a></li>
                                <li><a href="/1/1670.html" title="斗破苍穹 第一千四百零四章 绝对压制" target="_blank">第一千四百零四章 绝对压制</a></li>
                                <li><a href="/1/1671.html" title="斗破苍穹 第一千四百零五章 空间破裂" target="_blank">第一千四百零五章 空间破裂</a></li>
                                <li><a href="/1/1672.html" title="斗破苍穹 第一千四百零六章 二天尊，骨幽圣者" target="_blank">第一千四百零六章 二天尊，骨幽圣者</a></li>
                                <li><a href="/1/1673.html" title="斗破苍穹 第一千四百零七章   金帝焚天炎" target="_blank">第一千四百零七章   金帝焚天炎</a></li>
                                <li><a href="/1/1674.html" title="斗破苍穹 第一千四百零八章   对战半圣" target="_blank">第一千四百零八章   对战半圣</a></li>
                                <li><a href="/1/1675.html" title="斗破苍穹 第一千四百零九章   逼退骨幽" target="_blank">第一千四百零九章   逼退骨幽</a></li>
                                <li><a href="/1/1676.html" title="斗破苍穹 第一千四百一十章   闭关" target="_blank">第一千四百一十章   闭关</a></li>
                                <li><a href="/1/1677.html" title="斗破苍穹 第一千四百一十一章  灵族之变" target="_blank">第一千四百一十一章  灵族之变</a></li>
                                <li><a href="/1/1678.html" title="斗破苍穹 第一千四百一十二章  战帖" target="_blank">第一千四百一十二章  战帖</a></li>
                                <li><a href="/1/1679.html" title="斗破苍穹 第一千四百一十三章   大战来临【第一更！】" target="_blank">第一千四百一十三章   大战来临【第一更！】</a></li>
                                <li><a href="/1/1680.html" title="斗破苍穹 第一千四百一十四章   星界大战【第二更！】" target="_blank">第一千四百一十四章   星界大战【第二更！】</a></li>
                                <li><a href="/1/1681.html" title="斗破苍穹 第一千四百一十五章   破关而出，斗圣！【第三更！】" target="_blank">第一千四百一十五章   破关而出，斗圣！【第三更！】</a></li>
                                <li><a href="/1/1682.html" title="斗破苍穹 第一千四百一十三章 大战来临" target="_blank">第一千四百一十三章 大战来临</a></li>
                                <li><a href="/1/1683.html" title="斗破苍穹 第一千四百一十四章 星界大战" target="_blank">第一千四百一十四章 星界大战</a></li>
                                <li><a href="/1/1684.html" title="斗破苍穹 第一千四百一十五章 破关而出，斗圣！" target="_blank">第一千四百一十五章 破关而出，斗圣！</a></li>
                                <li><a href="/1/1685.html" title="斗破苍穹 第一千四百一十六章   佛怒轮回" target="_blank">第一千四百一十六章   佛怒轮回</a></li>
                                <li><a href="/1/1686.html" title="斗破苍穹 第一千四百一十七章   大杀四方" target="_blank">第一千四百一十七章   大杀四方</a></li>
                                <li><a href="/1/1687.html" title="斗破苍穹 第一千四百一十八章   魂族斗圣" target="_blank">第一千四百一十八章   魂族斗圣</a></li>
                                <li><a href="/1/1688.html" title="斗破苍穹 第一千四百一十九章 各宗隐秘" target="_blank">第一千四百一十九章 各宗隐秘</a></li>
                                <li><a href="/1/1689.html" title="斗破苍穹 第一千四百二十章   杀鸡儆猴" target="_blank">第一千四百二十章   杀鸡儆猴</a></li>
                                <li><a href="/1/1690.html" title="斗破苍穹 第一千四百二十一章   寻求盟友" target="_blank">第一千四百二十一章   寻求盟友</a></li>
                                <li><a href="/1/1691.html" title="斗破苍穹 第一千四百二十二章   再至丹塔" target="_blank">第一千四百二十二章   再至丹塔</a></li>
                                <li><a href="/1/1692.html" title="斗破苍穹 第一千四百二十三章   小丹塔" target="_blank">第一千四百二十三章   小丹塔</a></li>
                                <li><a href="/1/1693.html" title="斗破苍穹 第一千四百二十四章 竞选长老【第一更！】" target="_blank">第一千四百二十四章 竞选长老【第一更！】</a></li>
                                <li><a href="/1/1694.html" title="斗破苍穹 第一千四百二十五章   小丹塔大长老【第二更！】" target="_blank">第一千四百二十五章   小丹塔大长老【第二更！】</a></li>
                                <li><a href="/1/1695.html" title="斗破苍穹 第一千四百二十六章   那可未必【第三更！】" target="_blank">第一千四百二十六章   那可未必【第三更！】</a></li>
                                <li><a href="/1/1696.html" title="斗破苍穹 第一千四百二十四章 竞选长老" target="_blank">第一千四百二十四章 竞选长老</a></li>
                                <li><a href="/1/1697.html" title="斗破苍穹 第一千四百二十五章 小丹塔大长老" target="_blank">第一千四百二十五章 小丹塔大长老</a></li>
                                <li><a href="/1/1698.html" title="斗破苍穹 第一千四百二十六章 那可未必" target="_blank">第一千四百二十六章 那可未必</a></li>
                                <li><a href="/1/1699.html" title="斗破苍穹 第一千四百二十七章   黑魔雷" target="_blank">第一千四百二十七章   黑魔雷</a></li>
                                <li><a href="/1/1700.html" title="斗破苍穹 第一千四百二十八章  九品宝丹" target="_blank">第一千四百二十八章  九品宝丹</a></li>
                                <li><a href="/1/1701.html" title="斗破苍穹 第一千四百二十九章   联盟" target="_blank">第一千四百二十九章   联盟</a></li>
                                <li><a href="/1/1702.html" title="斗破苍穹 第一千四百三十章   天府联盟" target="_blank">第一千四百三十章   天府联盟</a></li>
                                <li><a href="/1/1703.html" title="斗破苍穹 第一千四百三十一章   魂殿副殿主" target="_blank">第一千四百三十一章   魂殿副殿主</a></li>
                                <li><a href="/1/1704.html" title="斗破苍穹 第一千四百三十二章   九幽黄泉" target="_blank">第一千四百三十二章   九幽黄泉</a></li>
                                <li><a href="/1/1705.html" title="斗破苍穹 第一千四百三十三章  九阴黄泉丹" target="_blank">第一千四百三十三章  九阴黄泉丹</a></li>
                                <li><a href="/1/1706.html" title="斗破苍穹 第一千四三十四章   古龙一族情势" target="_blank">第一千四三十四章   古龙一族情势</a></li>
                                <li><a href="/1/1707.html" title="斗破苍穹 第一千四百三十五章  冥蛇地脉" target="_blank">第一千四百三十五章  冥蛇地脉</a></li>
                                <li><a href="/1/1708.html" title="斗破苍穹 第一千四百三十六章   被锁之人" target="_blank">第一千四百三十六章   被锁之人</a></li>
                                <li><a href="/1/1709.html" title="斗破苍穹 第一千四百三十七章   妖暝" target="_blank">第一千四百三十七章   妖暝</a></li>
                                <li><a href="/1/1710.html" title="斗破苍穹 第一千四百三十八章  妖啸天" target="_blank">第一千四百三十八章  妖啸天</a></li>
                                <li><a href="/1/1711.html" title="斗破苍穹 第一千四百三十九章   暴打【第一更！】" target="_blank">第一千四百三十九章   暴打【第一更！】</a></li>
                                <li><a href="/1/1712.html" title="斗破苍穹 第一千四百四十章   九幽冥杖【第二更！】" target="_blank">第一千四百四十章   九幽冥杖【第二更！】</a></li>
                                <li><a href="/1/1713.html" title="斗破苍穹 第一千四百四十一章   大势已去【第三更！】" target="_blank">第一千四百四十一章   大势已去【第三更！】</a></li>
                                <li><a href="/1/1714.html" title="斗破苍穹 第一千四百三十九章 暴打" target="_blank">第一千四百三十九章 暴打</a></li>
                                <li><a href="/1/1715.html" title="斗破苍穹 第一千四百四十章 九幽冥杖" target="_blank">第一千四百四十章 九幽冥杖</a></li>
                                <li><a href="/1/1716.html" title="斗破苍穹 第一千四百四十一章 大势已去" target="_blank">第一千四百四十一章 大势已去</a></li>
                                <li><a href="/1/1717.html" title="斗破苍穹 第一千四百四十二章 黄泉妖圣" target="_blank">第一千四百四十二章 黄泉妖圣</a></li>
                                <li><a href="/1/1718.html" title="斗破苍穹 第一千四百四十三章   黄泉天怒" target="_blank">第一千四百四十三章   黄泉天怒</a></li>
                                <li><a href="/1/1719.html" title="斗破苍穹 第一千四百四十四章   灵魂争斗" target="_blank">第一千四百四十四章   灵魂争斗</a></li>
                                <li><a href="/1/1720.html" title="斗破苍穹 第一千一百四十五章 　　妖圣精血" target="_blank">第一千一百四十五章 　　妖圣精血</a></li>
                                <li><a href="/1/1721.html" title="斗破苍穹 第一千四百四十六章   寻找帮手" target="_blank">第一千四百四十六章   寻找帮手</a></li>
                                <li><a href="/1/1722.html" title="斗破苍穹 第一千四百四十七章   吸收妖圣精血" target="_blank">第一千四百四十七章   吸收妖圣精血</a></li>
                                <li><a href="/1/1723.html" title="斗破苍穹 第一千四百四十八章   天妖三凰【第一更！】" target="_blank">第一千四百四十八章   天妖三凰【第一更！】</a></li>
                                <li><a href="/1/1724.html" title="斗破苍穹 第一千四百四十九章   伏击【第二更！】" target="_blank">第一千四百四十九章   伏击【第二更！】</a></li>
                                <li><a href="/1/1725.html" title="斗破苍穹 第一千四百五十章   独斗双圣【第三更！】" target="_blank">第一千四百五十章   独斗双圣【第三更！】</a></li>
                                <li><a href="/1/1726.html" title="斗破苍穹 第一千四百四十八章 天妖三凰" target="_blank">第一千四百四十八章 天妖三凰</a></li>
                                <li><a href="/1/1727.html" title="斗破苍穹 第一千四百四十九章 伏击" target="_blank">第一千四百四十九章 伏击</a></li>
                                <li><a href="/1/1728.html" title="斗破苍穹 第一千四百五十章 独斗双圣" target="_blank">第一千四百五十章 独斗双圣</a></li>
                                <li><a href="/1/1729.html" title="斗破苍穹 第一千四百五十一章   绝对压制" target="_blank">第一千四百五十一章   绝对压制</a></li>
                                <li><a href="/1/1730.html" title="斗破苍穹 第一千四百五十二章   人质威胁" target="_blank">第一千四百五十二章   人质威胁</a></li>
                                <li><a href="/1/1731.html" title="斗破苍穹 第一千四百五十三章  路遇【第一更！】" target="_blank">第一千四百五十三章  路遇【第一更！】</a></li>
                                <li><a href="/1/1732.html" title="斗破苍穹 第一千四百五十四章    解决【第二更！】" target="_blank">第一千四百五十四章    解决【第二更！】</a></li>
                                <li><a href="/1/1733.html" title="斗破苍穹 第一千四百五十五章   再见紫研【第三更！】" target="_blank">第一千四百五十五章   再见紫研【第三更！】</a></li>
                                <li><a href="/1/1734.html" title="斗破苍穹 第一千四百五十六章   大战爆发【第一更！】" target="_blank">第一千四百五十六章   大战爆发【第一更！】</a></li>
                                <li><a href="/1/1735.html" title="斗破苍穹 第一千四百五十七章   三大龙王【第二更！】" target="_blank">第一千四百五十七章   三大龙王【第二更！】</a></li>
                                <li><a href="/1/1736.html" title="斗破苍穹 第一千四百五十八章   拼命【第三更！】" target="_blank">第一千四百五十八章   拼命【第三更！】</a></li>
                                <li><a href="/1/1737.html" title="斗破苍穹 第一千四百五十九章   屠龙剑【第一更！】" target="_blank">第一千四百五十九章   屠龙剑【第一更！】</a></li>
                                <li><a href="/1/1738.html" title="斗破苍穹 第一千四百五十三章 路遇" target="_blank">第一千四百五十三章 路遇</a></li>
                                <li><a href="/1/1739.html" title="斗破苍穹 第一千四百五十四章 解决" target="_blank">第一千四百五十四章 解决</a></li>
                                <li><a href="/1/1740.html" title="斗破苍穹 第一千四百五十五章 再见紫研" target="_blank">第一千四百五十五章 再见紫研</a></li>
                                <li><a href="/1/1741.html" title="斗破苍穹 第一千四百五十六章 大战爆发" target="_blank">第一千四百五十六章 大战爆发</a></li>
                                <li><a href="/1/1742.html" title="斗破苍穹 第一千四百五十七章 三大龙王" target="_blank">第一千四百五十七章 三大龙王</a></li>
                                <li><a href="/1/1743.html" title="斗破苍穹 第一千四百五十八章 拼命" target="_blank">第一千四百五十八章 拼命</a></li>
                                <li><a href="/1/1744.html" title="斗破苍穹 第一千四百五十九章 屠龙剑" target="_blank">第一千四百五十九章 屠龙剑</a></li>
                                <li><a href="/1/1745.html" title="斗破苍穹 努力到现在。" target="_blank">努力到现在。</a></li>
                                <li><a href="/1/1746.html" title="斗破苍穹 第一千四百六十章   大战落幕【第二更！】" target="_blank">第一千四百六十章   大战落幕【第二更！】</a></li>
                                <li><a href="/1/1747.html" title="斗破苍穹 第一千四百六十一章   二星斗圣！【第三更！】" target="_blank">第一千四百六十一章   二星斗圣！【第三更！】</a></li>
                                <li><a href="/1/1748.html" title="斗破苍穹 第一千四百六十章 大战落幕" target="_blank">第一千四百六十章 大战落幕</a></li>
                                <li><a href="/1/1749.html" title="斗破苍穹 第一千四百六十一章 二星斗圣！" target="_blank">第一千四百六十一章 二星斗圣！</a></li>
                                <li><a href="/1/1750.html" title="斗破苍穹 最后的二十四小时！！！！" target="_blank">最后的二十四小时！！！！</a></li>
                                <li><a href="/1/1751.html" title="斗破苍穹 第一千四百六十二章    魂殿动静【第一更！】" target="_blank">第一千四百六十二章    魂殿动静【第一更！】</a></li>
                                <li><a href="/1/1752.html" title="斗破苍穹 第一千四百六十三章  天罡殿【第二更！】" target="_blank">第一千四百六十三章  天罡殿【第二更！】</a></li>
                                <li><a href="/1/1753.html" title="斗破苍穹 第一千四百六十四章   血洗人殿 【第三更！】" target="_blank">第一千四百六十四章   血洗人殿 【第三更！】</a></li>
                                <li><a href="/1/1754.html" title="斗破苍穹 第一千四百六十二章 魂殿动静" target="_blank">第一千四百六十二章 魂殿动静</a></li>
                                <li><a href="/1/1755.html" title="斗破苍穹 第一千四百六十三章 天罡殿" target="_blank">第一千四百六十三章 天罡殿</a></li>
                                <li><a href="/1/1756.html" title="斗破苍穹 第一千四百六十四章 血洗人殿" target="_blank">第一千四百六十四章 血洗人殿</a></li>
                                <li><a href="/1/1757.html" title="斗破苍穹 第一千四百六十五章  大天尊" target="_blank">第一千四百六十五章  大天尊</a></li>
                                <li><a href="/1/1758.html" title="斗破苍穹 第一千四百六十六章   击溃" target="_blank">第一千四百六十六章   击溃</a></li>
                                <li><a href="/1/1759.html" title="斗破苍穹 第一千四百六十七章   血洗" target="_blank">第一千四百六十七章   血洗</a></li>
                                <li><a href="/1/1760.html" title="斗破苍穹 第一千四百六十八章   灵魂光团" target="_blank">第一千四百六十八章   灵魂光团</a></li>
                                <li><a href="/1/1761.html" title="斗破苍穹 第一千四百六十九章   吸收灵魂本源" target="_blank">第一千四百六十九章   吸收灵魂本源</a></li>
                                <li><a href="/1/1762.html" title="斗破苍穹 第一千四百七十章   天境大圆满" target="_blank">第一千四百七十章   天境大圆满</a></li>
                                <li><a href="/1/1763.html" title="斗破苍穹 第一千四百七十一章   魂殿殿主！" target="_blank">第一千四百七十一章   魂殿殿主！</a></li>
                                <li><a href="/1/1764.html" title="斗破苍穹 第一千四百七十二章  妖火降世！" target="_blank">第一千四百七十二章  妖火降世！</a></li>
                                <li><a href="/1/1765.html" title="斗破苍穹 第一千四百七十三章   四方云动" target="_blank">第一千四百七十三章   四方云动</a></li>
                                <li><a href="/1/1766.html" title="斗破苍穹 第一千四百七十四章   八荒破灭焱" target="_blank">第一千四百七十四章   八荒破灭焱</a></li>
                                <li><a href="/1/1767.html" title="斗破苍穹 第一千四百七十五章   再见薰儿" target="_blank">第一千四百七十五章   再见薰儿</a></li>
                                <li><a href="/1/1768.html" title="斗破苍穹 第一千四百七十六章 　药万归" target="_blank">第一千四百七十六章 　药万归</a></li>
                                <li><a href="/1/1769.html" title="斗破苍穹 第一千四百七十七章  不知好歹" target="_blank">第一千四百七十七章  不知好歹</a></li>
                                <li><a href="/1/1770.html" title="斗破苍穹 第一千四百七十八章   空间破裂" target="_blank">第一千四百七十八章   空间破裂</a></li>
                                <li><a href="/1/1771.html" title="斗破苍穹 第一千四百七十九章   妖火空间" target="_blank">第一千四百七十九章   妖火空间</a></li>
                                <li><a href="/1/1772.html" title="斗破苍穹 第一千四百八十章   闯关" target="_blank">第一千四百八十章   闯关</a></li>
                                <li><a href="/1/1773.html" title="斗破苍穹 第一千四百八十一章   血色巨斧" target="_blank">第一千四百八十一章   血色巨斧</a></li>
                                <li><a href="/1/1774.html" title="斗破苍穹 第一千四百八十二章   虚幻与真实" target="_blank">第一千四百八十二章   虚幻与真实</a></li>
                                <li><a href="/1/1775.html" title="斗破苍穹 第一千四百八十三章   突破幻境" target="_blank">第一千四百八十三章   突破幻境</a></li>
                                <li><a href="/1/1776.html" title="斗破苍穹 第一千四百八十四章   合作" target="_blank">第一千四百八十四章   合作</a></li>
                                <li><a href="/1/1777.html" title="斗破苍穹 第一千四百八十五章   七圣斗妖火" target="_blank">第一千四百八十五章   七圣斗妖火</a></li>
                                <li><a href="/1/1778.html" title="斗破苍穹 第一千四百八十六章   反控" target="_blank">第一千四百八十六章   反控</a></li>
                                <li><a href="/1/1779.html" title="斗破苍穹 第一千四百八十七章   天罗封魔阵" target="_blank">第一千四百八十七章   天罗封魔阵</a></li>
                                <li><a href="/1/1780.html" title="斗破苍穹 第一千四百八十八章   抢妖火本源！" target="_blank">第一千四百八十八章   抢妖火本源！</a></li>
                                <li><a href="/1/1781.html" title="斗破苍穹 第一千四百八十九章   惊天对撞" target="_blank">第一千四百八十九章   惊天对撞</a></li>
                                <li><a href="/1/1782.html" title="斗破苍穹 第一千四百九十章   萧晨出手" target="_blank">第一千四百九十章   萧晨出手</a></li>
                                <li><a href="/1/1783.html" title="斗破苍穹 第一千四百九十一章   魂魔老人" target="_blank">第一千四百九十一章   魂魔老人</a></li>
                                <li><a href="/1/1784.html" title="斗破苍穹 第一千四百九十二章  青牛牧童" target="_blank">第一千四百九十二章  青牛牧童</a></li>
                                <li><a href="/1/1785.html" title="斗破苍穹 第一千四百九十三章   炼天古阵" target="_blank">第一千四百九十三章   炼天古阵</a></li>
                                <li><a href="/1/1786.html" title="斗破苍穹 第一千四百九十四章   净莲妖圣？" target="_blank">第一千四百九十四章   净莲妖圣？</a></li>
                                <li><a href="/1/1787.html" title="斗破苍穹 第一千四百九十五章   妖圣VS妖火" target="_blank">第一千四百九十五章   妖圣VS妖火</a></li>
                                <li><a href="/1/1788.html" title="斗破苍穹 第一千四百九十六章  剥离" target="_blank">第一千四百九十六章  剥离</a></li>
                                <li><a href="/1/1789.html" title="斗破苍穹 第一千四百九十七章   最终获利" target="_blank">第一千四百九十七章   最终获利</a></li>
                                <li><a href="/1/1790.html" title="斗破苍穹 第一千四百九十八章   炼化妖火！" target="_blank">第一千四百九十八章   炼化妖火！</a></li>
                                <li><a href="/1/1791.html" title="斗破苍穹 第一千四百九十九章   中州事变" target="_blank">第一千四百九十九章   中州事变</a></li>
                                <li><a href="/1/1792.html" title="斗破苍穹 第一千五百章   破茧而出" target="_blank">第一千五百章   破茧而出</a></li>
                                <li><a href="/1/1793.html" title="斗破苍穹 第一千五百零一章   火婴" target="_blank">第一千五百零一章   火婴</a></li>
                                <li><a href="/1/1794.html" title="斗破苍穹 第一千五百零二章  妖火平原" target="_blank">第一千五百零二章  妖火平原</a></li>
                                <li><a href="/1/1795.html" title="斗破苍穹 第一千五百零三章  翻手灭殿" target="_blank">第一千五百零三章  翻手灭殿</a></li>
                                <li><a href="/1/1796.html" title="斗破苍穹 第一千五百零四章  风雨欲来" target="_blank">第一千五百零四章  风雨欲来</a></li>
                                <li><a href="/1/1797.html" title="斗破苍穹 第一千五百零五章   回家" target="_blank">第一千五百零五章   回家</a></li>
                                <li><a href="/1/1798.html" title="斗破苍穹 第一千五百零六章 战帖！" target="_blank">第一千五百零六章 战帖！</a></li>
                                <li><a href="/1/1799.html" title="斗破苍穹 第一千五百零七章  陨落之巅" target="_blank">第一千五百零七章  陨落之巅</a></li>
                                <li><a href="/1/1800.html" title="斗破苍穹 第一千五百零八章   魂千陌" target="_blank">第一千五百零八章   魂千陌</a></li>
                                <li><a href="/1/1801.html" title="斗破苍穹 第一千五百零九章  交锋" target="_blank">第一千五百零九章  交锋</a></li>
                                <li><a href="/1/1802.html" title="斗破苍穹 第一千五百一十章   平一局" target="_blank">第一千五百一十章   平一局</a></li>
                                <li><a href="/1/1803.html" title="斗破苍穹 第一千五百一十一章   最后一局" target="_blank">第一千五百一十一章   最后一局</a></li>
                                <li><a href="/1/1804.html" title="斗破苍穹 第一千五百一十二章   萧炎VS魂殿殿主" target="_blank">第一千五百一十二章   萧炎VS魂殿殿主</a></li>
                                <li><a href="/1/1805.html" title="斗破苍穹 第一千五百一十三章  虚无吞炎" target="_blank">第一千五百一十三章  虚无吞炎</a></li>
                                <li><a href="/1/1806.html" title="斗破苍穹 第一千五百一十四章   小伊显威" target="_blank">第一千五百一十四章   小伊显威</a></li>
                                <li><a href="/1/1807.html" title="斗破苍穹 第一千五百一十五章   分出胜负" target="_blank">第一千五百一十五章   分出胜负</a></li>
                                <li><a href="/1/1808.html" title="斗破苍穹 第一千五百一十六章   下杀手" target="_blank">第一千五百一十六章   下杀手</a></li>
                                <li><a href="/1/1809.html" title="斗破苍穹 第一千五百一十七章   黑色珠子" target="_blank">第一千五百一十七章   黑色珠子</a></li>
                                <li><a href="/1/1810.html" title="斗破苍穹 第一千五百一十八章  传信" target="_blank">第一千五百一十八章  传信</a></li>
                                <li><a href="/1/1811.html" title="斗破苍穹 第一千五百一十九章   凰天" target="_blank">第一千五百一十九章   凰天</a></li>
                                <li><a href="/1/1812.html" title="斗破苍穹 第一千五百二十章   两族对恃" target="_blank">第一千五百二十章   两族对恃</a></li>
                                <li><a href="/1/1813.html" title="斗破苍穹 第一千五百二十一章  交手" target="_blank">第一千五百二十一章  交手</a></li>
                                <li><a href="/1/1814.html" title="斗破苍穹 第一千五百二十二章   九色光柱" target="_blank">第一千五百二十二章   九色光柱</a></li>
                                <li><a href="/1/1815.html" title="斗破苍穹 第一千五百二十三章    彩鳞出关" target="_blank">第一千五百二十三章    彩鳞出关</a></li>
                                <li><a href="/1/1816.html" title="斗破苍穹 第一千五百二十四章   变故" target="_blank">第一千五百二十四章   变故</a></li>
                                <li><a href="/1/1817.html" title="斗破苍穹 第一千五百二十五章   化龙魔阵" target="_blank">第一千五百二十五章   化龙魔阵</a></li>
                                <li><a href="/1/1818.html" title="斗破苍穹 第一千五百二十六章   毁灭火体" target="_blank">第一千五百二十六章   毁灭火体</a></li>
                                <li><a href="/1/1819.html" title="斗破苍穹 第一千五百二十七章   疯狂的北龙王" target="_blank">第一千五百二十七章   疯狂的北龙王</a></li>
                                <li><a href="/1/1820.html" title="斗破苍穹 第一千五百二十八章   击杀" target="_blank">第一千五百二十八章   击杀</a></li>
                                <li><a href="/1/1821.html" title="斗破苍穹 第一千五百二十九章   炼制傀儡" target="_blank">第一千五百二十九章   炼制傀儡</a></li>
                                <li><a href="/1/1822.html" title="斗破苍穹 第一千五百三十章   北王" target="_blank">第一千五百三十章   北王</a></li>
                                <li><a href="/1/1823.html" title="斗破苍穹 第一千五百三十一章   吞噬黑魔雷" target="_blank">第一千五百三十一章   吞噬黑魔雷</a></li>
                                <li><a href="/1/1824.html" title="斗破苍穹 第一千五百三十二章   九玄金雷" target="_blank">第一千五百三十二章   九玄金雷</a></li>
                                <li><a href="/1/1825.html" title="斗破苍穹 第一千五百三十三章   聚灵" target="_blank">第一千五百三十三章   聚灵</a></li>
                                <li><a href="/1/1826.html" title="斗破苍穹 第一千五百三十四章   九玄金雷的力量" target="_blank">第一千五百三十四章   九玄金雷的力量</a></li>
                                <li><a href="/1/1827.html" title="斗破苍穹 第一千五百三十五章   变化" target="_blank">第一千五百三十五章   变化</a></li>
                                <li><a href="/1/1828.html" title="斗破苍穹 第一千五百三十六章  平静" target="_blank">第一千五百三十六章  平静</a></li>
                                <li><a href="/1/1829.html" title="斗破苍穹 第一千五百三十七章   药族药典" target="_blank">第一千五百三十七章   药族药典</a></li>
                                <li><a href="/1/1830.html" title="斗破苍穹 第一千五百三十八章   出手" target="_blank">第一千五百三十八章   出手</a></li>
                                <li><a href="/1/1831.html" title="斗破苍穹 第一千五百三十九章   凶悍" target="_blank">第一千五百三十九章   凶悍</a></li>
                                <li><a href="/1/1832.html" title="斗破苍穹 第一千五百四十章    万火长老" target="_blank">第一千五百四十章    万火长老</a></li>
                                <li><a href="/1/1833.html" title="斗破苍穹 第一千五百四十一章 魂虚子" target="_blank">第一千五百四十一章 魂虚子</a></li>
                                <li><a href="/1/1834.html" title="斗破苍穹 第一千五百四十二章   药典开始" target="_blank">第一千五百四十二章   药典开始</a></li>
                                <li><a href="/1/1835.html" title="斗破苍穹 第一千五百四十三章   讨教" target="_blank">第一千五百四十三章   讨教</a></li>
                                <li><a href="/1/1836.html" title="斗破苍穹 第一千五百四十四章  生灵之焱" target="_blank">第一千五百四十四章  生灵之焱</a></li>
                                <li><a href="/1/1837.html" title="斗破苍穹 第一千五百四十五章   炼丹较量" target="_blank">第一千五百四十五章   炼丹较量</a></li>
                                <li><a href="/1/1838.html" title="斗破苍穹 第一千五百四十六章     抢夺能量" target="_blank">第一千五百四十六章     抢夺能量</a></li>
                                <li><a href="/1/1839.html" title="斗破苍穹 第一千五百四十七章   丹雨" target="_blank">第一千五百四十七章   丹雨</a></li>
                                <li><a href="/1/1840.html" title="斗破苍穹 第一千五百四十八章  借玉" target="_blank">第一千五百四十八章  借玉</a></li>
                                <li><a href="/1/1841.html" title="斗破苍穹 第一千五百四十九章   惊变" target="_blank">第一千五百四十九章   惊变</a></li>
                                <li><a href="/1/1842.html" title="斗破苍穹 第一千五百五十章  本体" target="_blank">第一千五百五十章  本体</a></li>
                                <li><a href="/1/1843.html" title="斗破苍穹 第一千五百五十一章   药帝残魂" target="_blank">第一千五百五十一章   药帝残魂</a></li>
                                <li><a href="/1/1844.html" title="斗破苍穹 愿望终达成。" target="_blank">愿望终达成。</a></li>
                                <li><a href="/1/1845.html" title="斗破苍穹 第一千五百五十二章   吞灵" target="_blank">第一千五百五十二章   吞灵</a></li>
                                <li><a href="/1/1846.html" title="斗破苍穹 第一千五百五十三章   灭族之战" target="_blank">第一千五百五十三章   灭族之战</a></li>
                                <li><a href="/1/1847.html" title="斗破苍穹 第一千五百五十四章   借火" target="_blank">第一千五百五十四章   借火</a></li>
                                <li><a href="/1/1848.html" title="斗破苍穹 第一千五百五十五章   八色火莲" target="_blank">第一千五百五十五章   八色火莲</a></li>
                                <li><a href="/1/1849.html" title="斗破苍穹 第一千五百五十六章    逃生" target="_blank">第一千五百五十六章    逃生</a></li>
                                <li><a href="/1/1850.html" title="斗破苍穹 第一千五百五十七章   吞服" target="_blank">第一千五百五十七章   吞服</a></li>
                                <li><a href="/1/1851.html" title="斗破苍穹 第一千五百五十八章   逃" target="_blank">第一千五百五十八章   逃</a></li>
                                <li><a href="/1/1852.html" title="斗破苍穹 第一千五百五十九章   击退" target="_blank">第一千五百五十九章   击退</a></li>
                                <li><a href="/1/1853.html" title="斗破苍穹 第一千五百六十章   再进古界" target="_blank">第一千五百六十章   再进古界</a></li>
                                <li><a href="/1/1854.html" title="斗破苍穹 第一千五百六十一章   魂族之秘" target="_blank">第一千五百六十一章   魂族之秘</a></li>
                                <li><a href="/1/1855.html" title="斗破苍穹 第一千五百六十二章   六星中期" target="_blank">第一千五百六十二章   六星中期</a></li>
                                <li><a href="/1/1856.html" title="斗破苍穹 第一千五百六十三章   雷动" target="_blank">第一千五百六十三章   雷动</a></li>
                                <li><a href="/1/1857.html" title="斗破苍穹 第一千五百六十四章   出手" target="_blank">第一千五百六十四章   出手</a></li>
                                <li><a href="/1/1858.html" title="斗破苍穹 第一千五百六十五章   赐教" target="_blank">第一千五百六十五章   赐教</a></li>
                                <li><a href="/1/1859.html" title="斗破苍穹 第一千五百六十六章  窥视" target="_blank">第一千五百六十六章  窥视</a></li>
                                <li><a href="/1/1860.html" title="斗破苍穹 第一千五百六十七章   古怪" target="_blank">第一千五百六十七章   古怪</a></li>
                                <li><a href="/1/1861.html" title="斗破苍穹 第一千五百六十八章   搜寻" target="_blank">第一千五百六十八章   搜寻</a></li>
                                <li><a href="/1/1862.html" title="斗破苍穹 第一千五百六十九章   夺玉" target="_blank">第一千五百六十九章   夺玉</a></li>
                                <li><a href="/1/1863.html" title="斗破苍穹 第一千五百七十章   失玉" target="_blank">第一千五百七十章   失玉</a></li>
                                <li><a href="/1/1864.html" title="斗破苍穹 第一千五百七十一章   商议" target="_blank">第一千五百七十一章   商议</a></li>
                                <li><a href="/1/1865.html" title="斗破苍穹 第一千五百七十二章   再进天墓" target="_blank">第一千五百七十二章   再进天墓</a></li>
                                <li><a href="/1/1866.html" title="斗破苍穹 第一千五百七十三章   本源帝气" target="_blank">第一千五百七十三章   本源帝气</a></li>
                                <li><a href="/1/1867.html" title="斗破苍穹 第一千五百七十四章  天墓之魂" target="_blank">第一千五百七十四章  天墓之魂</a></li>
                                <li><a href="/1/1868.html" title="斗破苍穹 第一千五百七十五章    抽取灵魂本源" target="_blank">第一千五百七十五章    抽取灵魂本源</a></li>
                                <li><a href="/1/1869.html" title="斗破苍穹 第一千五百七十六章   帝境灵魂" target="_blank">第一千五百七十六章   帝境灵魂</a></li>
                                <li><a href="/1/1870.html" title="斗破苍穹 第一千五百七十七章   出天墓" target="_blank">第一千五百七十七章   出天墓</a></li>
                                <li><a href="/1/1871.html" title="斗破苍穹 第一千五百七十八章    大战前夕" target="_blank">第一千五百七十八章    大战前夕</a></li>
                                <li><a href="/1/1872.html" title="斗破苍穹 第一千五百七十九章    大军出动" target="_blank">第一千五百七十九章    大军出动</a></li>
                                <li><a href="/1/1873.html" title="斗破苍穹 第一千五百八十章   葬天山脉" target="_blank">第一千五百八十章   葬天山脉</a></li>
                                <li><a href="/1/1874.html" title="斗破苍穹 第一千五百八十一章   父子相见（明天请一天假）" target="_blank">第一千五百八十一章   父子相见（明天请一天假）</a></li>
                                <li><a href="/1/1875.html" title="斗破苍穹 第一千五百八十二章    大战" target="_blank">第一千五百八十二章    大战</a></li>
                                <li><a href="/1/1876.html" title="斗破苍穹 第一千五百八十三章   魂元天" target="_blank">第一千五百八十三章   魂元天</a></li>
                                <li><a href="/1/1877.html" title="斗破苍穹 第一千五百八十四章 死寂之门" target="_blank">第一千五百八十四章 死寂之门</a></li>
                                <li><a href="/1/1878.html" title="斗破苍穹 第一千五百八十五章   据为己有" target="_blank">第一千五百八十五章   据为己有</a></li>
                                <li><a href="/1/1879.html" title="斗破苍穹 第一千五百八十六章   破界" target="_blank">第一千五百八十六章   破界</a></li>
                                <li><a href="/1/1880.html" title="斗破苍穹 第一千五百八十七章   退走" target="_blank">第一千五百八十七章   退走</a></li>
                                <li><a href="/1/1881.html" title="斗破苍穹 第一千五百八十八章   定计" target="_blank">第一千五百八十八章   定计</a></li>
                                <li><a href="/1/1882.html" title="斗破苍穹 第一千五百八十九章  宁静" target="_blank">第一千五百八十九章  宁静</a></li>
                                <li><a href="/1/1883.html" title="斗破苍穹 第一千五百九十章   雷劫丹" target="_blank">第一千五百九十章   雷劫丹</a></li>
                                <li><a href="/1/1884.html" title="斗破苍穹 第一千五百九十一章 七星斗圣" target="_blank">第一千五百九十一章 七星斗圣</a></li>
                                <li><a href="/1/1885.html" title="斗破苍穹 第一千五百九十二章  探测古帝洞府" target="_blank">第一千五百九十二章  探测古帝洞府</a></li>
                                <li><a href="/1/1886.html" title="斗破苍穹 第一千五百九十三章    古帝洞府所在（此章免费！）" target="_blank">第一千五百九十三章    古帝洞府所在（此章免费！）</a></li>
                                <li><a href="/1/1887.html" title="斗破苍穹 第一千五百九十三章 古帝洞府所在" target="_blank">第一千五百九十三章 古帝洞府所在</a></li>
                                <li><a href="/1/1888.html" title="斗破苍穹 第一千五百九十四章  黑角域之难" target="_blank">第一千五百九十四章  黑角域之难</a></li>
                                <li><a href="/1/1889.html" title="斗破苍穹 第一千五百九十五章  赶至" target="_blank">第一千五百九十五章  赶至</a></li>
                                <li><a href="/1/1890.html" title="斗破苍穹 第一千五百九十六章 故人再见" target="_blank">第一千五百九十六章 故人再见</a></li>
                                <li><a href="/1/1891.html" title="斗破苍穹 第一千五百九十七章   再入岩浆世界" target="_blank">第一千五百九十七章   再入岩浆世界</a></li>
                                <li><a href="/1/1892.html" title="斗破苍穹 第一千五百九十八章  岩浆之底的空间" target="_blank">第一千五百九十八章  岩浆之底的空间</a></li>
                                <li><a href="/1/1893.html" title="斗破苍穹 第一千五百九十九章   神秘生物" target="_blank">第一千五百九十九章   神秘生物</a></li>
                                <li><a href="/1/1894.html" title="斗破苍穹 第一千六百章  对话" target="_blank">第一千六百章  对话</a></li>
                                <li><a href="/1/1895.html" title="斗破苍穹 第一千六百零一章  大战来临！" target="_blank">第一千六百零一章  大战来临！</a></li>
                                <li><a href="/1/1896.html" title="斗破苍穹 第一千六百零二章 洞府之战！" target="_blank">第一千六百零二章 洞府之战！</a></li>
                                <li><a href="/1/1897.html" title="斗破苍穹 第一千六百零三章   以一敌二" target="_blank">第一千六百零三章   以一敌二</a></li>
                                <li><a href="/1/1898.html" title="斗破苍穹 第一千六百零四章   洞府出现" target="_blank">第一千六百零四章   洞府出现</a></li>
                                <li><a href="/1/1899.html" title="斗破苍穹 第一千六百零五章   危机关头" target="_blank">第一千六百零五章   危机关头</a></li>
                                <li><a href="/1/1900.html" title="斗破苍穹 第一千六百零六章  老龙皇" target="_blank">第一千六百零六章  老龙皇</a></li>
                                <li><a href="/1/1901.html" title="斗破苍穹 第一千六百零七章   古帝洞府开启" target="_blank">第一千六百零七章   古帝洞府开启</a></li>
                                <li><a href="/1/1902.html" title="斗破苍穹 第一千六百零八章   异火广场" target="_blank">第一千六百零八章   异火广场</a></li>
                                <li><a href="/1/1903.html" title="斗破苍穹 第一千六百零九章  恐怖的帝品雏丹" target="_blank">第一千六百零九章  恐怖的帝品雏丹</a></li>
                                <li><a href="/1/1904.html" title="斗破苍穹 第一千六百一十章  抢夺帝品雏丹" target="_blank">第一千六百一十章  抢夺帝品雏丹</a></li>
                                <li><a href="/1/1905.html" title="斗破苍穹 第一千六百一十一章  失手" target="_blank">第一千六百一十一章  失手</a></li>
                                <li><a href="/1/1906.html" title="斗破苍穹 第一千六百一十二章 魂天帝的野心" target="_blank">第一千六百一十二章 魂天帝的野心</a></li>
                                <li><a href="/1/1907.html" title="斗破苍穹 第一千六百一十三章 中州之难" target="_blank">第一千六百一十三章 中州之难</a></li>
                                <li><a href="/1/1908.html" title="斗破苍穹 第一千六百一十四章 异火榜第一！" target="_blank">第一千六百一十四章 异火榜第一！</a></li>
                                <li><a href="/1/1909.html" title="斗破苍穹 第一千六百一十五章  帝之本源" target="_blank">第一千六百一十五章  帝之本源</a></li>
                                <li><a href="/1/1910.html" title="斗破苍穹 第一千六百一十六章 古帝传承" target="_blank">第一千六百一十六章 古帝传承</a></li>
                                <li><a href="/1/1911.html" title="斗破苍穹 第一千六百一十七章   源气" target="_blank">第一千六百一十七章   源气</a></li>
                                <li><a href="/1/1912.html" title="斗破苍穹 第一千六百一十八章  浩劫" target="_blank">第一千六百一十八章  浩劫</a></li>
                                <li><a href="/1/1913.html" title="斗破苍穹 第一千六百一十九章  魂帝，魂天帝！" target="_blank">第一千六百一十九章  魂帝，魂天帝！</a></li>
                                <li><a href="/1/1914.html" title="斗破苍穹 两年三个月，五百三十万。" target="_blank">两年三个月，五百三十万。</a></li>
                                <li><a href="/1/1915.html" title="斗破苍穹 第一千六百二十章  斗帝强者的力量！" target="_blank">第一千六百二十章  斗帝强者的力量！</a></li>
                                <li><a href="/1/1916.html" title="斗破苍穹 新书已发~~~" target="_blank">新书已发~~~</a></li>
                                <li><a href="/1/1917.html" title="斗破苍穹 第一千六百二十一章  出关！" target="_blank">第一千六百二十一章  出关！</a></li>
                                <li><a href="/1/1918.html" title="斗破苍穹 今天晚上七点半，斗破在线大活动。" target="_blank">今天晚上七点半，斗破在线大活动。</a></li>
                                <li><a href="/1/1919.html" title="斗破苍穹 第一千六百二十二章   双帝之战！（上）" target="_blank">第一千六百二十二章   双帝之战！（上）</a></li>
                                <li><a href="/1/1920.html" title="斗破苍穹 第一千六百二十三章 双帝之战！（下）" target="_blank">第一千六百二十三章 双帝之战！（下）</a></li>
                                <li><a href="/1/1921.html" title="斗破苍穹 第一千六百二十三章  结束，也是开始。" target="_blank">第一千六百二十三章  结束，也是开始。</a></li>
                                <li><a href="/1/1922.html" title="斗破苍穹 感言。" target="_blank">感言。</a></li>
                                <li><a href="/1/1923.html" title="斗破苍穹 第一章  五帝破空" target="_blank">第一章  五帝破空</a></li>
                                <li><a href="/1/1924.html" title="斗破苍穹 新书大主宰已发。" target="_blank">新书大主宰已发。</a></li>
                                <li><a href="/1/1925.html" title="斗破苍穹 萧玄魂天帝篇" target="_blank">萧玄魂天帝篇</a></li>
                                <li><a href="/1/1926.html" title="斗破苍穹 萧炎云韵篇" target="_blank">萧炎云韵篇</a></li>
                                <li><a href="/1/1927.html" title="斗破苍穹 《斗破苍穹：斗帝之路》手游·角色传记（上）" target="_blank">《斗破苍穹：斗帝之路》手游·角色传记（上）</a></li>
                                <li><a href="/1/1928.html" title="斗破苍穹 《斗破苍穹：斗帝之路》手游·角色传记（下）" target="_blank">《斗破苍穹：斗帝之路》手游·角色传记（下）</a></li>
                                <li><a href="/1/1929.html" title="斗破苍穹 新书元尊已在起点上传，欢迎大家阅读。" target="_blank">新书元尊已在起点上传，欢迎大家阅读。</a></li>
                            </ul>"""
#print(url)
r = '[\s\S]*?'
pattern1 = re.compile(r'<a href="({})"{}>{}</a>'.format(r,r,r))
pattern2 = re.compile(r'<a href="{}"{}>({})</a>'.format(r,r,r))
url = pattern1.findall(html)
name = pattern2.findall(html)
URL = []
NAME = []
dict_list = []
for i in url:
    URL.append("https://doupocangqiong1.com{}".format(i))
#print(URL)
for j in name:
    NAME.append("章节名字：{}".format(j))
dict_list = list(map(lambda t:dict([t]),zip(URL,NAME)))
for dict in dict_list:
    print(dict)

