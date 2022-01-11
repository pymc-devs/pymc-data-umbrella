(decision_tree2)=
# (2) Your sprint cheat sheet
Welcome to this PyMC & Data Umbrella sprint to help you get
started contributing to PyMC.

PyMC is already a mature package with multiple dedicated
teams within its core contributor base. PyMC welcomes
many types of contributions and we wanted to
host a sprint where this "functional" diversity was
one of the pillars.

We also wanted to allow people from many different backgrounds
to be able to participate from the sprint, so we eventually
decided not to do a sprint. Instead, **we are hosting
a whole series of webinars that culminates with a sprint**!

This is very ambitious (though hopefully not too much) and
can be confusing so we have written this document to help
you navigate this series, and attend the content that will
help you reach your goal.

This page is structured as a decision tree. We have written
questions and provide advise based on your answers.

If the answer to a question is yes, open the dropdown, otherwise
move the next one.

:::{dropdown} Not interested in Python nor PyMC?
:icon: light-bulb

Jump straight to the {ref}`last webinar about contributing to documentation <contributing_docs>`.
We have extensive statistical documentation to which you can contribute to!
For example examples with detailed explanation along the code,
a glossary of statistical terms,
or descriptions of distributions and their parametrizations.

The bulk of our documentation is written in markdown and Jupyter notebooks,
so most of the skills you'll use: git/github, stats, technical writing and markdown
transfer to any other stats related open source project
{bdg-ref-warning-line}`I understand, jump <stats_join2>`
:::

::::{dropdown} Do you know what Bayesian statistics is?
What about probabilistic programming languages?
And PyMC?

If you know _about_ this (no need to be an expert) move to the next question,
otherwise we recommend you watch the embedded video.

This talk by PyMC core contributor Oriol Abril Pla covers the basics of the Bayesian
paradigm, probabilistic programming and PyMC.

It is divided in two parts. The first half is explanatory of the concepts above.
The second half goes over some PyMC examples from the community which you can skip.
They use version 3 of PyMC but the sprint is focused on PyMC version 4.
One of the webinars of the series is about using PyMC which goes in much more detail.

:::{youtube} 6dc7JgR8eI0
:::
::::

:::{dropdown} Are you comfortable working with Python and NumPy arrays?
:icon: container
:open:

In case you aren't yet, we recommend the first webinar of the series: {ref}`array_ops`.
:::

:::{dropdown} Are you familiar with PyMC?
:icon: rocket
:open:

In case you aren't yet, we recommend the second webinar of the series: {ref}`probprog_pymc`.
:::

{bdg-danger}`STOP`: Any questions about PyMC so far? We encourage you to ask them on [PyMC Discourse](https://discourse.pymc.io/)
the whole PyMC community (core contributors included) will do their best to help you out.

---

(stats_join2)=
* **Interested in contributing to code, to documentation or a bit of both?** {octicon}`heart-filled`

Now you should have all the context necessary to start contributing.
Let's go watch the webinars preparing you to contribute.

From here on, there will be steps common to everyone and steps specific
to docs or code contributions. Specific steps are separated in two
columns, left for docs specific, right for code specific.

::::{grid} 2
:::{grid-item}
:margin: 0 0 0 3
Watch the webinar {ref}`contributing_docs`
:::
:::{grid-item}
Watch the webinar {ref}`contributing_to_pymc
:::
::::

:::{dropdown} Set up your contributing environment.
:icon: package-dependencies

TODO: add links, maybe even tabs
  * local python (recommended, but optional if you only want to contribute to documentation content)
  * local git (or github desktop)
  * github account
  * raw text editor
:::

:::{dropdown} Are you comfortable with Git and GitHub?
:icon: mark-github
:open:

Git and GitHub (plus {abbr}`CI (Continuous Integration)`)
often poses a challenge to newcomers to open source.
To avoid Git and GitHub to pile up and get in the way of contributing
to PyMC, we recommend to start with a getting started PR following
the step by step we provide. We believe by doing this you'll
quickly become comfortable with git and github and will be
able to focus on actual PyMC contributions instead of strugging
with git branches or github PRs.

(optional) Submit getting started PR. TODO: add links
:::

:::{dropdown} Planning to participate from the sprint?
:icon: people

Join Discord, watch [Discord intro video by DataUmbrella](https://www.youtube.com/watch?v=w2A8SknM-68) (10 mins)

More instructions coming soon
