# # git 添加到暂存区
git add .

# git 提交内容
read -p "请输入提交版本号：" v
# read -p "请输入提交内容：" input
echo 'update()：<'$v'> 详见readme.md文件'
git commit -m 'update()：<'$v'> 详见readme.md文件'
git tag -a $v -m $v
git push --tags

git push