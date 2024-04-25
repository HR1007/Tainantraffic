
//資料視覺化圖片
function ShowContent(contentId) {
    var  contentblock = document.getElementsByClassName("content-block");
    for (var i = 0; i < contentblock.length; i++) {
        contentblock[i].style.display = "none";
        var motivationText = contentblock[i].nextElementSibling;
                    if (motivationText) {
                        motivationText.style.display = "none";
                    }
   }
   var selectcontent = document.getElementById(contentId);
   if (selectcontent) {
    selectcontent.style.display = "block";
    var selectedMotivationText = selectcontent.nextElementSibling;
    if (selectedMotivationText) {
        selectedMotivationText.style.display = "block";
    }
   }

}
//按鈕觸發事件
function up(elem){
    elem.style.fontWeight = "normal";
}
function down(elem){
    elem.style.fontWeight = "bold";
}
function over(elem){
    elem.style.backgroundColor ="#DCDCDC";
}
function out(elem){
    elem.style.backgroundColor ="";
}//C要大寫



