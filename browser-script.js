var r = function(a, b) {
  return Math.random() * (b - a) + a;
};

var doScroll = function() {
  window.scrollBy({ top: r(-150, 150), left: 0, behavior: 'smooth' });
};

var doMove = function() {
  var x = r(0, innerWidth);
  var y = r(0, innerHeight);
  var el = document.elementFromPoint(x, y) || document.body;
  el.dispatchEvent(new MouseEvent('mousemove', {
    bubbles: true,
    clientX: x,
    clientY: y,
    screenX: x + screenX,
    screenY: y + screenY
  }));
};

var keepAlive = function() {
  document.title = document.title;
  var e = new Event('visibilitychange');
  document.dispatchEvent(e);
};

var go = function() {
  var a = Math.random();
  if (a < 0.4) doScroll();
  else if (a < 0.8) doMove();
  else keepAlive();
  setTimeout(go, r(3000, 6000));
};

go();
console.log('[activity] started');
