## 整数类型
当初始化一个没有显式指定类型的变量时，编译器会自动推断为自`Int`起足以表示该值的最小类型.

```
val one = 1 //Int
val threeBillion = 3000000000 // Long
val oneLong = 1L // Long
val oneByte: Byte = 1
```

## 浮点类型
对于以小数初始化的变量。编译器会推断为`Double`类型:
```
val pi = 3.14 // Double
// val one: Double = 1 // 错误：类型不匹配
val oneDouble = 1.0 // Double
```
显式指定为`Float`类型,添加`f`或`F`后缀。
```
val e = 2.7182818284 // Double
val eFloat = 2.7182818284f // Float,实际值为 2.7182817
```
!!! info
	Kotlin中的数字没有隐式拓宽转换。例如，具有`Double`参数的函数只能对`Double`值调用，而不能对`Float`、`Int`或者其他数字值调用：

	```
    fun main(){
	    fun printDouble(d: Double) { print(d) }

        val i = 1
        val d = 1.0
        val f = 1.0f

        printDouble(d)
    //  printDouble(i) // 错误：类型不匹配
    //  printDouble(f) // 错误：类型不匹配
    }
    ```
## 数字字面常量

- 十进制：`123`
	- Long类型用大写`L`标记：`123L`
- 十六进制：`0x0F`
- 二进制：`0b00001011`
> Kotlin 不支持八进制

浮点数常规表示方法：
- 默认double：`123.5`、`123.5e10`
- Float用`f`或者`F`标记`123.5.f`

可以用下划线使数字常量更易读：
```
val oneMillion = 1_000_000
val creditCardNumber = 1234_5678_90123_3456L
val socialSecurityNumber = 999_99_9999L
val hexBytes = 0xFF_EC_DE_5E
val bytes = 0b11010010_01101001_10010100_10010010
```

## 显式数字转换

较小的类型不能隐式转换成较大的类型。
```
val b:Byte = 1 //字面值会静态坚持
// val i: Int = b // 错误
val i1: Int = b.toInt()
```
算术运算会有重载做适当转换，例如：
```
val l = 1L + 3 // Long + Int => long
```

## 整数除法
需要返回浮点类型的(将其中一个参数显式转换成浮点类型)
```
fun main() {
	val x = 5 / 2.toDouble()
	println(x == 2L)
}
```
位运算列表:
- `shl(bits)` -有符号左移
- `shr(bits)` -有符号右移
- `ushr(bits)`-无符号右移
- `and(bits)`- 位与
- `or(bits)`-位或
- `xor(bits)`- 位异或
- `inv()`-位非

## 字符串
通常用双引号（`"`）
```
val str = "abcd 123"
```
可以用索引运算符访问：`s[i]`，也可以使用`for`循环遍历:
```
fun main(){
	val str = "acdf"
	for(c in str){
		println(c)
	}
}
```