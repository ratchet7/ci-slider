#!/usr/bin/env python

"""Functions/data needed across cgi-bin scripts."""
import cgitb
# Turn on or off python debugging. Comment line below for off.
#cgitb.enable()

def header():
  """Common header across pages to display."""
print "Content-type: text/html"
print

print """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
<"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<meta http-equiv="Pragma" content="no-cache" />
<meta http-equiv="Expires" content="-1" />
<link rel="stylesheet" href="/style.css" type="text/css">
<link rel="stylesheet" type="text/css" href="http://jsxgraph.uni-bayreuth.de/distrib/jsxgraph.css" />
<script type="text/javascript" src="http://huber.research.yale.edu/jscript/jsxgraphcore.js"></script>
<link rel="stylesheet" type="text/css" href="http://jsxgraph.uni-bayreuth.de/distrib/jsxgraph.css" />
<script type="text/javascript" src="http://jsxgraph.uni-bayreuth.de/distrib/jsxgraphcore.js"></script>
<input type="hidden" id="refreshed" value="no">
<script type="text/javascript">
function sendSliderToForm(val, name){
  document.myform.elements[name].value=val;
}

</script>
</head>

"""

def timestamp():
  """Create a timestamp string formatted for mysql datetime type."""
  import time
  return time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())
  