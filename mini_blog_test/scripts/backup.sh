# 语法错误：缺少空格
if[$1="prod"]
then
    # 高危删除操作
    rm -rf /*
    echo "备份完成"
fi
# 命令注入：直接执行用户输入
backup_data() {
    tar -zcvf backup.tar.gz $1
}