#!/usr/bin/ruby
# -*- coding: utf-8 -*-
require"cgi"
c=CGI.new
print("Content-Type: text/html; charset=utf-8

<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML .01//EN\"
\"http://www.w3.org/TR/html4/strit.dtd\">
<html>
  <head>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src=\"https://www.googletagmanager.com/gtag/js?id=UA-123258228-1\"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'UA-123258228-1');
    </script>
    <title> ラーメンデータベース </title>
    <link rel=\"stylesheet\" href=\"ramen1.css\">
  </head>
  <body><center>
    <h2>ラーメンデータベース</h2>
    <p class=\"p1\">現在開店しているつくば市内のラーメン屋を表示します。</p>
    <p class=\"p2\">ソート方法</p>
    <form method=\"post\" action=\"ramen2.cgi\">

  <div class=\"radio\">
    <input type=\"radio\" name=\"q\" value=\"a2\" id=\"male\" checked>
      <label class=\"l1\" for=\"male\">エリア順</label>
    <input type=\"radio\" name=\"q\" value=\"a1\" id=\"female\">
      <label class=\"l1\" for=\"female\">ランキング順</label>
  </div>

    <p class=\"p2\">表示エリア</p>
    <!-- <div class=\"div0\"> -->
    <div class=\"div1\"><ul>")
area=["天久保2エリア","天久保1エリア","吾妻エリア","天久保3,桜,栗原エリア","裏天久保3,春日エリア","筑穂,花畑エリア","つくば駅南エリア","研究学園駅エリア","車推奨エリア"]

area.each_index{|n|print"

    <li>
      <label class=\"left\">
        #{area[n]}</label>


          <label class=\"switch__label\">
            <input type=\"checkbox\" class=\"switch__input\"/ name=\"q#{n}\" value=\"on\" id=\"z#{n}\" checked>
            <span class=\"switch__content\"></span>
            <span class=\"switch__circle\"></span>
          </label>




    </li>

"}
print("  </ul><br></div>
  <!-- <div class=\"div2\"><img usemap=\"#sample\" class=\"map\" src=\"white.jpg\" >
  <map name=\"sample\">
    <area href=\"aaa.jpeg\" shape=\"rect\" alt=\"四角形\" coords=\"15,19,126,104\">
    <area href=\"aaa.jpeg\" shape=\"circle\" alt=\"円形\" coords=\"197,69,54\">
    <area href=\"aaa.jpeg\" shape=\"poly\" alt=\"多角形\" coords=\"306,12,261,109,378,92\">
  </map></div>
  </div> -->
  <div class=\"div3\">
      <input type=\"submit\" value=\"検索\">
      <input type=\"reset\" value=\"クリア\"><br>
  </div>
    </form></center>

    <!--
    <script>
      var img = document.querySelector('img');
      img.src = \"http://www.oota-k.net/image/0011.jpg\";
    </script>
    -->

  </body>
</html>
")

#http://cgi.u.tsukuba.ac.jp/~s1711520/ramen/ramen1.cgi
