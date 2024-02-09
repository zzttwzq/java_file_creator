flutter --version

# 清除修改的内容
git reset --hard

# 进入工作目录
cd ${WORKSPACE}/

# 进入
cd lib/config

# 替换成对应环境 ， 日志调整成对应的环境 测试 仿真 正式
if [ $BUILD_TYPE == "测试" ];then
     for file in config.dart; do sed -i '' 's/kCurrentType;/EnvType.dev;/g' $file; done
elif [ $BUILD_TYPE == "仿真" ];then
     for file in config.dart; do sed -i '' 's/kEnableMock;/false;/g' $file; done
     for file in config.dart; do sed -i '' 's/kCurrentLevel;/RequestLogLevel.none;/g' $file; done
     for file in config.dart; do sed -i '' 's/kCurrentType;/EnvType.preRelease;/g' $file; done
elif [ $BUILD_TYPE == "正式" ];then
     for file in config.dart; do sed -i '' 's/kEnableMock;/false;/g' $file; done
     for file in config.dart; do sed -i '' 's/kCurrentLevel;/RequestLogLevel.none;/g' $file; done
     for file in config.dart; do sed -i '' 's/kCurrentType;/EnvType.release;/g' $file; done
fi

# 替换iOS渠道标志
for file in config.dart; do sed -i '' 's/kCurrentChannelType;/ChannelType.macos;/g' $file; done
cd ../../

# 获取flutter包
flutter clean
flutter pub get

# 获取iOS包
cd macos
pod install
cd ../

# build app，里面的primary是前面的target
flutter build macos --release

# 进入原生项目
cd build/macos/Build/Products/Release/

create-dmg --volname nearhub \
     --window-pos 200 120 \
     --window-size 800 400 \
     --hide-extension NearHub.app \
     --app-drop-link 600 185 \
     nearhub.dmg \
     NearHub.app

LOCAL_PATH="test"
if [ $BUILD_TYPE == "测试" ]; then
     LOCAL_PATH="test"
elif [ $BUILD_TYPE == "仿真" ]; then
     LOCAL_PATH="prerelease"
elif [ $BUILD_TYPE == "正式" ]; then
     LOCAL_PATH="release"
fi

#%3$s 为 git commit message
if [ ! -n "$SCM_CHANGELOG" ]; then
     echo "没有commit记录 请注意"
else
     echo "SCM_CHANGELOG 如下 $SCM_CHANGELOG"
fi

STORE_PATH="/Users/mac/Desktop/"${LOCAL_PATH}"/"
if [ ! -d "$STORE_PATH" ]; then
     mkdir "$STORE_PATH"
fi

# 导出包到对应位置
mv nearhub.dmg /Users/mac/Desktop/${LOCAL_PATH}/nearhub_${VERSION}_${BUILD_TYPE}_$(date "+%m-%d_%H_%M_%S").dmg
