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

    <script type="text/javascript">
    
        function alert1(text1, text2)
        {
            alert("Ideology: "+text1+ " Uncertainty: "+text2);
        }        
        
        var count=0
        function count_click(){   
        count++;
        if (count<3 && (selfplaceslider.Value() < 23 || selfplaceslider.Value()> 27 || varianceslider.Value() < 12 || varianceslider.Value()> 13)){
            alert("Please reread the instructions and try again.  You are almost ready to start the survey!");
        }
        else if (count>2 && (selfplaceslider.Value() < 23 || selfplaceslider.Value()> 27 || varianceslider.Value() < 12 || varianceslider.Value()> 13)){
            document.location.href="http://survey.research.yale.edu/cgi-bin/notelig.py";
        }
        else{
            document.location.href="http://survey.research.yale.edu/cgi-bin/introslider4.py";
        }
            }
    </script> 

</head>



<body>


<h4> Putting it all Together </h4>

<p> Excellent! Now you've learned to indicate your best guess with the pointer and to adjust your answer range with the red circle.  Here's one
last example.  Suppose you have a new bag of marbles and your best guess is that there are 75 marbles in the bag.
Suppose also that you are 95 percent certain that there are between 50 and 100 marbles in the bag.
<br/>
<br/>

<p> <b>First</b>, please indicate that your <b>best guess</b> is 75 by dragging the arrowhead labeled "Number of Marbles" to <b>75</b>. 

<p> <b>Second</b>, please indicate that you are 95 percent certain that there are between 50 and 100 marbles in the bag by using
the red circle to adjust the <b>answer range</b> so that it goes <b>from 50 to 100</b>.
<br/>
<br/>
Click Next when you're done.

<div id="box" class="jxgbox" style="width:750px; height:225px;"></div>



<script type="text/javascript">



  /* Create board */

 var b = JXG.JSXGraph.initBoard('box', {boundingbox: [-60, 10, 75, -12], axis:false, grid:false, showCopyright:false, showNavigation:false});

  

 /* Create ideology placement line */

 var iline = b.create('line',[[-50,0],[50,0]], {fixed:true, straightFirst:false, straightLast:false, strokeWidth:3, highlightstrokeWidth:3, fillColor : '#000000', strokeColor : '#000000', highlightFillColor : '#000000', highlightStrokeColor : '#000000'});



 /* Create vertical markers at ends and key values */

 var ilineleft = b.create('line',[[-50,1],[-50,-1]], {fixed:true, straightFirst:false, straightLast:false, strokeWidth:1, highlightstrokeWidth:1, fillColor : '#000000', strokeColor : '#000000', highlightFillColor : '#000000', highlightStrokeColor : '#000000'});

 var ilineright = b.create('line',[[50,1],[50,-1]], {fixed:true, straightFirst:false, straightLast:false, strokeWidth:1, highlightstrokeWidth:1, fillColor : '#000000', strokeColor : '#000000', highlightFillColor : '#000000', highlightStrokeColor : '#000000'});

var ilinemiddle = b.create('line',[[0,1],[0,-1]], {fixed:true, straightFirst:false, straightLast:false, strokeWidth:1, highlightstrokeWidth:1, fillColor : '#000000', strokeColor : '#000000', highlightFillColor : '#000000', highlightStrokeColor : '#000000'});

var ilinemiddle = b.create('line',[[25,1],[25,-1]], {fixed:true, straightFirst:false, straightLast:false, strokeWidth:1, highlightstrokeWidth:1, fillColor : '#000000', strokeColor : '#000000', highlightFillColor : '#000000', highlightStrokeColor : '#000000'});

 var ilineleft = b.create('line',[[-25,1],[-25,-1]], {fixed:true, straightFirst:false, straightLast:false, strokeWidth:1, highlightstrokeWidth:1, fillColor : '#000000', strokeColor : '#000000', highlightFillColor : '#000000', highlightStrokeColor : '#000000'});


 /* Label endpoints and key values */

 ilinelefttxt1 = b.create('text',[-50.5,-2, '0'], {fixed:true, fontSize:12});

 ilinerighttxt1 = b.create('text',[48,-2, '100'], {fixed:true, fontSize:12});

 ilinemiddletxt1 = b.create('text',[-1.4,-2, '50'], {fixed:true, fontSize:12});
 
 ilinemiddletxt1 = b.create('text',[25,-2, '75'], {fixed:true, fontSize:12});
 
  ilinemiddletxt1 = b.create('text',[-25,-2, '25'], {fixed:true, fontSize:12});
 


   

  /* Create self placement slider */
  var selfplaceslider = b.create('slider',[[-50,1.5],[50,1.5],[-50,0,50]],
  {
    withLabel:false, withTicks:false, face:'v', strokeColor:'#000000', highlightStrokeColor:'#000000', fillColor:'#000000', highlightFillColor:'#000000', size:12, fixed:false,
    baseline:{strokeWidth:0,highlightstrokeWidth:0,strokeColor:'#000000',highlightStrokeColor:'#000000', visible:false },
    highline: {strokeWidth:0,highlightstrokeWidth:0,strokeColor:'#000000',highlightStrokeColor:'#000000', visible:false }
  });
  var selfplaceline = b.create('line',[[function(x){ return selfplaceslider.Value();},3],
   [function(x){ return selfplaceslider.Value();},2]], {straightFirst:false, straightLast:false, strokeWidth:3, highlightstrokeWidth:3, fillColor:'#000000', strokeColor:'#000000', highlightFillColor:'#000000', highlightStrokeColor:'#000000'});
  
  var selfplacelabel = b.create('text', [function(x){ return selfplaceslider.Value()-2.6;}, 5.8,'Number of'],
   {fontSize:14});
  
  var selfplacelabel = b.create('text', [function(x){ return selfplaceslider.Value()-1.6;}, 4,'Marbles'],
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

 /* var nflabel1 = b.create('text', [function(x){ return selfplaceslider.Value()-10;}, -5,'95 times out 100, the true'], {fontSize:12});

 var nflabel2 = b.create('text', [function(x){ return selfplaceslider.Value()-10;}, -7,'value will be in the red range'], {fontSize:12});  

 */

 </script>

<form method="post" onclick="count_click(); return false;"/>
<input type="submit" value="Next">
<input type="hidden" name="user_id" value="%s">
</form>     

</body>
</html>
""" 


