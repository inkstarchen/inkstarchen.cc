## 代码解释
```kotlin
class MainActivity : ComponentActivity() {
   override fun onCreate(savedInstanceState: Bundle?) {
       super.onCreate(savedInstanceState)
       setContent {
           GreetingCardTheme {
               // A surface container using the 'background' color from the theme
               Surface(
                   modifier = Modifier.fillMaxSize(),
                   color = MaterialTheme.colors.background
               ) {
                   Greeting("Android")
               }
           }
       }
   }
}
```

`onCreate()`函数时此应用的入口点，并会调用其他函数来构建UI。在Android应用中由`onCreate()`函数替代了`main()`在Kotlin程序中的作用.

`onCreate()`函数中的`setContent()`函数用于通过可组合函数定义布局.
任何标有`@Composable`注解的函数都可通过`setContent()`函数或其他可组合函数进行调用.

```kotlin
@Composable
fun Greeting(name: String) {//空格很重要
   Text(text = "Hello $name!")
}
```

`Greating()`函数是一种可组合函数,他会接受一些输入并生成屏幕上显示的内容。

```kotlin
@Preview(showBackground = true)
@Composable
fun DefaultPreview() {
   GreetingCardTheme {
       Greeting("Meghan")
   }
}
```

若想要使其成为预览函数，需要添加`@Preview`注解,`showBackground`参数可以用于添加背景

## 使用方法
### 更改背景颜色
若要为自我介绍设置不同的背景颜色，需要使用`Surface`将文本包围起来.`Surface`是一个容器，代表界面的一部分

1. 按下`Alt+Enter`(Windows)，选择**Surround with widget。**
2. 选择**Surround with Container**
3. 修改Box为你需要的容器
4. 设置Surface的color参数
5. 在顶部引入相应的color包androidx.compose.ui.graphics.Color

### 添加内边距
1. 映入相应的包
```kotlin
import androidx.compose.ui.unit.dp
import androidx.compose.foundation.layout.padding
```
2.使用`Modifier.padding()`函数