

## 函数

### 计算位宽的函数clog2
求2的对数log2(8) = 2

## 状态的改变
```verilog
typedef enum logic [1:0] {IDLE, WORK, FINAL} fsm_state;
// 将10\01\00三个状态分别定义为IDLE,WORK,FILNAL
```

# 阻塞赋值和非阻塞赋值
wire变量只能被 = 赋值
reg变量在always块中可以被=和<=两个运算符赋值,

```verilog
always@(posedge clk)begin
    a = b;//阻塞赋值
end

always@(posedge clk)begin
    a <= b;//非阻塞赋值
end
```
## 1 一个例子
```verilog
reg a;
reg b;
reg c;
always@(posedge clk)begin
    c <= b;
    a <= c;
    b <= a;
end
always@(posedge clk)begin
    c = b;
    a = c;
    b = a;
end
```
使用非阻塞赋值语句`<=`左侧是会被赋值的寄存器，右侧是各个寄存器和线路的输出构造的组合电路。同一个always块内的所有赋值语句是被同时执行的.
上述代码的功能就是寄存器 a、b、c 在下个时钟周期分别载入寄存器 c、a、b 的值。
![](../../images/Pasted%20image%2020240420140753.png)

使用阻塞赋值语句=，赋值语句左侧的 reg 变量并不一定会被建模为寄存器，而是如下图。这三句赋值语句是有先后关系的，首先变量 c 获得变量 b 的值，然后变量 a 获得变量 c 的值也就是原来 b 的值，最后 b 后的变量  的值也就是最开始变量 b 的值，形成环路。最后只有这个环路的最终结果 b 会被建模为寄存器，其他的 a、c 则会被建模为 wire。
![](../../images/Pasted%20image%2020240420141101.png)

## 阻塞赋值的电路
### 重命名
不同于非阻塞语句一个寄存器只能被赋值一次，阻塞语句的寄存器可以被多次赋值。例如：
```verilog
reg tmp;
wire [1:0] data;
always@(posedge clk)begin
    tmp = 1'b0;
    tmp = tmp + data[0];
    tmp = tmp + data[1];
    sum = tmp;
end
```
虽然看起来 tmp 寄存器被赋值了很多次，但是每个被赋值的 tmp 是不同的变量，他们只是暂时共用了 tmp 这个名字，我们可以将被先后赋值的 tmp 重命名为 tmp、tmp0、tmp1，则可以得到如下的 Verilog 语句。实际上变量的名字不是那么重要，它代表的数据发生了变化，它就是一个新的数据：

```verilog
reg tmp;
wire [1:0] data;
always@(posedge clk)begin
    tmp = 1'b0;
    tmp0 = tmp + data[0];
    tmp1 = tmp0 + data[1];
    sum = tmp1;
end
```

重命名的方法可以如下：

- 当一个变量被赋值，且在之前已经被赋值过或者充到源操作数之后，该变量分配一个新的名字
- 后续使用这个变量做源操作数的时候，用该变量最新被分配的名字做源操作数

### 无环图
always 块内部的阻塞赋值关系可以非常复杂，但无论多么复杂都是可以表示为一个数据流图的，数据流图是有向无环图，那些最终那些出度为 0 的节点才会被最终生成寄存器，而那些中间赋值的变量值会被生成 wire。例如：

```verilog
always@(posedge clk)begin
    a = b + c;
    d = a + c;
    e = a + b;
end
```

![](../../images/Pasted%20image%2020240420141608.png)
所以最后生成电路的时候，e 和 f 会生成寄存器，但是 a 只会得到线路 wire

### 中间变量的reg

一下若干种情况中间变量会变为寄存器，即这个中间变量的源操作数的值和自己有关，它的电路成环，如：

```verilog
wire d;
reg a,b,c;

assign d = a;

always@(posedge clk) begin
    a = b + d;
    b = a;
    c = b;
end
```
![](../../images/Pasted%20image%2020240420141720.png)因为线路 a 依赖于中间变量 a 的值，所以 a 不能被综合为 wire 不然会产生环路，因此这里 a 的线路结果会被保存进入寄存器 a，换句话说变量 a 确实会被综合为寄存器，但是变量 b 得到的不是寄存器 a 的输出，而是和 a 一样的输入。

b 也一样，b 如果被综合为 wire 也会有环路问题，所以 b 被综合为寄存器，变量 c 载入的值是寄存器 b 得输入而不是输出。

