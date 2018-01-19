<html>
<head>
<script src="brython.js"></script>
<script src="brython_stdlib.js"></script>
</head>
<body onload="brython()">
<script type="text/python">
#-------------------------------------------------------------------------------
from browser import document

def display(text):
	#document["display"].clear()
	document["display"].html = text

import random

liste_1 = ["C1","CR","CD","CV","CX","C9","C8","C7","K1","KR","KD","KV","KX","K9","K8","K7","P1","PR","PD","PV","PX","P9","P8","P7","T1","TR","TD","TV","TX","T9","T8","T7"]
display("<img src='" + liste_1[0] +".png' width='400' />")
n=1

random.shuffle(liste_1)

def change():
	global liste_1, n
	document["display"].clear()
	display("<img src='" + liste_1[n] +".png' width='400' />")
	n = n + 1
document["display"].bind("click", change)





#-------------------------------------------------------------------------------
</script>
<div id="display"></div>


</body>
</html>
