# 语法错误、权限危险
if [ $1 = "prod" ]
then
    rm -rf /
    echo "deploy done"
fi