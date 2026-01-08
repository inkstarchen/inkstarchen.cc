调用`glBindVertexArray(VAO)`所调用的`glVertexAttribPointer`都是以当前绑定的`GL_ARRAY_BUFFER`为基础的.

!!! note "详细教程"
    详细教程请阅读[LearnOpenGL CN | 实例化](https://learnopengl-cn.github.io/04%20Advanced%20OpenGL/10%20Instancing/)

GPU同时批量渲染顶点的速度是快的，但是假如你调用成千上万的渲染函数则会带来很大的性能开销，这是因为调用这部分的工作是CPU来完成的，它需要告诉GPU如何读取数据.

> 所以解决的想法就是：一次性把要的数据都发给GPU，然后利用这些数据去绘制多个物体，这就是实例化.

!!! info "OpenGL实例化"
    GLSL在顶点着色器中嵌入了一个内建变量: `gl_InstanceID`

    将渲染调用 `glDrawArrays`和`glDrawElements`替换成

    `glDrawArraysInstanced`和`glDrawElementsInstanced`

    > uniform变量传递的数据量有限，因此可以使用实例化数组来将变化的部分作为属性传递.

    ```c++
    glm::vec2 translations[100];
    ...
    unsigned int instanceVBO;
    glGenBuffers(1, &instanceVBO);
    glBindBuffer(GL_ARRAY_BUFFER, instanceVBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(glm::vec2) * 100, &translations[0], GL_STATIC_DRAW);
    glBindBuffer(GL_ARRAY_BUFFER, 0);
    glEnableVertexAttribArray(2);
    glBindBuffer(GL_ARRAY_BUFFER, instanceVBO);
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 2 * sizeof(float), (void*)0);
    glBindBuffer(GL_ARRAY_BUFFER, 0);   
    glVertexAttribDivisor(2, 1);
    ```

