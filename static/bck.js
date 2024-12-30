function checkInput() {  
    //获取用户名和密码
    var username = document.getElementById('username').value;  
    var password = document.getElementById('password').value;
    
    //只包含数字和英文字母的正则
    var alphanumericRegex = /^[a-zA-Z0-9]+$/

    //需要包含数字和字母的正则
    var containsnumber = /[0-9]/
    var containsletter = /[a-zA-Z]/

    //验证长度
    if (username.length < 8 || password.length < 8) {  
        alert("用户名密码必须大于8位");  
        return false;  
    }  

    //验证是否包含特殊字符
    if (!alphanumericRegex.test(username) || !alphanumericRegex.test(password)) {  
        alert("用户名和密码含有除数字和字母以外的特殊字符");  
        return false;  
    }  
    
    //验证是否同时包含数字和字母
    if (!containsnumber.test(username) || !containsletter.test(username)){
        alert("用户名没有同时包含数字和字母")
        return false;
    }
    if (!containsnumber.test(password) || !containsletter.test(password)){
        alert("密码没有同时包含数字和字母")
        return false;
    }
    return true;  
}  