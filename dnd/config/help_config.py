COM_HELP = {'.r': '投骰子 例如.r3#d20+(d6+4)*2 骰三次d20+（d6+4）*2的结果集d20代表20面骰 d6代表6面骰 ', '.jrrp': '查看用户今日运势 不与角色挂钩',
            '.help ': '查询dnd先关说明 例如.help 战士', '!dnd': '随机生成一套属性 纯功能不予角色挂钩',
            '.gen 姓名': '生成一个新角色', '.reroll': '重投当前角色的基础属性', '.attrup ': '选择属性进行提升，尽在有通知时可以使用 例如.attrup 力量 敏捷',
            '.attr': '查看当前角色全部属性', '.swap 属性A 属性B': '交换当前角色两种属性的值',
            '.language': '选择语言，仅当通知中提示选择语言时可以使用 例如.language 龙族语', '.ul': '查看用户列表', '.switch ': '切换用户 例如.switch 泽伦斯',
            '.race ': '设置种族 仅在创建角色时可以使用 例如.race 矮人', '.job ': '设置职业 仅在创建角色时可以使用 例如.job 战士',
            '.subrace': '选择亚种 仅在通知中出现时可以使用 例如.subrace 山地矮人',
            '.check': '进行检定 例如.check*2+2d6+1 力量豁免 进行两次力量豁免检定享受2d6+1的激励加值 取高者'}

