---
sider_position: 3
---
# 定积分(definite integral)

主要介绍一些公式和例题

:::note 

定积分相比不定积分计算更巧妙

:::

## 定积分的极限形式

$$
\int_a^b f(x)dx=\lim_{\lambda\rightarrow0}\sum_{i=1}^nf(\xi_i)\Delta x_i
$$

:::caution注意

但是他和$\xi_i$的分法和$x_i$的取法无关，仅与区间[a,b]和被积函数f(x)有关

:::
$$
\int_a^b f(x)dx=\lim_{\lambda\rightarrow0}\sum_{i=1}^nf(\xi_i)\Delta x_i=\lim_{n\rightarrow\infty}\frac{1}{n}\sum_{i=1}^nf(\frac{i}{n})
$$
这是一个非常常见的计算形式

> 例1：计算
> $$
> \lim_{n\rightarrow\infty}\frac{\sum_{k=1}^n\sqrt{k}}{\sum_{k=1}^n\sqrt{n+k}}
> $$
> 提示：提取$\frac1n$ ，答案是$\frac{1}{2\sqrt{2}-1}$

## 定积分存在条件

:::warning注意

下面列出的都是充分条件

:::

- f(x)在[a,b]上连续
- f(x)在[a,b]上有界，且只有有限个间断点
- f(x)在[a,b]上只有有限个第一类间断点（可去/跳跃间断点）

## 三角函数定积分公式

$$
\int_0^{\frac{\pi}{2}}sin^nxdx=\int_0^{\frac{\pi}{2}}cos^nxdx=
\left\{ 
\begin{align} 
&\frac{n-1}{n} · \frac{n-3}{n-2} ·\ \cdots\ 	·\frac12·\frac\pi2  \ \ \ &,n为正偶数\\
&\frac{n-1}{n} · \frac{n-3}{n-2} ·\ \cdots\ 	·\frac23\ \ \ &,n为大于1 的奇数
\end{align}
\right.
$$

---

$$
\int_0^\pi xf(sin\ x)dx=\frac\pi2 \int_0^\pi f(sin\ x)dx
$$

---

## 解题技巧

- 对称区间记得利用奇偶性化简
- 极限形式提取$\frac1n$
- 谨记三角函数公式

