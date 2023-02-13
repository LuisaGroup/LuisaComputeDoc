# API文档简介

## 查找/阅读API文档

C++ API文档为需要查找LC前端功能的用户准备，其单独介绍每个类型的设计概念，由于文档碎片化，不宜单独阅读，推荐结合教程部分阅读。文档中只会介绍类型的设计概念，而不会针对每一个成员函数、成员变量提供解释，而会指出其定义所在的.h文件中，您可能会在目标源文件的注释里发现更详细的介绍。

## 工程结构

在管理源码方面，LC采用多目标的构建方式，默认配置下，每一个目标都会被构建为动态的运行时库类型（如Linux操作系统的.so文件，或Windows操作系统的.dll文件），除计算后端以外，目标编译时会输出必需的符号以供其他目标或外部应用链接（在Windows操作系统会单独输出.lib文件），计算后端则不会经过编译器链接，而是运行时显式加载卸载。使用源码或Release版本可参考[安装](../getting_started/installation.md)文档。

## 子工程

* lc-core：核心功能，基础库
* lc-vstl: 应用库，非STL标准容器等
* lc-ast：语法树，提供kernel编译功能
* lc-runtime：运行时前端
* lc-gui：为支持窗口显示的后端（如DirectX-12, Metal）提供原生的GUI
* lc-dsl：C++ DSL模块
* lc-py：Python语言绑定模块
* lc-backend-dx, lc-backend-metal, lc-backend-cuda：计算后端模块
* lc-test：测试与案例

除src/rtx, src/raster目录内容属于runtime工程以外，其他目录与子工程同名。

## 子模块（submodule）

所有第三方子模块位于src/ext目录下。

### 必需第三方子模块（均为可免费试用的开源工程）

* [spdlog](https://github.com/LuisaGroup/spdlog.git)：为工程提供log，debug功能
* [xxHash](https://github.com/Cyan4973/xxHash.git)：提供hash算法
* [EASTL](https://github.com/LuisaGroup/EASTL.git): 提供实现确定的标准模板库
* [parallel-hashmap](https://github.com/greg7mdp/parallel-hashmap.git): 提供高效率的std::map实现

### 非必需第三方子模块（均为可免费试用的开源工程）

* [stb](https://github.com/nothings/stb.git)：导出图片库，lc-test目标依赖
* [glfw](https://github.com/glfw/glfw.git)：提供跨平台窗口，lc-gui, lc-test目标依赖
* [imgui](src/ext/imgui/imgui)：提供debug gui，lc-test目标依赖
* [pybind11](https://github.com/LuisaGroup/pybind11)：提供Python绑定，lc-py目标依赖
* [corrosion](https://github.com/corrosion-rs/corrosion)：提供rust编译支持，仅CMake源码编译用户需要。