## 阻塞赋值的优点
### 设计简单
阻塞赋值的执行方式和 C 语言的执行方式高度类似，如果有一段 C 代码，可以将它几乎不加修改的用阻塞赋值的方式实现，例如下面这段代码：
```C
b = b + a;
if(b < 0){
    b = b - a;
}
```
就可以直接用如下阻塞语句实现
```verilog
always@(posedge clk)begin
    b = b + a;
    if(b < 0) begin
        b = b - a;
    end 
end
```

### 实现灵活
对于复杂的中间过程的计算可以用定义大量中间变量进行暂存，甚至可以搭配 for、if 等高级语法使用，非常灵活方便，有很好的可读性。例如下面这段代码：
```verilog
always@(posedge clk)begin
    if(multiplier[0])begin
        result =result + multiplicant;
    end
    result = result >> 1;
end
```
如果使用阻塞赋值的方式实现的话，要么将多条表达式用嵌套的形式改为一条表达式，但是这种表达式可读性比较差，中间过程语义不明，且容易写错。
```verilog
always@(posedge clk)begin
    result <= (multiplier[0]?result + multiplicant:result) >> 1;
end
```

或者可以将复杂的组合电路运算拿到 always 块外面用 assign 语法加以分布实现。这样在可读性上虽然好了很多，但是一个完整的逻辑会被拆分为两块代码，还是有一定的间离。
```verilog
wire [31:0] add_one;
wire [31:0] shift;
assign add_one = multiplier[0]?result + multiplicant:result;
assign shift = add_one >> 1;

always@(posedge clk)begin
    result = shift;
end
```

## 阻塞赋值的缺点
### 忽略电路实现
因为阻塞赋值可以实现从 C 语言到 Verilog 的快速转换，所以容易出现对代码不加修改的直接照抄。不同于 C 语言每行代码较为廉价，多一条 C 语句只会导致 CPU 多执行几个周期，对于 Verilog 而言多一条语句可能就会多一个大型电路。例如上面我们照搬的例子，可以看到需要一套加法器和一条减法器。

```verilog
always@(posedge clk)begin
    b = b + a;
    if(b < 0)begin
        b = b -a;
    end
end
```
但我们只要稍作修改就可以只用一个加法器，而节约下一个减法器。语法简洁了之后，编程者容易忽略底层的硬件开销和电路实现，从而导致浪费，就像 Java 的开销远大于 C 一样。
```verilog
assign result = b + a;
always@(posedge clk)begin
    if(result >= 0)begin
        b = result;
    end
end
```
上面的例子只会导致电路的浪费，但是下面的例子会导致电路结构发生巨大的变化。我们以乘法器为例，在 lab3-3 的教程中我们提到将每次迭代当作一个状态，然后将这个状态迭代 32 次。但是部分同学会照抄伪代码得到如下的 Verilog：
```verilog
always@(posedge clk)begin
    for(i=0;i<32;i++)begin
        if(multiplier[0])begin
            product = product + multiplicant;
        end
        multiplier = multiplier >> 1;
        multiplicant = multiplicant << 1;
    end
end
```
该电路（当然还需要做调整才可以真的执行）确实可以实现乘法器的功能，但是实际上 for 循环会把电路展开为 32 份，也就是每次迭代执的加法器、选择器、移位器会被重复 32 次。最后我们不是一组电路 32 次迭代得到最终结果，而是 32 组电路串联然后一个周期得到最终结果。

```verilog
always@(posedge clk)begin
    if(multiplier[0])begin
        product = product + multiplicant;
    end
    multiplier = multiplier >> 1;
    multiplicant = multiplicant << 1;

    ...// 重复32 次

    if(multiplier[0])begin
        product = product + multiplicant;
    end
    multiplier = multiplier >>1;
    multiplicant = multiplicant << 1;
end
```

### 行为未定义
中间变量被外部调用的情况不确定。例如下面这个例子。因为 b 所在的数据成环路，所以 b 会成为一个寄存器，但是寄存器的值有输出的值、有输入的值，它们都叫做 b。那么对于 a 和 e 而言他们输入的数据 b 是寄存器的输出还是输入呢？这个是不确定的，有的模拟器认为是输入、有的认为是输出，所以在 always 块外部使用中间变量会导致大量的不确定问题。

```verilog
assign a = b;
always@(posedge clk)begin
    b = a + 1;
    c = b + 1;
end
always@(posedge clk)begin
    e = b;
end
```

## 如何正确使用阻塞赋值
### 构造组合电路
常见的选择是`always@(*)`搭配=构建组合电路，`always@(posedge clk)`搭配`<=`构建时序电路。

因为我们已经介绍了 always_ff 的写法，所以可以 always_ff 搭配 = 进行编程。

