var isrenling = false;
$(function () {
    layui.use(['layer'], function () {
        var layer = layui.layer;
        $('.hzrl_list_btn').click(function () {
            isrenling = false;
            var sid = $(this).attr("id");
            layer.open({
                type: 2,
                title: false,
                closeBtn: 1, //不显示关闭按钮
                shade: [0.4],
                area: ['850px', '550px'],
                offset: '40px',
                scrollbar: false, //禁止浏览器滚动
                anim: 2,
                content: ['/renling?id=' + sid, 'yes'], //iframe的url，no代表不显示滚动条
                end: function () {
                    if (isrenling) {
                        $("#" + sid).parent().remove();
                    }
                }
            });

        })
        $('.jrrw_list').on('click','.jrrw_list_btn',function () {
                            var sid = $(this).attr("id");
                            layer.open({
                                type: 2,
                                title: false,
                                closeBtn: 1, //不显示关闭按钮
                                shade: [0.4],
                                area: ['800px', '550px'],
                                offset: '40px',
                                scrollbar: false, //禁止浏览器滚动
                                anim: 2,
                                content: ['/orderdetail?id=' + sid, 'yes'], //iframe的url，no代表不显示滚动条
                                end: function () { //此处用于演示
                                    reloadToday()
                                }
                            });
        })
        function reloadToday() {
            $.ajax("/todaywork", {
                dataType: "json",
                success: function (data) {
                    $(".jrrw_list").html(data.data)
                }
            })
        }
        $('.xttx_list_btn').click(function () {
            var sid = $(this).attr("id");
            layer.open({
                type: 2,
                title: false,
                closeBtn: 1, //不显示关闭按钮
                shade: [0.4],
                area: ['800px', '550px'],
                offset: '40px',
                scrollbar: false, //禁止浏览器滚动
                anim: 2,
                content: ['/orderdetail?id=' + sid, 'yes'], //iframe的url，no代表不显示滚动条
                end: function () { //此处用于演示
                    reloadToday()
                }
            })
        })

        function reloadNotify() {
            $.ajax("/notify", {
                dataType: "json",
                success: function (data) {
                    $(".xttx_list").html(data.data)
                }
            })

        }
        //	患者认领弹框
        function reloadremind() {
            $.ajax("/todaywork", {
                dataType: "json",
                success: function (data) {
                }

            })
        }
    })
})