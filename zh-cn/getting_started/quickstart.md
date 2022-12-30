# 快速开始
## 了解LuisaCompute中的概念
### Context
在开始工作时，我们首先要创建一个Context，它是一切的基座，用于处理程序路径，多设备(Device)管理等基础工作。
### Device
为了支持一个硬件/软件设备，我们需要创建一个Device类，一个Device通常代表其指向一个硬件设备，但同时创建的多个Device也可能可以指向同一个硬件设备，这取决于您的平台要求，同时创建多个Device是被允许的。
### Stream
现代流处理器设备通常是将需要执行的计算积攒下并集中提交到硬件，这会带来更高的执行效率并允许LC对任务进行调度优化，因此我们引入Stream概念，这可以用类似的伪代码表达逻辑：<br>
// 在stream中提交a, b, c三个任务<br>
stream.dispatch(a)<br>
stream.dispatch(b)<br>
stream.dispatch(c)<br>
// 此时任务并没有开始执行<br>
stream.execute()<br>
// 此时任务开始异步的执行<br>
stream.synchronize()<br>
// 当前线程在此语句时等待任务完成<br>
### Kernel & Callable
一个可以被调度的最小的计算单位称之为Kernel，这通常是由DSL编写的一个独立的程序，而其本体也是一个函数，类似于main函数，而Callable则相当于其他自定义的函数，而Kernel本身是不可以直接调用的，而是需要经过Device提供的编译方法，编译后生成Shader才可以给当前的Device使用
### Shader
由于不同设备间不能够通用Kernel的编译结果(类似于Windows平台的exe不能够在Linux平台运行)，我们必须储存一份Kernel编译后的结果Shader，使用伪代码表达此逻辑：<br>
// 定义一个Kernel<br>
int kernel (int a, int b) {<br>
    return a + b;<br>
}<br>
// 编译成Shader<br>
shader = device.compile(kernel);<br>
### 选择计算后端
LuisaCompute目前支持CUDA, DirectX-12, Metal后端，每一种后端都有平台的限制和性能差距，我们会在官方网站提供不同后端的表现测试结果作为参考。
### 选择语言前端
LuisaCompute目前支持Rust, Python, C++作为前端语言，我们会提供这些语言的案例。同时由于语言之间各有长短，因此我们可以同时使用多种语言用于开发，如Python拥有编译速度快，类型系统动态的优势，可以用于编写Kernel，而对性能要求较高的运行时代码，则可以使用C++/Rust编写。在文档中我们会介绍这类操作的流程。
## Python
### Hello world
在确保[安装](installation.html)步骤完成以后，我们就可以开始编写第一个程序了:

from luisa import *<br>

@func<br>
def write_texture(tex):<br>
    set_block_size(16, 16, 1)<br>
    index = dispatch_id().xy<br>
    uv = (float2(index) + 0.5) / float2(dispatch_size().xy)<br>
    tex.write(index, float4(uv, 1, 1))<br>

res = 512, 512<br>
init()<br>
tex = Texture2D(*res, 4, float)<br>
write_texture(tex, dispatch_size=(*res, 1))<br>

gui = GUI("Hello World", res)<br>
while gui.running():<br>
    gui.set_image(tex)<br>
    gui.show()

以上这一段代码可以绘制一个分辨率为512x512的渐变颜色的窗口:

![py_hello_world](IMAGE_DIR/py_hello_world.png)