### 构造仿真激励

我们可以看到阻塞赋值的语法是按照指令顺序从前往后进行赋值的，我们在`initial`块对仿真输入做激励的时候就是用的阻塞赋值的语法。实际上`initial`也可以和`always`一样使用 for 语句和 if 语句，来实现复杂的激励功能。

### 不使用中间变量
### 使用logic

# reg 与时序电路
## 寄存器
```verilog 
reg a; //定义一个寄存器 a
reg [7:0] b; //定义寄存器组 b[0]-b[7]
reg [7:0] b [11:0];// 定义寄存器二维数组
reg [7:0] b [11:0]...[11:0];// 定义寄存器高维数组
// 数组长度、排列顺序、索引等和wire语法一致
```
## 触发器
Verilog的触发器可以简单地认为是D触发器.
*简单的示例*
```verilog
wire data;
reg a;
reg b;
always@(posedge clk)begin
//always at positive edge of clk
	a <= data;
	// 寄存器 a 载入线路data的数据
end

always@(negedge clk)begin
//always at negative edge of clk
	b <= a;
	// 寄存器载入线路 a 的数据
end
```
## 时序约束
当寄存器a和寄存器b之间的线路过长或门电路过多时,导致信号无法在下降沿之前到达.导致信号无法正确传输.

估算手段：电路材料、电线长度、中间门电路特性等

由于a是上升沿触发，b是下降沿触发，所以从a数据变化到寄存器b载入新的电平的时间窗口仅半个时钟周期.

常用的解决办法:
1. 布线优化：线路布线的时候将寄存器 a 和寄存器 b 的位置放置的足够近，减少之间电路的长度，从而降低时延，满足时序约束。Vivado 的 implementation 会尽可能的进行布线优化。
2. 逻辑优化：简化寄存器 a 和寄存器 b 之间的门电路逻辑，使得线路的时延减少。Vivado 的 implementation 会尽可能的进行逻辑优化。
3. 降低频率：将时钟频率降低，使得触发沿之间的时间间隔增大，但是整体电路的工作效率会变差
4. 统一时钟沿：寄存器 a 用上升沿触发，寄存器 b 用下降沿触发，其时间窗口只有半个周期，但是如果统一用上升沿或者下降沿就会有一个周期，时间间隔增大。虽然局部的工作效率会有所降低，但是整体的工作效率基本不受影响，所以请大家如无必要，统一时钟沿设计电路。
5. 其他：...

## 使能寄存器
有些寄存器会有一个使能引脚CE，只有当CE=1的时候寄存器才会载入输入data的值。

```verilog
always@(posedge clk)begin
	if(wen)begin
		a <= data;
	end
end
```
??? tip "注意"
	使用`always@(*)`综合得到的电路时用wire搭建的,只是借用了reg的always块语法.

	但是`always@(posedge clk)`的得到的电路使用真的寄存器搭建，不会有环路问题.

## 寄存器初始化
### 异步初始化
```verilog
reg a;
// 高电平异步复位寄存器
always@(posedge clk or posedge rst)begin
//always at positive edge of clk 
//or at positive edge edge of rst
	if(rst)begin
		a <= INTIAL_VALUE;
	end else if(wen)begin
		a <= data;
	end
end

reg a;
// 低电平异步复位寄存器
always@(posedge clk or negedge rstn)begin
//always at positive edge of clk 
//or at negative edge edge of rst
	if(~rst)begin
		a <= INTIAL_VALUE;
	end else if(wen)begin
		a <= data;
	end
end
```

FPGA内置的Flip Flop是异步高电平复位的带使能信号的上升沿触发器

### 同步初始化
```verilog
reg a;
//高电平同步复位寄存器
always@(posedge clk)begin
// always at positive edge of clk
	if(rst)begin
		a<= INTIAL_VALUE;
	end else if(wen)begin
		a <= data;
	end
end

reg a;
//低电平同步复位寄存器
always@(posedge clk)begin
	if(~rstn)begin
		a <= INTIAL_VALUE;
	end else if(wen)begin
		a <= data;
	end
end
```

同步电路没有显式的异步复位引脚，它的输入 data 前有一个多路选择器，然后用 rst/~rstn 作为选择子选择载入 INITIAL_VALUE 的结果还是 data 的结果。而 ~rstn|wen 则会被作为寄存器 CE 的输入。

所以不同于异步复位只要 rst=1/rstn=0，寄存器就可以复位得到初始化值；同步复位只有在时钟边沿到来的时候才会复位得到初始化的值。

