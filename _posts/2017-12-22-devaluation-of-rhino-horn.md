---
layout: post
title:  "An Evolutionary Game Theoretic Model of Rhino Horn Devaluation."
date:   2017-12-22
comments: false
---

The name rhinoceros means `nose horn' which is often shortened to rhino. The
name comes from the Greek words rhino (nose) and ceros (horn). Rhino populations
are at critical level today due the demand for rhino horn and the subsequent
poaching.

The current rhino populations are mainly in conventional large protected areas.
Wild life managers, the people in charge of these areas, are using several approaches
to secure the life of the animals. One of these approaches includes removing the
horn itself; dehorning. Namibia was the first country to use dehorning to protect
rhinos from poaching. There are numerous cases where dehorning has proved
insufficient to prevent rhinos from falling victim to poachers.

This situation can be described using a [game theoretic model](https://en.wikipedia.org/wiki/Game_theory).
Let us consider
two players, a life manager and a poacher. Both players have two strategies.
The manager can choose to either dehorn or not the rhinos of their camps. The
poacher on the other hand can choose to kill dehorned rhinos or not. Thus to be
a 'selective' poacher or an 'indiscriminate' one.

This work was done in [2016 by Tamsin Lee and David Roberts](https://ora.ox.ac.uk/objects/uuid:d6c01110-1f53-4efe-88c7-10fc35efb3ac)
and the game we just described is given by the following matrix,

<p align="center">
  <img src="{{site.baseurl}}/assets/images/RhinoPic.png" style='height: 40%; width: 60%; object-fit: contain'>
</p>

Assuming that both players will always behave so as to maximise their payoff,
there are three equilibriums. In the 2016's work the authors studied the following
two equilibriums,

- either all rhinos are devalued and all poachers are selective;
- or all horns are intact and all poachers are indiscriminate.

Their work concludes that poachers will always choose to behave indiscriminately,
and thus the game settles to the bottom right quadrant, i.e., the poachers win!

Their work though did not take into the population dynamic effect of these
strategies. For example in a population full of indiscriminate poachers would
there be a benefit for a poacher to behave selective?

In 2017, alongside Tamsin Lee, we further enhanced their work to allow for cross
dependencies across multiple poachers. The game we considered was not of a two
players any more but now the players are an infinite population of poachers. We
explored these dynamics using [evolutionary game](https://en.wikipedia.org/wiki/Evolutionary_game_theory).

There are three possible population that could be stable. These are,

- a population where everyone behave selectively;
- a population where everyone behave indiscriminately;
- a mixed population of poachers.

As seen in figure below,

<p align="center">
  <img src="{{site.baseurl}}/assets/images/evolutionary.png" style='height: 80%; width: 100%; object-fit: contain'>
</p>

Using a realistic and generic utility model we provided analytical evidence
that only the population of indiscriminate poachers is stable and further more
evolutionary stable. This was also explored numerically. The below figure illustrates
that for any given starting population everyone converges in an indiscriminately
behaviour.

<p align="center">
  <img src="{{site.baseurl}}/assets/images/IndiscriminateESS.png" style='height: 80%; width: 100%; object-fit: contain'>
</p>

However, our results reveal that it is possible for a population of selective
poachers to exist, but for this to occur a disincentive must be applied to the utility of indiscriminate poachers. The disincentive factor can have several interpretations;
such as engaging the rural communities that live with wildlife.

This work in more details developed in the following piece of work which is
no a pre print paper and under reviewing process. The pre print can be found
on arXiv:[https://arxiv.org/abs/1712.07640](https://arxiv.org/abs/1712.07640).
Furthermore, the code for all the numerical experiments held are
only and on github:
[https://github.com/drvinceknight/Evolutionary-game-theoretic-Model-of-Rhino-poaching](https://github.com/drvinceknight/Evolutionary-game-theoretic-Model-of-Rhino-poaching).
Note that all source code has been documented and tested
properly.

Finally I would like to thank all the co authors:

- [Tamsin E. Lee](https://twitter.com/t_e_lee)
- [Vincent Knight](https://twitter.com/drvinceknight)