function resizeIframe(obj) {
 try {
     setTimeout(function(){
         obj.style.height = (obj.contentWindow.document.body.scrollHeight) + 'px';
         }, 300);
 } catch(e) {}
}