### FPGA 初始化
FPGA 的复位信号 rstn 由 FPGA 芯片的 C12 引脚引入.当 vivado 将 bitstream 下载到 FPGA 板之后，rstn 信号会先保持一段时间的 0，使得所有的寄存器可以被充分初始化，然后 rstn 信号变为 1 且一直保持不变，这样所有的寄存器就从初始化阶段进入工作阶段，开始载入数据。

FPGA 进入工作阶段后，我们也可以按开发板的 reset 按钮，让 rstn 再次输入 0，重新复位所有寄存器的值。

```verilog
 set_property -dict {PACKAGE_PIN C12 IOSTANDARD LVCMOS33} [get_ports rstn]
```

因为 FPGA 板的 rstn 在初始化阶段是低电平，所以该信号只能直接用于复位低电平复位寄存器。对于高电平复位的寄存器可以将 rstn 取反，然后用 rst 作为复位信号。


```verilog
wire rst;
assign rst = ~rstn;
```

### 触发信号

实际上 reg 的触发边沿和复位电平是由寄存器本身的电气特性决定的，比如 FPGA 的 FF 一般是上升沿触发和高电平复位。但是我们可以通过给 clk 和 rstn 经过非门在连接到 reg 的方式实现所谓的下降沿触发和低电平复位（将非门和 reg 看成一个整体的话）

#### 问题一：多时钟触发
```verilog
always@(posedge clk1 or posedge clk2)
```
reg只有一个时钟输入端口,所以综合时无法实现.

#### 问题二：多边沿触发
```verilog
always@(clock)
always@(a or b or c)//电平翻转就触发
```
不存在多边沿触发，不能综合得到时序电路。

```verilog
reg d;
always@(a or b or c)begin
	if(a) d <= c;
	else d <= b;
end
```
可以综合得到组合电路.得到了一个二选一多路选择器.

!!!注意if-else、case-default搭配使用，不然会有latch warning。

!!! 仅在always 触发的信号是always块内部输出依赖的所有输入时,这个写法才有意义。

```verilog
reg d;
always@(*)begin
	if(a) d<= c;
	else d <= b;
end
```
任何信号变化就触发always块，它无论如何都是在更改电平的状态。

#### 问题三：多always块触发
```verilog
always@(posedge clk)begin
	d <= a;
end
always@(negedge clk)begin
	d <= b;
end
```
仿真允许reg在不同的always块被不同的时钟沿信号触发，但是在综合的时候一个reg不能被两个时钟沿触发.

```verilog
always@(posedge clk)begin
	if(c) d <= a;
end
always@(posedge clk)begin
	if(!c) d <= b;
end
```
仿真无法通过:wire不能被两个输出同时输入，reg也不能在两个always块内被赋值，会引起multi-driven错误.

#### 问题四：异步触发
```verilog
reg [1:0] d;
wire problem;
reg cond1;
reg cond2;
assign problem = cond1 & cond 2;
always@(posedge problem)begin
	d <= d + 2'b1;
end
```
##### 数据竞争
考虑下面这个情形
```verilog
initial begin
	cond1=1'b0;cond2=1'b1;
	#5;
	cond1=1'b1;cond2=1'b0;
end
```
在真实电路综合时，会因为时间延迟，造成，数据问题.

##### 转换成同步电路
本质上是，传播不同时使得电路处于不稳定状态.因此我们很多时候采用和应用逻辑无关的 clk 方波信号进行触发，确保上升沿来临的时候电路的电平已经全部传播完毕并且保持稳定：

```verilog
reg [1:0] d;
wire problem;
reg cond1;
reg cond2;
assign problem = cond1 & cond2;

always@(posedge clk)begin
	if(problem) d <= d + 2'b1;
end
```
如果只希望 problem 的上升沿使得 d 寄存器组加 1，则可以先试用 PosSample 上升沿采样电路对 problem 进行采样。参见常用模块 - 边沿采样。

### logic

SystemVerilog 提供的新变量类型。logic 类型的变量既可以用在`assign、always@(*)`等组合电路，也可以用在`always@(posedge clk)`等时序电路：如果用在`assign、always@(*)`等组合电路设计中，它的行为就是和 wire 类型保持一致的，最后会被综合得到 wire；如果用在`always@(posedge clk)`等时序电路设计中，它的行为就是和 reg 类型保持一致的，最后会被综合得到 reg 类型。

所以大家在编程的时候可以用 logic 全面替代 wire/reg 变量，然后让 SystemVerilog 自己根据场景确定 logic 的实际类型，方便编程者将更多的精力放在逻辑设计本身，而进一步忽略电路组件的细节。

