#iOS打包shell
flutter --version

#-------- 重置环境
# 清除修改的内容
git reset --hard

# 重新安装包
flutter clean
flutter pub get

LOCAL_PATH="test"
APP_PATH=build/ios/ipa/NearHub.ipa

#-------- 输出git日志
#%3$s 为 git commit message
if [ ! -n "$SCM_CHANGELOG" ] ;then
    echo "没有commit记录 请注意"
else
    echo "SCM_CHANGELOG 如下 $SCM_CHANGELOG"
fi

#-------- 替换环境参数
echo pwd;
# 替换成对应环境 ， 日志调整成对应的环境 测试 仿真 正式
if [ $BUILD_TYPE == "测试" ];then
     for file in lib/config/config.dart; do sed -i '' 's/kCurrentType;/EnvType.test;/g' $file; done
     for file in lib/config/config.dart; do sed -i '' 's/kCurrentLevel;/RequestLogLevel.fullLog;/g' $file; done
elif [ $BUILD_TYPE == "仿真" ];then
     for file in lib/config/config.dart; do sed -i '' 's/kCurrentType;/EnvType.preRelease;/g' $file; done
     for file in lib/config/config.dart; do sed -i '' 's/kEnableMock;/false;/g' $file; done
     for file in lib/config/config.dart; do sed -i '' 's/kCurrentLevel;/RequestLogLevel.fullLog;/g' $file; done
elif [ $BUILD_TYPE == "正式" ];then
     for file in lib/config/config.dart; do sed -i '' 's/kCurrentType;/EnvType.release;/g' $file; done
     for file in lib/config/config.dart; do sed -i '' 's/kEnableMock;/false;/g' $file; done
     for file in lib/config/config.dart; do sed -i '' 's/kCurrentLevel;/RequestLogLevel.none;/g' $file; done
fi

# 替换对应的渠道
for file in lib/config/config.dart; do sed -i '' 's/kCurrentChannelType;/ChannelType.ios;/g' $file; done

#-------- 打包完成处理
flutter build ipa

#-------- 打包完成处理
if [ $BUILD_TYPE == "测试" ];then
     LOCAL_PATH="test"
elif [ $BUILD_TYPE == "仿真" ];then
     LOCAL_PATH="prerelease"
elif [ $BUILD_TYPE == "正式" ];then
     LOCAL_PATH="release"
fi

# 检查本地转寸路径是否存在
STORE_PATH="/Users/mac/Desktop/"${LOCAL_PATH}"/";
if [ ! -d "$STORE_PATH" ]; then
     mkdir "$STORE_PATH"
fi

# 转存app
cp ${APP_PATH} ${STORE_PATH}nearhub_${PACKAGE_VERSION}_${BUILD_TYPE}_$(date "+%m-%d_%H_%M_%S").ipa

#-------- 打包ad-hoc
# uKey和api_key都可以去蒲公英自己的账号信息里查看
IOS_URL="https://www.pgyer.com/UbWxAR"
ANDROID_URL="https://www.pgyer.com/4fzdt1"
API_KEY="99d5f2bd5fca6f06478425d427613e74"
UKEY="aed55d5f25510758945664b84acdb8bb"
ADHOC_PATH=""
WORKSPACE_PATH=${WORKSPACE}/ios/Runner.xcworkspace
EXPORT_OPTIONS=/Users/mac/Desktop/ExportOptions.plist
ARCHIVE_PATH=/Users/mac/Desktop/archives/${BUILD_TYPE}/runner.xcarchive
EXPORTIPA=/Users/mac/Desktop/archives/${BUILD_TYPE}
if [ ! -d "$ARCHIVE_PATH" ]; then
     mkdir "$ARCHIVE_PATH"
fi

# 导出achive，里面的primary是前面的target
xcodebuild archive -workspace $WORKSPACE_PATH -scheme Runner -configuration Release -sdk iphoneos -archivePath $ARCHIVE_PATH

# 导出ipa
xcodebuild -exportArchive -archivePath $ARCHIVE_PATH -exportPath ${EXPORTIPA}/runner -exportOptionsPlist ${EXPORT_OPTIONS}

ADHOC_PATH=${EXPORTIPA}/runner/NearHub.ipa

# 上传蒲公英
echo "=================上传到正式蒲公英分发平台 ================="

# 上传文件
curl -F "file=@${ADHOC_PATH}" \
-F "_api_key="${API_KEY} \
-F "uKey="${UKEY} \
https://www.pgyer.com/apiv2/app/upload

# 消息通知
curl 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=d5d703bc-7e7f-4e7b-8ecd-127d8d55b651' \
   -H 'Content-Type: application/json' \
   -d '
   {
          "msgtype": "markdown",
          "markdown": {
          "content": "Nearhub IOS '${PACKAGE_VERSION}' nearhub_'${PACKAGE_VERSION}'_'${BUILD_TYPE}'_'$(date "+%m-%d_%H_%M_%S")'.ipa 打包完成, [下载链接]('${IOS_URL}')"
          }
   }'