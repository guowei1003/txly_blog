/**
 * Created by guowei on 2016/8/19.
 */

//时间及时
function update_time() {
    var mydate = new Date();
    var cur_time = mydate.getFullYear() + "年"
        + (mydate.getMonth() + 1) + "月"
        + mydate.getDate() + "日 "
        + mydate.getHours() + "时"
        + mydate.getMinutes() + "分"
        + mydate.getSeconds() + "秒";
    $("#update-time").html(cur_time);
}

$(function () {
    setInterval(update_time, 1000);
});