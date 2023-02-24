# 安装
## 安装Release版本
### Windows

### MacOS

### Linux

## C++源码编译
### 环境依赖
#### Windows
在Windows环境下，需要确保已经安装最新版本Visual Studio，保证C++模块被正确安装(建议安装并默认使用clang工具链):

![Visual Studio](IMAGE_DIR/vs_installer_zh.png)

### 拉取源码
[github.com/LuisaGroup/LuisaCompute](https://github.com/LuisaGroup/LuisaCompute)是我们首选的源码仓库，正式版本的更新会发布在master branch，通过指令

git clone https://github.com/LuisaGroup/LuisaCompute

即可拉取项目到本地。
### 使用xmake构建
TEXT_BEGIN
我们提供了基于xmake的源码构建流程，[xmake](https://xmake.io)是负责C++配置和构建的一体化工具，因此这可能是对您的环境配置要求最简单的构建方法
在确保xmake和上述的环境依赖项已经安装完成后，首先需要在源码所在的目录下执行配置(#符号内的内容表示需要按照当前环境进行选择,#符号本身必须删除)
xmake f -p #windows/linux/macos# -a x64 -m #debug/release#
随后调用命令:
xmake -w
完成编译，-w会输出警告，这有助于避免开发中遇到的潜在危险。
在配置后还可以输入自定义的选项，自定义选项的输入是 --选项名称=选项设置，在项目中我们提供了这些选项：
toolchain: 根据不同操作系统可以选择不同的工具链，这通常会影响编译体验，可选择的有clang, clang-cl, gcc, msvc等，若保持默认，将由xmake自动选择。
export_config: 当我们需要在其他项目中使用LuisaCompute的编译结果，而非直接使用源码编译时，可以设置此选项为true(默认为false)，这将会在编译完成时输出config/xmake_config.lua文件供其他工程使用。
enable_dsl: 设置为true(默认为false)将编译DSL模块，支持C++内使用DSL编写kernel。
enable_py: 设置为true(默认为false)将编译Python绑定支持。
enable_gui: 设置为true(默认为false)将编译原生窗口和GUI支持。
enable_rust: 设置为true(默认为false, 遇到依赖时会强制开启)将编译Rust绑定与后端支持(xmake会在编译C++部分的同时拉取Cargo编译，请确保您的计算机已经正确安装Cargo)。
enable_tests: 设置为true(默认为false，因tests模块依赖dsl，该选项将会强制启动enable_dsl)将编译test目录的构建，方便您测试与学习LuisaCompute的使用。
dx_backend, cuda_backend, metal_backend: 设置为true(默认为true，根据平台和当前环境自动选择)将编译DirectX-12后端。
use_mimalloc: 设置为false(默认为true)将禁用内存分配库mimalloc，并使用平台原生的内存分配。
use_unity_build: 设置为false(默认为true)将禁用unity build编译加速。
enable_simd: 设置为false(默认为true)将禁止编译器使用SSE优化。
TEXT_END
### 使用cmake构建
TEXT_BEGIN
[cmake](https://cmake.org/)构建也同样是我们支持的方法，由于cmake本身只支持配置，不支持构建，因此在您的环境中可能需要其他
TEXT_END
### 
## 使用Python源码