# Context

## 类定义
* 目录: src/runtime/context.h
* 所属工程目标：lc-runtime

## 注解

Context是整套流程中最基础的类型，要使用LC必须创建一个Context类型的实例，其主要功能是管理运行时，缓存等临时和永久目录，在目录下搜索可用的后端，以及根据用户需要生成指定后端的Device类。通常一个Context类可用类似的方法创建：

HTML_BEGIN
#include <runtime/context.h>
#include <runtime/device.h>
int main(int argc, char *argv[]) {
    using namespace luisa::compute;
    Context context{argv[0]};
    // 创建一个使用dx后端的device，其他如cuda, metal等均可以使用
    Device device = context.create_device("dx");
}
HTML_END