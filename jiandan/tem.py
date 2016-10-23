import requests
from lxml import etree
from bs4 import BeautifulSoup
import re

source="""
<!DOCTYPE html>
<html dir="ltr" lang="zh">
<head>
    <!-- BEGIN html head -->
<title>
妹子图 - 煎蛋正版认证
</title>
        <meta name="keywords" content="妹子图,煎蛋妹子图,妹子图官网,美女图片,软妹子,性感美女"/>
    <meta name="description" content="这儿才是正版妹子图。性感火辣，清纯甜美可爱的软妹子这儿都有，萌大奶的大丈夫和爱美臀的男子汉不要错过。"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="renderer" content="webkit">
    <meta http-equiv="Window-target" Content="_top">
    <meta name="baidu-site-verification" content="9wC0PEtTmEqSNlOk"/>
    <meta http-equiv="mobile-agent"
          content="format=html5; url=//i.jandan.net/ooxx/2012">
                    <meta name="robots" content="index,follow">
        <link rel="stylesheet" href="http://cdn.jandan.net/wp-content/themes/egg/style.css?v=20160420" type="text/css"
          media="screen"/>
        <link rel="apple-touch-icon" href="http://cdn.jandan.net/static/img/appicon.png">
    <link rel="shortcut icon" href="http://cdn.jandan.net/static/img/favicon.ico"/>
    <script>if (window != top)top.location.href = window.location.href;</script>
    <!--[if lt IE 9]>
    <script src="//lib.sinaapp.com/js/jquery/1.10.2/jquery-1.10.2.min.js"></script>
    <![endif]-->
    <!--[if gte IE 9]><!-->
    <script src="//lib.sinaapp.com/js/jquery/2.0.3/jquery-2.0.3.min.js"></script>
    <!--<![endif]-->
	<script src="http://cdn.jandan.net/static/js/jquery.lazyload.min.js?v=201603020"></script>
    <script>
        var options = {};
        options.COOKIE_HASH = '596e6fb28c1bb47f949e65e1ae03f7f5';
        options.SITE_URL = 'http://jandan.net';
    </script>
    <script src="http://cdn.jandan.net/static/js/common.js?v=20160501"></script>
    <script>
        eval(function(p,a,c,k,e,r){e=function(c){return c.toString(a)};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('(b(){0 d=["j","a","n","d","a","n",".","n","e","9"];0 5=2 g(d.1(\'\')+\'$\');4(!5.8(c.f)){0 a=6.7.h;4(a==\'/\'){a=\'\'}6.7.i=\'k://\'+d.1(\'\')+\'/\'+a}l(\'m\',3.o+\'#\'+2 p().q())})(3);',27,27,'var|join|new|options|if|r|window|location|test|t||function|document|||domain|RegExp|pathname|href||http|setCookie|jdna||COOKIE_HASH|Date|getTime'.split('|'),0,{}));
    </script>

</head>
<!-- END html head -->
<body>
<!-- BEGIN wrapper -->

<div id="wrapper">

    <!-- BEGIN header -->
    <div id="header">
        <div class="logo">
            <h1><a href="/" onclick="ga('send', 'pageview','/header/logo');">煎蛋</a></h1>
        </div>
        <div class="break"></div>
        <div class="nav">
            <ul class="nav-items">
                <li class="nav-item f"><a href="/" onfocus="blur()" onclick="ga('send', 'pageview','/header/index');" class="nav-link">首页</a></li>
                <li class="nav-item"><a class="nav-link" href="/new" onfocus="blur()" class="nav-link" target=_blank>更新</a></li>
                <li class="nav-item x">
	                <a href="javascript:;" class="nav-link">专题</a>
	                <div class="sub-items">
		                <table class="tag-cloud">
			                <thead>
			                <tr>
				                <th>科学</th>
				                <th>技术</th>
				                <th>极客</th>
				                <th>脑洞</th>
				                <th>故事</th>
				                <th>人类</th>
				                <th>折腾</th>
				                <th>NSFW</th>
			                </tr>
			                </thead>
			                <tbody>
			                <tr>
				                <td><a href="/tag/走进科学" onfocus="blur()" >走进科学</a></td>
				                <td><a href="/tag/tech" onfocus="blur()" >TECH</a></td>
				                <td><a href="/tag/GEEK" onfocus="blur()" >GEEK</a></td>
				                <td><a href="/tag/DIY" onfocus="blur()" >DIY</a></td>
				                <td><a href="/tag/冷新闻" onfocus="blur()">冷新闻</a></td>
				                <td><a href="/tag/女性" onfocus="blur()">女性</a></td>
				                <td><a href="/tag/减肥" onfocus="blur()">减肥</a></td>
				                <td><a href="/tag/sex" onfocus="blur()">SEX</a></td>
			                </tr>
			                <tr>
				                <td><a href="/tag/无厘头研究" onfocus="blur()" >无厘头研究</a></td>
				                <td><a href="/tag/人工智能" onfocus="blur()" >人工智能</a></td>
				                <td><a href="/tag/MEME" onfocus="blur()" >MEME</a></td>
				                <td><a href="/tag/艺术" onfocus="blur()" >艺术</a></td>
				                <td><a href="/tag/爷有钱" onfocus="blur()" >爷有钱</a></td>
				                <td><a href="/tag/熊孩子" onfocus="blur()" >熊孩子</a></td>
				                <td><a href="/tag/整形" onfocus="blur()" >整形</a></td>
				                <td><a href="/tag/wtf" onfocus="blur()" >WTF</a></td>

			                </tr>
			                <tr>
				                <td><a href="/tag/天文" onfocus="blur()" >天文</a></td>
				                <td><a href="/tag/无人机" onfocus="blur()" >无人机</a></td>
				                <td><a href="/tag/quora" onfocus="blur()" >QUORA</a></td>
				                <td><a href="/tag/设计" onfocus="blur()" >设计</a></td>
				                <td><a href="/tag/致富信息" onfocus="blur()" >致富信息</a></td>
				                <td><a href="/tag/大丈夫" onfocus="blur()" >大丈夫</a></td>
				                <td><a href="/tag/变性" onfocus="blur()" >变性</a></td>
				                <td><a href="/tag/lgbt" onfocus="blur()" >LGBT</a></td>
			                </tr>
			                <tr>
				                <td><a href="/tag/nasa" onfocus="blur()" >NASA</a></td>
				                <td><a href="/tag/3D打印" onfocus="blur()" >3D打印</a></td>
				                <td><a href="/tag/小学堂" onfocus="blur()" >小学堂</a></td>
				                <td><a href="/tag/广告" onfocus="blur()" >广告</a></td>
				                <td><a href="/tag/安全警示" onfocus="blur()" >安全警示</a></td>
				                <td><a href="/tag/笨贼" onfocus="blur()" >笨贼</a></td>
				                <td><a href="/tag/健康" onfocus="blur()" >健康</a></td>
				                <td><a href="/tag/重口味" onfocus="blur()" >重口味</a></td>
			                </tr>
			                <tr>
				                <td><a href="/tag/高科技" onfocus="blur()">高科技</a></td>
				                <td><a href="/tag/数码产品" onfocus="blur()">数码产品</a></td>
				                <td><a href="/tag/创意产品" onfocus="blur()">创意产品</a></td>
				                <td><a href="/tag/建筑" onfocus="blur()">建筑</a></td>
				                <td><a href="/tag/国内观光" onfocus="blur()">国内观光</a></td>
				                <td><a href="/tag/真的猛士" onfocus="blur()" >真的猛士</a></td>
				                <td><a href="/tag/教育" onfocus="blur()" >教育</a></td>
				                <td><a href="/tag/何其低俗焉" onfocus="blur()" >何其低俗焉</a></td>

			                </tr>
			                <tr>
				                <td><a href="/tag/环保" onfocus="blur()" >环保</a></td>
				                <td><a href="/tag/虚拟现实" onfocus="blur()" >虚拟现实</a></td>
				                <td><a href="/tag/whatif" onfocus="blur()">WHAT IF</a></td>
				                <td><a href="/tag/摄影" onfocus="blur()" >摄影</a></td>
				                <td><a href="/tag/史海钩沉" onfocus="blur()" >史海钩沉</a></td>
				                <td><a href="/tag/正能量" onfocus="blur()" >正能量</a></td>
				                <td><a href="/tag/旅游" onfocus="blur()" >旅游</a></td>
				                <td><a href="/tag/没品笑话集" onfocus="blur()" >没品笑话集</a></td>
			                </tr>
			                </tbody>
		                </table>


	                </div>
                </li>
                <li class="nav-item"><a class="nav-link" href="http://g.jandan.net/" onfocus="blur()" class="nav-link" target=_blank>小组</a></li>
                <li class="nav-item"><a class="nav-link" href="/v" onfocus="blur()" onclick="ga('send', 'pageview','/header/v');" class="nav-link">小电影</a></li>
                <li class="nav-item"><a class="nav-link" href="/duan" onfocus="blur()" onclick="ga('send', 'pageview','/header/duan');" class="nav-link">段子</a></li>
                <li class="nav-item"><a class="nav-link" href="/ooxx" onfocus="blur()" onclick="ga('send', 'pageview','/header/ooxx');" class="nav-link">妹子</a></li>
                <li class="nav-item"><a class="nav-link" href="/pic" onfocus="blur()" onclick="ga('send', 'pageview','/header/pic');" class="nav-link">无聊图</a></li>
                <li class="nav-item"><a class="nav-link" href="/top" onfocus="blur()" onclick="ga('send', 'pageview','/header/top');" class="nav-link">热榜</a></li>

            </ul>
            <div class="break"></div>
        </div>
    </div>
    <!-- END header -->

    <!-- BEGIN body -->
    <div id="body">
	<!-- BEGIN content -->
	<div id="content">
					<h1 class="title">妹子图</h1>
			<!-- begin post -->
			<div class="post f">
				<p>[1] 图片请上传到 <a target=_blank rel="external" href="http://photo.weibo.com/photos/upload">新浪微博相册</a>，在<a href="#respond">评论框</a>里粘帖图片地址即可发图<br />
[2] 原创图请注明来源。发布后请等待审核，未通过审核的原因可能是重复图或者敏感图</p>
<hr />
				<style>
	.switch {
		display: inline-block;
		padding: 0 5px;
		border: 1px solid #444;
		cursor: pointer;
		line-height: 14px;
		text-align: center;
		color: #aaa;
		font-size: 10px;
		vertical-align: middle;
	}
	.switch-current {
		background-color: #333;
		color: #fff;

	}

</style>
<p>
	GIF图点击加载: <span class="switch switch-current" id="gif-click-load-on">ON</span><span class="switch " id="gif-click-load-off">OFF</span>&nbsp;&nbsp;
	NSFW图自动隐藏: <span class="switch switch-current" id="nsfw-click-load-on">ON</span><span class="switch " id="nsfw-click-load-off">OFF</span>&nbsp;&nbsp;
	隐藏不受欢迎图片: <span class="switch switch-current" id="bad-click-load-on">ON</span><span class="switch " id="bad-click-load-off">OFF</span>
</p>			</div>
			<!-- end post -->
			<!-- begin comments -->
			<div id="comments">

    <div style="clear:both;"></div>

    <h3 class="title" id="comments">TOTAL COMMENTS: 50,287<span
            class="plusone"><a href="#respond" title="来一发">+1</a></span></h3>


    <span class="break"></span>
    <div class="comments">
                        <div class="cp-pagenavi">
                                                            <span class="current-comment-page">[2012]</span>
                                                            <a href="http://jandan.net/ooxx/page-2011#comments">
                    2011                </a>
                                                    <a title="Older Comments" href="http://jandan.net/ooxx/page-2011#comments" class="previous-comment-page">»</a>
                    </div>
            </div>


    <ol class="commentlist" style="list-style-type: none;">


            <li id="comment-3165730">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：d61affb446a470c4b1a2b9838b8d035a45c36e71" >弱水三千</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165730&quot;&gt;弱水三千&lt;/a&gt;: &#39;">@18 hours ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165730">3165730</a></span><p><a href="http://ww2.sinaimg.cn/large/6469180ajw1f4p9zfzb8yj20dw0k50v4.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww2.sinaimg.cn/mw600/6469180ajw1f4p9zfzb8yj20dw0k50v4.jpg" /></p>
<div class="vote" id="vote-3165730"><span id="acv_stat_3165730"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165730" onclick="acv_vote(event,3165730,1);" href="javascript:;">OO</a> [<span id="cos_support-3165730">136</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165730"  onclick="acv_vote(event,3165730,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165730">17</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165703">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：097ffe022415cd605ac308d621734068545b478d" >大爷来玩嘛</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165703&quot;&gt;大爷来玩嘛&lt;/a&gt;: &#39;">@18 hours ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165703">3165703</a></span><p>只能发coser什么的了……</p>
<p><a href="http://ww1.sinaimg.cn/large/005vbOHfgw1f4p9d1aqz1j30i20r3dmc.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww1.sinaimg.cn/mw600/005vbOHfgw1f4p9d1aqz1j30i20r3dmc.jpg" /></p>
<div class="vote" id="vote-3165703"><span id="acv_stat_3165703"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165703" onclick="acv_vote(event,3165703,1);" href="javascript:;">OO</a> [<span id="cos_support-3165703">67</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165703"  onclick="acv_vote(event,3165703,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165703">94</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165702">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：097ffe022415cd605ac308d621734068545b478d" >大爷来玩嘛</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165702&quot;&gt;大爷来玩嘛&lt;/a&gt;: &#39;">@18 hours ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165702">3165702</a></span><p><a href="http://ww2.sinaimg.cn/large/005vbOHfgw1f4p9cg73ufj30ig0rsgnd.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww2.sinaimg.cn/mw600/005vbOHfgw1f4p9cg73ufj30ig0rsgnd.jpg" /></p>
<div class="vote" id="vote-3165702"><span id="acv_stat_3165702"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165702" onclick="acv_vote(event,3165702,1);" href="javascript:;">OO</a> [<span id="cos_support-3165702">86</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165702"  onclick="acv_vote(event,3165702,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165702">35</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>

                                                 <span class="break"></span><li class="row" ID="adsense">
<div style="padding-left:120px;padding-top:10px;padding-bottom:15px;width:336px;">
<font color="#AAA">[ 广告 ]</font><br>
<!-- 336-baidu -->
<script type="text/javascript">
/*336*280*/
var cpro_id = "u529095";
</script>
<script src="http://cpro.baidustatic.com/cpro/ui/c.js" type="text/javascript"></script>                    </li>

            <li id="comment-3165701">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：097ffe022415cd605ac308d621734068545b478d" >大爷来玩嘛</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165701&quot;&gt;大爷来玩嘛&lt;/a&gt;: &#39;">@18 hours ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165701">3165701</a></span><p><a href="http://ww4.sinaimg.cn/large/005vbOHfgw1f4p9cw4zaqj30ia35ah28.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww4.sinaimg.cn/mw600/005vbOHfgw1f4p9cw4zaqj30ia35ah28.jpg" /></p>
<div class="vote" id="vote-3165701"><span id="acv_stat_3165701"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165701" onclick="acv_vote(event,3165701,1);" href="javascript:;">OO</a> [<span id="cos_support-3165701">41</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165701"  onclick="acv_vote(event,3165701,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165701">112</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165690">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：22edfd0c5061f0267f71933e745efe4a377d5d43" >丹迪佬</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165690&quot;&gt;丹迪佬&lt;/a&gt;: &#39;">@19 hours ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165690">3165690</a></span><p><a href="http://ww2.sinaimg.cn/large/7352978fgw1f4p8oqoe2vj20f00eraci.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww2.sinaimg.cn/mw600/7352978fgw1f4p8oqoe2vj20f00eraci.jpg" /></p>
<div class="vote" id="vote-3165690"><span id="acv_stat_3165690"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165690" onclick="acv_vote(event,3165690,1);" href="javascript:;">OO</a> [<span id="cos_support-3165690">208</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165690"  onclick="acv_vote(event,3165690,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165690">28</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165674">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：d61affb446a470c4b1a2b9838b8d035a45c36e71" >弱水三千</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165674&quot;&gt;弱水三千&lt;/a&gt;: &#39;">@19 hours ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165674">3165674</a></span><p><a href="http://ww3.sinaimg.cn/large/6469180ajw1f4p873xy5wj20jo0tm76x.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww3.sinaimg.cn/mw600/6469180ajw1f4p873xy5wj20jo0tm76x.jpg" /></p>
<div class="vote" id="vote-3165674"><span id="acv_stat_3165674"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165674" onclick="acv_vote(event,3165674,1);" href="javascript:;">OO</a> [<span id="cos_support-3165674">73</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165674"  onclick="acv_vote(event,3165674,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165674">74</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165673">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：d61affb446a470c4b1a2b9838b8d035a45c36e71" >弱水三千</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165673&quot;&gt;弱水三千&lt;/a&gt;: &#39;">@19 hours ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165673">3165673</a></span><p><a href="http://ww2.sinaimg.cn/large/6469180ajw1f4p87f5rw2j20ku0vbwjw.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww2.sinaimg.cn/mw600/6469180ajw1f4p87f5rw2j20ku0vbwjw.jpg" /></p>
<div class="vote" id="vote-3165673"><span id="acv_stat_3165673"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165673" onclick="acv_vote(event,3165673,1);" href="javascript:;">OO</a> [<span id="cos_support-3165673">38</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165673"  onclick="acv_vote(event,3165673,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165673">19</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165668">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：0b5b3c8ad5e45b0083c1f5b9b174b5b08f09a945" >臀魔</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165668&quot;&gt;臀魔&lt;/a&gt;: &#39;">@19 hours ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165668">3165668</a></span><p><a href="http://ww3.sinaimg.cn/large/55177ebejw1f4p2mc7f84j20np0zkq70.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww3.sinaimg.cn/mw600/55177ebejw1f4p2mc7f84j20np0zkq70.jpg" /></p>
<div class="vote" id="vote-3165668"><span id="acv_stat_3165668"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165668" onclick="acv_vote(event,3165668,1);" href="javascript:;">OO</a> [<span id="cos_support-3165668">93</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165668"  onclick="acv_vote(event,3165668,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165668">16</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165626">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：d61affb446a470c4b1a2b9838b8d035a45c36e71" >弱水三千</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165626&quot;&gt;弱水三千&lt;/a&gt;: &#39;">@20 hours ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165626">3165626</a></span><p><a href="http://ww4.sinaimg.cn/large/6469180ajw1f4p5q7s52ij20et0m8tb4.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww4.sinaimg.cn/mw600/6469180ajw1f4p5q7s52ij20et0m8tb4.jpg" /></p>
<div class="vote" id="vote-3165626"><span id="acv_stat_3165626"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165626" onclick="acv_vote(event,3165626,1);" href="javascript:;">OO</a> [<span id="cos_support-3165626">82</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165626"  onclick="acv_vote(event,3165626,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165626">94</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165474">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：6758578b706d695dae7b62f435d0389f56a5c802" >梁非凡</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165474&quot;&gt;梁非凡&lt;/a&gt;: &#39;">@1 day ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165474">3165474</a></span><p><a href="http://ww2.sinaimg.cn/large/a00dfa2agw1f4oyl2q4ing20b40697m9.gif" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww2.sinaimg.cn/thumb180/a00dfa2agw1f4oyl2q4ing20b40697m9.gif" org_src="http://ww2.sinaimg.cn/mw690/a00dfa2agw1f4oyl2q4ing20b40697m9.gif" onload="add_img_loading_mask(this, load_sina_gif);"/></p>
<div class="vote" id="vote-3165474"><span id="acv_stat_3165474"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165474" onclick="acv_vote(event,3165474,1);" href="javascript:;">OO</a> [<span id="cos_support-3165474">296</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165474"  onclick="acv_vote(event,3165474,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165474">20</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165323">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：d61affb446a470c4b1a2b9838b8d035a45c36e71" >弱水三千</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165323&quot;&gt;弱水三千&lt;/a&gt;: &#39;">@1 day ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165323">3165323</a></span><p><a href="http://ww2.sinaimg.cn/large/6469180ajw1f4osewkc11j20pa11qaiw.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww2.sinaimg.cn/mw600/6469180ajw1f4osewkc11j20pa11qaiw.jpg" /></p>
<div class="vote" id="vote-3165323"><span id="acv_stat_3165323"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165323" onclick="acv_vote(event,3165323,1);" href="javascript:;">OO</a> [<span id="cos_support-3165323">62</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165323"  onclick="acv_vote(event,3165323,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165323">20</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165321">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：d61affb446a470c4b1a2b9838b8d035a45c36e71" >弱水三千</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165321&quot;&gt;弱水三千&lt;/a&gt;: &#39;">@1 day ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165321">3165321</a></span><p><a href="http://ww2.sinaimg.cn/large/6469180ajw1f4ossuc0y1j20gm0p041e.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww2.sinaimg.cn/mw600/6469180ajw1f4ossuc0y1j20gm0p041e.jpg" /></p>
<div class="vote" id="vote-3165321"><span id="acv_stat_3165321"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165321" onclick="acv_vote(event,3165321,1);" href="javascript:;">OO</a> [<span id="cos_support-3165321">40</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165321"  onclick="acv_vote(event,3165321,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165321">22</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165276">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：0b5b3c8ad5e45b0083c1f5b9b174b5b08f09a945" >臀魔</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165276&quot;&gt;臀魔&lt;/a&gt;: &#39;">@1 day ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165276">3165276</a></span><p><a href="http://ww1.sinaimg.cn/large/55177ebejw1f4or66lm69j20n60xiafm.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww1.sinaimg.cn/mw600/55177ebejw1f4or66lm69j20n60xiafm.jpg" /></p>
<div class="vote" id="vote-3165276"><span id="acv_stat_3165276"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165276" onclick="acv_vote(event,3165276,1);" href="javascript:;">OO</a> [<span id="cos_support-3165276">123</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165276"  onclick="acv_vote(event,3165276,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165276">40</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165267">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：b507090b247469f051f350aaf56789475785e245" >glare</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165267&quot;&gt;glare&lt;/a&gt;: &#39;">@1 day ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165267">3165267</a></span><p><a href="http://ww4.sinaimg.cn/large/0064lcdugw1f4nyqsfgouj30eu0m8jv7.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww4.sinaimg.cn/mw600/0064lcdugw1f4nyqsfgouj30eu0m8jv7.jpg" /></p>
<div class="vote" id="vote-3165267"><span id="acv_stat_3165267"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165267" onclick="acv_vote(event,3165267,1);" href="javascript:;">OO</a> [<span id="cos_support-3165267">216</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165267"  onclick="acv_vote(event,3165267,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165267">38</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165188">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：6758578b706d695dae7b62f435d0389f56a5c802" >梁非凡</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165188&quot;&gt;梁非凡&lt;/a&gt;: &#39;">@1 day ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165188">3165188</a></span><p><a href="http://ww1.sinaimg.cn/large/a00dfa2agw1f4omruamhjj20m10msabt.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww1.sinaimg.cn/mw600/a00dfa2agw1f4omruamhjj20m10msabt.jpg" /></p>
<div class="vote" id="vote-3165188"><span id="acv_stat_3165188"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165188" onclick="acv_vote(event,3165188,1);" href="javascript:;">OO</a> [<span id="cos_support-3165188">90</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165188"  onclick="acv_vote(event,3165188,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165188">60</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165088">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：ebe76bc2bca9f2904033f4c3fd6353f2fdf4399f" >y</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165088&quot;&gt;y&lt;/a&gt;: &#39;">@2 days ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165088">3165088</a></span><p><a href="http://ww4.sinaimg.cn/large/78df33d3gw1eva0d3m9bhg209j07i1l6.gif" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww4.sinaimg.cn/thumb180/78df33d3gw1eva0d3m9bhg209j07i1l6.gif" org_src="http://ww4.sinaimg.cn/mw1024/78df33d3gw1eva0d3m9bhg209j07i1l6.gif" onload="add_img_loading_mask(this, load_sina_gif);"/></p>
<div class="vote" id="vote-3165088"><span id="acv_stat_3165088"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165088" onclick="acv_vote(event,3165088,1);" href="javascript:;">OO</a> [<span id="cos_support-3165088">251</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165088"  onclick="acv_vote(event,3165088,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165088">25</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165084">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：ebe76bc2bca9f2904033f4c3fd6353f2fdf4399f" >y</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165084&quot;&gt;y&lt;/a&gt;: &#39;">@2 days ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165084">3165084</a></span><p><a href="http://ww3.sinaimg.cn/large/006cMxh0gw1exj0jf5bu4g3099052hdt.gif" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww3.sinaimg.cn/thumb180/006cMxh0gw1exj0jf5bu4g3099052hdt.gif" org_src="http://ww3.sinaimg.cn/mw690/006cMxh0gw1exj0jf5bu4g3099052hdt.gif" onload="add_img_loading_mask(this, load_sina_gif);"/></p>
<div class="vote" id="vote-3165084"><span id="acv_stat_3165084"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165084" onclick="acv_vote(event,3165084,1);" href="javascript:;">OO</a> [<span id="cos_support-3165084">64</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165084"  onclick="acv_vote(event,3165084,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165084">31</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165083">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：ebe76bc2bca9f2904033f4c3fd6353f2fdf4399f" >y</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165083&quot;&gt;y&lt;/a&gt;: &#39;">@2 days ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165083">3165083</a></span><p><a href="http://ww1.sinaimg.cn/large/006cMxh0gw1exj0iuygtgg30ak07ob29.gif" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww1.sinaimg.cn/thumb180/006cMxh0gw1exj0iuygtgg30ak07ob29.gif" org_src="http://ww1.sinaimg.cn/mw690/006cMxh0gw1exj0iuygtgg30ak07ob29.gif" onload="add_img_loading_mask(this, load_sina_gif);"/></p>
<div class="vote" id="vote-3165083"><span id="acv_stat_3165083"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165083" onclick="acv_vote(event,3165083,1);" href="javascript:;">OO</a> [<span id="cos_support-3165083">133</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165083"  onclick="acv_vote(event,3165083,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165083">40</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165081">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：ebe76bc2bca9f2904033f4c3fd6353f2fdf4399f" >y</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165081&quot;&gt;y&lt;/a&gt;: &#39;">@2 days ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165081">3165081</a></span><p><a href="http://ww4.sinaimg.cn/large/006cMxh0gw1exgpw1ljwog30b408514y.gif" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww4.sinaimg.cn/thumb180/006cMxh0gw1exgpw1ljwog30b408514y.gif" org_src="http://ww4.sinaimg.cn/mw690/006cMxh0gw1exgpw1ljwog30b408514y.gif" onload="add_img_loading_mask(this, load_sina_gif);"/></p>
<div class="vote" id="vote-3165081"><span id="acv_stat_3165081"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165081" onclick="acv_vote(event,3165081,1);" href="javascript:;">OO</a> [<span id="cos_support-3165081">47</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165081"  onclick="acv_vote(event,3165081,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165081">59</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165080">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：ebe76bc2bca9f2904033f4c3fd6353f2fdf4399f" >y</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165080&quot;&gt;y&lt;/a&gt;: &#39;">@2 days ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165080">3165080</a></span><p><a href="http://ww1.sinaimg.cn/large/006cMxh0gw1exgpt8wqy1g304l06pqv5.gif" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww1.sinaimg.cn/thumb180/006cMxh0gw1exgpt8wqy1g304l06pqv5.gif" org_src="http://ww1.sinaimg.cn/mw690/006cMxh0gw1exgpt8wqy1g304l06pqv5.gif" onload="add_img_loading_mask(this, load_sina_gif);"/></p>
<div class="vote" id="vote-3165080"><span id="acv_stat_3165080"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165080" onclick="acv_vote(event,3165080,1);" href="javascript:;">OO</a> [<span id="cos_support-3165080">90</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165080"  onclick="acv_vote(event,3165080,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165080">30</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165077">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：ebe76bc2bca9f2904033f4c3fd6353f2fdf4399f" >y</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165077&quot;&gt;y&lt;/a&gt;: &#39;">@2 days ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165077">3165077</a></span><p><a href="http://ww2.sinaimg.cn/large/006cMxh0gw1exfilajapxg308z05dqed.gif" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww2.sinaimg.cn/thumb180/006cMxh0gw1exfilajapxg308z05dqed.gif" org_src="http://ww2.sinaimg.cn/mw690/006cMxh0gw1exfilajapxg308z05dqed.gif" onload="add_img_loading_mask(this, load_sina_gif);"/></p>
<div class="vote" id="vote-3165077"><span id="acv_stat_3165077"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165077" onclick="acv_vote(event,3165077,1);" href="javascript:;">OO</a> [<span id="cos_support-3165077">41</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165077"  onclick="acv_vote(event,3165077,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165077">17</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165075">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：ebe76bc2bca9f2904033f4c3fd6353f2fdf4399f" >y</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165075&quot;&gt;y&lt;/a&gt;: &#39;">@2 days ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165075">3165075</a></span><p><a href="http://ww4.sinaimg.cn/large/006cMxh0gw1exfiohorckg30be08k7wj.gif" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww4.sinaimg.cn/thumb180/006cMxh0gw1exfiohorckg30be08k7wj.gif" org_src="http://ww4.sinaimg.cn/mw690/006cMxh0gw1exfiohorckg30be08k7wj.gif" onload="add_img_loading_mask(this, load_sina_gif);"/></p>
<div class="vote" id="vote-3165075"><span id="acv_stat_3165075"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165075" onclick="acv_vote(event,3165075,1);" href="javascript:;">OO</a> [<span id="cos_support-3165075">29</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165075"  onclick="acv_vote(event,3165075,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165075">49</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165061">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：b22084df72955665901fc3650f16c51cfa9331ca" >喜欢喝喝茶</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165061&quot;&gt;喜欢喝喝茶&lt;/a&gt;: &#39;">@2 days ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165061">3165061</a></span><p><a href="http://ww2.sinaimg.cn/large/cd7861dcgw1f4koxbi245j20ku0v9q63.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww2.sinaimg.cn/mw600/cd7861dcgw1f4koxbi245j20ku0v9q63.jpg" /></p>
<div class="vote" id="vote-3165061"><span id="acv_stat_3165061"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165061" onclick="acv_vote(event,3165061,1);" href="javascript:;">OO</a> [<span id="cos_support-3165061">392</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165061"  onclick="acv_vote(event,3165061,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165061">11</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3165058">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：b22084df72955665901fc3650f16c51cfa9331ca" >喜欢喝喝茶</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3165058&quot;&gt;喜欢喝喝茶&lt;/a&gt;: &#39;">@2 days ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3165058">3165058</a></span><p><a href="http://ww4.sinaimg.cn/large/cd7861dcgw1f4oa5eeqyzj20i20c1mxz.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww4.sinaimg.cn/mw600/cd7861dcgw1f4oa5eeqyzj20i20c1mxz.jpg" /></p>
<div class="vote" id="vote-3165058"><span id="acv_stat_3165058"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3165058" onclick="acv_vote(event,3165058,1);" href="javascript:;">OO</a> [<span id="cos_support-3165058">173</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3165058"  onclick="acv_vote(event,3165058,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3165058">13</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



            <li id="comment-3164948">
                <div>
                    <div class="row">
                        <div class="author"><strong
                                title="防伪码：d61affb446a470c4b1a2b9838b8d035a45c36e71" >弱水三千</strong>                            <br>
                            <small><a href="#footer" title="@回复"
                                      onclick="document.getElementById('comment').value += &#39;@&lt;a href=&quot;http://jandan.net/ooxx/page-2012#comment-3164948&quot;&gt;弱水三千&lt;/a&gt;: &#39;">@2 days ago</a></span></small>
                        </div>
                        <div class="text"><span class="righttext"><a href="http://jandan.net/ooxx/page-2012#comment-3164948">3164948</a></span><p><a href="http://ww2.sinaimg.cn/large/6469180ajw1f4o7fx4qywj20ku0v978q.jpg" target="_blank" class="view_img_link">[查看原图]</a><br /><img src="http://ww2.sinaimg.cn/mw600/6469180ajw1f4o7fx4qywj20ku0v978q.jpg" /></p>
<div class="vote" id="vote-3164948"><span id="acv_stat_3164948"></span><a title="圈圈/支持" class="acvclick acv4" id="vote4-3164948" onclick="acv_vote(event,3164948,1);" href="javascript:;">OO</a> [<span id="cos_support-3164948">78</span>] <a title="叉叉/反对" class="acvclick acva"  id="votea-3164948"  onclick="acv_vote(event,3164948,0);" href="javascript:;">XX</a> [<span id="cos_unsupport-3164948">44</span>]</div>
</div>
                    </div>
                    <span class="break"></span></div>

            </li>



    </ol>


    <span class="break"></span>
    <div class="comments">

                <div class="cp-pagenavi">
                                                            <span class="current-comment-page">[2012]</span>
                                                            <a href="http://jandan.net/ooxx/page-2011#comments">
                    2011                </a>
                                                    <a title="Older Comments" href="http://jandan.net/ooxx/page-2011#comments" class="previous-comment-page">»</a>
                    </div>

        <h3>
            <p id="respond">发表评论</p>
        </h3>
    </div>



        <form action="http://jandan.net/wp-comments-post.php" method="post" id="commentform">


                <div class="hide-input">
                    <p><label for="author">称呼: </label><input type="text" name="author" id="author"
                                                              value=""
                                                              title="常用的网络 ID，必填项" size="22" tabindex="1"/></p>

                    <p><label for="email">邮箱: </label><input type="text" name="email" id="email"
                                                             value=""
                                                             title="真实 Email 地址，必填项" size="22" tabindex="2"/></p>
                </div>


            <p><textarea name="comment" id="comment" rows="10" tabindex="4"
                         onkeydown="if(event.ctrlKey&&event.keyCode==13){document.getElementById('submit').click();return false};"></textarea>
            </p>

            <p><input name="submit" id="submit" type="submit" tabindex="5" value="点击发布 / Ctrl+Enter"/>

                <input type="hidden" name="comment_post_ID" value="21183"/>
                <br/></p>
            <p style="display: none;"><input type="hidden" id="akismet_comment_nonce" name="akismet_comment_nonce" value="3e1c5910e9" /></p><p style="display: none;"><input type="hidden" id="ak_js" name="ak_js" value="231"/></p>
        </form>


</div>
			<!-- end comments -->
			<script type="text/javascript">
	var duoshuoQuery = {short_name:"jandan"};
	(function() {
		var ds = document.createElement('script');
		ds.type = 'text/javascript';ds.async = true;
		ds.src = '//static.duoshuo.com/embed.js';
		ds.charset = 'UTF-8';
		(document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ds);
	})();
		(function($) {
		var prev = $('<span id="nav_prev"><a href="javascript:;" title="上一页">&#8250;</a></span>');
		var next = $('<span id="nav_next"><a href="javascript:;" title="下一页">&#8249;</a></span>');

		$('#body').append(prev).append(next);
		$().ready(function() {
			var current_span = $('.current-comment-page');
			if (current_span.length == 0) {
				return;
			}
			var prev_link = current_span.prev('a');
			if (prev_link.length > 0) {
				next.show();
				next.find('a').attr('href', prev_link.attr('href'));
			} else {
				next.hide();
			}
			var next_link = current_span.next('a');
			if (next_link.length > 0) {
				prev.show();
				prev.find('a').attr('href', next_link.attr('href'));
			} else {
				prev.hide();
			}
		});
	})($);
	</script>
<script src="http://cdn.jandan.net/static/js/tucao.js?v=20160510"></script>
    <div id="tucao-gg">
        <div style="padding:20px 0 10px 125px;border-top:1px solid #EEE;border-bottom:1px solid #EEE;"><div style="width:336px;">
        <font color="#AAA">[ 广告 ]</font><br>
        <!-- 336[adsense+baidu] -->
        <script type="text/javascript">
/*336*280*/
var cpro_id = "u529095";
</script>
<script src="http://cpro.baidustatic.com/cpro/ui/c.js" type="text/javascript"></script>        </div></div>
    </div>
			<script>
	var gif_click_load = getCookie('gif-click-load');
	var bad_click_load = getCookie('bad-click-load');
	var nsfw_click_load = getCookie('nsfw-click-load');
	var gif_on = (gif_click_load == 'on' || gif_click_load == null) ? true : false;
	var nsfw_on = (nsfw_click_load == 'on' || nsfw_click_load == null) ? true : false;
	var bad_on = (bad_click_load == 'on' || bad_click_load == null) ? true : false;


	$('.switch').removeClass('switch-current');
	var btn_id = 'gif-click-load-off';
	if (gif_on) {
		btn_id = 'gif-click-load-on';
	}
	$('#'+btn_id).addClass('switch-current');

	btn_id = 'nsfw-click-load-off';
	if (nsfw_on) {
		btn_id = 'nsfw-click-load-on';
	}
	$('#'+btn_id).addClass('switch-current');


	btn_id = 'bad-click-load-off';
	if (bad_on) {
		btn_id = 'bad-click-load-on';
	}
	$('#'+btn_id).addClass('switch-current');



	$('#gif-click-load-on').click(function() {

		if ($(this).hasClass('switch-current'))
			return;
		setCookie('gif-click-load', 'on', 30);
		$('#gif-click-load-off').removeClass('switch-current');
		$(this).addClass('switch-current');
		location.reload();
	});

	$('#gif-click-load-off').click(function() {
		if ($(this).hasClass('switch-current'))
			return;
		setCookie('gif-click-load', 'off', 30);
		$('#gif-click-load-on').removeClass('switch-current');
		$(this).addClass('switch-current');
		location.reload();
	});

	$('#nsfw-click-load-on').click(function() {
		if ($(this).hasClass('switch-current'))
			return;
		setCookie('nsfw-click-load', 'on', 30);
		$('#nsfw-click-load-off').removeClass('switch-current');
		$(this).addClass('switch-current');
		location.reload();
	});

	$('#nsfw-click-load-off').click(function() {
		if ($(this).hasClass('switch-current'))
			return;
		setCookie('nsfw-click-load', 'off', 30);
		$('#nsfw-click-load-on').removeClass('switch-current');
		$(this).addClass('switch-current');
		location.reload();
	});

	$('#bad-click-load-on').click(function() {
		if ($(this).hasClass('switch-current'))
			return;
		setCookie('bad-click-load', 'on', 30);
		$('#bad-click-load-off').removeClass('switch-current');
		$(this).addClass('switch-current');
		location.reload();
	});

	$('#bad-click-load-off').click(function() {
		if ($(this).hasClass('switch-current'))
			return;
		setCookie('bad-click-load', 'off', 30);
		$('#bad-click-load-on').removeClass('switch-current');
		$(this).addClass('switch-current');
		location.reload();
	});
	$(".commentlist li").each(function () {
		var e = $(this);
		var is_bad = false;
		if (bad_on) {
			var oo = parseInt(e.find('.vote span[id^="cos_support"]').text());
			var xx = parseInt(e.find('.vote span[id^="cos_unsupport"]').text());
			// oo xx 总和超过50个，且xx占多数
			if ( (oo + xx) >= 50 && (oo / xx) < 0.618 ) {
				is_bad = true;
				var r = e.find("p").not('.bad_content');
				r.hide();
				e.find('.righttext').after('<p class="bad_content" style="color:#ddd">因不受欢迎已被超载鸡自动隐藏.  <a href="javascript:;" class="view_bad">[手贱一回]</a></p>');
				e.find(".view_bad").click(function () {
					if (this.innerHTML == '[手贱一回]' || this.innerHTML == '[再手贱一回]') {
						r.show();
						if (this.innerHTML == '[手贱一回]') {
							r.find('.gif-mask').remove();
							r.find('img').each(function() {
								var org_src = this.getAttribute('org_src');
								if (org_src)
									this.src = org_src;
							});
						}
						this.innerHTML = '[真不该手贱]';
					} else {
						r.hide();
						this.innerHTML = '[再手贱一回]';
					}
				});
			}
		}

		if ( ! is_bad && nsfw_on) {
			var p = e.find("p").not('.bad_content');
			if (p.length == 0) // ad line
				return;
			var content = p.html();
			if (content.indexOf('NSFW') > -1) {
				p.hide();
				e.find('.righttext').after('<p class="nsfw_content" style="color:#ff6600">此图被标记为<b>NSFW</b>被超载鸡自动隐藏.  <a href="javascript:;" class="view_nsfw">[旁边没人]</a></p>');
				e.find(".view_nsfw").click(function () {
					if (this.innerHTML == '[旁边没人]' || this.innerHTML == '[旁边还是没人]') {
						p.show();
						p.find('.gif-mask').remove();
						if (this.innerHTML == '[旁边没人]') {
							p.find('img').each(function() {
								var org_src = this.getAttribute('org_src');
								if (org_src)
									this.src = org_src;
							});
						}
						this.innerHTML = '[看完了，擦键盘]';
					} else {
						p.hide();
						this.innerHTML = '[旁边还是没人]';
					}
				});
			}
		}

	});
</script>			<script>
	$('.commentlist li p img').each(function (imgIndex) {
		var max_width = $(this).parent().parent().width();
		$(this).css('max-width', max_width);
		$(this).css('max-height', '750px').click(function () {
			var $this = $(this);
			if ($this.css('max-height') == 'none') {
				var max_width = $(this).parent().parent().width();
				$this.css('max-width', max_width);
				$this.css('max-height', '750px');
			} else {
				if ($this.parent().hasClass('acv_comment'))
					$this.css('max-width', 'none');
				$this.css('max-height', 'none');
			}
			$("html,body").animate(
				{
					scrollTop: $this.offset().top - 40
				},
				325
			);
		});
	});
	</script>			<script>
	$("img.lazy").each(function () {
		$(this).lazyload({
			effect: "fadeIn"
		});
	});
</script>
	</div>
	<!-- END content -->

<!-- BEGIN sidebar -->
<div id="sidebar">

    <form  method="get" action="http://s.jandan.net/cse/search" id="cse-search-box" target="_blank">
<input type="text" name="q" id="s" value="" placeholder="搜索"></input>
<button type="submit">Search</button>
<input type="hidden" name="s" value="18250727425702039732" />
<input type="hidden" name="source" value="jandan.net" />
</form>
<!-- 直投广告 -->
    <ul><h3>[ Sponsors ]</h3>
        <div ID="ads">
            <script>
var str=new Array("1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg","7.jpg");
var a;
a=str[parseInt(Math.random()*(str.length))];
document.write("<a href=\"http://jandan.net/money.php?redirect_id=10\" target=\"_blank\" rel=\"external nofollow\"><img src=\"http://s.jandan.com/static/gg/niuza/"+a+"\" border=\"0\" /></a>");
</script><!-- niuza -->
            <script>
var str=new Array("1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg");
var a;
a=str[parseInt(Math.random()*(str.length))];
document.write("<a href=\"http://jandan.net/money.php?redirect_id=79\" target=\"_blank\" rel=\"external nofollow\"><img src=\"http://s.jandan.com/static/gg/kiees/"+a+"\" border=\"0\" /></a>");
</script><!-- kiees -->
            <script>
var str=new Array("01.png","02.png","03.png","04.png");
var a;
a=str[parseInt(Math.random()*(str.length))];
document.write("<a href=\"http://jandan.net/money.php?redirect_id=108\" target=\"_blank\" rel=\"external nofollow\"><img src=\"http://s.jandan.com/static/gg/icuiya/"+a+"\" border=\"0\" /></a>");
</script><!-- icuiya -->
            <a href="http://jandan.net/money.php?redirect_id=122" target="_blank"><img src="http://s.jandan.com/static/gg/chaozaiji3.jpg" border="0" height="145" width="145"></a><!-- chaozaiji -->
           <script>
var str=new Array("29yx2.png","29yx3.png");
var a;
a=str[parseInt(Math.random()*(str.length))];
document.write("<a href=\"http://jandan.net/money.php?redirect_id=125\" target=\"_blank\" rel=\"external nofollow\"><img src=\"http://s.jandan.com/static/gg/"+a+"\" border=\"0\" /></a>");
</script><!-- 29yx -->
           <a href="http://jandan.net/money.php?redirect_id=41" target="_blank"><img src="http://s.jandan.com/static/gg/g2.png" border="0" height="145" width="145"></a><!-- G -->
        </div>
        <div id="random-ads" class="xy" style="display:none;"></div>
    </ul>

<!-- 首页 -->


<!-- 中部广告 -->
            <ul ID="adsense"><!-- 300-baidu[1] -->
            <script type="text/javascript">
    /*300*250[1]*/
    var cpro_id = "u520738";
</script>
<script src="http://cpro.baidustatic.com/cpro/ui/c.js" type="text/javascript"></script>        </ul>

<!-- 热文榜 -->
    <div class="hot-list">
        <ul class="hot-tabs">
            <li id="tab-hotposts" class="current">24H热文</li>
            <li id="tab-hotlike">三日最赞</li>
            <li id="tab-hotcomments">一周话题</li>
            <div class="break"></div>
        </ul>
        <div class="host-list-split"></div>
        <div class="hot-list-item hot-list-item-current" id="list-hotposts">
            <!-- 日点击排行 -->
            <ol>
		<script>
		document.write(decodeURIComponent('%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F09%2Fbreastfeeding-boyfriend.html%22%20title%3D%2240743%E6%AC%A1%E6%B5%8F%E8%A7%88%22%3E%E5%A5%B3%E5%AD%90%E6%94%BE%E5%BC%83%E5%B7%A5%E4%BD%9C%E7%94%A8%E5%8F%8C%E4%B9%B3%E5%96%82%E5%85%BB%E7%94%B7%E7%A5%A8%3C%2Fa%3E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F09%2Fbad-flip-flops.html%22%20title%3D%2210296%E6%AC%A1%E6%B5%8F%E8%A7%88%22%3E%E5%A4%8F%E5%A4%A9%E5%88%B0%E4%BA%86%EF%BC%8C%E4%BD%86%E6%98%AF%E4%BA%BA%E5%AD%97%E6%8B%96%E8%A6%81%E5%B0%BD%E9%87%8F%E5%B0%91%E7%A9%BF%3C%2Fa%3E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F10%2Fadult-actresses-eco.html%22%20title%3D%227904%E6%AC%A1%E6%B5%8F%E8%A7%88%22%3E%E8%B7%9F%E7%9D%80%E6%97%A5%E6%9C%ACAV%E5%A5%B3%E6%98%9F%E5%AD%A6%E7%8E%AF%E4%BF%9D%3C%2Fa%3E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F10%2Fcoins-fountains.html%22%20title%3D%225762%E6%AC%A1%E6%B5%8F%E8%A7%88%22%3E%E8%B0%81%E5%8A%A8%E4%BA%86%E8%AE%B8%E6%84%BF%E6%B1%A0%E7%9A%84%E7%A1%AC%E5%B8%81%3C%2Fa%3E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F09%2Fheavy-machinery-girl.html%22%20title%3D%225696%E6%AC%A1%E6%B5%8F%E8%A7%88%22%3E%E6%B0%94%E7%90%83%E6%8C%82%E5%9C%A8%E6%A0%91%E4%B8%8A%E4%BA%86%EF%BC%9F%E9%87%8D%E6%9C%BA%E5%B0%91%E5%A5%B3%EF%BC%8C%E5%87%BA%E5%8A%A8%EF%BC%81%3C%2Fa%3E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F10%2F100-temperatures.html%22%20title%3D%225443%E6%AC%A1%E6%B5%8F%E8%A7%88%22%3E%E5%85%B3%E4%BA%8E%E6%B8%A9%E5%BA%A6%E7%9A%84100%E4%B8%AA%E5%B0%8F%E7%9F%A5%E8%AF%86%3C%2Fa%3E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F09%2Fthey-are-ugly.html%22%20title%3D%225043%E6%AC%A1%E6%B5%8F%E8%A7%88%22%3E%E6%88%91%E7%88%B1%E4%BD%A0%EF%BC%8C%E6%88%91%E8%A7%89%E5%BE%97%E5%85%B6%E4%BB%96%E4%BA%BA%E9%83%BD%E4%B8%91%E7%88%86%E4%BA%86%3C%2Fa%3E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F09%2Fblood-safe.html%22%20title%3D%224109%E6%AC%A1%E6%B5%8F%E8%A7%88%22%3E%E6%88%90%E4%B8%BA%E5%90%B8%E8%A1%80%E9%AC%BC%E4%B9%8B%E5%89%8D%E7%9A%84%E7%96%91%E9%97%AE%EF%BC%9A%E5%96%9D%E8%A1%80%E9%9D%A0%E8%B0%B1%E5%90%97%EF%BC%9F%3C%2Fa%3E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F10%2Fhanyu-pinyin.html%22%20title%3D%223786%E6%AC%A1%E6%B5%8F%E8%A7%88%22%3E%E6%AD%AA%E5%9B%BD%E5%B0%8F%E4%BC%99%E5%90%90%E6%A7%BD%EF%BC%9A%E4%B8%BA%E4%BB%80%E4%B9%88%E6%B1%89%E8%AF%AD%E6%8B%BC%E9%9F%B3%E5%BE%88%E9%87%8D%E8%A6%81%3C%2Fa%3E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F09%2Fmammal-rules.html%22%20title%3D%223345%E6%AC%A1%E6%B5%8F%E8%A7%88%22%3E%E5%93%BA%E4%B9%B3%E5%8A%A8%E7%89%A9%E6%97%A9%E5%9C%A8%E6%81%90%E9%BE%99%E7%81%AD%E7%BB%9D%E4%B9%8B%E5%89%8D%E5%B0%B1%E5%BC%80%E5%A7%8B%E5%BE%81%E6%9C%8D%E5%9C%B0%E7%90%83%3C%2Fa%3E%3C%2Fli%3E'));
	</script>
</ol>
        </div>
        <div class="hot-list-item" id="list-hotlike">
            <!-- 日最赞排行 -->
            <ol>
		<script>
		document.write(decodeURIComponent('%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F08%2Fthree-naked-women.html%22%3E%E8%A3%B8%E4%BD%93%E5%BD%A9%E7%BB%98%EF%BC%9A%E4%B8%89%E4%B8%AA%E5%A5%B3%E4%BA%BA%E5%8C%96%E8%BA%AB%E4%B8%BA%E7%8B%BC%3C%2Fa%3E%20%20105%E8%B5%9E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F09%2Fgps-tracks-cats.html%22%3E%E7%94%A8GPS%E8%BF%BD%E8%B8%AA%E6%99%9A%E4%B8%8A%E7%9A%84%E7%8C%AB%EF%BC%8C%E7%BB%93%E6%9E%9C%E5%BE%88%E8%AF%A1%E5%BC%82%3C%2Fa%3E%20%2084%E8%B5%9E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F09%2Fjelly-bloody.html%22%3E%E7%A9%BF%E4%B8%8A%E8%BF%99%E5%8F%8C%E6%BC%82%E4%BA%AE%E7%9A%84%E7%AB%A5%E9%9E%8B%E6%89%8D%E5%8D%8A%E5%B0%8F%E6%97%B6%EF%BC%8C%E5%AD%A9%E5%AD%90%E7%9A%84%E8%84%9A%E5%B0%B1%E9%B2%9C%E8%A1%80%E6%B7%8B%E6%BC%93%3C%2Fa%3E%20%2081%E8%B5%9E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F09%2Frich-old-women.html%22%3E%E7%A0%94%E7%A9%B6%E5%8F%91%E7%8E%B0%E6%9C%89%E9%92%B1%E7%9A%84%E8%80%81%E5%A5%B3%E4%BA%BA%E6%80%A7%E7%94%9F%E6%B4%BB%E8%B4%A8%E9%87%8F%E5%B0%A4%E4%BD%B3%3C%2Fa%3E%20%2080%E8%B5%9E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F08%2Fsexual-assault-victim.html%22%3E%E6%B3%95%E5%BA%AD%E9%99%88%E8%BF%B0%EF%BC%9A%E8%87%B4%E6%80%A7%E4%BE%B5%E6%88%91%E7%9A%84%E6%96%AF%E5%9D%A6%E7%A6%8F%E7%94%B7%E7%94%9F%3C%2Fa%3E%20%2079%E8%B5%9E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F08%2Fjapan-pictures-45.html%22%3E%5B%E6%97%A5%E5%BC%8F%E5%8E%9F%E7%89%88%5D%E6%97%A0%E8%81%8A%E5%9B%BE%E5%A4%A7%E5%90%90%E6%A7%BD%E3%80%9045P%E3%80%91%3C%2Fa%3E%20%2068%E8%B5%9E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F08%2Ftesting-16-ramen.html%22%3E%E7%9C%9F%E7%9A%84%E7%8C%9B%E5%A3%AB%EF%BC%8C%E5%90%83%E4%B8%8B%E4%B8%80%E7%BD%9016%E5%B2%81%E7%9A%84%E6%8B%89%E9%9D%A2%3C%2Fa%3E%20%2054%E8%B5%9E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F08%2Fpvc_katana_diy.html%22%3E%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99%E4%BD%A0%E5%A6%82%E4%BD%95%28%E4%BD%8E%E6%88%90%E6%9C%AC%29DIY%E4%B8%80%E6%8A%8A%E5%88%A9%E5%88%83%3C%2Fa%3E%20%2051%E8%B5%9E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F08%2Fcrying-kids.html%22%3E%E7%8E%B0%E5%9C%A8%E7%9A%84%E5%B0%8F%E5%AD%A9%E5%95%8A%EF%BC%8C%E4%B8%80%E8%A8%80%E4%B8%8D%E5%90%88%E5%B0%B1%E6%B3%AA%E5%A5%94%3C%2Fa%3E%20%2045%E8%B5%9E%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F08%2Fline-clothes-refugees.html%22%3E%E6%9C%80%E7%82%AB%E9%9A%BE%E6%B0%91%E9%A3%8E%EF%BC%9A%E4%B8%93%E4%B8%BA%E9%9A%BE%E6%B0%91%E6%89%93%E9%80%A0%E7%9A%84%E6%97%B6%E8%A3%85%E7%B3%BB%E5%88%97%3C%2Fa%3E%20%2031%E8%B5%9E%3C%2Fli%3E'));
	</script>
</ol>
	        </div>
        <div class="hot-list-item" id="list-hotcomments">
            <!-- 周评论排行 -->
            <ol>
		<script>
		document.write(decodeURIComponent('%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F08%2Fsexual-assault-victim.html%22%3E%E6%B3%95%E5%BA%AD%E9%99%88%E8%BF%B0%EF%BC%9A%E8%87%B4%E6%80%A7%E4%BE%B5%E6%88%91%E7%9A%84%E6%96%AF%E5%9D%A6%E7%A6%8F%E7%94%B7%E7%94%9F%3C%2Fa%3E%20%20146%E8%AF%84%E8%AE%BA%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F04%2Fpromiscuous-gay-men.html%22%3E%E6%88%91%E4%BB%AC%E5%BA%94%E8%AF%A5%E5%9B%A0%E4%B8%BA%E9%83%A8%E5%88%86%E5%9F%BA%E4%BD%AC%E6%BB%A5%E4%BA%A4%E8%80%8C%E6%AD%A7%E8%A7%86%E6%95%B4%E4%B8%AA%E5%9F%BA%E4%BD%AC%E5%9C%88%E5%90%97%EF%BC%9F%3C%2Fa%3E%20%2090%E8%AF%84%E8%AE%BA%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F08%2Fgay-reproductive-refugees.html%22%3E%E8%A5%BF%E6%96%B9%E7%A6%81%E6%AD%A2%E4%BB%A3%E5%AD%95%E6%9C%8D%E5%8A%A1%EF%BC%9A%E5%90%8C%E6%80%A7%E6%81%8B%E5%A4%AB%E5%A6%BB%E6%81%90%E6%88%90%E6%9C%80%E5%A4%A7%E8%BE%93%E5%AE%B6%3C%2Fa%3E%20%2076%E8%AF%84%E8%AE%BA%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F03%2Ffucking-kids.html%22%3E%E2%80%9C%E7%86%8AXX%E2%80%9D%E4%BB%AC%E7%9A%84%E7%A0%B4%E5%9D%8F%E5%8A%9B%3C%2Fa%3E%20%2072%E8%AF%84%E8%AE%BA%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F06%2Fvideo-game-world.html%22%3E%E9%A9%AC%E4%B8%80%E9%BE%99%E8%AF%B4%E4%BA%BA%E7%B1%BB%E6%AD%A3%E7%94%9F%E6%B4%BB%E5%9C%A8%E9%AB%98%E7%BA%A7%E6%96%87%E6%98%8E%E7%9A%84%E7%94%B5%E5%AD%90%E6%B8%B8%E6%88%8F%E4%B8%AD%3C%2Fa%3E%20%2071%E8%AF%84%E8%AE%BA%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F09%2Fpokemon-election.html%22%3E%E7%B2%BE%E7%81%B5%E5%AE%9D%E5%8F%AF%E6%A2%A6%E4%BA%BA%E6%B0%94%E6%8A%95%E7%A5%A8%EF%BC%8C%E8%8E%B7%E8%83%9C%E8%80%85%E7%AB%9F%E7%84%B6%E4%B8%8D%E6%98%AF%E7%9A%AE%E5%8D%A1%E4%B8%98%3C%2Fa%3E%20%2068%E8%AF%84%E8%AE%BA%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F06%2Fbetter-boyfriend.html%22%3E%E6%97%A5%E6%9C%AC%E6%96%B0%E8%B0%83%E6%9F%A5%EF%BC%9A%E8%AF%A5%E7%BA%A6%E6%97%A0%E8%81%8A%E7%9A%84%E5%B8%85%E5%93%A5%E8%BF%98%E6%98%AF%E6%9C%89%E8%B6%A3%E7%9A%84%E4%B8%91%E7%94%B7%3C%2Fa%3E%20%2064%E8%AF%84%E8%AE%BA%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F06%2Fnot-welcome-chinese.html%22%3E%E4%B8%BA%E4%BB%80%E4%B9%88%E6%AD%8C%E8%88%9E%E4%BC%8E%E7%94%BA%E4%B8%8D%E6%AC%A2%E8%BF%8E%E4%B8%AD%E5%9B%BD%E6%B8%B8%E5%AE%A2%EF%BC%9F%3C%2Fa%3E%20%2063%E8%AF%84%E8%AE%BA%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F08%2Fpvc_katana_diy.html%22%3E%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99%E4%BD%A0%E5%A6%82%E4%BD%95%28%E4%BD%8E%E6%88%90%E6%9C%AC%29DIY%E4%B8%80%E6%8A%8A%E5%88%A9%E5%88%83%3C%2Fa%3E%20%2062%E8%AF%84%E8%AE%BA%3C%2Fli%3E%3Cli%3E%3Ca%20href%3D%22http%3A%2F%2Fjandan.net%2F2016%2F06%2F04%2Fprayer-mental-health.html%22%3E%E5%AE%97%E6%95%99%E4%BF%A1%E4%BB%B0%E6%9C%89%E4%BB%80%E4%B9%88%E7%A7%91%E5%AD%A6%E4%B8%8A%E7%9A%84%E7%94%A8%E5%A4%84%3C%2Fa%3E%20%2060%E8%AF%84%E8%AE%BA%3C%2Fli%3E'));
	</script>
</ol>
	        </div>
    </div>

<!-- 插入优评 -->

<!-- 底部广告 -->
            <div id="box">
            <div id="float" class="box">
                <ul ID="adsense"><!-- 300-taobao -->
                    <script type="text/javascript">
     document.write('<a style="display:none!important" id="tanx-a-mm_10008550_105090_10650815"></a>');
     tanx_s = document.createElement("script");
     tanx_s.type = "text/javascript";
     tanx_s.charset = "gbk";
     tanx_s.id = "tanx-s-mm_10008550_105090_10650815";
     tanx_s.async = true;
     tanx_s.src = "http://p.tanx.com/ex?i=mm_10008550_105090_10650815";
     tanx_h = document.getElementsByTagName("head")[0];
     if(tanx_h)tanx_h.insertBefore(tanx_s,tanx_h.firstChild);
</script>                </ul>
                <ul ID="adsense"><!-- 300-baidu -->
                    <script type="text/javascript">
    /*300*250*/
    var cpro_id = "u608784";
</script>
<script src="http://cpro.baidustatic.com/cpro/ui/c.js" type="text/javascript"></script>                </ul>
            </div>
        </div>


    <!-- random-ad JS -->
    <script>
        (function () {
            var source = document.getElementById("ads");
            var target = document.getElementById("random-ads");
            var ads = source.getElementsByTagName("a");
            var arr = [];
            for (var i = 0; i < ads.length; i++) {
                arr[i] = i;
            }

            function randomSort(d, c) {
                var e = parseInt((Math.random() + 0.5), 10);
                return e ? d - c : c - d;
            }

            arr.sort(randomSort);
            for (var i = 0; i < arr.length; i++) {
                target.appendChild(ads[arr[i]].cloneNode(true));
            }
            source.parentNode.removeChild(source);
            target.style.display = "block";
        })();
    </script>

    <!-- hot-tabs JS -->
    <script>
    (function($) {
        function add_show_more() {
            var $this = $(this);
            var pHeight = 0;
            $this.find('p').each(function () {
                pHeight += $(this).height();
            });
            if (pHeight > $this.height()) {
                var show_more = $this.find('.show_more');
                if (show_more.length == 0) {
                    $this.append('<div class="show_more"> &DownTeeArrow;  展开</div>')
                }
            }
        }

        $('.hot-tabs li').click(function () {
            var tab = this.id.split('-')[1];
            var parent = $(this).parent();
            parent.find('li').removeClass('current');
            parent.parent().find('.hot-list-item').removeClass('hot-list-item-current');
            $(this).addClass('current');
            var list_tab = $('#list-' + tab);
            list_tab.addClass('hot-list-item-current');
            list_tab.find('.acv_comment').each(add_show_more);
            list_tab.find('.gif-mask').each(function () {
                var $this = $(this);
                if ($this.height() > 0) {
                    return;
                }
                $this.parent().css('position', 'relative');
                var img = $this.prev();
                var position = img.position();
                $this.css({
                    'height': img.height(),
                    'width': img.width(),
                    'line-height': img.height() + 'px',
                    'left': position.left,
                    'top': position.top
                });
            });
        });
        $(window).load(function () {
            $('.acv_comment').click(function () {
                var $this = $(this);
                var show_more = $this.find('.show_more');
                if (show_more.length == 0) {
                    return;
                }
                if (!$this.hasClass('acv_comment_full_size')) {
                    $this.addClass('acv_comment_full_size');
                    show_more.html(' &UpTeeArrow; 收起');
                } else {
                    $this.removeClass('acv_comment_full_size');
                    show_more.html(' &DownTeeArrow; 展开');
                }
            }).each(add_show_more);
        });
    })($);
</script>
    <!-- END sidebar -->

    <div class="break"></div>
</div>
<!-- END body --><!-- BEGIN footer -->
</div>
<a id="nav_top" style="cursor:pointer;" title="回到页头"><span>&#9650;</span></a>
<div id="footer">
			&copy; 2006-2016. 煎蛋，每天更新鲜。</a>
		</div>
<!-- END footer -->
<!-- BEGIN JS -->

	<script src="http://cdn.jandan.net/static/js/comments-ajax.js?v=201603020"></script>

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');
  ga('create', 'UA-462921-3', 'auto');
  ga('send', 'pageview');
</script>
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?fd93b7fb546adcfbcf80c4fc2b54da2c";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>

<!-- END JS -->

</div>
<!-- END wrapper --></body>
</html>
"""

soup=BeautifulSoup(source,"html.parser")

# res=soup.findAll("li",attrs={"id":re.compile("comment-\d+")})
res=soup.findAll("div",attrs={"class":"text"})

for i in res:
    print(i)
    print("+++++++++++++++++++")
for i in res:
    imgPattern=re.compile("\"http://ww\d\.sinaimg\.cn/large.+?\"")
    soup=BeautifulSoup(str(i),"html.parser")
    voteHtml=soup.findAll("div",attrs={"class","vote"})
    upVoteNumPattern=re.compile("cos_support-\d+\">+(\d+)</span>")
    upVoteNum=re.findall(upVoteNumPattern,str(voteHtml))
    downVoteNumPattern=re.compile("cos_unsupport-\d+\">+(\d+)</span>")
    downVoteNum=re.findall(downVoteNumPattern,str(voteHtml))
    imgUrl=re.findall(imgPattern,str(i))
    print(imgUrl)
    print(upVoteNum[0]+"  "+downVoteNum[0])


# print(res[3])