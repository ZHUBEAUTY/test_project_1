// 未定义变量直接使用
function loadArticles() {
    if (userLoggedIn) {
        fetch("/api/articles")
    }
}

// 弱校验：密码长度<4也通过
function validatePwd(pwd) {
    return pwd.length > 2;
}

// XSS 拼接HTML
function renderComment(cont) {
    document.getElementById("articles").innerHTML = cont;
}

// 死循环风险
function loopTest() {
    let i = 0;
    while (i < 10) {
        // 忘记自增
    }
}