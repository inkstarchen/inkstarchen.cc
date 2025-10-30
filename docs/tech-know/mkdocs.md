## 基础设置

!!! note "自定义设置"
    参考[material-Getting_started-Customization]

[material-Getting_started-Customization]:https://squidfunk.github.io/mkdocs-material/customization/?h=

## 高级效果

### 文字高亮标记

```yaml title="mkdocs.yml"
markdown_extensions:
    - pymdownx.mark # (1)
```

1.  :man_raising_hand: I'm a code annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be written in Markdown.

### 代码块设置

!!! note "代码块设置"
    参考[Material-Reference-Codeblocks]

[Material-Reference-Codeblocks]:https://squidfunk.github.io/mkdocs-material/reference/code-blocks/


#### 示例代码

```py title="code block"
    ``` py title="test.py" linenums="1" hl_lines="2-3"
    def hello():
        print("Hello World!") # (1)
        return
    ```
    1. :man_raising_hand: Code annotation!
```

#### 实际效果

```py title="test.py" linenums="1" hl_lines="2-3"
def hello():
    print("Hello World!") # (1)
    return
```

1.  :man_raising_hand: Code annotation!

### Icons and Emojis

!!! note "图标和表情设置"
    参考[Material-Reference-Icons-and-emojis]

[Material-Reference-Icons-and-emojis]:https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/


- 查询后直接使用

#### 示例代码

```yaml title="code block"
:smile:
```

#### 实际效果

:smile:

### Grids

!!! note "网格设置"
    参考[Material-Reference-Grids]

[Material-Reference-Grids]:https://squidfunk.github.io/mkdocs-material/reference/grids/#using-generic-grids-unordered-list

#### 列表形式

##### 代码示例（纯列表）

```html title="code block"
<div class="grid cards" markdown>

- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>
```

##### 实际效果（纯列表）

<div class="grid cards" markdown>

- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>

##### 列表形式（增加排版）

```html title="code block"
<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Set up in 5 minutes__

    ---

    Install [`mkdocs-material`](#) with [`pip`](#) and get up
    and running in minutes

    [:octicons-arrow-right-24: Getting started](#)

-   :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Reference](#)

-   :material-format-font:{ .lg .middle } __Made to measure__

    ---

    Change the colors, fonts, language, icons, logo and more with a few lines

    [:octicons-arrow-right-24: Customization](#)

-   :material-scale-balance:{ .lg .middle } __Open Source, MIT__

    ---

    Material for MkDocs is licensed under MIT and available on [GitHub]

    [:octicons-arrow-right-24: License](#)

</div>
```

##### 实际效果（增加排版）
<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Set up in 5 minutes__

    ---

    Install [`mkdocs-material`](#) with [`pip`](#) and get up
    and running in minutes

    [:octicons-arrow-right-24: Getting started](#)

-   :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Reference](#)

-   :material-format-font:{ .lg .middle } __Made to measure__

    ---

    Change the colors, fonts, language, icons, logo and more with a few lines

    [:octicons-arrow-right-24: Customization](#)

-   :material-scale-balance:{ .lg .middle } __Open Source, MIT__

    ---

    Material for MkDocs is licensed under MIT and available on [GitHub]

    [:octicons-arrow-right-24: License](#)

</div>

#### 块形式

##### 示例代码
```html title="code block"
<div class="grid" markdown>

:fontawesome-brands-html5: __HTML__ for content and structure
{ .card }

:fontawesome-brands-js: __JavaScript__ for interactivity
{ .card }

:fontawesome-brands-css3: __CSS__ for text running out of boxes
{ .card }

> :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>
```

##### 实际效果
<div class="grid" markdown>

:fontawesome-brands-html5: __HTML__ for content and structure
{ .card }

> :fontawesome-brands-js: __JavaScript__ for interactivity


:fontawesome-brands-css3: __CSS__ for text running out of boxes
{ .card }

> :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>

#### 通用形式

##### 示例代码

```html title="code block"
<div class="grid" markdown>

=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci

    ``` title="Content tabs"
    === "Unordered list"

        * Sed sagittis eleifend rutrum
        * Donec vitae suscipit est
        * Nulla tempor lobortis orci

    === "Ordered list"

        1. Sed sagittis eleifend rutrum
        2. Donec vitae suscipit est
        3. Nulla tempor lobortis orci
    ```

</div>
```

##### 实际效果

<div class="grid" markdown>

=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci

``` title="Content tabs"
=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci
```

-   :material-scale-balance:{ .lg .middle } __Open Source, MIT__

    ---

    Material for MkDocs is licensed under MIT and available on [GitHub]

    [:octicons-arrow-right-24: License](#)

``` title="Content tabs"
-   :material-scale-balance:{ .lg .middle } __Open Source, MIT__

    ---

    Material for MkDocs is licensed under MIT and available on [GitHub]

    [:octicons-arrow-right-24: License](#)
```

</div>


### Admonitions
!!! note "警告设置"
    参考[Material-Reference-Admonitions]

[Material-Reference-Admonitions]:https://squidfunk.github.io/mkdocs-material/reference/admonitions/#removing-the-title

## 技巧

### 超链接插入

#### 代码
```
[我是一个链接] #在需要的位置放置
[我是一个链接]:https://squidfunk.github.io/mkdocs-material/ #在任意位置放置

```

#### 效果
[我是一个链接] 

[我是一个链接]:https://squidfunk.github.io/mkdocs-material/

### 跨文档连接

```markdown title="doc1.md"
test {#custom-id}
```

```markdown title="doc2.md"
[link](pathto/doc1.md#custom-id)
```
