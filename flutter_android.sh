#-------- android 打包shell
# none
# yingyongbao
# xiaomi
# huawei
# oppo
# vivo
# meizu
# wandoujia
# baidu
# googleplay
# langguo

flutter --version

#-------- 重置环境
# 清除修改的内容
git reset --hard

# 重新安装包
flutter clean
flutter pub get

# apk目录
WORKSPACE_PATH=""

# 打包 app 路径
APP_PATH=""

# app后缀名
APP_TAIL=""

# 上传蒲公英 uKey和api_key都可以去蒲公英自己的账号信息里查看
LOCAL_PATH="test"
if [ $CHANNEL_TYPE != "langguo" ];then
     API_KEY="0effabc3b34fa1a9cc72f1dcd83220f4"
     UKEY="f8a17cf8a41c3fab756da10f6acb7d32"
     URL="https://www.pgyer.com/rr5e"
else
     API_KEY="99d5f2bd5fca6f06478425d427613e74"
     UKEY="aed55d5f25510758945664b84acdb8bb"
     URL="https://www.pgyer.com/4fzdt1"
fi

#-------- 输出git日志
#%3$s 为 git commit message
if [ ! -n "$SCM_CHANGELOG" ] ;then
    echo "没有commit记录 请注意"
else
    echo "SCM_CHANGELOG 如下 $SCM_CHANGELOG"
fi

#-------- 替换环境参数
# 进入工作目录
cd ${WORKSPACE}/

# 替换朗国环境
if [ $CHANNEL_TYPE != "langguo" ];then
     for file in android/app/src/main/AndroidManifest.xml; do sed -i '' 's/android:sharedUserId="android.uid.system"//g' $file; done
     for file in android/app/src/main/java/com/awx/nearhub/App.java; do sed -i '' 's/UserAPI.getInstance().init(this);//g' $file; done
     for file in android/app/src/main/java/com/awx/nearhub/App.java; do sed -i '' 's/if(DeviceUtils.isLangoPlatform()) {//g' $file; done
     for file in android/app/src/main/java/com/awx/nearhub/App.java; do sed -i '' 's/        }//g' $file; done
fi

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
for file in lib/config/config.dart; do sed -i '' 's/kCurrentCHANNEL_TYPE;/CHANNEL_TYPE.'$CHANNEL_TYPE';/g' $file; done

#-------- 开发打包
# 编译打包
if [ $PACKAGE_TYPE == "apk" ];then
     WORKSPACE_PATH=${WORKSPACE}/build/app/outputs/flutter-apk/
	flutter build apk
elif [ $PACKAGE_TYPE == "aab" ];then
     WORKSPACE_PATH=${WORKSPACE}/build/app/outputs/bundle/release/
	flutter build appbundle
fi

#-------- 打包完成处理
# 进入打包完成目录
# cd ${WORKSPACE_PATH}

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

# app路径
if [ $PACKAGE_TYPE == "apk" ];then
     APP_TAIL="apk"
     APP_PATH=${WORKSPACE}/build/app/outputs/flutter-apk/app-release.apk
elif [ $PACKAGE_TYPE == "aab" ];then
     APP_TAIL="aab"
     APP_PATH=${WORKSPACE}/build/app/outputs/bundle/release/app-release.aab
fi

# 转存app
cp ${APP_PATH} ${STORE_PATH}nearhub_${PACKAGE_VERSION}_${CHANNEL_TYPE}_${BUILD_TYPE}_$(date "+%m-%d_%H_%M_%S").${APP_TAIL}
# APP_PATH=${STORE_PATH}nearhub_${PACKAGE_VERSION}_${CHANNEL_TYPE}_${BUILD_TYPE}_$(date "+%m-%d_%H_%M_%S").${APP_TAIL}

if [ $PACKAGE_TYPE == "apk" ];then
     # 上传蒲公英
     echo "=================上传到正式蒲公英分发平台 ================="

     # 上传文件
     curl -F "file=@${APP_PATH}" \
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
               "content": "Nearhub Android '${PACKAGE_VERSION}' nearhub_'${PACKAGE_VERSION}'_'${CHANNEL_TYPE}'_'${BUILD_TYPE}'_'$(date "+%m-%d_%H_%M_%S")'.'${APP_TAIL}'打包完成, [下载链接]('${URL}')"
               }
     }'
fi