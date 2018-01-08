---
layout: post
title:  "The power of memory."
date:   2018-01-05
comments: true
---

In interactions both social and biological how does cooperation emerges? Why
cells sacrifice themselves and why humans behave in an altruist manner? In
game theory, the [prisoner's dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma)
has been used for decades to explain the emergence of altruistic behaviour.

The prisoner's dilemma is a two players non cooperative game. Both players can
choose to **Cooperate** or **Defect** with each other. Both players are better of choosing
Cooperation (3), even so here is always a temptation for a player to Defect (5).
This is described by the game matrix given below,

<p align="center">
  <img src="{{site.baseurl}}/assets/images/matrix.png" style='height: 20%; width: 40%; object-fit: contain'>
</p>

In the 1980's, a political scientist called Robert Axelrod carried out a
[computer tournament](https://science.sciencemag.org/content/211/4489/1390)
of the iterated prisoner's dilemma. In the iterated version of the game the players
interact for an infinite number of time and they have access to the full history
of the matches. Axelrod's results showed that defecting strategies performed
very poorly in the tournament. On the other hand, strategies that begun a match
with a cooperation and where forgiving ranked on the top. Axelrod's findings
were from the earliest that explain how cooperation can be evolutionarily advantageous.

In 2012 [Press and Dyson](https://www.pnas.org/content/109/26/10409.abstract)
studied the iterated prisoner's dilemma in a similar manner as Axelrod. Although
their results were different. They suggested that the best performing strategies
strategies were selfish ones that led to extortion, not cooperation. These
strategies by Press and Dyson are called **zero determinant strategies**.

They stated that in a two players interaction, a player with the shortest memory
in effect sets the rules of the game. A player with a good memory-one strategy
can force the game to be played, effectively, as memory-one. Thus a
memory one player cannot be undone by another player's longer-memory strategy.
Thus, in the iterated prisoner's dilemma, memory is not advantageous.

The purpose of one of my undergoing projects is to consider a given memory one
strategy \\(q=(q_1, q_2, q_3, q_4)\\), (in a similar fashion to Press and Dyson).
However whilst Press and Dyson found a way for the opponent of \\(p\\) to manipulate
\\(q\\), my work will considers an optimisation approach to identify the best
response \\(p^*=(p_1, p_2, p_3, p_4)\\) to a strategy \\(q\\). In essence answering
the question:

**What is the best memory one strategy against a given other memory one strategy?**

<p align="center">
  <img src="{{site.baseurl}}/assets/images/against_one_player.png" style='height: 20%; width: 30%; object-fit: contain'>
</p>

But what are memory one strategies? Memory one strategies consider one the previous
turn in order to make a decision on their next action. Memory one strategies were
introduced by [M. Nowak in 1990](https://rd.springer.com/article/10.1007%2FBF00049570).

Depending on the simultaneous moves of two players the states of the game,
when only the previous round is considered, a state where both cooperated,
both defected or either of them defected. These states are represented as
\\(CC, CD, DC, DD\\). A memory one strategy can be written as the probability of
cooperating after each of these states. Thus as a vector of four probabilities
\\(p\\) where \\(p = (p_1, p_2, p_3, p_4) \in\mathbb{R}_{[0,1]}^{4}\\).

The above formulation offered a new framework of studying strategies. Consider
that two memory one strategies are in a game of the prisoner's dilemma. Their
interaction can be written as the following markov chain,

\\[M =
\begin{bmatrix}
    p_{1} q_{1} & p_{1} (- q_{1} + 1) & q_{1} (- p_{1} + 1) & (- p_{1} + 1) (- q_{1} + 1)
    \\\
    p_{2} q_{3} & p_{2} (- q_{3} + 1) & q_{3} (- p_{2} + 1) & (- p_{2} + 1) (- q_{3} + 1)
    \\\
    p_{3} q_{2} & p_{3} (- q_{2} + 1) & q_{2} (- p_{3} + 1) & (- p_{3} + 1) (- q_{2} + 1)
    \\\
    p_{4} q_{4} & p_{4} (- q_{4} + 1) & q_{4} (- p_{4} + 1) & (- p_{4} + 1) (- q_{4} + 1)
    \\\
\end{bmatrix}
\\]

where the opponent is denoted as \\(q=(q_1, q_2, q_3, q_4) \in\mathbb{R}_{[0,1]}^{4}\\).
The expected state that two opponents will end up can be estimated by calculating
the steady states of the markov chain.

The players are assumed to move from each state until the system reaches a
state steady. There after, the scores for each player can be retrieved by
multiplying the steady states with the payoffs matrix. Thus, the utility for
player \\(p\\) against \\(q\\), denoted as \\(u_q(p)\\).

The earliest result of this work was proving that the utility \\(u_q(p)\\) can be
written in compact way, which is given by equation,
is defined by equation.

\\[u_q(p) = \frac{\frac{1}{2}p^TQ + c^Tp + a}
            {\frac{1}{2}p^T\bar{Q} + \bar{c}^Tp + \bar{a}}\\]

where \\(Q, \bar{Q}\\) are matrices of \\(4 \times 4\\), and \\(c, \bar{c}\\) are
\\(4 \times 1\\) vectors  defined with the transition probabilities of the
opponent's transition probabilities \\(q_1, q_2, q_3, q_4\\).

Thus in order to answer the questions: `What is the best memory one strategy against
a given other memory one strategy?` we need to consider the following optimization
problem:

\\[ max_{q}: u_q(p) \\]
\\[st: \\ p \in\mathbb{R}_{[0,1]}^{4}\\]

Note that is a maximisation problem over 16 variables. Thus as a first step in order
get a better understanding of the problem I am going to consider a constrain
version of the problem. More specifically I have looked at a set of memory one
strategies where the transition probabilities of each state are the same, are
called **purely random strategies**.

\\[ \max_p: u_q(p) = \frac{n_2p^2 + n_1p +n_0 } {d_1p + d_0}\\]
\\[ p_1 = p_2 = p_3 = p_4 = p \\]
\\[ \ 0 \leq p \leq 1 \\]

Determining \(p^*\) for a given \(q\) becomes trivial now! The second result
of this work is the following theorem.

**Theorem 1.**

The optimal behaviour of a **purely random** player \\((p, p, p, p)\\) against a
memory one opponent \\(q\\) is given by:
\\[p^* = \text{argmax}(u_q(p)), \ p \in S_q,\\]

where the set \\(S_q\\) is defined as,

\\[S_q =  \\{0, p_{\pm}, 1  \| \begin{array}{l}  0 < p_{\pm} < 1, \\\ 
p_{\pm} \neq \\frac{-d_0}{d_1}  \end{array} \\}. \\]

To test Theorem computer trials have been performed! The results are shown
in the figure below,

**insert image**

This approach can also be expanded on to consider multiple players
\\(q^{(1)}, q^{(2)}, \dots ,q^{(N)} \\).

<p align="center">
  <img src="{{site.baseurl}}/assets/images/against_multiple_players.png" style='height: 20%; width: 30%; object-fit: contain'>
</p>

**Theorem 2.**

The optimal behaviour of a **purely random** player \\((p, p, p, p)\\)
in an \\(N-\\)memory one player tournament, \\(\{q_{(1)}, q_{(2)} \dots,q_{(N)} \}\\)
is given by:

\\[p^* = \text{argmax}(\displaystyle \sum_{i=1} ^ {N} {u_q}^{(i)} (p)), \ p \in S_{q(i)},\\]

where the set \\(S_{q(i)}\\) is defined as:

\\[ S_{q(i)} =  \overset{2N}{\underset{\lambda_i \neq \frac{do_i}{d1_i}}{\underset{i=1}{u}}}
\lambda_i \cup \{0, 1\} \\]

Note the size of candidate solutions is \\( 1 \leq\|S_{q(i)}\| \leq 2N + 2\\).

**insert image**

Several results are introduced from both theorems, these include:

- Obtaining the optimal random behaviour \\(p ^ *\\) reduces to a search over a
small finite set.

- Optimising against the mean utility can not be captured by optimising against
the mean opponent.

- A strategy with memory \\(< 1\\) out performs the optimal purely random player.

One can notice though that the answer to the main problem has not be given.
The next step (currently in progress) is to generalized both theorems to memory
one players! This will done with the assistance of the [resultant theory](https://en.wikipedia.org/wiki/Resultant),
which will allow me to solve multivariate systems, but I will leave this for another blog post.

I would like to note that all the written mathematics have been checked using
the symbolic mathematics python library [Sympy](http://www.sympy.org/en/index.html)
and the code for the numerical results has been developed using best practice techniques.

**p.s.** This blog post accompanied the following poster:
which was presented in the SIAM UKIE Annual Meeting 2018.
