/*Copyright (c) 2009 Johan Uhle

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

/* Initialize SoundManager */
soundManager.flashVersion = 9;
soundManager.debugMode = false;
soundManager.defaultOptions.multiShot = false;
soundManager.url = "http://a1.soundcloud.com/swf/soundmanager2_flash9.swf";

/* Initialize Google Maps */
var map;
var markerOptions1;
var markerOptions2;
var markerOptions3;

$(function() {
  if (GBrowserIsCompatible()) {
    map = new GMap2(document.getElementById("map_canvas"));
		map.addControl(new GSmallMapControl());
		map.addControl(new GMapTypeControl());
    map.setCenter(new GLatLng(46.437857, -42.011719), 3);				
	}
  
	var icon3 = new GIcon(G_DEFAULT_ICON);
  icon3.image = "images/sc_marker_3.png";
  icon3.iconSize = new GSize(22, 31);
  icon3.shadow = "images/sc_marker_3_shadow.png";
  icon3.shadowSize = new GSize(42, 31);
  icon3.iconAnchor = new GPoint(10, 29);
  icon3.infoWindowAnchor = new GPoint(10, 14);
  icon3.imageMap = [ 10,29, 1,16, 0,5, 5,0, 12,4, 18,2, 21,12, 21,16 ]; 	
	markerOptions3 = { icon:icon3 };       
	
	var icon2 = new GIcon(G_DEFAULT_ICON);
  icon2.image = "images/sc_marker_2.png";
  icon2.iconSize = new GSize(18, 27);
  icon2.shadow = "images/sc_marker_2_shadow.png";
  icon2.shadowSize = new GSize(42, 31);
  icon2.iconAnchor = new GPoint(10, 29);
  icon2.infoWindowAnchor = new GPoint(10, 14);
  icon2.imageMap = [ 10,29, 1,16, 0,5, 5,0, 12,4, 18,2, 21,12, 21,16 ]; 	
	markerOptions2 = { icon:icon2 };           
	
	var icon1 = new GIcon(G_DEFAULT_ICON);
  icon1.image = "images/sc_marker_1.png";
  icon1.iconSize = new GSize(12, 23);
  icon1.shadow = "images/sc_marker_1_shadow.png";
  icon1.shadowSize = new GSize(42, 31);
  icon1.iconAnchor = new GPoint(10, 29);
  icon1.infoWindowAnchor = new GPoint(10, 14);
  icon1.imageMap = [ 10,29, 1,16, 0,5, 5,0, 12,4, 18,2, 21,12, 21,16 ]; 	
	markerOptions1 = { icon:icon1 };
	
});
