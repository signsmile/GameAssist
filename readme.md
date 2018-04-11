数据查询页面：
=
	http://game.signsmile.com/

数据提交接口
=
请求URL:
-
	http://game.signsmile.com/addact 
	
HTTP请求方式:
-
    GET
    
请求参数：  
-
|参数名|参数含义|类型|备注|
|:------------|:------------|:------------|:------------|
|game_id|游戏:<br>1:口袋妖怪复刻<br>2:口袋妖怪起源<br>3:神无月<br>4:火影忍者|int||
|system_id|系统:<br>1:IOS<br>2:Android|||
|platform_id|平台:<br>1:果盘<br>2:优趣<br>3:虫虫<br>4:TT<br>5:爱应用<br>6:乐8<br>7:快用<br>8:当乐|int||
|precinct|所选区|string||
|actnum|账号|string||
|pwd|密码|string||
|sex_id|性别:<br>1:男<br>2:女|int||
|pet_id|宠物|int||
|goods_id|获得物品:<br>1:狃拉<br>2:剧毒珠<br>3:伊布<br>4:急冻拳<br>5:打草结<br>6:吸收拳<br>7:冥想<br>8:振奋精神的绑带<br>9:剩饭<br>10:先攻之爪<br>11:巨大根茎<br>12:黑色淤泥<br>13:铁面忍者<br>14:高级狩猎券|int||
|pet_id|宠物:<br>1:妙蛙种子<br>2:小火龙<br>3:杰尼龟|int||
|character_id|性格:<br>1:胆小<br>2:天真<br>3:开朗<br>4:大胆<br>5:保守<br>6:沉着<br>7:固执<br>8:急躁<br>9:慎重<br>10:淘气|int||
|remark|备注|string||

提交例子：
-    
    http://game.signsmile.com/addact?gamename_id=2&system_id=2&platform_id=2&precinct=190&actnum=123456789&pwd=123456789&sex_id=1&pet_id=2&goods_id=2&character_id=5&remark=你好

新注册账户提交接口
=
请求URL:
-
	http://game.signsmile.com/addnewact
HTTP请求方式
-
    GET
请求参数：
-
|参数名|参数含义|类型|备注|
|:------------|:------------|:------------|:------------|
|actnum|账号|string||
|pwd|密码|string||
|platform|平台|string||
|gamename|游戏|string||

提交例子：
-
    http://game.signsmile.com/addnewact?actnum=123456789&pwd=123456789&platform=TT&gamename=口袋妖怪复刻
    http://localhost:8000/addnewact?actnum=123456789&pwd=123456789&platform=TT&gamename=口袋妖怪复刻

新注册账户获取接口
=
请求URL
-   
	http://game.signsmile.com/getnewact
	http://localhost/getnewact
HTTP请求方式
-
    GET
    
返回参数
-
{
    'result':'success',              //结果状态
    'actnum': 123651021,             //账号
    'pwd': 123456,                   //密码
    'platform': TT,                  //平台
    'gamename': 口袋妖怪复刻         //游戏
}

    