HELPER = {
    # 职业
    '战士': '战士\n \n穿着厚重板甲的人类持盾在前冲入了大群地精中间。在她身后，身穿皮甲的精灵用他精制的弓向地精射出连珠箭矢。他们附近还有名半兽人喊着口号，帮助这两位勇士协作杀敌。\n 身着链甲的矮人举盾站在他的伙伴和食人魔之间，挡开敌人致命的攻击。他的同伴，一名穿着鳞甲的半精灵，两把弯刀翻飞如风，在巨魔身边游弋寻找他疏于防御的时机。\n 一名在竞技场中搏斗的角斗士，三叉戟和捕网用的出神入化，精于摔绊敌人并拖着他绕场移动的技巧————这既为他赢得了观众的喝彩，也让他在战斗中保持优势。他的对手剑上一点蓝芒闪过，随即一道闪电向他射来。\n 这些就是战士，也许是龙与地下城的世界中最具多样性的职业。无论是四处探索的骑士或是到处征伐的领主，皇家勇士或是精英步兵，冷酷的雇佣兵还是还是山贼王————作为战士，他们都拥有高超的武艺，以及全面的战斗知识。他们熟悉死亡，无惧的面对并且挑战它。\n \n主属性：力量或敏捷\n \n豁免：力量、体制\n \n生命值\n 生命骰：１ｄ１０每战士等级\n 1级生命值：１０＋体质调整值\n 升级生命值：每战士等级１ｄ１０（或６）＋体质调整值\n',
    '游侠': '游侠\n \n一个相貌粗野的人类在树丛的阴影间穿行，对一群将要袭击附近村庄的兽人们展开追捕。他双手各持一柄短剑，像钢铁的狂风一般将敌人接连斩杀。\n 避开一团霜冻气息后，一名精灵再度站稳，拉开她的弓，将一支箭送向白龙的方向。无视巨龙散发着的恐惧气息和吐息带来的寒冷，她将箭矢一支接一支地射入巨龙鳞片的缝隙中。\n 一名半精灵高举着手臂，用口哨将盘旋在他头顶的猎鹰召回身边。在用精灵语下达了指令后，他指向了自己正在追踪的那只枭熊，准备好自己的弓箭，让猎鹰去吸引注意力。\n 远离城市与乡镇的喧嚣还有那隔绝危险的荒野的围墙，游侠们在茂密的森林中和广袤的原野上继续着他们无尽的守望。（此段由Palantir提供翻译）\n \n主属性：敏捷\n \n豁免：敏捷、力量\n \n生命值\n 生命骰：1d10每游侠等级\n 1级生命值：10+体质调整值\n 升级生命值：每游侠等级1d10（或6）＋体质调整值\n',
    '游荡者': '游荡者\n \n示意她的同伴等待，一名半身人匍匐前进穿过地城大厅。她将一只耳朵贴在门上，然后掏出一套工具并在眨眼间撬开了锁。紧接着她消失在阴影之中，而她的战士朋友走上前来一脚踢开了门。\n 当一名人类隐藏在一条小巷的阴影中的时候，他的同伙正在准备着在这次伏击中她负责的部分。当他们的目标－－一个声名狼藉的奴隶贩子－－穿过这条巷道的时候，同伙大声呼喊起来，吸引这名奴隶贩子前来查探，然后刺客之刃在他能发出声音之前割断了他的咽喉。\n 一名侏儒忍住笑声，摇晃着他的手指然后魔术般地从守卫的腰带上抬起钥匙环。下一刻，钥匙出现在了他的手上，房门被打开，而她和她的同伴们已经自由了。\n 游荡者依赖于利用技能，隐匿，和他们敌人的弱点以在任何情况下建立优势。他们有找到所有问题的解决办法的本领，证明了足智多谋和多才多艺是一个成功的冒险团队的基础。\n \n主属性：敏捷\n \n豁免：敏捷、智力\n \n生命值\n 生命骰：每游荡者等级１ｄ８\n 首级生命值：８＋体质调整值\n 高级生命值：１级后每游荡者等级１ｄ８（或者５）＋体质调整值\n',
    '吟游诗人': '吟游诗人 Bard\n \n远地废墟中，她的手指在一座古旧的纪念碑上徐徐划过，身着毛皮的半精灵在此寻求刻骨铭心的英知，并尝试用音乐和魔法将它展现再世——那些古圣先贤记载在纪念碑上的传奇和它所赞颂的诗篇。\n 面容坚定的人类战士有节奏地用长剑敲击自己的鳞甲，随着节拍吟诵英雄史诗鼓励他的伙伴要记住勇气和信念。音乐之中的魔力渐渐笼罩了他们。\n 欢笑着她拨动琴弦，侏儒小姐巧妙地将魔力隐藏在音乐中，影响着那些群聚的贵族，让他们可以接受伙伴们的话语。\n 无论是学者、歌者、还是无赖，诗人们用他们包含魔力的语言和音乐来激励伙伴，或削弱敌人，或操控心灵，或创造幻象，甚至治愈伤口。\n \n主属性：魅力\n \n豁免：魅力、敏捷\n \n生命值\n 生命骰：每吟游诗人等级１ｄ８\n 首级生命值：８＋你的体质调整值\n 其后生命值：每吟游诗人等级１ｄ８（或５）＋你的体质调整值\n',
    '野蛮人': '野蛮人（Barbarian）\n \n高大的男人披裘执斧在暴风雪中奔走，大笑着冲向那些胆敢偷猎他族人饲养的麋鹿的霜巨人。\n 半兽人朝着胆敢挑战自己在部落中权威的对手咆哮，准备徒手扭断他的脖子————正如她对前六个挑战者做的那样。\n 矮人口沫横飞的把头盔拍在一名卓尔敌人脸上，转身又用铠甲包裹的肘部撞向另一只。\n 野蛮人们彼此不同，但他们却都有这标志性的暴怒：无虑，无驭，无尽的怒火。对于野蛮人，愤怒并不仅仅是一种情感，而是猎食者走投无路时爆发的狂怒，是暴风雨般不顾一切的猛袭，也是大海中翻滚不息的波涛。\n 一些野蛮人认为他们的愤怒之力来自于和猛兽之灵的交流，其他则认为那来自于对世间无尽苦痛的愤恨。对野蛮人来说，狂暴并不止点燃了他们的战斗狂热，也是他们灵活闪避，抵挡伤害和增强力量的源泉。\n \n主属性：力量\n \n豁免：力量，体质\n \n生命值\n 生命骰：１ｄ１２每野蛮人等级\n １级生命值：１２＋体质调整值\n 升级生命值：每野蛮人等级１ｄ１２（或７）＋体质调整值\n \n \n',
    '武僧': '武僧\n \n她双掌如电，眨眼之间拍飞袭来之箭，这名半精灵随后冲出掩体，投身进大片大地精的战团中。她轮圆自己的胳膊，挨个赏赐每个大地精一巴掌，将它们全都扇倒在地，仅剩自己站立当场。\n 深呼一口气，一名人纹身人类摆好架势。面对第一个冲锋过来的兽人，他张口一吐，喷发出火焰咆哮，吞没了面前的敌人。\n 作为暗夜中的无声黑影，黑衣半精灵跳进拱门下的一抹影子中，随后瞬间出现在另外一个阳台下的墨色之中。悄无声息得从黑袍下特制刀鞘中抽出短刃，拨开窗户——让室内的暴君今夜之后陷入入眠吧。\n 经过各种训练之后，武僧对于操控体内的那股能量有了高度的认识。无论是引导它加强战斗技艺，还是精妙地将它集中于防御和移动，这股能量全面加强了武僧。\n \n主属性：敏捷\n \n豁免：敏捷、力量\n \n生命值\n 生命骰：每武僧等级１ｄ８\n 首级生命值：8+你的体质调整值\n 升级生命值：每武僧等级１ｄ８（或５）＋你的体质调整值\n',
    '术士': '术士 SORCERER\n \n眼中闪过一道金光，那人类女孩伸出手，释放出血脉中龙族的烈焰。当这地狱狂怒般的业火吞噬敌人时，女孩背后生出革质的双翼，一飞冲天。\n 长发在咒法唤来的烈风中飘扬，半精灵张开双臂，高高扬起下巴。涌动的魔法使他暂时双脚离地，而魔力之潮从他体内涌起，流过四肢百骸喷薄而出，化作威力无穷的闪电。\n 躲在石笋后，半身人伸出手指，指着冲锋的穴居人。一道火焰从她指间爆发而出，击中了那只生物。她迅速躲回巨石后面，脸上带着一个微笑——却没有发现狂野魔法已经把她的皮肤变成了蓝色。\n 术士驾驭着与生俱来的魔法。这种魔法，可能来自超自然的血脉，来自异界的影响，或者来自暴露于某种未知的大宇宙力量的经历。你不可能像学习语言一样学习术法，正如你不可能学习如何度过传奇般的人生。没有人选择术法；是术法选择了你。\n \n主属性：魅力\n \n豁免：魅力、体质\n \n生命值：\n 生命骰：1d6/术士等级\n 1级生命值：6+体质调整值\n 升级生命值：1d6（或4）+体质调整值 / 每术士等级\n',
    '圣武士': '圣武士\n \n板甲在阳光下虽仍闪光，却也已经被征尘蒙罩。但这位人类女士顾不上这许多。她抛下剑盾，将她的双手按在一个受了致命重伤的男人身上。神圣的光华在她的手上闪耀着，男人的伤口神奇地愈合了，他本已闭上的眼睛再次睁开——满溢着惊奇和喜悦。\n 矮人蹲伏在突出地面的巨岩后面，他漆黑的斗篷在黑夜中几不可见。他监视着一支兽人战团，这支战团正庆贺不久前的胜利。矮人站起身来，无声无息的潜入兽人们之中，低语着神圣的誓言。两名兽人倒地而死——至死都没有发现就站在那里的矮人。\n 银发在只照耀他一人的光辉下闪耀，随着骄傲和兴奋的笑声，精灵将如同他双眼般闪亮的长矛狠狠刺向那扭曲的巨人。他一次又一次刺向那怪物，直到他的圣光最终穿透了那丑陋的黑暗。\n 不论过往何如，不论身负何事，圣武士皆因其对抗邪恶的誓言而联合在一起。无论在神坛前，由牧师见证立下神圣誓言；抑或在林中圣地，向自然精魂许下承诺；又或在悲哀与绝望之刻立誓，而死亡是唯一的见证；圣武士之誓言都是极具力量的契约。正是誓言的伟力，将一名虔诚的战士化作身负祝福的斗士。\n \n主属性：力量\n \n豁免：感知、魅力\n \n生命值：\n 生命骰：1d10/圣武士等级\n 1级生命值：10+体质调整值\n 升级生命值：【1d10（或6）+体质调整值】/每个1级以后的圣武士等级\n',
    '牧师': '牧师\n \n双手向上，眼望苍天，口中祈祷，一名精灵散发出浸满光芒的能量来医治他受伤的同伴。\n 吟诵荣耀之歌，一个矮人举起他的斧头挥砍周围的大批兽人敌人，每当敌人倒下都会大声叫喊他神祗的名字。\n 对着不死生物降下诅咒，一个人类举起他的圣徽，光芒从圣徽中溢出，那些爬向他同伴的僵尸们被驱逐了。\n 牧师是凡人世界和神祗世界的联系者，侍奉不同的神祗，牧师背负着神授予的不同的艰难任务。不像普通神父，牧师是神圣法术的施展者。\n \n主属性：感知\n \n豁免：感知、魅力\n \n生命值：\n 生命骰：1d8每牧师等级\n 1级起始生命值：8+你的体质调整\n 升级生命值：1d8（或5）+你的体质调整\n',
    '魔导士': '魔导士Warlock\n \n伪龙盘卧在他的肩膀上，这名一袭金色长袍的年轻精灵温和地微笑着，并将法咒融入甜言蜜语之中，使皇宫的卫兵屈从于他的意志。\n 火焰从一名削瘦的人类手中跃出，她的口中则默念着她邪魔宗主的秘名，并将炼狱的魔咒融入她的法术之中。\n 他的视线从一本残破的书册转到头顶怪异排布着的群星，这名目光中透着疯狂的魔裔咏唱着那开启远方世界门扉的神秘仪式。\n 魔导士是发掘在多元宇宙根源中所潜藏的知识的探索者。魔导士通过与超自然的神话存在结缔契约来了解微妙并壮观的魔法效果。从那些妖精贵族、恶魔、魔鬼、鬼婆、以及遥远国度的异界存在处获取远古的知识，魔导士将这些高深的奥秘互相交融，得以增强自己的力量。\n \n主属性：魅力\n \n豁免：感知、魅力\n \n生命值\n 生命骰：1d8/每魔导士等级\n 1级生命值：8+体质调整值\n 升级生命值：1d8（或5）+体质调整值/1级后的每个魔导士等级\n',
    '法师': '法师\n \n身着标示她地位的银色长袍，一位精灵闭上眼睛，摒除战场带来的杂念，并开始咏唱她的法术。随着手指在身前的舞动，她完成了她的法术，并向敌人的行列中掷去一个小小的，火焰构成的珠子，而这枚珠子转瞬间就爆发成一个巨大的火球，吞噬了那些士兵。\n 一遍又一遍检查着他的作品，一位人类法师在光滑的石地板上画出复杂的法阵，然后将铁粉撒过每一条直线，每一条优美的曲线。在法阵完成后，他念起长长的咒语。一个深不见底的洞在法阵中打开，带来一股来自另一个位面的，硫磺的气味。\n 趴在地下城中某个十字路口的地板上，一位侏儒将几块刻有神秘符记的骨头扔在地上，喃喃着充满力量的词句。他闭上眼睛，以便看得更清晰，然后慢慢点了点头，睁开眼睛，指向左面的路。\n 法师是最优秀的魔法使用者，按他们使用的魔法被定义和归类为一个职业。通过汲取那弥漫于整个宇宙的，精微奥妙的魔法之网的力量，法师用他们的法术唤来爆炸的火焰，噼啪作响的闪电，施加微妙的欺骗或强硬的精神控制。他们的魔法从其他存在的位面唤来恐怖的怪物，透过时间的缝隙瞥见未来，或者将敌人的尸体化作绝对听命的僵尸。他们最强大的法术可以将一种物质转化为另一种，可以从天空中唤来陨石，甚至撕裂次元的障壁，打开前往其他世界的传送门。\n \n主属性：智力\n \n豁免：智力、感知\n \n生命值：\n 生命骰：1d6/法师等级\n 1级生命值：6+体质调整值\n 升级生命值：1d6（或4）+体质调整值 /每个1级以后的法师等级\n',
    '德鲁伊': '德鲁伊\n \n伴随着圣言高举多节杖，一个精灵召唤风暴之怒并且降下闪电惩罚那些摧毁她森林的兽人们。\n 在视野之外高高的树枝上，以豹形态蜷缩着，一个人类凝视着丛林之外的邪恶气元素神殿，密切关注着那里的信徒。\n 以火焰形态挥舞着利刃，一个半精灵冲进白骨士兵群中，劈开这些邪恶的生物。\n 无论是呼唤自然界的元素之力，还是模仿动物世界中的生物，德鲁伊是自然变化的体现，狡猾而凶暴。他们对自然无欲无求。相对的，他们将自己视为自然不屈意志的延伸。\n \n主属性：感知\n \n豁免：感知、智力\n \n生命值\n 生命骰：每德鲁伊等级１ｄ８\n 首级生命值：８＋体质调整值\n 升级生命值：１级后每德鲁伊等级１ｄ８（或者５）＋体质调整值\n',
    # 种族
    '侏儒': '侏儒 Gnome \n \n在侏儒们的紧密群落里，由于忙碌工作而发出的不间断的嗡嗡声弥漫在拥挤的公寓社区及周边。更响亮的声音时不时插入进这嗡嗡声中：这边传来齿轮吱嘎作响的研磨声，那边响起轻微的爆炸声，因喜悦或惊讶的尖叫声，尤其是迸发的笑声，各种声音交织在一起。侏儒们愉快的生活着，享受着发明、探索、研究、创造和游戏的每一刻。\n \n年龄： 侏儒成年的速率与人类相同，大多数的侏儒预计在40岁左右定居并像成人一样生活。他们能活到350到接近500岁。\n 阵营：守序、混乱\n 体型：侏儒平均在3~4尺高，约40磅。体型为小型。\n 速度：你的基本行走速度25尺\n 语言：通用语、侏儒语\n 种族亚种：在D&D世界中有两种亚种侏儒：林侏儒和岩侏儒。选择其中一种。\n \n技能：\n 属性值提升：你的智力+2.\n \n黑暗视觉：在昏暗照明下，你可以看清60尺内的东西，如同在明亮照明下；在黑暗中，你可以看清60尺内的东西，如同在昏暗照明下。在黑暗中时你无法辨别颜色，只能看到灰色的影子。\n \n侏儒狡黠：你对所有对抗魔法的智力，感知和魅力的豁免鉴定有优势。\n \n \n \n亚种：林侏儒\n 属性提升：你的敏捷+1\n 天生幻术师：你懂得小幻象术。相关魔法能力值是智力。\n 动物沟通：通过声音和手势，你能和小型或更小的野兽简单沟通。\n \n亚种：岩侏儒\n 属性提升：你的体质+1\n 工匠知识：当你进行关于魔法物品，炼金物品或是工艺元件的智力（历史）检定时，你可以加上两倍的熟练加值来代替原有的熟练加值。\n 修补匠：你熟练于匠人工具（修补工具）。用这些工具，你能用1小时时间和10金币价值的材料来创造一个超小型的发条机械装置（AC5,1hp）。这个装置在24小时后停止运转（除非你花1小时来修理它，让它保持运行），或者当你用动作来取消它，这时你能收回用来制造它的材料。同一时间你最多能激活3个这样的装置。\n 当你制造这个装置时，选择下列选项之一：\n 发条玩具： 这玩具可以是个机械的动物、怪物或人，例如青蛙、老鼠、鸟、龙或者士兵。当被放在地上时，这个玩具能在你的行动轮内随机向一个方向移动5尺，玩具发出噪声用来表现它模拟生物的叫声。\n \n打火机： 这个装置用产生微小的火焰，你可以用来点蜡烛，火炬或营火。使用装置需要动作。\n \n音乐盒： 当打开时，这个音乐盒以适中的音量奏响固定的一首的歌曲。当音乐播放完或者音乐盒被关闭时，便会停止。\n',
    '提夫林': '提夫林 Tiefling\n \n总是受到注视和私语，总是承受街上的暴力和侮辱，总是看到他人眼中的不信任和恐惧：这就是提夫林。雪上加霜的是，提夫林知道这是因为世代之前订下的契约将阿斯蒙蒂斯——九层地狱之主的精髓注入了他们的血脉。他们的外貌和本性并不是他们的错，而是远古罪孽的结果，然而他们、他们的子孙以及子孙的子孙将永远担负起这个重担。\n \n年龄：提夫林成年岁数和人类相仿，不过寿命会长数年。\n 阵营：邪恶\n 体型：提夫林和人类体型相近，都是中型。\n 速度：你的基本步行速度是30尺。\n 语言：通用语、地狱语\n \n技能：\n 属性值提升：你的智力增加1点，魅力增加2点。\n 黑暗视觉：在昏暗情况下你能看见60尺内的东西，犹如明亮情况一般，在黑暗情况下则犹如昏暗情况一般。在黑暗情况下你无法分辨颜色，只能辨识黑白。\n 地狱抗力：你对火焰伤害有抗力。\n 地狱遗赠：你懂得奇术（thaumaturgy）这个戏法。3级时，你每次长休息间能以2环法术施展一次炼狱喝斥（hellish rebuke）。5级时，你每次长休息间能施展一次黑暗术（darkness）。魅力是你的施法属性。\n',
    '人类': '人类 Human\n \n在大部分世界的创世史里，人类都是最年轻的常见种族，姗姗来迟兼且比矮人、精灵、巨龙都要短寿。也许是因为他们的有限岁月，他们会尽力燃烧仅存的有限年日。又或者也许他们觉得需要证明自己给宗祖种族看，为此用抢掠和贸易建立强大的王国。不论是甚么原因，人类是众世界的革新者、登峰者、先驱者。\n \n年龄：人类不到20 岁就成年，很少活到100 岁。\n 阵营：任意\n 体形：人类身高差距很大，由刚好5 尺到远超过6 尺。不论你有多高，你的体型为中型。\n 速度：你的基本行走速度是30 尺。\n 语言：你能说、读、写通用语和额外的一项自选语言。\n \n技能：\n 能力调整值：你的全部能力值 +1。\n',
    '龙裔': '龙裔 Dragonborn\n \n就如他们的名字所显示的，生而为龙的龙裔带着世俗对他们的偏见和误解行走在这个世界。由龙神或者龙类塑造的龙裔最初是从龙蛋中孵化而来的，他们结合了龙类和类人生物的最佳优点。一些龙裔是真龙的虔诚仆从，另一些则在伟大的战争中加入了士兵的行列，还有一些则四处漂泊，没有明确的生活目标。\n 年龄：年幼的龙裔成长速度很快，在孵化后几小时后就可以行走。在3岁的时候就达到了人类10岁儿童的体型和发育水平（development）。\n 阵营：龙裔的阵营趋于极端化，在善与恶之间无尽的战争中作出有意识的选择（分别通过代表巴哈姆特或是提亚马特）。绝大多数龙裔是善良的，但是那些选择支持提亚马特的龙裔会是可怕的恶棍。\n 速度：你的基本行走速度是为30尺\n 语言：通用语、龙语\n \n技能：\n 属性点数提升：你的力量点数增加2点，你的魅力点数增加1点。\n 龙族血统：你拥有巨龙的血统。在龙族血统表中选择一个龙类。你的喷吐武器和伤害抗性由所选择的龙的种类所决定，如表所示。\n 黑龙：强酸，30尺长5尺宽，线形(敏捷豁免)\n 蓝龙：闪电，30尺长5尺宽，线形(敏捷豁免)\n 黄铜龙：火焰，30尺长5尺宽，线形(敏捷豁免)\n 青铜龙：闪电，30尺长5尺宽，线形(敏捷豁免)\n 赤铜龙：强酸，30尺长5尺宽，线形(敏捷豁免)\n 金龙：火焰，15尺，锥形（敏捷豁免）  \n 绿龙：毒素，15尺，锥形（敏捷豁免）\n 红龙：火焰，15尺，锥形（敏捷豁免）\n 银龙：寒冷，15尺，锥形（敏捷豁免）\n 白龙：寒冷，15尺，锥形（敏捷豁免）\n 喷吐武器：你能够用行动来呼出破坏性的能量，你的龙族血统决定了吐息的范围、形状和伤害类型。当你使用你的喷吐武器，吐息范围内的每一个生物都必须做一次豁免检定，豁免的类型取决于你的龙族血统。这次豁免的DC=8+你的体质调整值+你的熟练加值。如果豁免失败，这个生物将会受到2d6点伤害。在6级时伤害增加到3d6，在11级增加到4d6，16级增加到5d6。当你使用过喷吐武器后，必须经过一次长休息或短休息后才能再次使用它。\n 伤害抵抗：你的龙族血统给你带来了相应的伤害类型的抵抗。\n \n \n',
    '精灵': '精灵 Elf\n \n精灵是一种奇幻的，有着超尘脱俗的优雅的生物。他们生活在这个世界，却又不完全属于这里。他们居住在有超凡之美的所在，那些远古森林的中心，或在那闪耀着仙灵之光的银色尖塔之下。在他们的家园，轻悠的音乐在空气中流淌，幽雅的芬芳从溪流中飘荡。精灵热爱着自然和魔法，热爱着艺术本身和它的作品，热爱着诗歌和音乐，热爱着这世界一切的美好存在。\n \n年龄：一般来说，精灵一般在100岁前后宣布成年，寿命可达750岁。\n 阵营：混乱阵营、善良阵营\n 体型：精灵的身高从不到5英尺到超过6英尺都有，他们身材纤细。你的体型是中体型。\n 速度：你的基础陆地移动速度是30尺。\n 语言：通用语、精灵语\n 亚种：精灵族自古以来的分离使得今天的精灵可以分为三个亚种：高等精灵，木精灵，和一般被称做卓尔的黑暗精灵。本文介绍了其中的两个亚种。在某些世界观中，这些亚种族会被进一步细分（如被遗忘的国度世界观中的日精灵和月精灵）。如果你愿意，你也可以选择这些进一步细分的亚种。\n \n技能：\n 属性值提升：你的敏捷+2.\n \n黑暗视觉：在昏暗照明下，你可以看清60尺内的东西，如同在明亮照明下；在黑暗中，你可以看清60尺内的东西，如同在昏暗照明下。在黑暗中时你无法辨别颜色，只能看到灰色的影子。\n \n敏锐感知：你对搜查技能熟练。\n \n妖精先祖：你对魅惑效果的豁免取得优势。你不会因魔法陷入睡眠。\n \n出神：精灵不需要睡觉取而代之的是冥想，保持半清醒状态，维持4个小时，以这种方式休息后，你获得人类睡眠8小时的全部好处。\n \n \n亚种：高等精灵\n 属性值提升：你的智力+1\n 熟练武器：你熟练于长剑，短剑，短弓和长弓。\n 戏法：从法师法术列表中选择一个戏法，现在你掌握了它。你的关键施法属性是智力。\n 额外语言：你可以听、说、读、写一种额外的语言，由你选择。\n \n亚种：木精灵\n 属性值提升：你的感知+1\n 熟练武器：你熟练于长剑，短剑，短弓和长弓。\n 轻捷步伐：你的基础陆地移动速度增加至35尺。\n 野性面具：即使你只因树丛、大雨、落雪、雾气或者其他自然现象获得轻微掩蔽（lightly obscured），你也可以尝试躲藏，只要为你提供掩蔽的是一种自然现象。\n \n亚种：黑暗精灵（卓尔）\n 属性值提升：你的魅力+1\n 高等黑暗视觉：你的黑暗视觉能力范围提升至120尺\n 日光敏感：如果你本人，你要攻击的目标，或者你试图察觉到的东西位于阳光直射下，你在攻击检定和感知（搜查）检定上获得劣势。\n 卓尔魔法：你掌握了舞光术戏法。当你达到3级，你可以使用妖火，每次长休息一次。当你达到5级，你可以使用黑暗术，每次长休息一次。这些法术的关键施法属性是魅力。\n 熟练武器：你熟练于细剑，短剑和手弩。\n \n亚种：爱拉德琳  （DMG范例亚种）\n 属性值提升：你的智力+1\n 熟练武器：你熟练于长剑，短剑，短弓和长弓。\n 妖精步：当你使用此特性，你可以施展一次迷踪步法术。每当你完成一次短休息或长休息，你将重获此能力。\n',
    '半兽人': '半兽人 Half-Orc\n \n无论是在强大的魔导士（warlock）的领导之下而联合在一起或是有过多年的冲突，兽人和人类的部落有时候会结成同盟，加入到一个大的部落中以对抗来自邻近的文明世界的恐惧。当这些同盟被密切地结合在一起，半兽人降生了。一些半兽人成长成了兽人部落的酋长，他们的人类血统给了他们对纯血兽人的一些优势。一些半兽人冒险进入人类和其他文明种族的世界来证明自己的价值。许多半兽人成为了冒险者，去实现他们伟大的伟业或是展现他们臭名昭著的野蛮风俗和狂暴与残忍。\n \n年龄：半兽人比人类更快地成熟，在14岁左右便成年。他们的衰老明显而快速，很少有能够活得超过75岁。\n 阵营：混乱、善良\n 体型：半兽人比人类更大更壮，他们的身高范围在5英尺到超过6英尺。你的体形为中型。\n 速度：你的基础步行速度是30英尺。\n 语言：通用语、兽人语（兽人语没有自己的文字，使用矮人语进行书写。）\n \n技能：\n 属性值提升：你的力量属性提升2，你的体质属性提升1。\n 黑暗视觉：在昏暗环境下，你可以将你周围60英尺内的区域视为明亮光照；在黑暗环境下，你可以将光照视为昏暗光照。你在黑暗中无法分清颜色，只能看到灰色的影子。\n 凶恶：你获得威吓技能作为本职技能。\n 残暴耐性：当你的HP降为0而没有完全死亡时，你可以改为使HP降低到1。直到你完成一次长休息前你不能再使用该能力。\n 野蛮攻击：当你用近战武器攻击造成重击，你可以额外骰一个该武器的伤害骰并将数值加入到重击的额外伤害中。\n',
    '半身人': '半身人 Halfing\n \n大部分半身人都以安稳的家作为生命目标：一处详和安宁的居所，远离剽掠的魔物、争战的军队，有温暖的火炉、饱足的 三餐，把酒言欢。虽然有半身人在偏远的农村里过了一生，但也有的被海阔天空吸引，组成旅程无尽的游牧队伍去见识奇风异族。但这些行者依然热爱和平、美食、火炉、家园，即使家园可能是泥路上的篷车或在河上漂浮的篷船。\n \n年龄：半身人约20岁成年，一般能活到150岁。\n 阵营：守序善良\n 体型：半身人约3尺高，重约40磅。你的体型为小型。\n 速度：你的基本步行速度为25 尺。\n 亚种：半身人的两大主要种类，轻足和强魄，像血缘相近的大家庭多于像亚种。选择一类亚种。\n 语言：通用语、半身人语\n \n技能：\n 能力调整值：你的敏捷值 +2。\n 幸运：当你在攻击骰、能力检定、豁免上投出 1 时，你可以重投它，但必需用新的结果。\n 勇敢：你在对抗恐慌的豁免带优势。\n 半身人灵巧：你可以穿越任何体形比你大的生物的空间。\n \n亚种：轻足半身人\n 能力调整值：你的魅力值 +1。\n 天生善匿：当你从体形比自己大的生物获得遮蔽时，你可以尝试躲藏。\n \n亚种：强魄半身人\n 能力调整值：你的体质值 +1。\n 强魄壮体：你在对抗毒素的豁免带有优势，你也对毒素伤害有抗力。\n',
    '半精灵': '半精灵Half-Elf\n \n半精灵行走在两个世界的交界之处，但无论在那一边都无法找到自己真正的归宿。有人说半精灵身上集中了人类和精灵两族的优点：从精灵处继承来的的敏锐感觉、艺术修养和热爱自然的天性，调和了人类血统中的的好奇心、创造力和野心。有些半精灵与人类一起生活，却因为情感和体质上的差别而和人类产生隔阂，虽然青春依旧但却不得不看着自己的朋友与恋人逐渐老去；其他半精灵则是在精灵社会中生活，他们在永恒不变的精灵国度中成长着，愈发感到不安，因为他们逐渐长大成人，可是与他们同时出生的精灵孩童却依然还是孩子。许多半精灵既无法融入人类社会又无法适应精灵社会的生活，最后只好选择独自流浪，或是与其他不合群者结伴踏上冒险的旅程。\n \n年龄：半精灵成长的速度和人类一样，在20岁左右成年。但他们的寿命远比人类要长，经常能活到180岁以上。\n 阵营：混乱\n 体型：半精灵的体型和人类差不多，身高在5英尺到6英尺之间。你是中体型生物。\n 速度：你的基本步行速度是30英尺。\n 语言：你可以说、读、写通用语和精灵语，以及你选择的一项语言。\n \n技能：\n 属性值提升：你的魅力增加2。再选择其他两项属性各增加1。\n 黑暗视觉：在昏暗环境下，你可以将你周围60英尺内的区域视为明亮光照；在黑暗环境下，你可以将光照视为昏暗光照。你在黑暗中无法分清颜色，只能看到灰色的影子。\n 妖精先祖：你在进行对魅惑的豁免检定时有优势，而且魔法不能使你陷入睡眠。\n 多才多艺：选择两个技能，你获得这两个技能的擅长。\n',
    '矮人': '矮人\n \n描述：矮而壮硕\n 勇猛而顽强的矮人们被认为是技艺纯熟的战士，矿工，以及精通石头和金属的工匠。尽管他们大多身高不及5英尺，矮人宽大而壮实的身体使得他们往往和高出2英尺的人类差不多重。他们的勇气和耐力更不比任何大家伙差。\n 矮人的肤色差距很大，从深棕色到略带红色的苍白都有，但最常见的是浅棕色，或者说深一点的小麦色，给人一种泥土的感觉。矮人蓄长发，但不梳花哨的复杂发型。矮人的头发通常呈黑，灰或棕色，但肤色较浅的矮人往往有着红发。男性矮人将他们的胡子视若珍宝，并常常对其进行小心的梳理。\n \n年龄：他们直到50岁前都能被认为是年轻矮人。他们平均能够活350年。\n 阵营：守序、善良阵营。\n 体型：矮人站立时在4到5英尺高，平均重约150磅。属于中体型。\n 速度：你的基本行走速度是25英尺。你的速度不会因穿着重甲而减慢。\n 语言：通用语、矮人语\n \n 技能：\n 属性加成：你的体质点数增加2\n 黑暗视觉：60英尺内的微光环境对你来说如同亮光环境，60英尺内的黑暗环境对你来说如同亮光环境。在黑暗环境下你无法分辨颜色，只能看到不同深浅的灰色。\n 矮人刚毅：你在对毒素的豁免检定中具有优势，同时你对毒素伤害拥有抗力\n 熟练：战斧，手斧，轻锤和战锤。\n 工具熟练：铁匠工具，酿酒工具或石匠工具。\n 熟悉岩石：每当你对一件石制品的起源做智力（历史）检定时，你视为熟练于历史技能，并可以在检定中加上双倍的熟练加值，而非你平时的熟练加值。\n \n亚种：D&D世界中存在着两种主要矮人亚种：丘陵矮人和山地矮人。在两种亚种之中选择一个。\n \n1.1丘陵矮人\n 属性加成：你的感知点数增加1。\n 矮人耐力：你的生命值最大值增加1，同时此后升级时都增加1。\n 1.2山地矮人\n 属性加成：你的力量点数增加2。\n 盔甲熟练：你能够熟练使用轻甲和中甲。\n',
}