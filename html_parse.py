# coding=utf-8
from xml.etree import ElementTree
from bs4 import BeautifulSoup

movie_map = {}
def parse(html_str):
    soup = BeautifulSoup(html_str, "html.parser")
    for tag in soup.find_all('span'):
        if tag.text.find('评分') >= 0:
            print(tag.contents[1].text)
    for tag in soup.find_all('p'):
        if tag.text.find('译　　名') >= 0:
            movie_map['name'] = tag.text[6:]
            break
    for tag in soup.find_all('table'):
        print(tag)
    pass


if __name__ == '__main__':
    html_content = """<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<META http-equiv=Content-Type content="text/html; charset=gb2312">
<title>2013年国产喜剧剧情片《摩登时代》HD中英双字迅雷下载_电影天堂</title>
<meta name=keywords content="摩登时代下载">
<meta name=description content="摩登时代免费下载,电影下载,迅雷下载">
<link href="/css/dygod.css" rel="stylesheet" type="text/css" />
<script type="text/javascript">
function goPAGE() {
	if ((navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i))) {
		return "wap";
}
	else {
		return "win";	
		}
}
</script>
<base target="_blank">
</head><body><div id="header"><div class="contain"><h4><a href="/"></a></h4>
        <div id="headerright"><div id="about" align="right">
<script type="text/javascript">if(goPAGE()=="win"){document.writeln("<SCRIPT src='/jsdd/760h.js'></SCR"+"IPT>")}</script>
          </div>
      </div>
    <div id="menu"><div class="contain"><ul>
<li><a href="/2/">动作片</a></li>
<li><a href="/0/">剧情片</a></li>
<li><a href="/3/">爱情片</a></li>
<li><a href="/1/">喜剧片</a></li>
<li><a href="/4/">科幻片</a></li>
<li><a href="/8/">恐怖片</a></li>
<li><a href="/5/">动画片</a></li>
<li><a href="/7/">惊悚片</a></li>
<li><a href="/14/">战争片</a></li>
<li><a href="/15/">犯罪片</a></li>
<li><a href="/html/tv/hytv/index.html">华语连续剧</a></li><li>
<a href="/html/tv/oumeitv/index.html">美剧</a></li><li>
<a href="/html/tv/rihantv/index.html">日韩剧</a></li><li>
<a href="/html/zongyi2013/index.html">综艺</a></li><li>
<a href="/html/dongman/index.html">动漫资源</a></li><li>
<a href="/support/GuestBook.php" target="_blank">留言板</a></li><li>
<a href="#" onclick="javascript:window.external.AddFavorite('http://www.dy2018.com', '电影天堂-dy2018.com')" target="_self">加入收藏</a></li><li>
<a href="index.html" onClick="this.style.behavior='url(#default#homepage)';this.setHomePage('http://www.dy2018.com/');return(false);" style="behavior: url(#default#homepage)">设为主页</a></li>
</ul>   </div>
 </div>
<div class="bd2">
<!--
<div class="bd4l" style="width: 960px">
<table cellspacing="1" border="0" cellpadding="4" width="100%"  >
 <tr align="center" >
 <script type="text/javascript">if(goPAGE()=="win"){document.writeln("<SCRIPT src='/jsdd/960.js'></SCR"+"IPT>")}</script>
</tr>
</table>
</div>-->
<!--##########}end:header###########-->
<!--{start:body content-->
<div class="bd3" style="marigin-top:10px;">
<!--{start:内容区左侧-->
<div class="bd3l" style="width:310px;line-height:35px;">
当前位置：<a href="/">电影天堂</a>&nbsp;>&nbsp;<a href="/html/gndy/">电影</a>&nbsp;>&nbsp;<a href="/html/gndy/dyzz/">最新电影</a>>下载页面
</div>
<!--}end:内容区左侧-->
<div class="bd3r" style="width:650px; float:left;">
<div style="width:100px; float:left;line-height:35px;">
<a href="javascript:window.external.addFavorite('http://www.dy2018.com/','dy2018.com-电影天堂')"class="style11" target=_self  style="font-size:16px;color:#000" ><b>点击收藏</b></a>
</div>
<div>
<!--{start:搜索-->
<div class="search" style="width:550px; float:left;">
<script src="/js/search.js" language="javascript"></script>
</div>
<!--}end:搜索-->
<div class="x"></div>
</div></div>
<div class="bd3">
<div class="x"></div>
</div>
<div style="clear: both;"></div>
<div style="width: 960px;">
<table cellspacing="0" border="0" cellpadding="0" width="100%"  >
<tr align="center" >
<script type="text/javascript">if(goPAGE()=="win"){document.writeln("<SCRIPT src='/jsdd/960-1.js'></SCR"+"IPT>")}</script>
</tr>
</table>
</div>
<div class="co_area2">
<div class="title_all"><h1>2013年国产喜剧剧情片《摩登时代》HD中英双字</h1></div>
<div class="co_content8">
<ul>
 <div class="position">
    <span>评分：<strong class="rank">7</strong></span>    <span>类型：<a href='/0/'>剧情片</a> / <a href='/1/'>喜剧片</a></span>  <span class="updatetime">发布时间：2013-09-23</span>
 </div>
<tr>
      <tr>
        <td colspan="2">&nbsp;</td>
      </tr>
      <tr> 
      <td colspan="2" align="center" valign="top"><div id="Zoom">
<!--Content Start-->
<p>&nbsp;<img src="http://img.23juqing.com/tupian/103405-064254d85fyfyyl7gfz68f.jpg" border="0" style="border: 0px; color: rgb(51, 51, 51); font-family: Arial; font-size: 14px; line-height: 21.59375px; max-width: 700px;" alt="" /></p>
<p>◎译　　名　摩登时代</p>
<p>◎片　　名　Fake Fiction</p>
<p>◎年　　代　2013</p>
<p>◎国　　家　中国大陆 &nbsp;</p>
<p>◎类　　别　剧情 / 喜剧</p>
<p>◎语　　言　汉语普通话</p>
<p>◎字　　幕　中文/英文</p>
<p>◎文件格式　X264+ AAC</p>
<p>◎视频尺寸　1920 x 804</p>
<p>◎文件大小　1CD 1.61G</p>
<p>◎片　　长　95min</p>
<p>◎导　　演　邵晓黎 Xiao Li Shao &nbsp;....总导演</p>
<p>◎主　　演　徐峥 Zheng Xu &nbsp;....欧大卫</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 张子枫 Zifeng Zhang &nbsp;....丢丢</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 王宣予 Xuan Yu Wang &nbsp;....毛娜</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 张颂文 Zhang Song Wen &nbsp;....魏建</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 王太利 Taili Wang &nbsp;....李文学</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 肖央 Yang Xiao &nbsp;....交警</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 岳小军 Xiaojun Yue &nbsp;....魔术店老板</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 杜鹏 Peng Du &nbsp;....废品店老板</p>
<p>&nbsp;</p>
<p>◎简　　介　</p>
<p>&nbsp;</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; 靠魔术行骗的江湖骗子欧大卫（徐峥 饰）掉进自己编织的骗局中，突然又冒出一个八岁的孩子丢丢（张子枫饰）声称是他的女儿。莫名其妙的大卫对丢丢十分不耐烦，但遭到了丢丢的连环制裁。次日，欧大卫的搭档李文学（王太利饰）给他带来了一笔大生意：一场&ldquo;大变海神之母&rdquo;的魔术表演。当然，这对骗子只打算拿到定金就跑路。不料欧大卫却再遭李文学的连环骗局，不得面对那根本无法完成的魔术。丢丢更是紧追不舍，在被迫一起寻找魔术方法的旅途中，丢丢和欧大卫开始互相了解，逐渐产生深厚的&ldquo;父女&rdquo;情，而大卫因为丢丢获得了&ldquo;大变海神之母&rdquo;的灵感。一场极度危险的深水逃生魔术即将开始，为爱，他要表演一个不可能完成的魔术。</p>
<p>&nbsp;</p>
<p>◎影片截图</p>
<p>&nbsp;<img src="http://img.23juqing.com/tupian/103405-M37Y.jpg" alt="" /></p>
<p><strong><span style="color: rgb(153, 51, 0);"><span style="font-size: 14px;">&nbsp;站长点评</span></span></strong><span style="color: rgb(153, 51, 0);"><span style="font-size: 14px;">：剧情有点像尼古拉斯.凯奇主演过的一部电影《火柴人》。据说本片是在《泰囧》之前拍的，借着《泰囧》大卖的这股风推出。徐峥依然在演那些一股&ldquo;囧&rdquo;味的角色，前半程逗乐，后半程煽情，没有什么硬伤，也没有什么特地值得赞赏的地方。前面还行，后面如果觉得有点泄气也可以直接关掉，6.2分推荐</span></span></p>
<p style="margin: 0px; padding: 0px; color: rgb(24, 55, 120); font-family: Verdana, Arial, Helvetica, sans-serif;"><font color="#ff0000"><strong><font size="4">【迅雷下载地址】</font></strong></font></p>
<p style="margin: 0px; padding: 0px; color: rgb(24, 55, 120); font-family: Verdana, Arial, Helvetica, sans-serif;">&nbsp;</p>
<p style="margin: 0px; padding: 0px; color: rgb(24, 55, 120); font-family: Verdana, Arial, Helvetica, sans-serif;">&nbsp;</p>
<p style="margin: 0px; padding: 0px; color: rgb(24, 55, 120); font-family: Verdana, Arial, Helvetica, sans-serif;">&nbsp;</p>
<p style="margin: 0px; padding: 0px; color: rgb(24, 55, 120); font-family: Verdana, Arial, Helvetica, sans-serif;">&nbsp;</p>
<table border="0" cellspacing="0" cellpadding="6" width="95%" align="center" style="color: rgb(24, 55, 120); font-family: Verdana, Arial, Helvetica, sans-serif; font-size: 12px; border-color: rgb(204, 204, 204); table-layout: fixed;">
    <tbody>
        <tr>
            <td bgcolor="#fdfddf" style="word-wrap: break-word;">
            <div class="msg Nth"><font color="#ff0000"><a href="ftp://7:7@d3.dl1234.com:8006/[电影天堂www.dy2018.com]摩登时代720P中英双字.mkv">ftp://7:7@d3.dl1234.com:8006/[电影天堂www.dy2018.com]摩登时代720P中英双字.mkv</a></font></div>
            </td>
        </tr>
    </tbody>
</table><!--duguPlayList Start-->
<!--xunleiDownList Start-->
</td>
      </tr>
<script type="text/javascript">if(goPAGE()=="win"){document.writeln("<SCRIPT src='/jsdd/750.js'></SCR"+"IPT>")}</script>
<br>
      <tr>
        <td colspan="2"><hr color="#CC6600" size="1px" /></td>
      </tr>
</tr>
        <center><font color="#ff000">请把www.dy2018.com分享给你的朋友,更多人使用，速度更快 电影天堂www.dy2018.com欢迎你每天来!</font></center>
</div>
   <td colspan="2"><hr color="#CC6600" size="1px" /></td>
<table border=0 cellpadding=0 cellspacing=0 width=950 style="margin-left:10px;"><tr><td width=470 align=left>
●本栏目本周最新资源列表：<br>
·<a href="/i/100608.html" title="2019年国产6.0分爱情片《一吻定情》BD国语中字">2019年国产6.0分爱情片《一吻定情》BD国语中字</a><br/>
·<a href="/i/100723.html" title="2019年美国欧美剧《权力的游戏第八季》连载至4">2019年美国欧美剧《权力的游戏第八季》连载至4</a><br/>
·<a href="/i/100774.html" title="2019年欧美6.9分动作片《冷血追击》BD中英双字">2019年欧美6.9分动作片《冷血追击》BD中英双字</a><br/>
·<a href="/i/100773.html" title="2019年国产6.9分剧情片《老师·好》HD高清国语中字">2019年国产6.9分剧情片《老师·好》HD高清国语中字</a><br/>
·<a href="/i/100765.html" title="2019年印度6.7分科幻片《宝莱坞机器人2.0：重生归来》BD中英双">2019年印度6.7分科幻片《宝莱坞机器人2.0：重生归来》BD中英双</a><br/>
·<a href="/i/100755.html" title="2019年国产8.0分科幻片《流浪地球》HD国语中字修复">2019年国产8.0分科幻片《流浪地球》HD国语中字修复</a><br/>
·<a href="/i/100737.html" title="2019年美国6.7分悬疑片《忌日快乐2》BD中英双字">2019年美国6.7分悬疑片《忌日快乐2》BD中英双字</a><br/>
·<a href="/i/100759.html" title="2019年欧美6.8分动画片《乐高大电影2》BD中英双字">2019年欧美6.8分动画片《乐高大电影2》BD中英双字</a><br/>
·<a href="/i/100757.html" title="2018年欧美8.8分剧情片《何以为家》BD中字">2018年欧美8.8分剧情片《何以为家》BD中字</a><br/>
·<a href="/i/100753.html" title="复习经典《复仇者联盟1到3》BD中英双字">复习经典《复仇者联盟1到3》BD中英双字</a><br/>
</td><td width=470 align=left>●本栏目本周最热门资源列表：<br>
·<a href="/i/94980.html" title="2015年美国8分动作片《王牌特工:特工学院》BD国英双语双字">2015年美国8分动作片《王牌特工:特工学院》BD国英双语双字</a><br/>
·<a href="/i/97555.html" title="2016年国产8.4分喜剧片《驴得水》HD国语中字">2016年国产8.4分喜剧片《驴得水》HD国语中字</a><br/>
·<a href="/i/97291.html" title="2016年美国7分动作片《机械师2：复活》BD中英双字">2016年美国7分动作片《机械师2：复活》BD中英双字</a><br/>
·<a href="/i/95214.html" title="2015年美国8.4分动作片《疯狂的麦克斯4：狂暴之路》BD中英双字">2015年美国8.4分动作片《疯狂的麦克斯4：狂暴之路》BD中英双字</a><br/>
·<a href="/i/94896.html" title="2015年吴京余男动作战争片《战狼/特种兵之战狼》BD国语中字">2015年吴京余男动作战争片《战狼/特种兵之战狼》BD国语中字</a><br/>
·<a href="/i/97338.html" title="2016年美国6.7分动作片《X特遣队》BD中英双字">2016年美国6.7分动作片《X特遣队》BD中英双字</a><br/>
·<a href="/i/97252.html" title="2016年韩国8.3分动作片《釜山行》BD韩语中字">2016年韩国8.3分动作片《釜山行》BD韩语中字</a><br/>
·<a href="/i/97094.html" title=" 2016年美国7.4分科幻动作片《X战警：天启》BD中英双语双字"> 2016年美国7.4分科幻动作片《X战警：天启》BD中英双语双字</a><br/>
·<a href="/i/98477.html" title="2017年欧美7.0分科幻片《猩球崛起3：终极之战》BD双语中英双字">2017年欧美7.0分科幻片《猩球崛起3：终极之战》BD双语中英双字</a><br/>
·<a href="/i/98818.html" title="2017年美国6.7分科幻片《正义联盟》BD中英双语双字">2017年美国6.7分科幻片《正义联盟》BD中英双语双字</a><br/>
</td></tr></table>
<script src='https://pstatic.xunlei.com/js/webThunderDetect.js'></script>
<script src="/js/base64.js"></script>
<script src='/js/thunderForumLinker.js'></script>
<script language="javascript">
  var thunderPid="00000";
    var thunderExceptPath="play.html";
thunderFuncType=false;
thunderLinker();
</script>
<div class="x"></div>
</div>
<div class="x"></div>
</div>
<div class="x"></div>
</div>
<div class="x"></div>
</div>
<!--}end:body conten-->
<!--{start:友情链接-->
<div class="bd6">
<ul>
<center>
<script type="text/javascript">if(goPAGE()=="win"){document.writeln("<SCRIPT src='/jsdd/960d.js'></SCR"+"IPT>")}</script>
 </center>
</ul>
<div class="x"></div>
</div>
<!--}end:友情链接-->
<!--{start:footer-->
<!--}end:footer-->
<!--}end:body conten-->
<script language=javascript src="/js/tj.js"></script>
<script type="text/javascript">if(goPAGE()=="win"){document.writeln("<SCRIPT src='/js17/pf.js'></SCR"+"IPT>")}</script>
<div style="display:none;"><script src=/e/public/ViewClick/?classid=12&id=91866&addclick=1></script></div>
</body>
</html>"""
    parse(html_content)
    pass