```verilog
logic [1:0] d;
logic problem;
logic cond1;
logic cond2;
assign problem = cond1 & cond2; // problem 自动识别为wire
always@(posedge clk)begin
	if(problem) d <= d + 2'b1; // d 自动识别为 reg
end
```
其实对于仿真本身而言，wire/reg 都只是一个 C 语言变量而已，所以全部取代为 logic 完全没有问题。wire 和 reg 的区别仅仅在综合成电路、具有电气特性之后才有意义。

### 扩展always
为此 SystemVerilog 扩展了 always 语法，为时序电路、组合电路、锁存器电路分别提供了 always_ff、always_comb、always_latch 三个关键字。

#### always_comb
你还在为 always@(\*) 语法的看起来在做 reg 编程实际上在做 wire 编程苦恼吗？always_comb 关键字就解决了这个问题，它说明一下的行为描述就是直接被生成组合电路的，内部被赋值的 logic 都会被综合为 wire，然后会对 if-else 缺失、case-default 缺失等问题进行检查。大家可以用`logic+always_comb`语法全面替代`reg+always@(*)`语法，这样在享受 always 便利的行为描述语法的同时，也可以享受编译器的电路问题检查。

```verilog
//修改前
reg d;
always@(*)begin
	if(a) d <= c;
	else d <= b;
end

//修改后
logic d;
always_ff begin
	if(a) d <= c;
	else d <= b;
end

//修改前
reg d;
always@(*)begin
	if(a) d <= c;// 可能得到锁存器latch电路
end

//修改后
logic d;
always_ff begin
	if(a) d <= c; //没有else分支，给出报错
end
```

#### always_ff
always_ff 语法说明这个 always 块是专门用于生成 ff 电路，内部被赋值的 logic 都会被综合为 reg。语法上只需要将 always 替换为 always_ff 即可。

```verilog
always_ff@(posedge clk)begin
	if(problem) d <= d + 2'b1;
end
```

#### always_latch
always_latch 语法说明这个 always 块是专门用于生成 latch 电路的，这是很不常用、很危险的电路，大家如无必要不要尝试使用。原来的 always@(\*) 如果 if-else、case-default 完整就是得到组合电路，有所缺失就是得到 latch 电路；always_latch 则是会严格检查语法，确保存在 if-else、case-default 缺失。

```verilog
//修改前
reg d;
always@(*)begin
	if(a) d <= c;
end

//修改后
logic d;
always_latch begin
	if(a) d <= c;
end
```

## 常用模块介绍
### 分频器
```verilog
module ClkDic(// repo/sys-project/lab3-1/synClkDic.v
	input clk,
	inpuut rstn,
	output reg [31:0] clk_div
);

	always@(posedge clk)begin
		if(~rstn)clk_div<=32'b0;
		else clk_div<=clk_div+32'b1;
	end

endmodule
```

`clk_div[0]` 每个时钟周期翻转一次，所以它的时钟频率是 clk 的一半；`clk_div[1]` 每两个时钟周期翻转一次，时钟频率是 clk 的四分之一；`clk_div[2]` 到 `clk_div[31]` 依次减半。

于是我们可以用分频器得到不同频率的时钟。我们 lab1-2 的七段数码管动态刷新所使用的时钟要求频率比较低，因此使用 `clk_div[10]` 以满足时钟频率的要求。

### 按键去抖器

```verilog
module Debouncer (// repo/sys-project/lab3-1/syn/Debouncer.v
	input wire clk,//100Mhz 2^10
	input wire btn,,
	output wire btn_dbnc
);

	reg [7:0] shift = 0;

	always@(posedge clk) begin
		shift <= {shift[6:0],btn};
	end

	assign btn_dbnc = &shift;
endmodule
```

可以看到如果连续 8 个周期的时钟输入是高电平，则输出高电平；这里的时钟使用 100 KHz，时钟周期为 10 us，也就是连续 80us 都是高电平，则认为按钮输入高电平，这样就可以将按钮按下和松开时抖动产生的毛刺过滤掉。

### 边沿采样

```verilog
module PosSample (//repo/sys-project/lab3-1/syn/Debouncer.v
	input clk,
	input data,
	output sample
);

	reg old_data;
	always@(posedge clk)begin
		old_data <= data;
	end

	assign sample = ~old_data & data;

endmodule
```
如果上一个周期采样的是低电平而这个周期采样的是高电平，则发现了一个上升沿，输出高电平。如果之后一直是持续高电平或者低电平则不响应，输出低电平。同理还可以实现下降沿采样和翻转采样。