// 未定义变量使用
function showUser(id) {
    if (userActive) {
        fetch("/api/user/" + id)
    }
}

// 弱密码校验
function checkPassword(pwd) {
    return pwd.length > 3;
}

// XSS 拼接HTML
function renderComment(text) {
    document.getElementById("comment").innerHTML = text;
}