#!/usr/bin/env python

"""training-mean"""

import os
import cgi
import PubGlobals
import cgitb; #cgitb.enable()
import random
import MySQLdb


PubGlobals.header()

print"""
 

 </head>



<body>

<form method="post" action="example5.py">

<h4> Introduction to the Ideology Slider </h4>

<p>Great! We're almost ready to get started. 

<p>You can also use this tool to tell us what you think about politics.  <br/> <br/>


<div id="box" class="jxgbox" style="width:750px; height:225px;"></div>



<script type="text/javascript">
 
  /* Create board */

 var b = JXG.JSXGraph.initBoard('box', {boundingbox: [-60, 10, 75, -12], axis:false, grid:false, showCopyright:false, showNavigation:false});

  

 /* Create ideology placement line */

 var iline = b.create('line',[[-50,0],[50,0]], {fixed:true, straightFirst:false, straightLast:false, strokeWidth:3, highlightstrokeWidth:3, fillColor : '#000000', strokeColor : '#000000', highlightFillColor : '#000000', highlightStrokeColor : '#000000'});



 /* Create vertical markers at ends and midpoint */

 var ilineleft = b.create('line',[[-50,1],[-50,-1]], {fixed:true, straightFirst:false, straightLast:false, strokeWidth:1, highlightstrokeWidth:1, fillColor : '#000000', strokeColor : '#000000', highlightFillColor : '#000000', highlightStrokeColor : '#000000'});

 var ilineright = b.create('line',[[50,1],[50,-1]], {fixed:true, straightFirst:false, straightLast:false, strokeWidth:1, highlightstrokeWidth:1, fillColor : '#000000', strokeColor : '#000000', highlightFillColor : '#000000', highlightStrokeColor : '#000000'});

 var ilinemiddle = b.create('line',[[0,1],[0,-1]], {fixed:true, straightFirst:false, straightLast:false, strokeWidth:1, highlightstrokeWidth:1, fillColor : '#000000', strokeColor : '#000000', highlightFillColor : '#000000', highlightStrokeColor : '#000000'});
 
 var ilinemiddle = b.create('line',[[-25,1],[-25,-1]], {fixed:true, straightFirst:false, straightLast:false, strokeWidth:1, highlightstrokeWidth:1, fillColor : '#000000', strokeColor : '#000000', highlightFillColor : '#000000', highlightStrokeColor : '#000000'});
 
 var ilinemiddle = b.create('line',[[25,1],[25,-1]], {fixed:true, straightFirst:false, straightLast:false, strokeWidth:1, highlightstrokeWidth:1, fillColor : '#000000', strokeColor : '#000000', highlightFillColor : '#000000', highlightStrokeColor : '#000000'});
 

 

 /* Label endpoints and midpoint */

 ilinelefttxt1 = b.create('text',[-52,-2, 'Very'], {fixed:true, fontSize:12});

 ilinelefttxt2 = b.create('text',[-53,-3.5, 'Liberal'], {fixed:true, fontSize:12});

 ilinerighttxt1 = b.create('text',[48,-2, 'Very'], {fixed:true, fontSize:12});

 ilinerighttxt2 = b.create('text',[45,-3.5, 'Conservative'], {fixed:true, fontSize:12});

 ilinemiddletxt1 = b.create('text',[-4,-2, 'Moderate'], {fixed:true, fontSize:12});
 
 ilinerighttxt1 = b.create('text',[21,-2, 'Somewhat'], {fixed:true, fontSize:12});

 ilinerighttxt2 = b.create('text',[20,-3.5, 'Conservative'], {fixed:true, fontSize:12});
 
  ilinerighttxt1 = b.create('text',[-29,-2, 'Somewhat'], {fixed:true, fontSize:12});

 ilinerighttxt2 = b.create('text',[-28,-3.5, 'Liberal'], {fixed:true, fontSize:12});
 
 







  /* Label 95percent percentiles */

 var nfline = b.create('line',[[function(x){ return selfplaceslider.Value()-2*varianceslider.Value();},-.25],[function(x){ return selfplaceslider.Value()+2*varianceslider.Value();},-.25]],{straightFirst:false, straightLast:false, strokeWidth:10, highlightstrokeWidth:10, fillColor : '#FF0000', strokeColor : '#FF0000', highlightFillColor : '#FF0000', highlightStrokeColor : '#FF0000'});

/* var nflabel1 = b.create('text', [function(x){ return selfplaceslider.Value()-10;}, -5,'95 times out a 100, the true'], {fontSize:12});

 var nflabel2 = b.create('text', [function(x){ return selfplaceslider.Value()-10;}, -7,'value will be in the red range'], {fontSize:12});  
*/
  

 </script>


<br/>

<p>We hear a lot of talk these days about liberals and conservatives. In this study, we'd like you to think about
individuals being either more or less liberal or conservative, and that this characteristic can be represented on a line.
We've displayed such a line above, which ranges
from individuals who are "very liberal" on the left,
to individuals who are "very conservative" on the right, with somewhat liberal, somewhat conservative, and moderate in between.

<form method="post" />
<p><input type="submit" value="Next">
<input type="hidden" name="user_id" value="%s">
</form>   

</body>
</html>
""" 




