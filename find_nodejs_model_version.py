import os
from pathlib import Path

def list_directory_with_oswalk(root_path, list):
    ll = []

    root_path = Path(root_path).resolve()  # 标准化路径
    for dirpath, dirnames, filenames in os.walk(root_path):
        # print(f"dirpath: {dirpath}")
        # # 计算当前目录相对于根目录的深度
        depth = len(Path(dirpath).relative_to(root_path).parts)
        if depth > 2:
            continue  # 跳过超过两层的目录
        
        # 输出当前目录下的所有文件和子目录
        indent = '  ' * depth
        
        # print(f"{indent}├── {Path(dirpath).name}/")
        for file in filenames:
            # print(f"{indent}│   └── {file}")
            if file == "package.json":
                file_path = os.path.join(dirpath, file)
                ss = file_path.split("/")[-2]
                for i in list:
                    if i == ss:
                        with open(file_path, "r", encoding="utf-8") as f:
                            data = f.read()
                            # print(f"{file_path}: {data}")
                            if "version" in data:
                                version = data.split('"version":')[1].split(",")[0].strip().replace('"', "")
                                # print(f"{ss}:{version}")
                                if ss not in ll:
                                    ll.append(f"{ss}:{version}")
                            else:
                                print(f"{ss}: No version found")

    return ll

def getunpkg_static(name, version):
    url = f"{name}@{version}:: https://unpkg.com/{name}@{version}/dist/{name}.min.js"
    return url

l = [
     "vue", 
     "vuex", 
     "vue-router", 
     "vue-i18n",
     "ant-design-vue",
     "axios",
     "animate.css",
     "echarts",
     "moment",
     "vue",
     "nprogress",
     "clipboard",
     "js-md5",
     "mavon-editor",
     "xlsx",
     "jsencrypt",
     "js-cookie",
     ]
# 示例用法
lll = list_directory_with_oswalk("/Users/wuzhiqiang/Documents/GitHub/blog/admin/node_modules", l)

for i in lll:
    name = i.split(":")[0]
    version = i.split(":")[1]
    url = getunpkg_static(name, version)
    print(f"{name}: {url}")
