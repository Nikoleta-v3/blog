---
layout: post
title:  "Resultants in SymPy"
date:   2018-06-03
comments: False
---

I recently have been doing some work on the memory size of strategies for the
Iterated Prisoner's Dilemma. This work has lead to the need of studying systems
of polynomials. In my search of a way of handling them I came across the
**resultant theory**. In this blog post I aim to give an introduction to resultant
theory and a demonstration of how we can use the Python package [SymPy](http://www.sympy.org/en/index.html)
to calculate the resultant of systems.

To start of let us familiarise ourselves with some mathematical definitions and
we will be doing so using SymPy for several examples.

{% highlight python %}
>>> import sympy as sym
{% endhighlight %}

Α **polynomial** is an expression consisting of variables and coefficients.
Using the following code we can define a polynomial \\(f\\) and \\(g\\) depended
on a variable \\(x\\).

{% highlight python %}
>>> x = sym.symbols('x')
>>> f = x ** 2 - 5 * x + 6
>>> g = x ** 2 - 3 * x + 2
{% endhighlight %}

A **system of polynomial equations** is a set of simultaneous equations.
Consider a system where,

\\[f(x) = 0\\]
\\[g(x) = 0\\]

We are interested in the values of \\(x\\) for which both equations \\(f\\) and \\(g\\)
simultaneously fall to zero. More superficially we are interested if values for
which all polynomials nullify exist. Though there are methods for solving such problem
here we consider the **resultant**. The resultant of two polynomials is a polynomial
expression of their coefficients, which is equal to zero if and only if the polynomials
have a common root.

Several resultant formulations exist within the literature. One of the most common
ones is the Sylvester's resultant which is defined as the determinant of the
[ Sylvester's matrix](http://mathworld.wolfram.com/SylvesterMatrix.html).Sylvester's
formulation is implemented within SymPy and it can easily be calculated using a
few lines of code.

{% highlight python %}
>>> from sympy.polys import subresultants_qq_zz
>>> matrix = subresultants_qq_zz.sylvester(f, g, x)
>>> matrix
Matrix([
[1, -5,  6, 0],
[0,  1, -5, 6],
[1, -3,  2, 0],
[0,  1, -3, 2]])
{% endhighlight %}

By calculating the determinant of the Sylvester's resultant we know that the
system has a common root. That is because the determinant is equal to 0.
The common root is for \\(x=2\\) which is trivial if we were to factorise
\\(f\\) and \\(g\\).

{% highlight python %}
>>> f.factor()
(x - 3)*(x - 2)
>>> g.factor()
(x - 2)*(x - 1)
{% endhighlight %}

The resultant can do more than just assure as that systems do have roots. For
example when we have system of two variables we solve for one and the second is
kept as a coefficient.Thus we can find the roots of the equations, that is why
the resultant is often refereed to as the **eliminator**. Let's consider
a new example.

{% highlight python %}
>>> y = sym.symbols('y')
>>> f = x ** 2 + x * y + 2 * x + y -1
>>> g = x ** 2 + 3 * x - y ** 2 + 2 * y - 1
>> matrix = subresultants_qq_zz.sylvester(f, g, y)
>> matrix
Matrix([
[x + 1, x**2 + 2*x - 1,              0],
[    0,          x + 1, x**2 + 2*x - 1],
[   -1,              2, x**2 + 3*x - 1]])
>>> matrix.det().factor()
-x*(x - 1)*(x + 3)
{% endhighlight %}

Thus in order for the system to have a common root \\(x \in \{-3, 0, 1\}\\).
We can now substitute for each value are retrieve the roots for \\(y\\).

But what if we had a more generic system. A system of \\(m\\) polynomials with
of \\(n\\) variables. Sylvester's formulation can not be applied to such systems,
for such systems we use **multivariate resultants**. An example of a multivariate
resultant is [Dixon's resultant](https://pdfs.semanticscholar.org/074d/652f97d07a2d5150764c2f448a6d98d3ab3b.pdf).
 Let us consider a final example.

{% highlight python %}
>>> from sympy.polys.multivariate_resultants import DixonResultant
>>> p = x + y
>>> q = x ** 2 + y ** 3
>>> h = x ** 2 + y
>>> matrix = DixonResultant(variables=[x, y], polynomials=[p, q, h])
>>> matrix.det()
0
{% endhighlight %}

Multivariate resultants have many advantages. If allow us to know if a large
system has roots. Moreover there are several ways the roots can be extract,
but we will not cover those, however this great paper does
[Comparison of various multivariate resultant formulations](https://dl.acm.org/citation.cfm?id=220370).

Multivariate resultants were not implemented within SymPy until recently. I am
happy to say that Dixon's and [Macaulay's resultant](https://projecteuclid.org/euclid.chmm/1263317746)
have been my first contribution to the library. Sympy is great project that continuously
has helped me with my research. I am very happy to have contributed to the project!