#!/usr/bin/env python

"""dems placement"""

import os
import cgi
import PubGlobals
import cgitb; #cgitb.enable() # comment out when for real


form = cgi.FieldStorage()
placementmean = cgi.escape(form.getvalue('placementmean'))
placementvar = cgi.escape(form.getvalue('placementvar'))
user_id = cgi.escape(form.getvalue('user_id'))
timestamp=PubGlobals.timestamp()

#PubGlobals.selfQuery(timestamp, placementmean, placementvar, user_id)

PubGlobals.header()

print"""

<script type="text/javascript">



function alert1(text1, text2)

{

alert("Ideology: "+text1+ " Uncertainty: "+text2);

}



</script> 

 

 

 </head>


<body>
<form method="post" name="myform" action="reps9.py" onsubmit="sendSliderToForm(selfplaceslider.Value(), 'placementmean'); sendSliderToForm(varianceslider.Value(), 'placementvar')"; >



<p>Where would you place the <b><FONT COLOR=blue>Democratic</font> Party</b>?
<br/>
<br/>

<p> <b>First</b>, indicate your <b>best guess</b> by dragging the arrowhead labeled "Democratic Party" to to a location on the slider. 

<p> <b>Second</b>, use the red circle to adjust the <b>answer range</b> so that you're
95 percent certain that the true ideology of the Democratic Party is in the red range.
<br/>
<br/>


<p> Click Next when you are finished.

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
 
 

   

  /* Create self placement slider */
  var selfplaceslider = b.create('slider',[[-50,1.5],[50,1.5],[-50,0,50]],
  {
    withLabel:false, withTicks:false, face:'v', strokeColor:'#000000', highlightStrokeColor:'#000000', fillColor:'#000000', highlightFillColor:'#000000', size:12, fixed:false,
    baseline:{strokeWidth:0,highlightstrokeWidth:0,strokeColor:'#000000',highlightStrokeColor:'#000000', visible:false },
    highline: {strokeWidth:0,highlightstrokeWidth:0,strokeColor:'#000000',highlightStrokeColor:'#000000', visible:false }
  });
  var selfplaceline = b.create('line',[[function(x){ return selfplaceslider.Value();},3],
   [function(x){ return selfplaceslider.Value();},2]], {straightFirst:false, straightLast:false, strokeWidth:3, highlightstrokeWidth:3, fillColor:'#000000', strokeColor:'#000000', highlightFillColor:'#000000', highlightStrokeColor:'#000000'});
  
  var selfplacelabel = b.create('text', [function(x){ return selfplaceslider.Value()-8;}, 4,'Democratic Party'],
   {fontSize:14});
    
     /* Variance slider */
    
     var varianceslider = b.create('slider',[[63,-5],[63,5],[21,11,1]],
     {
     withLabel:false, withTicks: false, face:'o', strokeColor : '#000000', highlightStrokeColor : '#000000', fillColor : '#FF0000', highlightFillColor : '#FF0000', size: 6,
    
      baseline: {strokeWidth: 3, highlightstrokeWidth: 3, strokeColor : '#000000', highlightStrokeColor : '#000000', visible: true },
    
      highline: {strokeWidth: 3, highlightstrokeWidth: 3, strokeColor : '#000000', highlightStrokeColor : '#000000', visible: true }
    
      });

  

  var poweradj=.25

  /* normal distribution approximated using logistic 

  var temp=b.create('functiongraph', [function(x){return 12*(1/Math.pow(varianceslider.Value()*2.506628274631000502415765284811,poweradj))*Math.pow(2.718281828,-(((x-selfplaceslider.Value())*(x-selfplaceslider.Value()))/(varianceslider.Value()*varianceslider.Value()*2)));},-60,60]);   */

  /* This approximation reduces the variance adjustment (the part out front, 1/...) to decreae more slowly so the curve is still visible for higher values Current this value is set at poweradj*/





  /* Label 95 percent percentiles */

 var nfline = b.create('line',[[function(x){ return selfplaceslider.Value()-2*varianceslider.Value();},-.25],[function(x){ return selfplaceslider.Value()+2*varianceslider.Value();},-.25]],{straightFirst:false, straightLast:false, strokeWidth:10, highlightstrokeWidth:10, fillColor : '#FF0000', strokeColor : '#FF0000', highlightFillColor : '#FF0000', highlightStrokeColor : '#FF0000'});

/* var nflabel1 = b.create('text', [function(x){ return selfplaceslider.Value()-10;}, -5,'95 times out a 100, the true'], {fontSize:12});

 var nflabel2 = b.create('text', [function(x){ return selfplaceslider.Value()-10;}, -7,'value will be in the red range'], {fontSize:12});  
*/
  

 </script>



<form method="post" />
<p><input type="submit" value="Next">
<input type="hidden" name="placementmean" value="">
<input type="hidden" name="placementvar" value="">
<input type="hidden" name="user_id" value="%s">
</form>



</body>
</html>
""" %(user_id)


