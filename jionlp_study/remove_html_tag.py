import jionlp as jio

text = """


<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <link rel="canonical" href="https://blog.csdn.net/dongrixinyu/article/details/120244906"/>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit"/>
    <meta name="force-rendering" content="webkit"/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="report" content='{"pid": "blog", "spm":"1001.2101"}'>
    <meta name="referrer" content="always">
    <meta http-equiv="Cache-Control" content="no-siteapp" /><link rel="alternate" media="handheld" href="#" />
    <meta name="shenma-site-verification" content="5a59773ab8077d4a62bf469ab966a63b_1497598848">
    <meta name="applicable-device" content="pc">
    <link  href="https://g.csdnimg.cn/static/logo/favicon32.ico"  rel="shortcut icon" type="image/x-icon" />
    <title>提取文本中的金额，提取货币，Python实现与在线使用_冬日新雨的博客-CSDN博客_python 处理金额</title>
    <script>
      (function(){ 
        var el = document.createElement("script"); 
        el.src = "https://s3a.pstatp.com/toutiao/push.js?1abfa13dfe74d72d41d83c86d240de427e7cac50c51ead53b2e79d40c7952a23ed7716d05b4a0f683a653eab3e214672511de2457e74e99286eb2c33f4428830"; 
        el.id = "ttzz"; 
        var s = document.getElementsByTagName("script")[0]; 
        s.parentNode.insertBefore(el, s);
      })(window)
    </script>
        <meta name="keywords" content="python 处理金额">
        <meta name="csdn-baidu-search"  content='{"autorun":true,"install":true,"keyword":"python 处理金额"}'>
    <meta name="description" content="给定一篇文本，提取出文本中涉及到的所有的货币和金额。例如：'张三赔偿李四人民币车费601,293.11元，工厂费一万二千三百四十五元,利息9佰日元，打印费十块钱。' 从中提取出'601,293.11元', '一万二千三百四十五元', '9佰日元', '十块钱' 这样的字符串，并把他们都规范化，形成'601293.11元', '12345.00元', '900.00日元', '10.00元' 这样的结果。方便存储和计算。⭐ 源码戳 =&amp;gt; JioNLPhttps://github....">
    <script src="//g.csdnimg.cn/tingyun/1.8.5/blog.js" type='text/javascript'></script>
        <link rel="stylesheet" type="text/css" href="https://csdnimg.cn/release/blogv2/dist/pc/css/detail_enter-98da382783.min.css">
    <script type="application/ld+json">{"@context":"https://ziyuan.baidu.com/contexts/cambrian.jsonld","@id":"https://blog.csdn.net/dongrixinyu/article/details/120244906","appid":"1638831770136827","pubDate":"2021-09-11T23:22:24","title":"提取文本中的金额，提取货币，Python实现与在线使用_冬日新雨的博客-CSDN博客_python 处理金额","upDate":"2021-09-11T23:27:20"}</script>
        <link rel="stylesheet" type="text/css" href="https://csdnimg.cn/release/blogv2/dist/pc/themesSkin/skin3-template/skin3-template-762f7595fd.min.css">
    <script src="https://csdnimg.cn/public/common/libs/jquery/jquery-1.9.1.min.js" type="text/javascript"></script>
    <script type="text/javascript">
        var isCorporate = false;//注释删除enterprise
        var username =  "dongrixinyu";
        var skinImg = "white";
        var blog_address = "https://blog.csdn.net/dongrixinyu";
        var currentUserName = "G_sir_";
        var isOwner = false;
        var loginUrl = "http://passport.csdn.net/account/login?from=https://blog.csdn.net/dongrixinyu/article/details/120244906";
        var blogUrl = "https://blog.csdn.net/";
        var avatar = "https://profile.csdnimg.cn/A/3/3/3_dongrixinyu";
        var articleTitle = "提取文本中的金额，提取货币，Python实现与在线使用";
        var articleDesc = "给定一篇文本，提取出文本中涉及到的所有的货币和金额。例如：\'张三赔偿李四人民币车费601,293.11元，工厂费一万二千三百四十五元,利息9佰日元，打印费十块钱。\' 从中提取出\'601,293.11元\', \'一万二千三百四十五元\', \'9佰日元\', \'十块钱\' 这样的字符串，并把他们都规范化，形成\'601293.11元\', \'12345.00元\', \'900.00日元\', \'10.00元\' 这样的结果。方便存储和计算。⭐ 源码戳 =&amp;gt; JioNLPhttps://github....";
        var articleTitles = "提取文本中的金额，提取货币，Python实现与在线使用_冬日新雨的博客-CSDN博客_python 处理金额";
        var nickName = "冬日新雨";
        var articleDetailUrl = "https://blog.csdn.net/dongrixinyu/article/details/120244906";
        if(window.location.host.split('.').length == 3) {
            blog_address = blogUrl + username;
        }
        var skinStatus = "White";
        var blogStaticHost = "https://csdnimg.cn/release/blogv2/"
        var mallTestStyle = "control"
    </script>
    <script src="https://g.csdnimg.cn/??fixed-sidebar/1.1.6/fixed-sidebar.js" type="text/javascript"></script>
    <script src='//g.csdnimg.cn/common/csdn-report/report.js' type='text/javascript'></script>
    <link rel="stylesheet" type="text/css" href="https://csdnimg.cn/public/sandalstrap/1.4/css/sandalstrap.min.css">
    <style>
        .MathJax, .MathJax_Message, .MathJax_Preview{
            display: none
        }
    </style>
    <script src="https://dup.baidustatic.com/js/ds.js"></script>
</head>
  <body class="nodata " style="">
        <script>
            var toolbarSearchExt = '{"landingWord":["python 处理金额"],"queryWord":"","tag":["python","开发语言"],"title":"提取文本中的金额，提取货币，Python实现与在线使用"}';
        </script>
    <script src="https://g.csdnimg.cn/common/csdn-toolbar/csdn-toolbar.js" type="text/javascript"></script>
    <script>
    (function(){
        var bp = document.createElement('script');
        var curProtocol = window.location.protocol.split(':')[0];
        if (curProtocol === 'https') {
            bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
        }
        else {
            bp.src = 'http://push.zhanzhang.baidu.com/push.js';
        }
        var s = document.getElementsByTagName("script")[0];
        s.parentNode.insertBefore(bp, s);
    })();
    </script>
<link rel="stylesheet" href="https://csdnimg.cn/release/blogv2/dist/pc/css/blog_code-01256533b5.min.css">
<link rel="stylesheet" href="https://csdnimg.cn/release/blogv2/dist/mdeditor/css/editerView/chart-3456820cac.css" />

<script>
    var articleId = 120244906;
    var commentscount = 1;
    var curentUrl = "https://blog.csdn.net/dongrixinyu/article/details/120244906";
    var myUrl = "https://my.csdn.net/";
    var highlight = ["python","语言","使用","处理","文本","提取","货币","实现","开发","在线","金额","的","，","中","与"];//高亮数组
    var isRecommendModule = true;
    var isBaiduPre = true;
    var baiduCount = 2;
    var setBaiduJsCount = 10;
    var share_card_url = "https://app-blog.csdn.net/share?article_id=120244906&username=dongrixinyu"
	var articleType = 1;
    var baiduKey = "python 处理金额";
    var userNewReport = true;
    var needInsertBaidu = true;
    var recommendRegularDomainArr = ["blog.csdn.net/.+/article/details/","download.csdn.net/download/","edu.csdn.net/course/detail/","ask.csdn.net/questions/","bbs.csdn.net/topics/","www.csdn.net/gather_.+/"]
    var codeStyle = "";
    var baiduSearchType = "baidulandingword";
    var canRead = true;
    var blogMoveHomeArticle = false;
    var showPcWindowAd = false;
    var showHeadWord = true;
    var showSearchText = "";
    var linkPage = true;
    var articleSource = 1;
    var articleReport = '{"pid": "blog", "spm":"1001.2101"}';
    var isShowToQuestion = false;
    var baiduSearchChannel = 'pc_relevant'
    var baiduSearchIdentification = '.topnsimilarv1'
    var distRequestId = '1662454009194_41596'
    var initRewardObject = {
        giver: "G_sir_",
        anchor: "dongrixinyu",
        articleId: "120244906",
        sign: "5ee82ea01b71ad9444db3b17f6b0121d",
    }
    var isLikeStatus = false;
    var isUnLikeStatus = false;
    var studyLearnWord = "";
    var isCurrentUserVip = false;
    var testNewStyle = "control"
    var contentViewsHeight = 3820;
    var contentViewsCount = 10;
    var contentViewsCountLimit = 40;
    var isShowConcision = true
    var isCookieConcision = false
    var isHasDirectoryModel = false
    var isShowSideModel = false
    var isShowDirectoryModel = true
    function getCookieConcision(sName){
        var allCookie = document.cookie.split("; ");
        for (var i=0; i < allCookie.length; i++){
            var aCrumb = allCookie[i].split("=");
            if (sName == aCrumb[0])
                return aCrumb[1];
        }
        return null;
    }
    if (getCookieConcision('blog_details_concision') && getCookieConcision('blog_details_concision') == 0){
        isCookieConcision = true
        isShowSideModel = true
        isShowDirectoryModel = false
    }
    var isShowCommentModele = "newStyle1"
</script>
<div class="main_father clearfix d-flex justify-content-center mainfather-concision" style="height:100%;"> 
    <div class="container clearfix container-concision" id="mainBox">
        <script>
        if(!isCookieConcision){
            $('.main_father').removeClass('mainfather-concision')
            $('.main_father .container').removeClass('container-concision')
        }
        </script>
        <main>
<script type="text/javascript">
    function getQueryString(name) {   
      var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象  
      var r = window.location.search.substr(1).match(reg);  //匹配目标参数
      if( r != null ) return decodeURIComponent( r[2] ); return '';   
    }
    function stripscript(s){ 
      var pattern = new RegExp("[`~!@#$^&*()=|{}':;',\\[\\].<>/?~！@#￥……&*（）——|{}【】‘；：”“'。，、？%]") 
      var rs = ""; 
      for (var i = 0; i < s.length; i++) { 
        rs = rs+s.substr(i, 1).replace(pattern, ''); 
      } 
      return rs; 
    }
    var blogHotWords = stripscript(getQueryString('utm_term')).length > 1 ? stripscript(getQueryString('utm_term')) : ''
</script>
<div class="blog-content-box">
        <div class="article-header-box">
        <div class="article-header">
            <div class="article-title-box">
                <h1 class="title-article" id="articleContentId">提取文本中的金额，提取货币，Python实现与在线使用</h1>
            </div>
            <div class="article-info-box">
                <div class="article-bar-top">
                    <img class="article-type-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/original.png" alt="">
                    <div class="bar-content">
                        <span class="c-gray">置顶</span>
                    <a class="follow-nickName " href="https://blog.csdn.net/dongrixinyu" target="_blank" rel="noopener">冬日新雨</a>
                    <img class="article-time-img article-heard-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/newUpTime2.png" alt="">
                    <span class="time">已于&nbsp;2022-07-26 09:51:22&nbsp;修改</span>
                    <img class="article-read-img article-heard-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/articleReadEyes2.png" alt="">
                    <span class="read-count">887</span>
                    <a id="blog_detail_zk_collection" class="un-collection" data-report-click='{"mod":"popu_823","spm":"1001.2101.3001.4232","ab":"new"}'>
                        <img class="article-collect-img article-heard-img un-collect-status isdefault" style="display:inline-block" src="https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png" alt="">
                        <img class="article-collect-img article-heard-img collect-status isactive" style="display:none" src="https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png" alt="">
                        <span class="name">收藏</span>
                        <span class="get-collection">
                            1
                        </span>
                    </a>
                    </div>
                </div>
                <div class="blog-tags-box">
                    <div class="tags-box artic-tag-box">
                            <span class="label">分类专栏：</span>
                                <a class="tag-link" href="https://blog.csdn.net/dongrixinyu/category_7207684.html" target="_blank" rel="noopener">正则表达式re</a>
                                <a class="tag-link" href="https://blog.csdn.net/dongrixinyu/category_10399650.html" target="_blank" rel="noopener">NLP</a>
                                <a class="tag-link" href="https://blog.csdn.net/dongrixinyu/category_6898690.html" target="_blank" rel="noopener">Python</a>
                            <span class="label">文章标签：</span>
                                <a data-report-click='{"mod":"popu_626","spm":"1001.2101.3001.4223","strategy":"python","ab":"new","extra":"{\"searchword\":\"python\"}"}' class="tag-link" href="https://so.csdn.net/so/search/s.do?q=python&amp;t=blog&amp;o=vip&amp;s=&amp;l=&amp;f=&amp;viparticle=" target="_blank" rel="noopener">python</a>
                                <a data-report-click='{"mod":"popu_626","spm":"1001.2101.3001.4223","strategy":"开发语言","ab":"new","extra":"{\"searchword\":\"开发语言\"}"}' class="tag-link" href="https://so.csdn.net/so/search/s.do?q=%E5%BC%80%E5%8F%91%E8%AF%AD%E8%A8%80&amp;t=blog&amp;o=vip&amp;s=&amp;l=&amp;f=&amp;viparticle=" target="_blank" rel="noopener">开发语言</a>
                    </div>
                </div>
                <div class="up-time"><span>于&nbsp;2021-09-11 23:27:20&nbsp;首次发布</span></div>
                <div class="slide-content-box">
                    <div class="article-copyright">
                        <div class="creativecommons">
                            版权声明：本文为博主原创文章，遵循<a href="http://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener"> CC 4.0 BY-SA </a>版权协议，转载请附上原文出处链接和本声明。
                        </div>
                        <div class="article-source-link">
                            本文链接：<a href="https://blog.csdn.net/dongrixinyu/article/details/120244906" target="_blank">https://blog.csdn.net/dongrixinyu/article/details/120244906</a>
                        </div>
                    </div>
                </div>
                <div class="operating">
                    <a class="href-article-edit slide-toggle">版权</a>
                </div>
            </div>
        </div>
    </div>
    <div id="blogHuaweiyunAdvert"></div>
        <div id="blogColumnPayAdvert">
            <div class="column-group">
                <div class="column-group-item column-group0 ">
                    <div class="item-l">
                        <a class="item-target" href="https://blog.csdn.net/dongrixinyu/category_7207684.html" target="_blank" title="正则表达式re"
                        data-report-view='{"spm":"1001.2101.3001.6332"}'
                        data-report-click='{"spm":"1001.2101.3001.6332"}'>
                            <img class="item-target" src="https://img-blog.csdnimg.cn/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="">
                            <span class="title item-target">
                                <span>
                                <span class="tit">正则表达式re</span>
                                    <span class="dec more">同时被 3 个专栏收录<img src="https://csdnimg.cn/release/blogv2/dist/pc/img/newArrowDown1White.png" alt=""></span>
                                </span>
                            </span>
                        </a>
                    </div>
                    <div class="item-m">
                        <span>5 篇文章</span>
                        <span>0 订阅</span>
                    </div>
                    <div class="item-r">
                            <a class="item-target article-column-bt articleColumnFreeBt" data-id="7207684">订阅专栏</a>
                    </div>
                </div>
                <div class="column-group-item column-group1 ">
                    <div class="item-l">
                        <a class="item-target" href="https://blog.csdn.net/dongrixinyu/category_10399650.html" target="_blank" title="NLP"
                        data-report-view='{"spm":"1001.2101.3001.6332"}'
                        data-report-click='{"spm":"1001.2101.3001.6332"}'>
                            <img class="item-target" src="https://img-blog.csdnimg.cn/20201014180756926.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="">
                            <span class="title item-target">
                                <span>
                                <span class="tit">NLP</span>
                                </span>
                            </span>
                        </a>
                    </div>
                    <div class="item-m">
                        <span>8 篇文章</span>
                        <span>1 订阅</span>
                    </div>
                    <div class="item-r">
                            <a class="item-target article-column-bt articleColumnFreeBt" data-id="10399650">订阅专栏</a>
                    </div>
                </div>
                <div class="column-group-item column-group2 ">
                    <div class="item-l">
                        <a class="item-target" href="https://blog.csdn.net/dongrixinyu/category_6898690.html" target="_blank" title="Python"
                        data-report-view='{"spm":"1001.2101.3001.6332"}'
                        data-report-click='{"spm":"1001.2101.3001.6332"}'>
                            <img class="item-target" src="https://img-blog.csdnimg.cn/20201014180756926.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="">
                            <span class="title item-target">
                                <span>
                                <span class="tit">Python</span>
                                </span>
                            </span>
                        </a>
                    </div>
                    <div class="item-m">
                        <span>57 篇文章</span>
                        <span>1 订阅</span>
                    </div>
                    <div class="item-r">
                            <a class="item-target article-column-bt articleColumnFreeBt" data-id="6898690">订阅专栏</a>
                    </div>
                </div>
            </div>
        </div>
    <article class="baidu_pl">
        <div id="article_content" class="article_content clearfix">
        <link rel="stylesheet" href="https://csdnimg.cn/release/blogv2/dist/mdeditor/css/editerView/ck_htmledit_views-b3c43d3711.css">
                <div id="content_views" class="htmledit_views">
                    <p>给定一篇文本&#xff0c;提取出文本中涉及到的所有的货币和金额。例如&#xff1a;</p> 
<blockquote> 
 <pre>&#39;张三赔偿李四人民币车费601,293.11元&#xff0c;工厂费一万二千三百四十五元,利息9佰日元&#xff0c;打印费十块钱。&#39; </pre> 
</blockquote> 
<p>从中提取出 &#39;601,293.11元&#39;, &#39;一万二千三百四十五元&#39;, &#39;9佰日元&#39;, &#39;十块钱&#39; 这样的字符串&#xff0c;并把他们都规范化&#xff0c;形成  &#39;601293.11元&#39;, &#39;12345.00元&#39;, &#39;900.00日元&#39;, &#39;10.00元&#39; 这样的结果。方便存储和计算。</p> 
<h1>⭐ 源码戳 &#61;&gt; <a class="link-info has-card" href="https://github.com/dongrixinyu/JioNLP" title="JioNLPhttps://github.com/dongrixinyu/JioNLP"><span class="link-card-box"><span class="link-title">JioNLPhttps://github.com/dongrixinyu/JioNLP</span><span class="link-link"><img alt="" class="link-link-icon" src="https://csdnimg.cn/release/blog_editor_html/release1.9.1/ckeditor/plugins/CsdnLink/icons/icon-default.png?t&#61;L892" />https://github.com/dongrixinyu/JioNLP</span></span></a></h1> 
<h1>⭐ 在线使用戳 &#61;&gt; <a class="link-info" href="http://182.92.160.94:16666/#/parse_money" title="提取货币金额">提取货币金额</a></h1> 
<p></p> 
<h2>安装 Installation</h2> 
<ul><li>python&gt;&#61;3.6 <strong>github 版本略领先于 pip</strong></li></ul>
<pre><code>$ git clone https://github.com/dongrixinyu/JioNLP
$ cd ./JioNLP
$ pip install .
</code></pre> 
<ul><li>pip 安装</li></ul>
<pre><code>$ pip install jionlp
</code></pre> 
<ul><li>可能存在的问题</li></ul>
<pre><code># 如安装失败&#xff0c;遇到安装时提示的 pkuseg、Microsoft Visual C&#43;&#43;、gcc、g&#43;&#43; 等信息&#xff0c;
# 则说明是 pkuseg 安装失败&#xff0c;需要在相应系统中安装 C 和 C&#43;&#43; 编译器&#xff0c;重新安装。
# pip install pkuseg</code></pre> 
<h2> 使用 Usage</h2> 
<p>抽取文本中的金额字符串&#xff0c;并提供将其转换为标准数字格式的函数。</p> 
<pre><code class="language-python">
&gt;&gt;&gt; import jionlp as jio
&gt;&gt;&gt; text &#61; &#39;张三赔偿李四人民币车费601,293.11元&#xff0c;工厂费一万二千三百四十五元,利息9佰日元&#xff0c;打印费十块钱。&#39; 
&gt;&gt;&gt; moneys &#61; jio.extract_money(text)
&gt;&gt;&gt; standard_moneys &#61; [jio.money_standardization(i) for i in moneys]

#  moneys: [&#39;601,293.11元&#39;, &#39;一万二千三百四十五元&#39;, &#39;9佰日元&#39;, &#39;十块钱&#39;]
#  standard_moneys: [&#39;601293.11元&#39;, &#39;12345.00元&#39;, &#39;900.00日元&#39;, &#39;10.00元&#39;]
</code></pre> 
<ul><li>支持标准数字格式&#xff0c;如&#xff1a;1,034,192.07元</li><li>支持纯数字格式&#xff0c;如&#xff1a;987273.3美元</li><li>支持大写中文金额&#xff0c;如&#xff1a;柒仟六佰零弎萬肆仟叁佰贰拾壹元伍分</li><li>支持混合格式&#xff0c;如&#xff1a;1.26万港元</li><li>支持<strong>口语化中文</strong>格式&#xff0c;如&#xff1a;三十五块三毛&#xff1b;但对于“三十五块八”这样的字符串&#xff0c;在文本中存在<strong>歧义</strong>&#xff0c;如“三十五块八颗糖”等&#xff0c;因此&#xff0c;<code>extract_money</code> 对于此字符串不予抽取&#xff0c;但<code>money_standardization</code>可以将“三十五块八”看作完整的口语化金额&#xff0c;标准化为“35.80元”</li><li>支持多种常见货币类型&#xff1a;人民币&#xff0c;港元&#xff0c;澳门元&#xff0c;美元&#xff0c;日元&#xff0c;澳元&#xff0c;韩元&#xff0c;卢布&#xff0c;英镑&#xff0c;马克&#xff0c;法郎&#xff0c;欧元&#xff0c;加元等。</li></ul>
<p>如果觉得好用&#xff0c;就点一下 Star 赞啊&#xff01;可以直接在 <a class="link-info" href="http://182.92.160.94:16666/#/parse_money" title="提取货币金额">提取货币金额</a> 使用。</p> 
<p><a class="link-info" href="https://blog.csdn.net/dongrixinyu/article/details/120245280" title="JioNLP时间语义解析">JioNLP时间语义解析</a></p>
                </div>
        </div>
        <div id="treeSkill"></div>
    </article>
  <script>
  $(function() {
    setTimeout(function () {
      var mathcodeList = document.querySelectorAll('.htmledit_views img.mathcode');
      if (mathcodeList.length > 0) {
        var testImg = new Image();
        testImg.onerror = function () {
          mathcodeList.forEach(function (item) {
            $(item).before('<span class="img-codecogs">\\(' + item.alt + '\\)</span>');
            $(item).remove();
          })
          MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
        }
        testImg.src = mathcodeList[0].src;
      }
    }, 1000)
  })
  </script>
</div>
<div class="more-toolbox-new" id="toolBarBox">
    <div class="left-toolbox">
        <div class="toolbox-left">
            <div class="profile-box"><a class="profile-href" target="_blank" href="https://blog.csdn.net/dongrixinyu"><img class="profile-img" src="https://profile.csdnimg.cn/A/3/3/3_dongrixinyu"><span class="profile-name">冬日新雨</span></a></div>
            <div class="profile-attend">
                    <a class="tool-attend tool-bt-button tool-bt-attend" href="javascript:;" data-report-view='{"mod":"1592215036_002","spm":"1001.2101.3001.4232","extend1":"关注"}'>关注</a>
                <a class="tool-item-follow active-animation" style="display:none;">关注</a>
            </div>
        </div>
        <div class="toolbox-middle">
        <ul class="toolbox-list">
            <li class="tool-item tool-item-size tool-active is-like" id="is-like">
            <a class="tool-item-href">
                <img style="display:none;" id="is-like-imgactive-animation-like" class="animation-dom active-animation" src="https://csdnimg.cn/release/blogv2/dist/pc/img/tobarThumbUpactive.png" alt="">
                <img class="isactive" style="display:none" id="is-like-imgactive" src="https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2021Active.png" alt="">
                <img class="isdefault" style="display:block" id="is-like-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2021Black.png" alt="">  
                <span id="spanCount" class="count ">
                        0
                </span>
            </a>
            <div class="tool-hover-tip"><span class="text space">点赞</span></div>
            </li>
            <li class="tool-item tool-item-size tool-active is-unlike" id="is-unlike">
            <a class="tool-item-href">
                <img class="isactive" style="margin-right:0px;display:none" id="is-unlike-imgactive" src="https://csdnimg.cn/release/blogv2/dist/pc/img/newUnHeart2021Active.png" alt="">
                <img class="isdefault" style="margin-right:0px;display:block" id="is-unlike-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/newUnHeart2021Black.png" alt="">
                <span id="unlikeCount" class="count "></span>
            </a>
            <div class="tool-hover-tip"><span class="text space">踩</span></div>
            </li>
            <li class="tool-item tool-item-size tool-active is-collection ">
            <a class="tool-item-href" href="javascript:;" data-report-click='{"mod":"popu_824","spm":"1001.2101.3001.4130","ab":"new"}'>
                <img style="display:none" id="is-collection-img-collection" class="animation-dom active-animation" src="https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive.png" alt="">
                <img class="isdefault" id="is-collection-img" style="display:block" src="https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectBlack.png" alt="">
                <img class="isactive" id="is-collection-imgactive" style="display:none" src="https://csdnimg.cn/release/blogv2/dist/pc/img/newCollectActive.png" alt="">
                <span class="count get-collection " id="get-collection">
                    1
                </span>
            </a>
            <div class="tool-hover-tip"><span class="text space">收藏</span></div>
            </li>
            <li class="tool-item tool-item-size tool-active tool-item-reward">
                <a class="tool-item-href" href="javascript:;" data-report-click='{"mod":"popu_830","spm":"1001.2101.3001.4237","dest":"","ab":"new"}'>
                <img class="isdefault reward-bt" id="rewardBtNew" src="https://csdnimg.cn/release/blogv2/dist/pc/img/newRewardBlack.png" alt="打赏">
                <span class="count"></span>
                </a>
                <div class="tool-hover-tip"><span class="text space">打赏</span></div>
            </li>
            <li class="tool-item tool-item-size tool-active tool-item-comment">
            <a class="tool-item-href go-side-comment" data-report-click='{"spm":"1001.2101.3001.7009"}'>
                <img class="isdefault" src="https://csdnimg.cn/release/blogv2/dist/pc/img/newComment2021Black.png" alt="">
                <span class="count">
                    1
                </span>
            </a>
            <div class="tool-hover-tip"><span class="text space">评论</span></div>
            </li>
            <li class="tool-item tool-item-bar">
            </li>
            <li class="tool-item tool-item-size tool-active tool-QRcode" id="tool-share">
                <a class="tool-item-href" href="javascript:;" data-report-click='{"mod":"1582594662_002","spm":"1001.2101.3001.4129","ab":"new"}'>
                    <img class="isdefault" src="https://csdnimg.cn/release/blogv2/dist/pc/img/newShareBlack.png" alt="">
                </a>
                <div class="QRcode" id="tool-QRcode">
                    <div class="share-bg-icon icon1" id="shareBgIcon"></div>
                    <div class="share-bg-box">
                        <div class="share-content">
                            <img class="share-avatar" src="https://profile.csdnimg.cn/A/3/3/3_dongrixinyu" alt="">
                            <div class="share-tit">提取文本中的金额，提取货币，Python实现与在线使用</div>
                            <div class="share-dec">给定一篇文本，提取出文本中涉及到的所有的货币和金额。例如：'张三赔偿李四人民币车费601,293.11元，工厂费一万二千三百四十五元,利息9佰日元，打印费十块钱。' 从中提取出'601,293.11元', '一万二千三百四十五元', '9佰日元', '十块钱' 这样的字符串，并把他们都规范化，形成'601293.11元', '12345.00元', '900.00日元', '10.00元' 这样的结果。方便存储和计算。⭐ 源码戳 =&amp;gt; JioNLPhttps://github....</div>
                            <a id="copyPosterUrl" class="url" data-report-click='{"spm":"1001.2101.3001.7493"}' data-report-view='{"spm":"1001.2101.3001.7493"}'>复制链接</a>
                        </div>
                        <div class="share-code">
                            <div class="share-code-box" id='shareCode'></div>
                            <div class="share-code-text">扫一扫</div>
                        </div>
                    </div>
                   
                </div>
            </li>
        </ul>
        </div>
        <div class="toolbox-right">
                <div class="tool-directory">
                    <a class="bt-columnlist-show"
                    data-id="7207684"
                    data-free="true"
                    data-subscribe="false"
                    data-title="正则表达式re"
                    data-img="https://img-blog.csdnimg.cn/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_64,w_64"
                    data-url="https://blog.csdn.net/dongrixinyu/category_7207684.html"
                    data-sum="5"
                    data-people="0"
                    data-price="0"
                    data-oldprice="0"
                    data-join="false"
                    data-studyvip="false"
                    data-studysubscribe="false"
                    data-report-view='{"spm":"1001.2101.3001.6334","extend1":"专栏目录"}'
                    data-report-click='{"spm":"1001.2101.3001.6334","extend1":"专栏目录"}'
                    >专栏目录</a>
                </div>
        </div>
    </div>  
</div>
<script type=text/javascript crossorigin src="https://csdnimg.cn/release/phoenix/production/qrcode-7c90a92189.min.js"></script>
<script src="//g.csdnimg.cn/??sharewx/1.2.1/sharewx.js" type="text/javascript"></script>
<script type="text/javascript" crossorigin src="https://g.csdnimg.cn/user-login/3.0.1/user-login.js"></script>
<script type="text/javascript" crossorigin src="https://g.csdnimg.cn/collection-box/2.1.0/collection-box.js"></script>
                <div class="first-recommend-box recommend-box ">
<div class="recommend-item-box type_blog clearfix" data-url="https://blog.csdn.net/dongrixinyu/article/details/120959407"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6661.1","mod":"popu_871","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant_t0.none-task-blog-2~default~CTRLIST~Rate-1-120959407-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"1","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/dongrixinyu/article/details/120959407"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://blog.csdn.net/dongrixinyu/article/details/120959407" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6661.1","mod":"popu_871","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant_t0.none-task-blog-2~default~CTRLIST~Rate-1-120959407-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"1","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/dongrixinyu/article/details/120959407"}'  data-report-query='spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-120959407-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-120959407-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1"><em>文本</em><em>货币</em><em>金额</em>抽取<em>与</em>解析<em>，</em>JioNLP</div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/dongrixinyu" target="_blank"><span class="blog-title">dongrixinyu的专栏</span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">10-25</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					471
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://blog.csdn.net/dongrixinyu/article/details/120959407" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6661.1","mod":"popu_871","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant_t0.none-task-blog-2~default~CTRLIST~Rate-1-120959407-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"1","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/dongrixinyu/article/details/120959407"}'  data-report-query='spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-120959407-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-120959407-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1">给定一段<em>文本</em><em>，</em><em>提取</em>其<em>中</em><em>的</em><em>货币</em><em>金额</em>字符串<em>，</em>并将所有<em>的</em><em>金额</em>做标准化。

JioNLP <em>中</em>文预<em>处理</em><em>与</em>解析工具包https://github.com/dongrixinyu/JioNLP其<em>中</em><em>，</em>jio.ner.extract_money <em>与</em> jio.parse_money 可以从一段<em>文本</em><em>中</em>抽取出<em>货币</em><em>金额</em><em>，</em>并将结果进行标准化。我们不妨看一个例子：

给定一段<em>文本</em>如：



海航亏损7000万港元出售香港公寓。12月12日<em>，</em>据《香港经济日报》报道<em>，</em>海航集团将持有<em>的</em>部分位于香港铜锣湾Yoo Residence大楼<em>中</em><em>的</em>物业以</div>
			</a>
		</div>
	</div>
</div>
                </div>
            <script src="https://csdnimg.cn/release/blogv2/dist/components/js/pc_wap_commontools-452728399d.min.js" type="text/javascript" async></script>
            <div class="second-recommend-box recommend-box ">
<div class="recommend-item-box type_download clearfix" data-url="https://download.csdn.net/download/weixin_38694355/12874440"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.1","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-download-2~default~CTRLIST~Paid-1-12874440-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"1","strategy":"2~default~CTRLIST~Paid","dest":"https://download.csdn.net/download/weixin_38694355/12874440"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://download.csdn.net/download/weixin_38694355/12874440" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.1","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-download-2~default~CTRLIST~Paid-1-12874440-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"1","strategy":"2~default~CTRLIST~Paid","dest":"https://download.csdn.net/download/weixin_38694355/12874440"}'  data-report-query='spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-download-2%7Edefault%7ECTRLIST%7EPaid-1-12874440-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-download-2%7Edefault%7ECTRLIST%7EPaid-1-12874440-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1"><em>Python</em>进行数据<em>提取</em><em>的</em>方法总结</div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info display-flex">
					<span class="info-block">09-21</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://download.csdn.net/download/weixin_38694355/12874440" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.1","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-download-2~default~CTRLIST~Paid-1-12874440-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"1","strategy":"2~default~CTRLIST~Paid","dest":"https://download.csdn.net/download/weixin_38694355/12874440"}'  data-report-query='spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-download-2%7Edefault%7ECTRLIST%7EPaid-1-12874440-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-download-2%7Edefault%7ECTRLIST%7EPaid-1-12874440-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1">数据<em>提取</em>是分析师日常工作<em>中</em>经常遇到<em>的</em>需求。如某个用户<em>的</em>贷款<em>金额</em><em>，</em>某个月或季度<em>的</em>利息总收入<em>，</em>某个特定时间段<em>的</em>贷款<em>金额</em>和笔数<em>，</em>大于5000元<em>的</em>贷款数量等等。本篇文章介绍如何通过<em>python</em>按特定<em>的</em>维度或条件对数据进行<em>提取</em><em>，</em>完成数据<em>提取</em>需求。</div>
			</a>
		</div>
	</div>
</div>
            </div>
<a id="commentBox" name="commentBox"></a>
<div id="pcCommentBox" class="comment-box comment-box-new2  login-comment-box-new" style="display:block">
		<div class="has-comment" style="display:block">
		<div class="has-comment-tit">评论<span class="count go-side-comment">1</span><span class="text go-side-comment">条</span><img class="go-side-comment more" src="https://csdnimg.cn/release/blogv2/dist/pc/img/commentArrowRightWhite.png" alt=""><a class="has-comment-bt-right go-side-comment focus">写评论</a></div>
			<div class="has-comment-con comment-operate-item"></div>
		</div>
		<div class="unhas-comment" style="display:none">
			<div class="unhas-comment-left">评论</div>
			<div class="unhas-comment-right"><a class="go-side-comment focus">写评论</a></div>
		</div>
</div>
            <div class="recommend-box insert-baidu-box recommend-box-style ">
                <div class="recommend-item-box no-index" style="display:none"></div>
<div class="recommend-item-box type_blog clearfix" data-url="https://chengyanan.blog.csdn.net/article/details/114990738"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.2","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-2-114990738-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"2","strategy":"2~default~CTRLIST~Rate","dest":"https://chengyanan.blog.csdn.net/article/details/114990738"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://chengyanan.blog.csdn.net/article/details/114990738" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.2","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-2-114990738-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"2","strategy":"2~default~CTRLIST~Rate","dest":"https://chengyanan.blog.csdn.net/article/details/114990738"}'  data-report-query='spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-114990738-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-114990738-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1"><em>python</em> 爬虫抓取某电商页面<em>的</em>商品价格</div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/qq_26502245" target="_blank"><span class="blog-title">ChengYanan的博客</span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">03-18</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					4704
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://chengyanan.blog.csdn.net/article/details/114990738" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.2","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-2-114990738-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"2","strategy":"2~default~CTRLIST~Rate","dest":"https://chengyanan.blog.csdn.net/article/details/114990738"}'  data-report-query='spm=1001.2101.3001.6650.2&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-114990738-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-2-114990738-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1">业务需求
最近想通过爬虫抓取某电商商品页<em>的</em>价格。
页面如下：

实践
然后就兴冲冲<em>的</em>写了段代码来爬取网页数据。
# 厨房卫浴
href = &#39;http://search.gome.com.cn/search?question=%E5%8E%A8%E6%88%BF%E5%8D%AB%E6%B5%B4&#39;

res = requests.get(href)
# print(res.text)
soup = BeautifulSoup(res.text, &#39;html.parser&#39;)
# product_list </div>
			</a>
		</div>
	</div>
</div>
<div class="recommend-item-box type_blog clearfix" data-url="https://blog.csdn.net/anshe1896/article/details/101120860"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.3","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-3-101120860-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"3","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/anshe1896/article/details/101120860"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://blog.csdn.net/anshe1896/article/details/101120860" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.3","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-3-101120860-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"3","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/anshe1896/article/details/101120860"}'  data-report-query='spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-101120860-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-101120860-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1">正则表达式获取<em>金额</em></div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/anshe1896" target="_blank"><span class="blog-title"></span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">05-09</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					561
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://blog.csdn.net/anshe1896/article/details/101120860" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.3","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-3-101120860-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"3","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/anshe1896/article/details/101120860"}'  data-report-query='spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-101120860-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-3-101120860-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1">public string isExists(string str) {  return Regex.Match(str, @&quot;[+-]?\d+(.\d{2})?&quot;).Value;  }
Response.Write( isExists(&quot;&lt;b&gt;-AU&iuml;&frac14;&bdquo;15.08&lt;/b&gt;...</div>
			</a>
		</div>
	</div>
</div>
		<dl id="recommend-item-box-tow" class="recommend-item-box type_blog clearfix">
			
		</dl>
<div class="recommend-item-box type_blog clearfix" data-url="https://blog.csdn.net/wuxizhi777/article/details/50946723"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.4","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-4-50946723-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"4","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/wuxizhi777/article/details/50946723"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://blog.csdn.net/wuxizhi777/article/details/50946723" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.4","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-4-50946723-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"4","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/wuxizhi777/article/details/50946723"}'  data-report-query='spm=1001.2101.3001.6650.4&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-50946723-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-50946723-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1"><em>python</em> 数字<em>金额</em>转化</div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/wuxizhi777" target="_blank"><span class="blog-title">wuxizhi777的专栏</span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">03-21</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					2131
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://blog.csdn.net/wuxizhi777/article/details/50946723" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.4","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-4-50946723-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"4","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/wuxizhi777/article/details/50946723"}'  data-report-query='spm=1001.2101.3001.6650.4&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-50946723-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-50946723-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1">import re


dict= {&#39;1&#39;: &#39;壹&#39;, &#39;2&#39;: &#39;贰&#39;, &#39;3&#39;: &#39;叁&#39;, &#39;4&#39;: &#39;肆&#39;, &#39;5&#39;: &#39;伍&#39;,&#39;6&#39;:&#39;陆&#39;,&#39;7&#39;:&#39;柒&#39;,&#39;8&#39;:&#39;捌&#39;,&#39;9&#39;:&#39;玖&#39;,&#39;0&#39;:&#39;零&#39;}


dict1= {&#39;0&#39;:&#39;&#39;,&#39;1&#39;:&#39;拾&#39;,&#39;2&#39;:&#39;佰&#39;,&#39;3&#39;:&#39;仟&#39;,&#39;4&#39;:&#39;万&#39;,&#39;5&#39;:&#39;万拾&#39;,&#39;6&#39;:&#39;万百&#39;,&#39;7&#39;:&#39;万千&#39;,&#39;8&#39;:&#39;亿&#39;,
</div>
			</a>
		</div>
	</div>
</div>
<div class="recommend-item-box type_blog clearfix" data-url="https://blog.csdn.net/u010687164/article/details/85320691"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.5","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-5-85320691-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"5","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/u010687164/article/details/85320691"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://blog.csdn.net/u010687164/article/details/85320691" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.5","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-5-85320691-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"5","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/u010687164/article/details/85320691"}'  data-report-query='spm=1001.2101.3001.6650.5&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-5-85320691-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-5-85320691-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1"><em>Python</em>结合正则式匹配<em>与</em>分句<em>的</em>方式<em>提取</em><em>文本</em><em>中</em><em>的</em><em>金额</em></div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/u010687164" target="_blank"><span class="blog-title">人的抱怨源自，自我无能的愤怒</span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">12-28</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					4642
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://blog.csdn.net/u010687164/article/details/85320691" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.5","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-5-85320691-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"5","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/u010687164/article/details/85320691"}'  data-report-query='spm=1001.2101.3001.6650.5&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-5-85320691-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-5-85320691-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1">本博文将一个<em>文本</em><em>中</em><em>的</em><em>金额</em>信息利用正则式和分句<em>的</em>方式<em>提取</em>出来。对于一个<em>文本</em>而言<em>文本</em>内容包含<em>的</em>信息多种多样<em>，</em>往往我们感兴趣<em>的</em>关键信息都只是简单<em>的</em>几个字符或者一个简单<em>的</em>句子<em>，</em>基于这样<em>的</em>应用场景对于一个上万字<em>的</em><em>文本</em>而言怎样才能高效而且准确<em>的</em>获取<em>文本</em><em>的</em>关键信息？本文以获取<em>文本</em><em>中</em><em>金额</em>为例讲些一下鄙人对<em>文本</em>结构化<em>与</em>关键信息<em>提取</em><em>的</em>理解。

首先假设我们拿到一个<em>文本</em>内容如下：


content=&#39;&#39;&#39;排10西沙湾...</div>
			</a>
		</div>
	</div>
</div>
<div class="recommend-item-box type_blog clearfix" data-url="https://blog.csdn.net/Offivensive888/article/details/124772218"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.6","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-6-124772218-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"6","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/Offivensive888/article/details/124772218"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://blog.csdn.net/Offivensive888/article/details/124772218" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.6","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-6-124772218-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"6","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/Offivensive888/article/details/124772218"}'  data-report-query='spm=1001.2101.3001.6650.6&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-6-124772218-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-6-124772218-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1"><em>Python</em>识别图片<em>中</em>数字/数值<em>的</em>方法笔记</div>
					<div class="tag">最新发布</div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/Offivensive888" target="_blank"><span class="blog-title">山中坐的博客</span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">05-14</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					2538
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://blog.csdn.net/Offivensive888/article/details/124772218" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.6","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-6-124772218-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"6","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/Offivensive888/article/details/124772218"}'  data-report-query='spm=1001.2101.3001.6650.6&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-6-124772218-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-6-124772218-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1">import easyocr         #识别图片上<em>的</em>数字/数值/文字方法
from PIL import Image  #打开图片<em>，</em>传输图片信息
import re              #正则表达式
# import pytesseract   #识别图片上<em>的</em>数字/数值方法



应用场景：单独识别图片<em>中</em>某个区域<em>的</em>数字或者/数值<em>，</em>然后做数据<em>处理</em>。
首先是导入我们需要<em>的</em>库（如上）<em>，</em>这里识别图片上数字或者数值<em>的</em>原理是<em>，</em>首先截图（截取屏幕）<em>，</em>然后截取我们需要<em>的</em>图片上<em>的</em>数字/数值区域<em>，</em>方便第三方库识别</div>
			</a>
		</div>
	</div>
</div>
<div class="recommend-item-box type_blog clearfix" data-url="https://blog.csdn.net/surpass_li/article/details/83923520"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.7","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-7-83923520-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"7","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/surpass_li/article/details/83923520"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://blog.csdn.net/surpass_li/article/details/83923520" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.7","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-7-83923520-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"7","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/surpass_li/article/details/83923520"}'  data-report-query='spm=1001.2101.3001.6650.7&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-7-83923520-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-7-83923520-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1">一个从字符串<em>中</em><em>提取</em><em>金额</em><em>的</em>正则表达式
</div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/surpass_li" target="_blank"><span class="blog-title">surpass_li</span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">05-19</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					4900
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://blog.csdn.net/surpass_li/article/details/83923520" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.7","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-7-83923520-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"7","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/surpass_li/article/details/83923520"}'  data-report-query='spm=1001.2101.3001.6650.7&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-7-83923520-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-7-83923520-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1">

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 
一个从字符串<em>中</em><em>提取</em><em>金额</em><em>的</em>正则表达式<em>，</em>初学者<em>，</em>写得有点乱<em>，</em>请大家指正
            String str = &quot;asd2312.3fasf-0.114fa+234.3sdf&quot;;

            //String regxp = &quot;[^(-)?(([1-9]{1}\\d*)|([0]{1}))(\\.(\\d){1,2})?]&quot;;
         ...</div>
			</a>
		</div>
	</div>
</div>
<div class="recommend-item-box type_blog clearfix" data-url="https://blog.csdn.net/guanyonglai/article/details/89512659"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.8","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-8-89512659-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"8","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/guanyonglai/article/details/89512659"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://blog.csdn.net/guanyonglai/article/details/89512659" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.8","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-8-89512659-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"8","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/guanyonglai/article/details/89512659"}'  data-report-query='spm=1001.2101.3001.6650.8&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-8-89512659-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-8-89512659-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1">玩转<em>python</em><em>的</em>正则表达式|<em>提取</em>字符串<em>中</em><em>的</em>所有数字</div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/guanyonglai" target="_blank"><span class="blog-title">guanyonglai的博客</span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">04-25</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					1万+
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://blog.csdn.net/guanyonglai/article/details/89512659" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.8","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-8-89512659-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"8","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/guanyonglai/article/details/89512659"}'  data-report-query='spm=1001.2101.3001.6650.8&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-8-89512659-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-8-89512659-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1">感谢：https://blog.csdn.net/weixin_40907382/article/details/79654372#commentBox

一直被<em>python</em><em>的</em>正则表达式绕<em>的</em>脑壳疼<em>，</em>看到诸如&#39;#%.*#!~%^&amp;&amp;++&#39;<em>的</em>东西简直是心<em>中</em>一万个烫烫烫屯屯屯锟斤拷滚过！！所以决定昨天花一整天<em>的</em>时间弄懂这一块：

首先<em>，</em><em>使用</em><em>python</em><em>的</em>正则表达式需要 import...</div>
			</a>
		</div>
	</div>
</div>
<div class="recommend-item-box type_blog clearfix" data-url="https://bennyrhys.blog.csdn.net/article/details/89440722"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.9","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-9-89440722-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"9","strategy":"2~default~CTRLIST~Rate","dest":"https://bennyrhys.blog.csdn.net/article/details/89440722"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://bennyrhys.blog.csdn.net/article/details/89440722" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.9","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-9-89440722-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"9","strategy":"2~default~CTRLIST~Rate","dest":"https://bennyrhys.blog.csdn.net/article/details/89440722"}'  data-report-query='spm=1001.2101.3001.6650.9&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-9-89440722-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-9-89440722-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1"><em>Python</em>&mdash;&mdash;字符串和列表<em>的</em>转化</div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/weixin_43469680" target="_blank"><span class="blog-title">瑞新の博客：bennyrhys</span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">04-21</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					2万+
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://bennyrhys.blog.csdn.net/article/details/89440722" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.9","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-9-89440722-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"9","strategy":"2~default~CTRLIST~Rate","dest":"https://bennyrhys.blog.csdn.net/article/details/89440722"}'  data-report-query='spm=1001.2101.3001.6650.9&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-9-89440722-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-9-89440722-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1">a = &#39;abcd efg&#39;
b = list(a) #字符串列表化
c = &#39;&#39;.join(b) #列表字符串化
d = a.split() #split对单词列表化不是对每个字母
print(&#39;b is :&#39;,b)
print(&#39;d is :&#39;,d)
 
print(&#39;c is:&#39;,c)
 
b is : [&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;, &#39; &#39;, &#39;e&#39;, &#39;f&#39;, &#39;g&#39;]
d i...</div>
			</a>
		</div>
	</div>
</div>
<div class="recommend-item-box type_blog clearfix" data-url="https://blog.csdn.net/weixin_34080951/article/details/86323397"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.10","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-10-86323397-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"10","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/weixin_34080951/article/details/86323397"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://blog.csdn.net/weixin_34080951/article/details/86323397" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.10","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-10-86323397-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"10","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/weixin_34080951/article/details/86323397"}'  data-report-query='spm=1001.2101.3001.6650.10&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-10-86323397-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-10-86323397-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1">[<em>python</em>]decimal常用操作和需要注意<em>的</em>地方</div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/weixin_34080951" target="_blank"><span class="blog-title">weixin_34080951的博客</span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">02-22</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					1362
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://blog.csdn.net/weixin_34080951/article/details/86323397" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.10","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-10-86323397-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"10","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/weixin_34080951/article/details/86323397"}'  data-report-query='spm=1001.2101.3001.6650.10&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-10-86323397-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-10-86323397-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1">decimal模块
简介
decimal意思为十进制<em>，</em>这个模块提供了十进制浮点运算支持。
常用方法
1.可以传递给Decimal整型或者字符串参数<em>，</em>但不能是浮点数据<em>，</em>因为浮点数据本身就不准确。
2.要从浮点数据转换为Decimal类型
from decimal import *
Decimal.from_float(12.222)
# 结果为Decimal(&#39;12.2219999999999995...</div>
			</a>
		</div>
	</div>
</div>
<div class="recommend-item-box type_blog clearfix" data-url="https://blog.csdn.net/weixin_34014555/article/details/93526405"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.11","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-11-93526405-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"11","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/weixin_34014555/article/details/93526405"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://blog.csdn.net/weixin_34014555/article/details/93526405" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.11","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-11-93526405-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"11","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/weixin_34014555/article/details/93526405"}'  data-report-query='spm=1001.2101.3001.6650.11&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-11-93526405-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-11-93526405-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1"><em>python</em> 人民币数字转汉字大写<em>金额</em></div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/weixin_34014555" target="_blank"><span class="blog-title">weixin_34014555的博客</span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">06-27</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					1164
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://blog.csdn.net/weixin_34014555/article/details/93526405" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.11","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-11-93526405-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"11","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/weixin_34014555/article/details/93526405"}'  data-report-query='spm=1001.2101.3001.6650.11&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-11-93526405-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-11-93526405-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1"><em>python</em> 人民币数字转汉字大写<em>金额</em>
			
	
	
		http://siroh.blog.sohu.com/274593310.html

  1 &#39;&#39;&#39;
  2 人民币数字转大写汉字
  3 &#39;&#39;&#39;
  4 
  5 # coding: utf-8
  6 import warnings
  7 from decimal import De...</div>
			</a>
		</div>
	</div>
</div>
<div class="recommend-item-box type_blog clearfix" data-url="https://blog.csdn.net/qq_27590277/article/details/88367541"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.12","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-12-88367541-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"12","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/qq_27590277/article/details/88367541"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://blog.csdn.net/qq_27590277/article/details/88367541" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.12","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-12-88367541-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"12","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/qq_27590277/article/details/88367541"}'  data-report-query='spm=1001.2101.3001.6650.12&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-12-88367541-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-12-88367541-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1">【珍藏版】长文详解<em>python</em>正则表达式</div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/qq_27590277" target="_blank"><span class="blog-title">zenRRan的博客</span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">03-09</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					326
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://blog.csdn.net/qq_27590277/article/details/88367541" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.12","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~CTRLIST~Rate-12-88367541-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"12","strategy":"2~default~CTRLIST~Rate","dest":"https://blog.csdn.net/qq_27590277/article/details/88367541"}'  data-report-query='spm=1001.2101.3001.6650.12&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-12-88367541-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-12-88367541-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1">目录

 一、正则函数

 二、re模块调用

 三、贪婪模式

 四、分组

 五、正则表达式修饰符

 六、正则表达式模式

 七、常见<em>的</em>正则表达式



导读

想要<em>使用</em><em>python</em><em>的</em>正则表达式功能就需要调用re模块<em>，</em>re模块为高级字符串<em>处理</em>提供了正则表达式工具。模...</div>
			</a>
		</div>
	</div>
</div>
<div class="recommend-item-box type_blog clearfix" data-url="https://blog.csdn.net/u010412858/article/details/83062200"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.13","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-13-83062200-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"13","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/u010412858/article/details/83062200"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://blog.csdn.net/u010412858/article/details/83062200" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.13","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-13-83062200-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"13","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/u010412858/article/details/83062200"}'  data-report-query='spm=1001.2101.3001.6650.13&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-13-83062200-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-13-83062200-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1"><em>python</em>正则表达式从字符串<em>中</em><em>提取</em>数字</div>
					<div class="tag">热门推荐</div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/u010412858" target="_blank"><span class="blog-title">赵大宝的博客</span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">10-15</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					13万+
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://blog.csdn.net/u010412858/article/details/83062200" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.13","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-13-83062200-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"13","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/u010412858/article/details/83062200"}'  data-report-query='spm=1001.2101.3001.6650.13&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-13-83062200-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-13-83062200-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1"><em>python</em>从字符串<em>中</em><em>提取</em>数字
<em>使用</em>正则表达式<em>，</em>用法如下：
## 总结
## ^ 匹配字符串<em>的</em>开始。
## $ 匹配字符串<em>的</em>结尾。
## \b 匹配一个单词<em>的</em>边界。
## \d 匹配任意数字。
## \D 匹配任意非数字字符。
## x? 匹配一个可选<em>的</em> x 字符 (换言之<em>，</em>它匹配 1 次或者 0 次 x 字符)。
## x* 匹配0次或者多次 x 字符。
## x+ 匹配1次或者多次 x 字符。...</div>
			</a>
		</div>
	</div>
</div>
<div class="recommend-item-box type_blog clearfix" data-url="https://blog.csdn.net/SAN_YUN/article/details/84241862"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.14","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-14-84241862-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"14","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/SAN_YUN/article/details/84241862"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://blog.csdn.net/SAN_YUN/article/details/84241862" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.14","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-14-84241862-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"14","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/SAN_YUN/article/details/84241862"}'  data-report-query='spm=1001.2101.3001.6650.14&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-14-84241862-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-14-84241862-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1"><em>python</em><em>处理</em><em>金额</em></div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/SAN_YUN" target="_blank"><span class="blog-title">SAN_YUN的专栏</span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">06-29</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					553
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://blog.csdn.net/SAN_YUN/article/details/84241862" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.14","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-14-84241862-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"14","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/SAN_YUN/article/details/84241862"}'  data-report-query='spm=1001.2101.3001.6650.14&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-14-84241862-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-14-84241862-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1">今天又犯错了<em>，</em>调用拍拍API返回<em>的</em><em>金额</em>需要自己<em>处理</em><em>，</em>99元<em>，</em>paipai返回<em>的</em>是9900。当时通过截取字符串来<em>实现</em><em>的</em><em>，</em>没考虑99.99<em>的</em>情况<em>，</em>正确<em>的</em>做法是
[code=&quot;<em>python</em>&quot;]
 &#39;%0.2f&#39; % price/100.0
[/code]

<em>python</em> 格式化：http://www.cnblogs.com/JerySpace/archive/2010/12/17/190962...</div>
			</a>
		</div>
	</div>
</div>
<div class="recommend-item-box type_blog clearfix" data-url="https://luoxianxiong.blog.csdn.net/article/details/88823009"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.15","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-15-88823009-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"15","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://luoxianxiong.blog.csdn.net/article/details/88823009"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://luoxianxiong.blog.csdn.net/article/details/88823009" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.15","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-15-88823009-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"15","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://luoxianxiong.blog.csdn.net/article/details/88823009"}'  data-report-query='spm=1001.2101.3001.6650.15&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-15-88823009-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-15-88823009-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1">数据挖掘4：自然<em>语言</em><em>处理</em>（NLP）信息<em>提取</em>技术</div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/LuoXianXion" target="_blank"><span class="blog-title">大数据处理，智能搜索推荐，自然语言处理，AI机器人对话，数据库读写分离</span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">03-26</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					3947
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://luoxianxiong.blog.csdn.net/article/details/88823009" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.15","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-15-88823009-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"15","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://luoxianxiong.blog.csdn.net/article/details/88823009"}'  data-report-query='spm=1001.2101.3001.6650.15&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-15-88823009-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-15-88823009-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1">目录

第1步：基础知识

第2步：确定宏观<em>与</em>微观理解

第3步：确定您想要<em>的</em>是什么（在合理<em>的</em>成本内）

第4步：理解整个文档（宏观理解）

第5步：<em>提取</em>事实<em>，</em>实体和关系（微观理解）

第6步：保持原产地/可追溯性

第7步：人工辅助过程





一旦识别<em>，</em><em>提取</em>和清理了用例所需<em>的</em>内容<em>，</em>下一步就是要了解该内容。在许多用例<em>中</em><em>，</em>具有最重要信息<em>的</em>内容以自然<em>语言</em>（例如英语<em>，</em>德语<em>，</em>西班牙语<em>，</em><em>中</em>文等...</div>
			</a>
		</div>
	</div>
</div>
<div class="recommend-item-box type_blog clearfix" data-url="https://blog.csdn.net/weixin_44963170/article/details/109382093"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.16","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-16-109382093-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"16","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/weixin_44963170/article/details/109382093"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://blog.csdn.net/weixin_44963170/article/details/109382093" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.16","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-16-109382093-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"16","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/weixin_44963170/article/details/109382093"}'  data-report-query='spm=1001.2101.3001.6650.16&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-16-109382093-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-16-109382093-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1">NLP关键词<em>提取</em>（抽取）方法总结及<em>实现</em></div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/weixin_44963170" target="_blank"><span class="blog-title">weixin_44963170的博客</span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">10-30</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					2245
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://blog.csdn.net/weixin_44963170/article/details/109382093" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.16","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-16-109382093-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"16","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/weixin_44963170/article/details/109382093"}'  data-report-query='spm=1001.2101.3001.6650.16&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-16-109382093-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-16-109382093-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1">NLP关键词<em>提取</em>（抽取）方法总结及<em>实现</em>
参考 https://blog.csdn.net/asialee_bird/article/details/96454544

</div>
			</a>
		</div>
	</div>
</div>
<div class="recommend-item-box type_blog clearfix" data-url="https://blog.csdn.net/Wind__Chaser/article/details/107116459"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.17","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-17-107116459-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"17","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/Wind__Chaser/article/details/107116459"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://blog.csdn.net/Wind__Chaser/article/details/107116459" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.17","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-17-107116459-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"17","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/Wind__Chaser/article/details/107116459"}'  data-report-query='spm=1001.2101.3001.6650.17&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-17-107116459-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-17-107116459-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1">NLP 关键词<em>提取</em>常用方法</div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/Wind__Chaser" target="_blank"><span class="blog-title">Wind__Chaser的博客</span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">07-08</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					1806
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://blog.csdn.net/Wind__Chaser/article/details/107116459" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.17","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-17-107116459-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"17","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://blog.csdn.net/Wind__Chaser/article/details/107116459"}'  data-report-query='spm=1001.2101.3001.6650.17&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-17-107116459-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-17-107116459-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1">特征词<em>提取</em>常见算法
1.TF-IDF
重要性=每个单词<em>的</em>词频TF * 逆文档频率IDF。
2.TextRank
候选词<em>的</em>重要性根据它和其他候选词<em>的</em>关系来确定。
3.基于语义<em>的</em>关键词<em>提取</em>（SKE）
得分由三部分组成：1、居间度密度Vd；2、词性pos(名词、动词&hellip;&hellip;), 位置loc(标题<em>，</em>段首<em>，</em>段尾）<em>，</em>词长；3、TF-IDF值；对1、2、3加权得到最后<em>的</em>词语关键度得分。居间度密度为这篇论文提出<em>的</em>特征。
4.Word2vec + Kmeans
候选词对应<em>的</em>词向量<em>，</em>对词向量进行聚类<em>，</em>距离聚类<em>中</em>心点最近<em>的</em>向量为关键</div>
			</a>
		</div>
	</div>
</div>
<div class="recommend-item-box type_blog clearfix" data-url="https://little-coder.blog.csdn.net/article/details/82460727"  data-report-view='{"ab":"new","spm":"1001.2101.3001.6650.18","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-18-82460727-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"18","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://little-coder.blog.csdn.net/article/details/82460727"}'>
	<div class="content-box">
		<div class="content-blog display-flex">
			<div class="title-box">
				<a href="https://little-coder.blog.csdn.net/article/details/82460727" class="tit" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.18","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-18-82460727-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"18","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://little-coder.blog.csdn.net/article/details/82460727"}'  data-report-query='spm=1001.2101.3001.6650.18&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-18-82460727-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-18-82460727-blog-120244906.topnsimilarv1'>
					<div class="left ellipsis-online ellipsis-online-1">NLP关键字<em>提取</em>之TextRank算法</div>
				</a>
			</div>
			<div class="info-box display-flex">
				<div class="info">
					<a href="https://blog.csdn.net/qq_20989105" target="_blank"><span class="blog-title">小小码农</span></a>
				</div>
				<div class="info display-flex">
					<span class="info-block time">09-06</span>
					<span class="info-block read"><img class="read-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					2518
					</span>
				</div>
			</div>
		</div>
		<div class="desc-box">
			<a href="https://little-coder.blog.csdn.net/article/details/82460727" target="_blank"  data-report-click='{"ab":"new","spm":"1001.2101.3001.6650.18","mod":"popu_387","extra":"{\"highlightScore\":0.0,\"utm_medium\":\"distribute.pc_relevant.none-task-blog-2~default~BlogCommendFromBaidu~Rate-18-82460727-blog-120244906.topnsimilarv1\",\"dist_request_id\":\"1662454009194_41596\"}","dist_request_id":"1662454009194_41596","ab_strategy":"topnsimilarv1","index":"18","strategy":"2~default~BlogCommendFromBaidu~Rate","dest":"https://little-coder.blog.csdn.net/article/details/82460727"}'  data-report-query='spm=1001.2101.3001.6650.18&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-18-82460727-blog-120244906.topnsimilarv1&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-18-82460727-blog-120244906.topnsimilarv1'>
				<div class="desc ellipsis-online ellipsis-online-1">
  今天看了一下HanLP框架<em>的</em>关键字<em>提取</em><em>的</em>算法<em>，</em>总<em>的</em>来说很简单<em>，</em>就是互相计算词频<em>的</em>一个算法。


谈起自动摘要算法<em>，</em>常见<em>的</em>并且最易<em>实现</em><em>的</em>当属TF-IDF<em>，</em>但是感觉TF-IDF效果一般<em>，</em>不如TextRank好。

TextRank是在Google<em>的</em>PageRank算法启发下<em>，</em>针对<em>文本</em>里<em>的</em>句子设计<em>的</em>权重算法<em>，</em>目标是自动摘要。它利用投票<em>的</em>原理<em>，</em>让每一个单词给它<em>的</em>邻居（术语称窗口）投赞成票<em>，</em>票<em>的</em>权重取...</div>
			</a>
		</div>
	</div>
</div>
            </div>
<div id="recommendNps" class="recommend-nps-box common-nps-box">
  <h3 class="aside-title">“相关推荐”对你有帮助么？</h3>
  <div class="aside-content">
      <ul class="newnps-list">
          <li class="newnps-item" data-type="非常没帮助">
              <div class="newnps-img-box">
                  <img class="newnps-img active" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeel1.png" alt="">
                  <img class="newnps-img default" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeelGrey1.png" alt="">
              </div>
              <div class="newnps-text">非常没帮助</div>
          </li>
          <li class="newnps-item" data-type="没帮助">
              <div class="newnps-img-box">
                  <img class="newnps-img active" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeel2.png" alt="">
                  <img class="newnps-img default" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeelGrey2.png" alt="">
              </div>
              <div class="newnps-text">没帮助</div>
          </li>
          <li class="newnps-item" data-type="一般">
              <div class="newnps-img-box">
                  <img class="newnps-img active" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeel3.png" alt="">
                  <img class="newnps-img default" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeelGrey3.png" alt="">
              </div>
              <div class="newnps-text">一般</div>
          </li>
          <li class="newnps-item" data-type="有帮助">
              <div class="newnps-img-box">
                  <img class="newnps-img active" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeel4.png" alt="">
                  <img class="newnps-img default" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeelGrey4.png" alt="">
              </div>
              <div class="newnps-text">有帮助</div>
          </li>
          <li class="newnps-item" data-type="非常有帮助">
              <div class="newnps-img-box">
                  <img class="newnps-img active" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeel5.png" alt="">
                  <img class="newnps-img default" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeelGrey5.png" alt="">
              </div>
              <div class="newnps-text">非常有帮助</div>
          </li>
      </ul>
      <div class="newnps-form-box">
      <div class="newnps-form">
          <input type="text" placeholder="请输入建议或反馈后点击提交" class="newnps-input">
          <span class="newnps-btn">提交</span>
      </div>
      </div>
  </div>
</div>            <div class="template-box">
                <span>©️2022 CSDN</span>
                <span>皮肤主题：大白</span>
                <span> 设计师：CSDN官方博客</span>
                <span>
                    <a href="https://blog.csdn.net/" class="back-home c-blue c-blue-hover c-blue-focus">返回首页</a>
                </span>
            </div>
<div class="blog-footer-bottom" style="margin-top:10px;"></div>
<script src="https://g.csdnimg.cn/common/csdn-footer/csdn-footer.js" data-isfootertrack="false" type="text/javascript"></script>
<script type="text/javascript">
    window.csdn.csdnFooter.options = {
        el: '.blog-footer-bottom',
        type: 2
    }
</script>        </main>
<aside class="blog_container_aside">
<div id="asideProfile" class="aside-box">
    <div class="profile-intro d-flex">
        <div class="avatar-box d-flex justify-content-center flex-column">
            <a href="https://blog.csdn.net/dongrixinyu" target="_blank" data-report-click='{"mod":"popu_379","spm":"1001.2101.3001.4121","dest":"https://blog.csdn.net/dongrixinyu","ab":"new"}'>
                <img src="https://profile.csdnimg.cn/A/3/3/3_dongrixinyu" class="avatar_pic">
            </a>
        </div>
        <div class="user-info d-flex flex-column profile-intro-name-box">
            <div class="profile-intro-name-boxTop">
                <a href="https://blog.csdn.net/dongrixinyu" target="_blank" class="" id="uid" title="冬日新雨" data-report-click='{"mod":"popu_379","spm":"1001.2101.3001.4122","dest":"https://blog.csdn.net/dongrixinyu","ab":"new"}'>
                    <span class="name " username="dongrixinyu">冬日新雨</span>
                </a>
                <span>
                </span>
                <span class="flag expert-blog">
                <span class="bubble">CSDN认证博客专家</span>
                </span>
                <span class="flag company-blog">
                <span class="bubble">CSDN认证企业博客</span>
                </span>
            </div>
            <div class="profile-intro-name-boxFooter">
                <span class="personal-home-page personal-home-years" title="已加入 CSDN 10年">码龄10年</span>
                    <span class="personal-home-page">
                    <a class="personal-home-certification" href="https://i.csdn.net/#/uc/profile?utm_source=14998968" target="_blank" title="暂无认证">
                    <img src="https://csdnimg.cn/identity/nocErtification.png" alt="">
                    暂无认证
                    </a>
                    </span>
            </div>
        </div>
    </div>
    <div class="data-info d-flex item-tiling">
        <dl class="text-center" title="82">
            <a href="https://blog.csdn.net/dongrixinyu" data-report-click='{"mod":"1598321000_001","spm":"1001.2101.3001.4310"}' data-report-query="t=1">  
                <dt><span class="count">82</span></dt>
                <dd class="font">原创</dd>
            </a>
        </dl>
        <dl class="text-center" data-report-click='{"mod":"1598321000_002","spm":"1001.2101.3001.4311"}' title="43933">
            <a href="https://blog.csdn.net/rank/list/weekly" target="_blank">
                <dt><span class="count">4万+</span></dt>
                <dd class="font">周排名</dd>
            </a>
        </dl>
        <dl class="text-center" title="1287667">
            <a href="https://blog.csdn.net/rank/list/total" data-report-click='{"mod":"1598321000_003","spm":"1001.2101.3001.4312"}' target="_blank">
                <dt><span class="count">128万+</span></dt>
                <dd class="font">总排名</dd>
            </a>
        </dl>
        <dl class="text-center" style="min-width:58px" title="203754">  
            <dt><span class="count">20万+</span></dt>
            <dd>访问</dd>
        </dl>
        <dl class="text-center" title="5级,点击查看等级说明">
            <dt><a href="https://blog.csdn.net/blogdevteam/article/details/103478461" target="_blank">
                <img class="level" src="https://csdnimg.cn/identity/blog5.png">
            </a>
            </dt>
            <dd>等级</dd>
        </dl>
    </div>
    <div class="item-rank"></div>
    <div class="data-info d-flex item-tiling">
        <dl class="text-center" title="2768">
            <dt><span class="count">2768</span></dt>
            <dd>积分</dd>
        </dl>
         <dl class="text-center" id="fanBox" title="205">
            <dt><span class="count" id="fan">205</span></dt>
            <dd>粉丝</dd>
        </dl>
        <dl class="text-center" title="114">
            <dt><span class="count">114</span></dt>
            <dd>获赞</dd>
        </dl>
        <dl class="text-center" title="42">
            <dt><span class="count">42</span></dt>
            <dd>评论</dd>
        </dl>
        <dl class="text-center" title="482">
            <dt><span class="count">482</span></dt>
            <dd>收藏</dd>
        </dl>
    </div>
    <div class="aside-box-footer" data-report-view='{"spm":"3001.4296"}'>
        <div class="badge-box d-flex">
            <div class="badge d-flex">
                <div class="icon-badge" title="持之以恒">
                    <div class="mouse-box">
                        <img class="medal-img" data-report-click='{"spm":"3001.4296"}' src="https://csdnimg.cn/medal/chizhiyiheng@240.png" alt="持之以恒">
                    </div>
                </div>
                <div class="icon-badge" title="笔耕不辍">
                    <div class="mouse-box">
                        <img class="medal-img" data-report-click='{"spm":"3001.4296"}' src="https://csdnimg.cn/70592b2299594e37aedcaa91fc52a294.png" alt="笔耕不辍">
                    </div>
                </div>
                <div class="icon-badge" title="勤写标兵">
                    <div class="mouse-box">
                        <img class="medal-img" data-report-click='{"spm":"3001.4296"}' src="https://csdnimg.cn/medal/qixiebiaobing4@240.png" alt="勤写标兵">
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="profile-intro-name-boxOpration">
        <div class="opt-letter-watch-box">
        <a class="bt-button personal-letter" href="https://im.csdn.net/chat/dongrixinyu" target="_blank" rel="noopener">私信</a>
        </div>
        <div class="opt-letter-watch-box"> 
            <a class="personal-watch bt-button" id="btnAttent" >关注</a>  
        </div>
    </div>
</div>
 <div id="asideSearchArticle" class="aside-box">
	<div class="aside-content search-comter">
    <div class="aside-search aside-search-blog">         
        <input type="text" class="input-serch-blog" name="" autocomplete="off" value="" id="search-blog-words" placeholder="搜博主文章">
        <a class="btn-search-blog">
                    <img src="//csdnimg.cn/cdn/content-toolbar/csdn-sou.png?v=1587021042">
        </a>
    </div>
    </div>
</div>


<div id="asideHotArticle" class="aside-box">
	<h3 class="aside-title">热门文章</h3>
	<div class="aside-content">
		<ul class="hotArticle-list">
			<li>
				<a href="https://blog.csdn.net/dongrixinyu/article/details/78775057" target="_blank"  data-report-click='{"mod":"popu_541","spm":"1001.2101.3001.4139","dest":"https://blog.csdn.net/dongrixinyu/article/details/78775057","ab":"new"}'>
				【数据结构与算法】刷题汇总 Python 版
					<img src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					<span class="read">19540</span>
                </a>
			</li>
			<li>
				<a href="https://blog.csdn.net/dongrixinyu/article/details/79039215" target="_blank"  data-report-click='{"mod":"popu_541","spm":"1001.2101.3001.4139","dest":"https://blog.csdn.net/dongrixinyu/article/details/79039215","ab":"new"}'>
				【机器学习】支持向量机SVM - 对SVM与核函数的理解及sklearn参数详解
					<img src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					<span class="read">12911</span>
                </a>
			</li>
			<li>
				<a href="https://blog.csdn.net/dongrixinyu/article/details/78555796" target="_blank"  data-report-click='{"mod":"popu_541","spm":"1001.2101.3001.4139","dest":"https://blog.csdn.net/dongrixinyu/article/details/78555796","ab":"new"}'>
				【计算机网络】网络安全知识要点
					<img src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					<span class="read">11221</span>
                </a>
			</li>
			<li>
				<a href="https://blog.csdn.net/dongrixinyu/article/details/77919075" target="_blank"  data-report-click='{"mod":"popu_541","spm":"1001.2101.3001.4139","dest":"https://blog.csdn.net/dongrixinyu/article/details/77919075","ab":"new"}'>
				Python中文文本信息抽取中常见的正则表达式
					<img src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					<span class="read">9289</span>
                </a>
			</li>
			<li>
				<a href="https://blog.csdn.net/dongrixinyu/article/details/78535488" target="_blank"  data-report-click='{"mod":"popu_541","spm":"1001.2101.3001.4139","dest":"https://blog.csdn.net/dongrixinyu/article/details/78535488","ab":"new"}'>
				【微积分】复习
					<img src="https://csdnimg.cn/release/blogv2/dist/pc/img/readCountWhite.png" alt="">
					<span class="read">8664</span>
                </a>
			</li>
		</ul>
	</div>
</div>
<div id="asideCategory" class="aside-box flexible-box">
    <h3 class="aside-title">分类专栏</h3>
    <div class="aside-content">
        <ul>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_10399653.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_10399653.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756916.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        数据增强
                    </span>
                </a>
                <span class="special-column-num">2篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_10399650.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_10399650.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756926.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        NLP
                    </span>
                </a>
                <span class="special-column-num">8篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_6898690.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_6898690.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756926.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        Python
                    </span>
                </a>
                <span class="special-column-num">57篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7207684.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7207684.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        正则表达式re
                    </span>
                </a>
                <span class="special-column-num">5篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7207685.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7207685.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        中文文本
                    </span>
                </a>
                <span class="special-column-num">5篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7208689.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7208689.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756928.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        数据结构
                    </span>
                </a>
                <span class="special-column-num">20篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7256888.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7256888.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756923.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        http协议
                    </span>
                </a>
                <span class="special-column-num">2篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7275803.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7275803.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756927.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        docker
                    </span>
                </a>
                <span class="special-column-num">1篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7277870.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7277870.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756926.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        网络
                    </span>
                </a>
                <span class="special-column-num">3篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7277871.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7277871.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756927.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        应用层
                    </span>
                </a>
                <span class="special-column-num">1篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7280031.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7280031.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756927.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        算法
                    </span>
                </a>
                <span class="special-column-num">34篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7280814.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7280814.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756913.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        数学
                    </span>
                </a>
                <span class="special-column-num">7篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7292813.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7292813.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756916.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        信号
                    </span>
                </a>
                <span class="special-column-num">1篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7292814.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7292814.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756913.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        系统
                    </span>
                </a>
                <span class="special-column-num">1篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7292823.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7292823.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756927.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        安全
                    </span>
                </a>
                <span class="special-column-num">1篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7300012.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7300012.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756919.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        ip
                    </span>
                </a>
                <span class="special-column-num">1篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7300320.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7300320.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        传输层
                    </span>
                </a>
                <span class="special-column-num">1篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7301558.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7301558.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756738.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        计算机
                    </span>
                </a>
                <span class="special-column-num">10篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7301559.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7301559.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756724.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        存储器
                    </span>
                </a>
                <span class="special-column-num">1篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7304229.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7304229.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756928.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        总线
                    </span>
                </a>
                <span class="special-column-num">1篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7304232.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7304232.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756919.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        IO设备
                    </span>
                </a>
                <span class="special-column-num">1篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7304246.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7304246.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756918.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        指令系统
                    </span>
                </a>
                <span class="special-column-num">1篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7333525.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7333525.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        git
                    </span>
                </a>
                <span class="special-column-num">1篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7336857.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7336857.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756754.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        数据库
                    </span>
                </a>
                <span class="special-column-num">2篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7346587.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7346587.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756930.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        机器学习
                    </span>
                </a>
                <span class="special-column-num">5篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7361273.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7361273.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756916.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        操作系统
                    </span>
                </a>
                <span class="special-column-num">4篇</span>
            </li>
            <li>
                <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7361343.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7361343.html","ab":"new"}'>
                    <div class="special-column-bar "></div>
                    <img src="https://img-blog.csdnimg.cn/20201014180756927.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                    <span class="title oneline">
                        进程
                    </span>
                </a>
                <span class="special-column-num">1篇</span>
            </li>
        </ul>
    </div>
    <p class="text-center">
        <a class="flexible-btn" data-fbox="aside-archive"><img class="look-more" src="https://csdnimg.cn/release/blogv2/dist/pc/img/arrowDownWhite.png" alt=""></a>
    </p>
</div>
<div id="asideNewComments" class="aside-box">
    <h3 class="aside-title">最新评论</h3>
    <div class="aside-content">
        <ul class="newcomment-list">
            <li>
                <a class="title text-truncate" target="_blank" href="https://blog.csdn.net/dongrixinyu/article/details/120244906#comments_23079619" data-report-click='{"mod":"popu_542","spm":"1001.2101.3001.4231","dest":"https://blog.csdn.net/dongrixinyu/article/details/120244906#comments_23079619","ab":"new"}' data-report-view='{"mod":"popu_542","spm":"1001.2101.3001.4231","dest":"https://blog.csdn.net/dongrixinyu/article/details/120244906#comments_23079619","ab":"new"}'>提取文本中的金额，提取货币，Python实现与在线使用</a>
                <p class="comment ellipsis">
                    <a href="https://blog.csdn.net/bob1112" class="user-name" target="_blank">bob1112: </a>
                    <span class="code-comments">你好,在测试这段文字&quot;决定给予人民币贰万元整罚款的行政处罚&quot;提取出错.</span>
                </p>
            </li>
            <li>
                <a class="title text-truncate" target="_blank" href="https://blog.csdn.net/dongrixinyu/article/details/120244906#comments_23077830" data-report-click='{"mod":"popu_542","spm":"1001.2101.3001.4231","dest":"https://blog.csdn.net/dongrixinyu/article/details/120244906#comments_23077830","ab":"new"}' data-report-view='{"mod":"popu_542","spm":"1001.2101.3001.4231","dest":"https://blog.csdn.net/dongrixinyu/article/details/120244906#comments_23077830","ab":"new"}'>提取文本中的金额，提取货币，Python实现与在线使用</a>
                <p class="comment ellipsis">
                    <a href="https://blog.csdn.net/bob1112" class="user-name" target="_blank">bob1112: </a>
                    <span class="code-comments">standard_moneys = [jio.money_standardization(i) for i in moneys]报错,可改为如下代码
standard_moneys = [jio.parse_money(i) for i in moneys]</span>
                </p>
            </li>
            <li>
                <a class="title text-truncate" target="_blank" href="https://blog.csdn.net/dongrixinyu/article/details/108660386#comments_22668992" data-report-click='{"mod":"popu_542","spm":"1001.2101.3001.4231","dest":"https://blog.csdn.net/dongrixinyu/article/details/108660386#comments_22668992","ab":"new"}' data-report-view='{"mod":"popu_542","spm":"1001.2101.3001.4231","dest":"https://blog.csdn.net/dongrixinyu/article/details/108660386#comments_22668992","ab":"new"}'>NLP自然语言处理的文本数据增强&mdash;&mdash;回译（内含python工具包）</a>
                <p class="comment ellipsis">
                    <a href="https://blog.csdn.net/qq_40260063" class="user-name" target="_blank">卡布里藍: </a>
                    <span class="code-comments">你好，我想问下，如果我想使用EDA对平行语料进行增强，那我是应该①同时对源端目标端进行EDA操作，②还是对源端进行EDA操作后翻译至tgt&#39;组成新的伪语料对，③还是对源端进行EDA操作后，目标端不变</span>
                </p>
            </li>
            <li>
                <a class="title text-truncate" target="_blank" href="https://blog.csdn.net/dongrixinyu/article/details/108660386#comments_22668991" data-report-click='{"mod":"popu_542","spm":"1001.2101.3001.4231","dest":"https://blog.csdn.net/dongrixinyu/article/details/108660386#comments_22668991","ab":"new"}' data-report-view='{"mod":"popu_542","spm":"1001.2101.3001.4231","dest":"https://blog.csdn.net/dongrixinyu/article/details/108660386#comments_22668991","ab":"new"}'>NLP自然语言处理的文本数据增强&mdash;&mdash;回译（内含python工具包）</a>
                <p class="comment ellipsis">
                    <a href="https://blog.csdn.net/qq_40260063" class="user-name" target="_blank">卡布里藍: </a>
                    <span class="code-comments">你好，我想问下，如果我想使用EDA对平行语料进行增强，那我是应该①同时对源端目标端进行EDA操作，②还是对源端进行EDA操作后翻译至tgt&#39;组成新的伪语料对，③还是对源端进行EDA操作后，目标端不变</span>
                </p>
            </li>
            <li>
                <a class="title text-truncate" target="_blank" href="https://blog.csdn.net/dongrixinyu/article/details/96901862#comments_21280602" data-report-click='{"mod":"popu_542","spm":"1001.2101.3001.4231","dest":"https://blog.csdn.net/dongrixinyu/article/details/96901862#comments_21280602","ab":"new"}' data-report-view='{"mod":"popu_542","spm":"1001.2101.3001.4231","dest":"https://blog.csdn.net/dongrixinyu/article/details/96901862#comments_21280602","ab":"new"}'>给定一篇文本（新闻），确定其归属地（地名）的python工具</a>
                <p class="comment ellipsis">
                    <a href="https://blog.csdn.net/dongrixinyu" class="user-name" target="_blank">冬日新雨: </a>
                    <span class="code-comments">英文不行，针对中文</span>
                </p>
            </li>
        </ul>
    </div>
</div>
<div id="asideNewNps" class="aside-box common-nps-box">
    <h3 class="aside-title">您愿意向朋友推荐“博客详情页”吗？</h3>
    <div class="aside-content">
        <ul class="newnps-list">
            <li class="newnps-item" data-type="强烈不推荐">
                <div class="newnps-img-box">
                    <img class="newnps-img active" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeel1.png" alt="">
                    <img class="newnps-img default" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeelGrey1.png" alt="">
                </div>
                <div class="newnps-text">强烈不推荐</div>
            </li>
            <li class="newnps-item" data-type="不推荐">
                <div class="newnps-img-box">
                    <img class="newnps-img active" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeel2.png" alt="">
                    <img class="newnps-img default" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeelGrey2.png" alt="">
                </div>
                <div class="newnps-text">不推荐</div>
            </li>
            <li class="newnps-item" data-type="一般般">
                <div class="newnps-img-box">
                    <img class="newnps-img active" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeel3.png" alt="">
                    <img class="newnps-img default" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeelGrey3.png" alt="">
                </div>
                <div class="newnps-text">一般般</div>
            </li>
            <li class="newnps-item" data-type="推荐">
                <div class="newnps-img-box">
                    <img class="newnps-img active" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeel4.png" alt="">
                    <img class="newnps-img default" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeelGrey4.png" alt="">
                </div>
                <div class="newnps-text">推荐</div>
            </li>
            <li class="newnps-item" data-type="强烈推荐">
                <div class="newnps-img-box">
                    <img class="newnps-img active" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeel5.png" alt="">
                    <img class="newnps-img default" src="https://csdnimg.cn/release/blogv2/dist/pc/img/npsFeelGrey5.png" alt="">
                </div>
                <div class="newnps-text">强烈推荐</div>
            </li>
        </ul>
        <div class="newnps-form-box">
        <div class="newnps-form">
            <input type="text" placeholder="请输入建议或反馈后点击提交" class="newnps-input">
            <span class="newnps-btn">提交</span>
        </div>
        </div>
    </div>
</div>
<div id="asideArchive" class="aside-box" style="display:block!important; width:300px;">
    <h3 class="aside-title">最新文章</h3>
    <div class="aside-content">
        <ul class="inf_list clearfix">
            <li class="clearfix">
            <a href="https://blog.csdn.net/dongrixinyu/article/details/120959407" target="_blank" data-report-click='{"mod":"popu_382","spm":"1001.2101.3001.4136","dest":"https://blog.csdn.net/dongrixinyu/article/details/120959407","ab":"new"}' data-report-view='{"mod":"popu_382","dest":"https://blog.csdn.net/dongrixinyu/article/details/120959407","ab":"new"}'>文本货币金额抽取与解析，JioNLP</a>
            </li>
            <li class="clearfix">
            <a href="https://blog.csdn.net/dongrixinyu/article/details/120245280" target="_blank" data-report-click='{"mod":"popu_382","spm":"1001.2101.3001.4136","dest":"https://blog.csdn.net/dongrixinyu/article/details/120245280","ab":"new"}' data-report-view='{"mod":"popu_382","dest":"https://blog.csdn.net/dongrixinyu/article/details/120245280","ab":"new"}'>时间语义解析工具 Python版，从文本中提取时间，并解析其含义，在线使用，时间语义识别</a>
            </li>
            <li class="clearfix">
            <a href="https://blog.csdn.net/dongrixinyu/article/details/120245042" target="_blank" data-report-click='{"mod":"popu_382","spm":"1001.2101.3001.4136","dest":"https://blog.csdn.net/dongrixinyu/article/details/120245042","ab":"new"}' data-report-view='{"mod":"popu_382","dest":"https://blog.csdn.net/dongrixinyu/article/details/120245042","ab":"new"}'>文本清洗？一个工具搞定！Python版 NLP 文本清洗工具</a>
            </li>
        </ul>
        <div class="archive-bar"></div>
        <div class="archive-box">
                <div class="archive-list-item"><a href="https://blog.csdn.net/dongrixinyu?type=blog&amp;year=2021&amp;month=10" target="_blank" data-report-click='{"mod":"popu_538","spm":"1001.2101.3001.4138","ab":"new","dest":"https://blog.csdn.net/dongrixinyu?type=blog&amp;year=2021&amp;month=10"}'><span class="year">2021年</span><span class="num">5篇</span></a></div>
                <div class="archive-list-item"><a href="https://blog.csdn.net/dongrixinyu?type=blog&amp;year=2020&amp;month=12" target="_blank" data-report-click='{"mod":"popu_538","spm":"1001.2101.3001.4138","ab":"new","dest":"https://blog.csdn.net/dongrixinyu?type=blog&amp;year=2020&amp;month=12"}'><span class="year">2020年</span><span class="num">4篇</span></a></div>
                <div class="archive-list-item"><a href="https://blog.csdn.net/dongrixinyu?type=blog&amp;year=2019&amp;month=07" target="_blank" data-report-click='{"mod":"popu_538","spm":"1001.2101.3001.4138","ab":"new","dest":"https://blog.csdn.net/dongrixinyu?type=blog&amp;year=2019&amp;month=07"}'><span class="year">2019年</span><span class="num">1篇</span></a></div>
                <div class="archive-list-item"><a href="https://blog.csdn.net/dongrixinyu?type=blog&amp;year=2018&amp;month=01" target="_blank" data-report-click='{"mod":"popu_538","spm":"1001.2101.3001.4138","ab":"new","dest":"https://blog.csdn.net/dongrixinyu?type=blog&amp;year=2018&amp;month=01"}'><span class="year">2018年</span><span class="num">6篇</span></a></div>
                <div class="archive-list-item"><a href="https://blog.csdn.net/dongrixinyu?type=blog&amp;year=2017&amp;month=12" target="_blank" data-report-click='{"mod":"popu_538","spm":"1001.2101.3001.4138","ab":"new","dest":"https://blog.csdn.net/dongrixinyu?type=blog&amp;year=2017&amp;month=12"}'><span class="year">2017年</span><span class="num">67篇</span></a></div>
        </div>
    </div>
</div>
	<div id="footerRightAds" class="isShowFooterAds">
		<div class="aside-box">
			<div id="kp_box_57" data-pid="57"><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1076724771190722"
     crossorigin="anonymous"></script>
<!-- ~PC-博客-博文页-左侧-视窗-* -->
<ins class="adsbygoogle"
     style="display:inline-block;width:300px;height:600px"
     data-ad-client="ca-pub-1076724771190722"
     data-ad-slot="3806919815"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script><img class="pre-img-lasy" data-src="https://kunyu.csdn.net/1.png?p=57&adId=6816&a=6816&c=0&k=提取文本中的金额，提取货币，Python实现与在线使用&spm=1001.2101.3001.5001&articleId=120244906&d=1&t=3&u=51232781bd534275b2b13cfe49d9fae9" style="display: block;width: 0px;height: 0px;"></div>
		</div>
	</div>
    <!-- 详情页显示目录 -->
<!--文章目录-->
<div id="asidedirectory" class="aside-box">
    <div class='groupfile' id="directory">
        <h3 class="aside-title">目录</h3>
        <div class="align-items-stretch group_item">
            <div class="pos-box">
            <div class="scroll-box">
                <div class="toc-box"></div>
            </div>
            </div>
        </div>
    </div>
</div>
</aside>
<script>
	$("a.flexible-btn").click(function(){
		$(this).parents('div.aside-box').removeClass('flexible-box');
		$(this).parents("p.text-center").remove();
	})
</script>
<script type="text/javascript"  src="https://g.csdnimg.cn/user-tooltip/2.7/user-tooltip.js"></script>
<script type="text/javascript"  src="https://g.csdnimg.cn/user-medal/2.0.0/user-medal.js"></script>    </div>
<div class="recommend-right align-items-stretch clearfix" id="rightAside" data-type="recommend">
    <aside class="recommend-right_aside">
        <div id="recommend-right" >
                                <div class="programmer1Box">
                        <div id="kp_box_530" data-pid="530"><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1076724771190722"
     crossorigin="anonymous"></script>
<!-- ~PC-博客-博文页-右侧-视窗-1 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:300px;height:600px"
     data-ad-client="ca-pub-1076724771190722"
     data-ad-slot="6842192987"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script><img class="pre-img-lasy" data-src="https://kunyu.csdn.net/1.png?p=530&adId=6859&a=6859&c=0&k=提取文本中的金额，提取货币，Python实现与在线使用&spm=1001.2101.3001.4647&articleId=120244906&d=1&t=3&u=41a8329af3e94746a487a982e223dc08" style="display: block;width: 0px;height: 0px;"></div>
                    </div>
            <div class='flex-column aside-box groupfile' id="groupfile">
                <div class="groupfile-div">
                <h3 class="aside-title">目录</h3>
                <div class="align-items-stretch group_item">
                    <div class="pos-box">
                        <div class="scroll-box">
                            <div class="toc-box"></div>
                        </div>
                    </div>
                </div>
                </div>
            </div>
                <div id="recommendAdBox">
                    <div id="kp_box_479" data-pid="479"><script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1076724771190722"
     crossorigin="anonymous"></script>
<!-- PC-博客-详情页-右侧视窗2 -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-1076724771190722"
     data-ad-slot="9900373613"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script><img class="pre-img-lasy" data-src="https://kunyu.csdn.net/1.png?p=479&adId=1014577&a=1014577&c=0&k=提取文本中的金额，提取货币，Python实现与在线使用&spm=1001.2101.3001.4834&articleId=120244906&d=1&t=3&u=28758e0d03c54793ba2de8ddd79d6dff" style="display: block;width: 0px;height: 0px;"></div>
                </div>
            <div class='aside-box kind_person d-flex flex-column'>
                    <h3 class="aside-title">分类专栏</h3>
                    <div class="align-items-stretch kindof_item" id="kind_person_column">
                        <div class="aside-content">
                            <ul>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_10399653.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_10399653.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756916.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            数据增强
                                        </span>
                                    </a>
                                    <span class="special-column-num">2篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_10399650.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_10399650.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756926.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            NLP
                                        </span>
                                    </a>
                                    <span class="special-column-num">8篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_6898690.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_6898690.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756926.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            Python
                                        </span>
                                    </a>
                                    <span class="special-column-num">57篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7207684.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7207684.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            正则表达式re
                                        </span>
                                    </a>
                                    <span class="special-column-num">5篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7207685.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7207685.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            中文文本
                                        </span>
                                    </a>
                                    <span class="special-column-num">5篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7208689.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7208689.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756928.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            数据结构
                                        </span>
                                    </a>
                                    <span class="special-column-num">20篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7256888.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7256888.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756923.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            http协议
                                        </span>
                                    </a>
                                    <span class="special-column-num">2篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7275803.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7275803.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756927.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            docker
                                        </span>
                                    </a>
                                    <span class="special-column-num">1篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7277870.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7277870.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756926.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            网络
                                        </span>
                                    </a>
                                    <span class="special-column-num">3篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7277871.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7277871.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756927.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            应用层
                                        </span>
                                    </a>
                                    <span class="special-column-num">1篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7280031.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7280031.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756927.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            算法
                                        </span>
                                    </a>
                                    <span class="special-column-num">34篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7280814.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7280814.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756913.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            数学
                                        </span>
                                    </a>
                                    <span class="special-column-num">7篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7292813.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7292813.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756916.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            信号
                                        </span>
                                    </a>
                                    <span class="special-column-num">1篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7292814.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7292814.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756913.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            系统
                                        </span>
                                    </a>
                                    <span class="special-column-num">1篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7292823.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7292823.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756927.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            安全
                                        </span>
                                    </a>
                                    <span class="special-column-num">1篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7300012.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7300012.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756919.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            ip
                                        </span>
                                    </a>
                                    <span class="special-column-num">1篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7300320.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7300320.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            传输层
                                        </span>
                                    </a>
                                    <span class="special-column-num">1篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7301558.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7301558.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756738.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            计算机
                                        </span>
                                    </a>
                                    <span class="special-column-num">10篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7301559.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7301559.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756724.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            存储器
                                        </span>
                                    </a>
                                    <span class="special-column-num">1篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7304229.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7304229.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756928.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            总线
                                        </span>
                                    </a>
                                    <span class="special-column-num">1篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7304232.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7304232.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756919.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            IO设备
                                        </span>
                                    </a>
                                    <span class="special-column-num">1篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7304246.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7304246.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756918.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            指令系统
                                        </span>
                                    </a>
                                    <span class="special-column-num">1篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7333525.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7333525.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756925.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            git
                                        </span>
                                    </a>
                                    <span class="special-column-num">1篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7336857.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7336857.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756754.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            数据库
                                        </span>
                                    </a>
                                    <span class="special-column-num">2篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7346587.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7346587.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756930.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            机器学习
                                        </span>
                                    </a>
                                    <span class="special-column-num">5篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7361273.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7361273.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756916.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            操作系统
                                        </span>
                                    </a>
                                    <span class="special-column-num">4篇</span>
                                </li>
                                <li>
                                    <a class="clearfix special-column-name" target="_blank" href="https://blog.csdn.net/dongrixinyu/category_7361343.html" data-report-click='{"mod":"popu_537","spm":"1001.2101.3001.4137","strategy":"pc付费专栏左侧入口","dest":"https://blog.csdn.net/dongrixinyu/category_7361343.html","ab":"new"}'>
                                        <div class="special-column-bar "></div>
                                        <img src="https://img-blog.csdnimg.cn/20201014180756927.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="" onerror="this.src='https://img-blog.csdnimg.cn/20201014180756922.png?x-oss-process=image/resize,m_fixed,h_64,w_64'">
                                        <span class="">
                                            进程
                                        </span>
                                    </a>
                                    <span class="special-column-num">1篇</span>
                                </li>
                            </ul>
                        </div>
                    </div>
            </div>
        </div>
    </aside>
</div>

<div class="recommend-right1  align-items-stretch clearfix" id="rightAsideConcision" data-type="recommend">
    <aside class="recommend-right_aside">
        <div id="recommend-right-concision" >
            <div class='flex-column aside-box groupfile' id="groupfileConcision">
                <div class="groupfile-div1">
                <h3 class="aside-title">目录</h3>
                <div class="align-items-stretch group_item">
                    <div class="pos-box">
                        <div class="scroll-box">
                            <div class="toc-box"></div>
                        </div>
                    </div>
                </div>
                </div>
            </div>
        </div>
    </aside>
</div>

</div>
<div class="mask-dark"></div>
<script src="https://csdnimg.cn/public/sandalstrap/1.4/js/sandalstrap.min.js"></script>
<div class="skin-boxshadow"></div>
<div class="directory-boxshadow"></div>
<div class="comment-side-box-shadow comment-side-tit-close" id="commentSideBoxshadow">
<div class="comment-side-content">
	<div class="comment-side-tit">
	<div class="comment-side-tit-count">评论&nbsp;<span class="count">1</span></div>
	<img class="comment-side-tit-close" src="https://csdnimg.cn/release/blogv2/dist/pc/img/closeBt.png"></div>
	<div id="pcCommentSideBox" class="comment-box comment-box-new2 " style="display:block">
		<div class="comment-edit-box d-flex">
			<div class="user-img">
				<a href="https://blog.csdn.net/G_sir_" target="_blank">
					<img src="https://profile.csdnimg.cn/F/3/2/3_g_sir_">
				</a>
			</div>
			<form id="commentform">
				<textarea class="comment-content" name="comment_content" id="comment_content" placeholder="欢迎高质量的评论，低质的评论会被折叠" maxlength="1000"></textarea>
				<div class="comment-operate-box">
					<div class="comment-operate-l">
						<span id="tip_comment" class="tip">还能输入<em>1000</em>个字符</span>
					</div>
					<div class="comment-operate-c">
						&nbsp;
					</div>
					<div class="comment-operate-r">
						<div class="comment-operate-item comment-emoticon">
							<img class="comment-operate-img" data-url="https://csdnimg.cn/release/blogv2/dist/pc/img/" src="https://csdnimg.cn/release/blogv2/dist/pc/img/commentEmotionIcon.png" alt="表情包">
							<span class="comment-operate-tip">插入表情</span>
							<div class="comment-emoticon-box comment-operate-isshow">
								<div class="comment-emoticon-img-box"></div>
							</div>
						</div>
						<div class="comment-operate-item comment-code">
							<img class="comment-operate-img" data-url="https://csdnimg.cn/release/blogv2/dist/pc/img/" src="https://csdnimg.cn/release/blogv2/dist/pc/img/commentCodeIcon.png" alt="表情包">
							<span class="comment-operate-tip">代码片</span>
							<div class="comment-code-box comment-operate-isshow">
								<ul id="commentCode">
									<li><a data-code="html">HTML/XML</a></li>
									<li><a data-code="objc">objective-c</a></li>
									<li><a data-code="ruby">Ruby</a></li>
									<li><a data-code="php">PHP</a></li>
									<li><a data-code="csharp">C</a></li>
									<li><a data-code="cpp">C++</a></li>
									<li><a data-code="javascript">JavaScript</a></li>
									<li><a data-code="python">Python</a></li>
									<li><a data-code="java">Java</a></li>
									<li><a data-code="css">CSS</a></li>
									<li><a data-code="sql">SQL</a></li>
									<li><a data-code="plain">其它</a></li>
								</ul>
							</div>
						</div>
						<div class="comment-operate-item">
							<input type="hidden" id="comment_replyId" name="comment_replyId">
							<input type="hidden" id="article_id" name="article_id" value="120244906">
							<input type="hidden" id="comment_userId" name="comment_userId" value="">
							<input type="hidden" id="commentId" name="commentId" value="">
							<a data-report-click='{"mod":"1582594662_003","spm":"1001.2101.3001.4227","ab":"new"}'>
							<input type="submit" class="btn-comment btn-comment-input" value="评论">
							</a>
						</div>
					</div>
				</div>
			</form>
		</div>
		<div class="comment-list-container">
			<div class="comment-list-box comment-operate-item">
			</div>
			<div id="lookGoodComment" class="look-good-comment side-look-comment">
				<a class="look-more-comment">查看更多评论<img src="https://csdnimg.cn/release/blogv2/dist/pc/img/commentArrowDownWhite.png" alt=""></a>
			</div>
			<div id="lookFlodComment" class="look-flod-comment">
					<span class="count"></span>&nbsp;条评论被折叠&nbsp;<a class="look-more-flodcomment">查看</a>
			</div>
			<div class="opt-box text-center">
				<div class="btn btn-sm btn-link-blue" id="btnMoreComment"></div>
			</div>
		</div>
	</div>
	<div id="pcFlodCommentSideBox" class="pc-flodcomment-sidebox">
		<div class="comment-fold-tit"><span id="lookUnFlodComment" class="back"><img src="https://csdnimg.cn/release/blogv2/dist/pc/img/commentArrowLeftWhite.png" alt=""></span>被折叠的&nbsp;<span class="count"></span>&nbsp;条评论
		 <a href="https://blogdev.blog.csdn.net/article/details/122245662" class="tip" target="_blank">为什么被折叠?</a>
		 <a href="https://bbs.csdn.net/forums/FreeZone" class="park" target="_blank">
		 <img src="https://csdnimg.cn/release/blogv2/dist/pc/img/iconPark.png">到【灌水乐园】发言</a>                                
		</div>
		<div class="comment-fold-content"></div>
		<div id="lookBadComment" class="look-bad-comment side-look-comment">
			<a class="look-more-comment">查看更多评论<img src="https://csdnimg.cn/release/blogv2/dist/pc/img/commentArrowDownWhite.png" alt=""></a>
		</div>
	</div>
</div>
</div>
<div id="rewardNew" class="reward-popupbox-new">
	<p class="rewad-title">打赏作者<span class="reward-close"><img src="https://csdnimg.cn/release/blogv2/dist/pc/img/closeBt.png"></span></p>
	<dl class="profile-box">
		<dd>
		<a href="https://blog.csdn.net/dongrixinyu" data-report-click='{"mod":"popu_379","dest":"https://blog.csdn.net/dongrixinyu","ab":"new"}'>
			<img src="https://profile.csdnimg.cn/A/3/3/3_dongrixinyu" class="avatar_pic">
		</a>
		</dd>
		<dt>
			<p class="blog-name">冬日新雨</p>
			<p class="blog-discript">你的鼓励将是我创作的最大动力</p>
		</dt>
	</dl>
	<div class="reward-box-new">
			<div class="reward-content"><div class="reward-right"></div></div>
	</div>
	<div class="money-box">
				<span class="choose-money choosed" data-id="2">¥2</span>
				<span class="choose-money " data-id="4">¥4</span>
				<span class="choose-money " data-id="6">¥6</span>
				<span class="choose-money " data-id="10">¥10</span>
				<span class="choose-money " data-id="20">¥20</span>
				<input id="customizeMoney" class="customize-money" name="" type="" value="" placeholder="自定义"/>
				<div class="customize-tip">输入1-500的整数</div>
	</div>
	<div class="pay-box">
		<div class="pay-type-blance pay-type active" data-type="blance">
			<img class="unchoose" src="https://csdnimg.cn/release/blogv2/dist/pc/img/newUnChoose.png" alt="">
			<img class="choose"src="https://csdnimg.cn/release/blogv2/dist/pc/img/newChoose.png" alt="">
			<span class="pay-type-name">余额支付</span>
			<span class="pay-type-num">(余额：-- )</span>
		</div>
		<div class="pay-type-money pay-type" data-type="money">
			<img class="unchoose" src="https://csdnimg.cn/release/blogv2/dist/pc/img/newUnChoose.png" alt="">
			<img class="choose"src="https://csdnimg.cn/release/blogv2/dist/pc/img/newChoose.png" alt="">
			<span class="pay-type-name">扫码支付</span>
		</div>
	</div>
	<div class="sure-box">
		<div class="sure-box-money">
			<div class="code-box">
				<div class="code-num-box">
					<span class="code-name">扫码支付：</span><span class="code-num">¥2</span>
				</div>
				<div class="code-img-box">
					<div class="renovate">
					<img src="https://csdnimg.cn/release/blogv2/dist/pc/img/pay-time-out.png">
					<span>获取中</span>
					</div>
				</div>
				<div class="code-pay-box">
					<img src="https://csdnimg.cn/release/blogv2/dist/pc/img/newWeiXin.png" alt="">
					<img src="https://csdnimg.cn/release/blogv2/dist/pc/img/newZhiFuBao.png" alt="">
					<span>扫码支付</span>
				</div>
			</div>
		</div>
		<div class="sure-box-blance">
			<p class="tip">您的余额不足，请更换扫码支付或<a target="_blank" data-report-click='{"mod":"1597646289_003","spm":"1001.2101.3001.4302"}' href="https://i.csdn.net/#/wallet/balance/recharge?utm_source=RewardVip" class="go-invest">充值</a></p>
			<p class="is-have-money"><a class="reward-sure">打赏作者</a></p>
		</div>
	</div>
</div>
<div class="pay-code">
    <div class="pay-money">实付<span class="pay-money-span" data-nowprice='' data-oldprice=''>元</span></div>
    <div class="content-blance"><a class="blance-bt" href="javascript:;">使用余额支付</a></div>
    <div class="content-code">
    <div id="payCode" data-id="">
            <div class="renovate">
                <img src="https://csdnimg.cn/release/blogv2/dist/pc/img/pay-time-out.png">
                <span>点击重新获取</span>
            </div>
        </div>
        <div class="pay-style"><span><img src="https://csdnimg.cn/release/blogv2/dist/pc/img/weixin.png"></span><span><img src="https://csdnimg.cn/release/blogv2/dist/pc/img/zhifubao.png"></span><span><img src="https://csdnimg.cn/release/blogv2/dist/pc/img/jingdong.png"></span><span class="text">扫码支付</span></div>
    </div>
    <div class="bt-close"><svg t="1567152543821" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="10924" xmlns:xlink="http://www.w3.org/1999/xlink" width="12" height="12"><defs><style type="text/css"></style></defs><path d="M512 438.378667L806.506667 143.893333a52.032 52.032 0 1 1 73.6 73.621334L585.621333 512l294.485334 294.485333a52.074667 52.074667 0 0 1-73.6 73.642667L512 585.621333 217.514667 880.128a52.053333 52.053333 0 1 1-73.621334-73.642667L438.378667 512 143.893333 217.514667a52.053333 52.053333 0 1 1 73.621334-73.621334L512 438.378667z" fill="" p-id="10925"></path></svg></div>
    <!-- <p style="margin-top: 8px;font-size: 14px;" class="text-center">支付成功即可阅读</p> -->
    <div class="pay-balance">
    <input type="radio" class="pay-code-radio" data-type="details"> 
    <span class="span">钱包余额</span>
    <span class="balance" style="color:#FC5531;font-size:14px;">0</span>  
    <div class="pay-code-tile">
        <img src="https://csdnimg.cn/release/blogv2/dist/pc/img/pay-help.png" alt="">
        <div class="pay-code-content">
            <div class="span">
                <p class="title">抵扣说明：</p>
                <p> 1.余额是钱包充值的虚拟货币，按照1:1的比例进行支付金额的抵扣。<br> 2.余额无法直接购买下载，可以购买VIP、C币套餐、付费专栏及课程。</p>
            </div>
        </div>
    </div>
    </div>
    <a class="pay-balance-con" href="https://i.csdn.net/#/wallet/balance/recharge" target="_blank"><img src="https://csdnimg.cn/release/blogv2/dist/pc/img/recharge.png" alt=""><span  >余额充值</span></a>
</div>
<div style="display:none;">
	<img src="" onerror='setTimeout(function(){if(!/(csdn.net|iteye.com|baiducontent.com|googleusercontent.com|360webcache.com|sogoucdn.com|bingj.com|baidu.com)$/.test(window.location.hostname)){window.location.href="\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x63\x73\x64\x6e\x2e\x6e\x65\x74"}},3000);'>
</div>
<div class="keyword-dec-box" id="keywordDecBox"></div>
</body>
    <!-- 富文本柱状图  -->
	<link rel="stylesheet" href="https://csdnimg.cn/release/blog_editor_html/release1.6.12/ckeditor/plugins/chart/chart.css"/>
	<script type="text/javascript" src="https://csdnimg.cn/release/blog_editor_html/release1.6.12/ckeditor/plugins/chart/lib/chart.min.js"></script>
    <script type="text/javascript" src="https://csdnimg.cn/release/blog_editor_html/release1.6.12/ckeditor/plugins/chart/widget2chart.js"></script>
<script src="https://csdnimg.cn/release/blogv2/dist/components/js/pc_wap_highlight-2a2586c533.min.js" type="text/javascript"></script>
<script src="https://csdnimg.cn/release/blogv2/dist/components/js/pc_wap_common-fbcbe8567e.min.js" type="text/javascript"></script>
<script src="https://csdnimg.cn/release/blogv2/dist/components/js/edit_copy_code-ce0f06f94b.min.js" type="text/javascript"></script>
<link rel="stylesheet" href="https://csdnimg.cn/release/blog_editor_html/release1.6.12/ckeditor/plugins/codesnippet/lib/highlight/styles/atom-one-light.css">
<script src="https://g.csdnimg.cn/user-accusation/1.0.5/user-accusation.js" type="text/javascript" ></script>
<script>
 // 全局声明
 if (window.csdn === undefined) {
      window.csdn = {};
    }
    window.csdn.sideToolbar = {
        options: {
            report:{
                isShow: true,
            },
            qr: {
                isShow: false,
            },
            guide: {
                isShow: true
            }
        }
    }
    $(function(){
        $(document).on('click',"a.option-box[data-type='report']",function() {
            window.csdn.userLogin.loadAjax(function(res){
                window.csdn.feedback({
                    "type":'blog',
                    "rtype":'article',
                    "rid":articleId,
                    "reportedName":username,
                    "submitOptions":{
                        "title":articleTitle,
                        "contentUrl":articleDetailUrl
                    },
                    "callback":function(){
                        showToast({
                            text: "感谢您的举报，我们会尽快审核！",
                            bottom: '10%', 
                            zindex: 9000, 
                            speed: 500,
                            time: 1500
                        });
                    }
                })
            })
        });
    })
</script>
    <script src="https://g.csdnimg.cn/baidu-search/1.0.12/baidu-search.js"  type="text/javascript"></script>
<script src="https://csdnimg.cn/release/download/old_static/js/qrcode.js"></script>
<script src="https://g.csdnimg.cn/lib/qrcode/1.0.0/qrcode.min.js"></script>
<script src="https://g.csdnimg.cn/user-ordercart/3.0.1/user-ordercart.js" type="text/javascript"></script>
<script src="https://g.csdnimg.cn/user-ordertip/5.0.1/user-ordertip.js" type="text/javascript" ></script>
<script src="https://g.csdnimg.cn/order-payment/4.0.1/order-payment.js" type="text/javascript" ></script>
<script src="https://csdnimg.cn/release/blogv2/dist/pc/js/common-a1dfbf1dc3.min.js" type="text/javascript"></script>
<script src="https://csdnimg.cn/release/blogv2/dist/pc/js/detail-07085d66a4.min.js" type="text/javascript"></script>
<script src="https://csdnimg.cn/release/blogv2/dist/pc/js/column-2e5cf567c5.min.js" type="text/javascript"></script>
<script src="https://g.csdnimg.cn/side-toolbar/3.4/side-toolbar.js" type="text/javascript"></script>
<script src="https://g.csdnimg.cn/copyright/1.0.4/copyright.js" type="text/javascript"></script>
<script>
    $(".MathJax").remove();
    if ($('div.markdown_views pre.prettyprint code.hljs').length > 0) {
        $('div.markdown_views')[0].className = 'markdown_views';
    }
</script>
<script type="text/javascript" src="https://csdnimg.cn/release/blog_mathjax/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
            "HTML-CSS": {
                    linebreaks: { automatic: true, width: "94%container" },
                    imageFont: null
            },
            tex2jax: {
                preview: "none",
                ignoreClass:"title-article"
            },
            mml2jax: {
                preview: 'none'
            }
    });
</script>
<script type="text/javascript" crossorigin src="https://g.csdnimg.cn/common/csdn-login-box/csdn-login-box.js"></script></html>

"""
res = jio.remove_html_tag(text)
print(res)

# 效果一般哈哈
