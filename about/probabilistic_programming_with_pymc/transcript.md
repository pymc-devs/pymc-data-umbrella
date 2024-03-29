# Video transcript

:::{note}
This "draft" transcript has been downloaded from YouTube and needs to be polished.
:::

Video:  [Introduction to Probabilistic Programming with PyMC](https://youtu.be/Qu6-_AnRCs8)

Speakers: Austin Rochford (AR), Reshama Shaikh (RS)

**RS:** Hello, everyone. Welcome to Data Umbrella's webinar. I'm going to do a brief introduction about Data Umbrella and then Austin will do his talk and during the talk you are free to ask any questions in the
chat and then we will answer them, you know just like whenever it's a good time, either every 10 minutes or towards the end. This webinar is being recorded it will be placed on our YouTube typically within 24 hours and I will post the link to our YouTube in the chat once I finish my brief presentation.

A little bit about Data Umbrella. We are a community for underrepresented persons in data science. About me: I am a statistician slash data scientist. I'm based in New York City as you can hear the sirens. That is quite normal from here. You can find me on Twitter, LinkedIn and GitHub at reshamas. We have a code of conduct and thank you for helping make this a welcoming friendly professional community for all of us. There are various ways that you can support Data Umbrella -- the first and foremost is to follow our code of conduct and contribute to making it a really you know welcoming collaborative space where people want to return.

We also have a discord where you can join and ask and answer general questions and share events or information. We're also on Open Collective so if you would like, feel free to donate.  If you work for a corporation
that uses Benevity, this is a company match platform, you can also find us on Benevity. We have various video playlists on YouTube. And one of them is contributing to open source and you can see here that we have videos for numpy and core python and scikit-learn and pandas.

We also have a playlist on career advice. We've had four fabulous speakers so check that out if you are looking for that and these are all the playlists that we have. We have career advice, data visualization, data science beginner friendly videos, contributing to open source, scikit-learn sprint. And we have just started a new playlist for the PyMC series and this will be added to that one and this is just a sampling of some of the videos that we have on our YouTube.

We also have a lot of resources on our website related to using inclusive language, allyship, burnout, AI ethics. You can check those out on your own. We are on all social media platforms as data umbrella. The ones that I have highlighted, Twitter, LinkedIn, are the most active. Meetup is the place to join to find out about upcoming events and updates. And we have a blog as well and we have a monthly newsletter so I will share the link to that. Feel free to sign up. We only send a newsletter once a month and we promise not to spam you in any way, so if you'd like to sign up for that that's also helpful.

We use BigMarker for our webinar platforms and there is live captioning available so if you go to the very top there is should be a button set that says cc and you can turn on the live captioning. From the feedback that I've heard the English live captioning is pretty good. You can try the other languages, I think they're not
they're not quite as accurate.

Our upcoming event that we have is "Automating Workflows with GitHub actions." That's going to be on January 18th, oops, lost my slides. Hang on just a minute, sorry about that, all right, there we go. Yeah sorry I don't know what's going on.

Today's talk is Introduction to Probabilistic Programming with PyMC with Austin Rochford. Austin is the chief data scientist at Kibo Commerce. He is a recovering mathematician who is passionate about math education,  Bayesian statistics and machine learning, and you can find Austin on Linkedin, Twitter and GiHub at austinrochford. I don't know if I'm pronouncing the name right but Austin will let us know when when he speaks. And feel free to tweet about the event. Our twitter is at data umbrella and with that I am going to turn off my
mic and camera and hand it over to Austin.

**AR:** Thank you Reshama for that introduction and thank you for organizing this event together with all of the other Data Umbrella folks on your team for organizing and promoting and it takes a lot of work to put an event together. And thanks to the folks on the PyMC side who's who have been coordinating with Reshama and her team with Data Umbrella so thank you for asking me to speak here today. I'm excited to share something I care a lot about with all of you and Oriol as well and everyone else who is contributing to that effort.

So my goal today is to introduce the idea of both probabilistic
programming and how it works in pi mc kind of from a knowledge of python a
little bit of numpy um up to an actually interesting application to give you an idea of what
is probabilistic programming why do we at pi mc find it exciting
um so about this talk as you can tell this talk is a jupiter notebook uh the slide
rendering the code was difficult to see so i'm just going to scroll through the notebook apologies for that it's available on the
pi mc data umbrella sprint github repo at this link i think oriole and i have both also
shared uh links in the chat with access to this notebook so please
do load it up on your own play with some of the examples modify them for yourself
so in terms of an outline where are we going to go for the next 40 minutes or so 45 minutes we're going to
talk about probabilistic programming from two different perspectives philosophical and mathematical this is a
little bit of motivation we're going to see how exactly does probabilistic programming play out in pi
mc we're going to use two somewhat simple examples here to illustrate the basic concepts one is one
of my favorite little probability exercises the monty hall problem which you've probably seen or heard about
before and the second is robust regression this will show how we can easily iterate on a
model using probabilistic programming one of its real strengths then we'll talk about why pymc why should you
actually care about pi mc as opposed to coding these inferences from scratch or some other system so we're going to talk
a little bit about the strengths of hamiltonian monte carlo and asera which is kind of pi mc's uh peer project that
that enables a lot of the exciting things that pi mc does then i'm going to give you a taste of
what a real uh you know a near real analysis that i've done around lego pricing
with this so if you can tell from my background i collect legos uh star wars
space dinosaurs a smattering of other ones uh so i'm very interested in what drives the prices of lego sets if you go
on my website which is just austin rochford.com i've written about this fair amount show how to analyze those
using pymc so a real world application and provide some resources and next steps right and i think rachma will ask
uh maybe mean all to to say what the next steps are with the sprint that we're enabling here but if you want to
learn more about either bayesian statistics probabilistic programming or pi mc i have some
resources linked at the end as well so the interest of time let's dive right in
so i take two different perspectives on probabilistic programming the first is a little philosophical right so people a
lot about a lot of the time talk about data science as doing inference to tell stories right data science is all about
telling stories with data i've included uh one of two favorite images here
um this is the size of napoleon's army right as he marches to and then back
from moscow during his ill-fated invasion of russia what's the story this data visualization tells you i think it
tells you not to invade russia during the winter uh but it's very much data goes to stories right that's the direction the
arrow flows you do some calculations on your data you use that to tell a story
probabilistic programming one of the real strengths about it and how i think about is it kind of turns that arrow around probabilistic programming says
i'm going to tell the story of how my data is generated and then encode and then i'm going to
use that to perform inference about unknown quantities uh whether it's the size of napoleon's army at a certain
point in time whether it's the probability that a coin is flat fair whether it's the effect that the number
of pieces has on the price of a lego set you know there's some unknown quantity in the world i'm going to tell a story
about how it relates to the data i see and then i'm going to use the data i've seen to infer
some things about that unknown quantity so that is how probabilistic programming kind of turns that around
um and it turns that around if you if you put your you know mathematical hat on a
little bit and you think about turn that around okay so if i have uh
a story and i get data from that story how do i turn that conditional probability around
well that's bayesian statistics right bayesian statistics is all about how do i go from the probability of b
given a and turn that into the probability of a given b right so this is all about how do i reverse
conditional probabilities same idea here going from data to storytelling and turning that
out around is what really motivates me here so this is kind of the philosophical level could say a lot more
there i'm not going to dwell too deeply let's dive into the mathematical level so the mathematical level this all plays
out um in something called monte carlo methods right we're going to be talking about
advanced monte carlo methods here and so what's a simple example of a monte carlo method well i'll give you one right here
let's generate 5 000 points that are uniformly distributed in the square that
ranges from negative one to one right so that's shown here
okay and i apologize these some of these things will be duplicated because these were built to be rendered as slides but
the formatting wasn't making the code legible so we're being a little bit flexible here so we've got our five thousand points in
this square negative one to one right let's count the number of them that are inside the circle with radius
ones so these are inside the circle with radius one if x squared plus y squared is less than one
right this plot highlights those that are inside the circle of radius one uh the green ones are inside the circle
the orange ones aren't inside the circle uh and then you know
what proportion of these should we expect to be inside the circle right
well it probably has to do with the area of the circle right the area of the circle is one
right the area of the square is four so if we take you know number of points
green points inside the circle and we divide that by total number of points which is five thousand we should get the
ratio of the area of the circle to the area of the square which is pi over four
and sure enough we add up the number that are in the circle we divide it by five thousand and
we multiply it by four we get not an awful approximation to pi right so this is what a monte carlo
method is a monte carlo method is all about using random numbers cleverly to approximate the quantity
you're interested in and we'll get into how that connects to probabilistic programming and bayesian inference in a second
how does this connect to bayesian inference well what we've done here is actually approximate this integral
right if you think back to calculus this integral relationship is true right because the square root of one minus x
squared that defines this quarter circle right so this integral gives you the area of
this quarter circle here multiply that by four you should get the area of the whole circle which is pi
right so we instead of doing this integral through maybe a trigonometric substitution or whatever you might have
learned in calculus approximated its value through random number generation
and bayes theorem has often very many intractable
integrals here right one way to restate the bayes theorem as i showed above is this way where theta are your unknown
parameters and d is your data right so if we want to know about our
unknown parameters given our data it tells us that it's data given unknown parameters probabilistic programming is
all about specifying this quantity right prior is not that hard also
specify the prior but then calculating this integral at the bottom is intractable
not possible provably impossible for a lot of interesting models and if we restrict ourselves to models just models
where you can calculate this quantity life becomes a lot less interesting we close off a lot of potential
applications so that's what gets us to consider probabilistic programming using monte
carlo methods in this case with pi mc although there are many different uh packages out there to do it with
um so all of that was great theory let's get down to practice now and let's talk
about the monty hall problem so if you're not familiar with the monty hall problem right there's a famous game show
in the united states going back 50 years even maybe probably even longer than that called let's make a deal right the
host was named mommy hall for a number of years and so that's where this comes from and one of the games the contestants would play in
let's make a deal would be that monty would show them three doors closed right behind two doors were goats
and behind one door was a sports car right so obviously in
the end you want to open the door that has a sports car behind it so how this game would play out is that
monty would ask the contestant to choose a door right and not open it yet so say you
chose door number one the first door right what monty would then do is open one of the other doors
in this example door three but it could be whichever one to show you a goat and then this is where the drama comes
in he would ask you do you want to switch your choice of door yes or no
right and this is one of the kind of first examples where conditional probability becomes a little bit
counterintuitive uh probably a lot of you know is that the answer is yes you should switch your
choice of door right um there after he's opened a door to show
you a goat there's now a one-third chance that your door contains the sports car
and a two-third chance that the other unopened door contains a sports car so you should switch
in order to maximize the chance that you choose the prize you actually want right and we could work this out
mathematically here i'm not going to run through it because it's tedious the point is probabilistic programming will
enable us to write some code to avoid doing this right because it's possible in this situation but not particularly
interesting and a lot of situations it won't be possible to work out like this so it's always good when you're learning
a new numerical method to apply it to a problem where you can get the answer with pen and paper to make sure they
agree that gives you confidence when you're moving to situations that you can't just use pen and paper for right so you
should be able to get a known answer in a situation uh that you can work out
explicitly so that you build confidence when in situations where you can't work out the answer explicitly
so let's see how we solve this monty hall problem in pi mc
that was supposed to be a hidden cell um thank you for bearing with me so what does the pi mc solution looks like well
initially we have no information about which door the uh prize is behind so i'm importing
pi mc i'm creating a pi mc model with this context manager on normal you know python stuff we do and then i'm saying
hey this prize comes from a discrete uniform distribution all that means is
each number between 0 1 and 2 has the same chance of containing the door right there's a one-third chance
it's behind door zero uh the first door one third chance that's behind the second door a one-third chance it's
behind the third door so here i'm telling the story of how my data is generated before i get any
information don't know where the door is the prize is i should consider each door equally likely
then we need to think about things from the host perspective right which door is he going to open
based on the door we have chosen well we've chosen the first door so he's not going to open that door right there
would be no drama there if he opens it and there's a car we just stick with the open door if we open it and there's a goat
we switch doors and it doesn't really matter which one we choose so he's not gonna choose the door we chose which is
door one now if the prize is behind door one this
is the first row he won't open door one we've already said he could open door two or three
they both contain goats that's fine if the prize is behind door two he's not going to open door one again that
destroys any drama he's not going to open door two also because he doesn't want to show us the car because yeah we
would just switch to door to the door with the car okay so he's forced to open door three
right and similarly if the prize is behind door three he's forced to open door two so this is how monty makes his
decisions of which door to open so we can see if the prize is behind
door one there's a fifty percent chance he opens door two or door three if the prize is behind door two there's
a hundred percent chance he opens door three and similarly if the prize is behind door three there's a hundred percent chance he opens door two
so in the spirit of probabilistic programming we want to encode these chances he opens each door given where
the prize is as code so i'm going to import this package name asara uh and i'll i'll talk a little bit
about a sar in a second so just bear with me for the moment and i'm going to write p open which is the probability he opens each door as a
switch statement here so this is basically the asara version of an if statement
so this is saying if prize is behind the first door then we
know zero percent chance he opens the first door fifty percent he opens the second fifty percent he opens the third
that corresponds to this line right if it's not behind the first door a nested if statement if he's behind the
second door zero percent chance he opens door one zero percent chance he opens door two a
hundred percent chance he opens door three that corresponds to this row right and then this final thing if it's
not behind the first door not behind the second door gotta be behind the third door 100 chance he opens the second door
so why have i written this in terms of aet aceratenser.switch and it's
sarahtenser.equal instead of regular python if then else statements we'll answer that question in
a little bit and it's all about increasing the efficiency of our sampling algorithms through calculus
acera lets us differentiate expressions automatically without having to do any calculus with pen and paper in a way
normal python if then else statements do not and so that's the benefit we get by writing this
which totally could be an if-then-else statement and somewhat awkward uh syntax and we'll see that that's really
worthwhile once we move towards more complex examples so we've said our prior belief about
which door the prize is behind we've said what are the chances monty opens each door given where the prize is now
we know he opened the last door the third door and showed us a goat right
so which door he opened is now a categorical random variable it's either first second or third
the probability each door was open is that p open we just defined through those switch statements and we know he
opened the third door since this is zero index the third door corresponds to this two
right so we've said how where the prize is influences the
likelihood he opens each door and then what data we've observed now we're going to perform inference and
inference in pi mc is through sampling right this is where the mark this is where the monte carlo
uh inference comes into play so we sample from the posterior distribution to use the bayesian terminology
here and we get uh an x-array array of samples we're going to get in this case
um 20 000 samples from the posterior distribution of places the door of the
door the prize is behind in 20 000 different simulations of this right just like when we were using monte carlo
methods to approximate pi we had 5 000 different samples there a certain proportion of them were inside
the circle we use that proportion to determine pi we're going to do draw 20 000 random numbers here we're going to
see how many of them are zero saying the prize is behind the first door we're going to see how many of them are one
saying the prize is behind the second door and those proportions are what's going to tell us the probability that
determines whether or not we should switch doors so we get these traces here okay
uh these samples and i'm going to check the posterior prize so this says how
many times is the prize behind the first door right and this says one third of the
time the prize is behind the first door given the information we've input which means that two-thirds of the time it's
behind the second door so we should switch doors right this is the well-known result that we could derive uh with pen
and paper and i did on a previous slide so um
so it's good we've recreated this result using probabilistic programming by telling the story of how our data was
generated we have inferred what are the chances the sports car is behind the first or
second door and we know the correct answer is to switch door so let's step back a bit and talk about
the components i've just flashed in front of you two components we've talked about so far we've talked about pi mc
distributions right we saw discrete uniform and categorical distributions there so any
probability distribution almost any probability distribution you can think of from statistics
has been implemented in pi mc and if it hasn't they're actually quite straightforward to add those are some
good first contributions or to add uh new probability distributions it it's
kind of uh there's a lot of boilerplate code with um some small tweaks you can use and that's
actually really good and important work i like to think of these given that i'm a lego collector it's kind of the lego
bricks of probabilistic programming right distributions are the bricks pi mc lets
you put those bricks together in different ways to perform inference and so
in the case above we use the discrete uniform and the categorical distribution i've just chosen to highlight two to
show flexibility obviously there are normal distributions there are zero inflated poisson distributions if you
were to click on this link it takes you to the documentation shows you you know uh many dozens if not hundreds of
distributions that are available to build up your statistical models from and then what were those
aet.switch aet.eq things doing well they were invoking acera
which is pi mc's uh kind of tensor computational back-end right you can see
a little a little blurb from the acera documentation here i'm not going to read it out loud for you you can think of a
sarah as filling the same niche as uh you know pie torch
or tensorflow fill in uh various other you know maybe
deep learning ecosystems which is it will optimize your numerical computational graph
and it will also allow you to calculate derivatives of that computational graph without having to do the calculations
yourself and that is really key and what pi mc really leans on asera for to enable
efficient inference in high dimensions which we'll talk about in a little bit it's very much worth the uh
the cost of wrapping p open in these asera switch and sarah equality
statements to get uh you know automatic differentiation and optimization for
free uh once you start thinking in that way it's not hard to port a lot of the common code you would write to that and
the benefits are great so i'm going to walk through another kind of simple example to illustrate a
couple more key concepts and ingredients of pi mc
uh or dependencies perhaps before we ramp up to our more realistic lego examples so we're going to take a data
set from anscom's quartet an interesting you know instructional data set of four different groups of
data that have some similar summary statistics i want to talk a little bit about how we can use pi mc to do robust regression
today so let's focus on the third entry in this quartet that is almost exactly linear except for
one outlier i'm going to show you how you can really powerfully use these kind of swappable distributions in
pi mc to capture the linear trend here and ignore this outlier in kind of a toy example but
that's instructive for real life applications so let's see ordinary least squares
let's first do something we know will be uh prone to responding to this outlier
what are the mathematical assumptions behind your good old ordinary least squares regressions well
they are that all values of the slope and the intercept b and the um
[Music] the error the noise variants are equally likely so i'm going to build a pi mc
model that encode these things and flat here is the distribution the lego brick that
says all real numbers are equally likely to be the value of m all real numbers are
equally likely to be all the va uh the values of b all positive real numbers that's what
half here means are equally likely to be the value of theta right so you write out some math here
y is mx plus b plus some noise this is one way to view it this is equivalent
statistically to saying y has a normal distribution with mean mx plus b variance sigma squared so that's
how this is encoded in pi m c really really simple right and here you'll see
again we're saying hey i observed this data y 3 y 3 being the
y-coordinates of these data points in the third entry in the quartet
so we can come on down and we can sample from this model again you see pi mc's doing some sampling for us and it's
warning us some things there were five divergences after tuning so this is great pi mc is not only trying to infer
the values of m and b here but it's going to warn us when it's not doing a
great job when our monte carlo methods may be failing so this is a really powerful and user-friendly thing about
pi mc how can we visualize these divergences where inference is failing well we can
use one of the other important components of the the probabilistic programming ecosystem here which is rvs
a kind of sibling project to pi mc to plot the values of mb and theta that
are causing these divergences right so the the idea here is that rvs is a library
that contains a lot of pre-built visualizations and statistical routines
that will help you understand the results of your inference that you did with pi mc
and visualize debug those results right so what two more key components
that this uncovers one is rvs right and rvs is really cool because
it's agnostic about the probabilistic programming library you use to conduct the inference right the plots of
posterior distributions or divergences or you know many other things you want
to make are agnostic about whether or not pi mc is your program probabilistic
programming package of choice or stan is your probabilistic programming package of choice or
you know numpyro is your probabilistic programming package of choice there are many probabilistic programming languages
out there they all want similar visualizations rvs exists to say hey if
you provide the results of inference in a standard format we'll build those visualizations for you no matter what
uh upstream inference package you use so our visa is really awesome um i strongly encourage everyone to take
a look at it when we look at the results of inference right we took
we said pm.sample store this in ols ordinarily squares trace
we look at the type of that that's an rv's inference data object okay you just need to encode there was the samples
from your monte carlo uh approximations in this object get
uh rvs to work on it if we look at the posterior component of that trace that's an
x-array data set an x-ray is a really awesome library that's you know i think about it almost
as like pandas in more than two dimensions right it's a great way to define flexible
labels labeled arrays in arbitrarily many dimensions and this is exactly what
you want to do when you're doing invasion inference and visualization of bajan inference the results of bayesian
imprints excuse me and we will see uh where those labels are very powerful
um so there's a question why do we assume that it is normally distributed in the
ordinary least squares model that's a great question you can motivate the ordinary least squares model a bunch of different ways
uh right usually it's viewed as minimizing the mean squared error with a bunch of
restrictions applied that turns out to be equivalent to placing a a normal
likelihood on your data so it's just one of the assumptions that goes in here there are a bunch of different equivalent ways to frame it so
great question so what do we want to do well we want to
compare our inferred values of m and b to the robust values we would get if we
ignored the outlier and the outlier here happens when x is equal to 13. so we're going to use numpy's uh
polynomial fit of degree one same equivalent to ordinary least squares regression to get
the slope and intercept and we're going to compare those to our posterior distributions for m and b
that we got using pi mc right and you can see here
the reference value so the the robust slope is a little bit smaller than it's
a little bit towards the low end of our posterior credible interval we've slightly overestimated the slope
underestimated the intercept here this has really meant the details of this visualization aren't that important it's
just that all of this came out of you know one line essentially of rvs because rv's is this powerful showing what's the
true value that i'm trying to get out of inference versus what's the posterior distribution uh that happened when i fit
my model so we can also plot the lines here that come out of this inference right and we
can see okay the blue line is the average the posterior expected value
that you get using pi m c and the red line is what you get when you calculate the same thing using numpy
just to show that they agree when you when you match up your assumptions so that's good but we see you know this has
definitely been pulled upwards by the outlier underestimating the true intercept over estimating the
true slope due to this outlier how can we swap out some of those lego bricks
those distributions uh pi mc distributions in order to make
this less sensitive to that outlier well we can start out by saying let's
regularize a little bit let's move from ordinarily squares to ridge regression for those of you that are familiar with
the machine learning concept of ridge regression what is ridge regression it's really just normal priors on your
coefficients right so instead of saying m is a flat distribution here we're going to swap
that out and say it's normally distributed mean 0 standard deviation 1. how to choose these parameters as a
subject in and of itself um i've just chosen these here for convenience you could change them
um [Music] yes so reishima has asked if y were distributed
as a binomial yeah you could absolutely you know build say a logistic or a probit
regression model this way uh you know there are distributions for any kind of typical glm that you've seen out there
i've written up examples on my blog austinrockford.com around you know negative binomial regression using pi mc
or even you know ordinal regression to see what factors drive lego set star
ratings uh so the the number of distributions is really flexible really is legos the goal
is to enable you to build whatever models you want um using these building bricks here we're
sticking with normal observed likelihoods just for simplicity uh since this is an introductory talk
but this can get as complex as you like you can make a zero inflated binomial model or something similar uh with the
building blocks that pi mc provides a great question reishma um
so we're going to throw these on these pry these normal priors on the
uh slope and intercept this is equivalent to ridge regression i'd have to do some math to determine
what regularization penalty it is but it is equivalent uh we perform inference again we get a
little a few a couple fewer um a couple fewer warnings
uh but there are still some divergences we can check our plots again our true values our robust values of the slope
and intercept are actually even further from what we've inferred so huh well this makes sense
regularization of this sort tends to be more useful let me find the correct
thing when your x values are extreme and not your y values so we've added in
robustness to extreme x values but not to extreme y values actually reshma this will speak
to your next question which is
um which is how can we change that
observational likelihood to be more robust against this extreme y value well to get robust regression out of
this we can use the fact that students t distribution has fatter tails than a normal distribution
right and so here the blue line is the standard normal distribution the orange
line is a student's t distribution with two degrees of freedom we see the tails are fatter
this will respond due to those fatter tails this will respond be less sensitive to outlying y values
so we'll specify the model for m b and theta same as we did before but we'll change y obs here from a
normal random variable to a student t distribution we have to specify a prior on our
degrees of freedom here i say it's a uniform between one and ten
uh right because as the degrees of freedom goes to infinity the t distribution becomes a normal distribution it's less interesting if
the degrees of freedom is huge we expect it to be small here because there is an outlier but similarly you know mean is
mx plus b sigma is sigma we perform inference we see
in our posterior plots we've captured the true robust values of these things quite well
we can visualize the outcome lines here the green line is going right through
our uh you know non-outlier data points and the outlier has been ignored this is
a little bit of a silly example right because there's no noise in the these things outside of the one outlier that's
why these posterior distributions look real wacky you could add a little noise here to make it more realistic the point
is these distributions are easily swappable uh chandra asks can we model using
tweety regression i believe we can uh if not it's possible to add
just depends has the distribution necessary been pre-built
how do we choose hyper parameters and can we go wrong by choosing a distribution um
just like right this is just one kind of tool in your statistical toolbox out of many
uh you can always go wrong choosing your statistical tools so there is tons of
uh ways to choose these prior distributions and evaluate the goodness
of your choice that are really outside the scope of this talk at the end i will give
some references that will include um discussions of these sorts of things but
that's a great question so yes absolutely you can make bad decisions if you don't choose the appropriate tools
as with any statistical method um and how to how to decide whether you are
in a good spot or not is something that's outside the scope of this talk but there are many references out there
that i will share so why are we using a sarah again and
i'm going to move quickly here to make sure we have time for q a at the end um
so apologies but hopefully it will still be somewhat clear why are we using uh
a sarah why are we using that aet.switch aet.equal and under the covers here when
we write uh you know pm.normal there's a bunch of acera operations going under
the covers when we call this class constructor uh pi mcs just providing a nice layer
over those for you so you don't have to think about them unless you want to um
why we use the sarah is to do something called hamiltonian monte carlo and what makes it hamiltonian what makes it
hamiltonian is that you want to take into account the geometry of the model you're specifying
right and geometry in the sense of differential geometry is all about curvature
and curvature is about derivatives in a past life i was a differential geometer
and the way i think about it is curvature is always about the failure of partial derivatives to commute
so uh you know if you differentiate with x and then differentiate with respect to y
and then do the derivative of y with respect to y and then the derivative with respect to x
those two things are the same in flat space on the plane they are in general different if you're
on a curved surface um and that is how geo geometers or at
least a certain set of geometers think about curvature and that's actually really important for doing this kind of
inference in high dimensional models models that we're really interested in here as
accurate representations of reality due to the curse of dimensionality which you're probably familiar with from
machine learning what's the way the curse of dimensionality uh is reflected
geometrically is that the volume of the unit sphere as the number of dimensions
increases goes to zero exponentially fast right so
you can think of the unit circle and then the uni in two dimensions the unit sphere in four dimensions the unit hyper
the unit sphere in three dimensions there's a hyper sphere in four five six seven dimensions what's that volume
it drops to zero really fast as the number of dimensions increases even mildly here we can see that between 100
and 1000 dimensions it's already you know 10 to the negative 196
right what this means is that typical points in your data set near the origin there's a nice definition of typical but i i
won't get into what that exactly means here are hard to find in high dimensions
if we just treat the spaces flat when we take into account the curvature
of the space they become a lot easier to find and asera is what lets us do that by automating those derivatives we need
to cut um to quantify curvature
so where does acera really help us as a toy example let's show using a sarah that the derivative of x cubed is 3x
squared familiar to all of us who have taken calculus right so we're going to define x as a scalar y
is x cubed then we're i'm going to ask acera to pretty print the gradient of y
with respect to x that should be this derivative let's walk through this and i'll tell you how to read it
so this says fill x cubed with x is one okay so one cubed is one this term is
just one one times three okay so we've got this coefficient of 3 here
and then we've got times x to the 3 minus 1. so we've got 3 from this term we've got x cubed from this term
beautiful right so sarah is doing calculus under the covers
to quantify the curvature of space to make sure that we are not dealing with these absurdly small numbers
uh that we would if we didn't acknowledge the that geometry all a bit hand wavy right now
there are great uh references here uh there's no way to go super deep on that
theory in an introductory talk i just want to wave at why it's important so
let me take about five minutes to run through this final example where the shape of the posterior does
become important and in that tweety regression or that binomial or ordered logit or probit regression this becomes
a lot more important than our you know simple to you know univariate linear model
with like two or three parameters um it becomes a lot more important as your
model gets more complex and realistic so let's talk briefly about a bayesian analysis of lego prices so on the left
here you have a small sampling of my lego collection to my left here there is some of it as well
i came at this with a motivating example of here's darth vader's meditation chamber a set lego released uh last year
in 2021 is this model worth the 70 they were charging it or not how can we answer
that question with data so i went out there and
scraped a bunch of data from brickset which is just a lego fan site that has references all sorts of data you can see
it here i've made it available online you can find the data if you're interested in that sort of thing you'll see there's about
6400 sets from 1980 to 90 uh to 2021
you can see there's a pretty good i'm gonna move quickly here because i know we have some other things to cover off in the end and i want to leave time for
q a um there's a log linear relationship between the piece count of the set and
the price of the set that's not surprising right lego has both fixed and variable costs in manufacturing it sets
larger um sets obviously will incur those larger variable costs so they're going
to charge us more to cover their costs plus whatever profit that that makes perfect sense we see where darth vader's meditation
chamber kind of fits in this we can look at to make this model a
little more interesting a little more realistic we can look at how these prices have varied over time
so how has the recommended retail price per piece varied over time and we could
see where darth vader's meditation chamber fits in there we can break this down
by different themes so we can see star wars creator harry potter and disney
we can build a model i don't know why my math is not working here apologies for the last minute
change that says you know basically each component the intercept and then
the price per piece uh has a time varying component so a gaussian random walk and you can come
into the notebook and see how this is built up here from our pm.normal lego bricks
and a theme component which is a hierarchical normal random variable you can see how that's built up here this is
not a ton of code to specify a fairly flexible model with both time and theme effects
if we try to sample this without hamiltonian monte carlo i can do this using a metropolis step
which is the simple naive thing to do i get a ton of errors if i calculate the r
hat statistics here i see they're enormous they're up above three for some of these things r hat statistics of one indicate
convergence so i shouldn't trust this these results this is one of the ways
that pi mc tries to help you decide if your results are trustworthy or not you can see this took about a minute
let me do this with right there 351 parameters here so there's a lot of them
uh let me do this with the more advanced samplers the hamiltonian monte carlo nut
stands for no u-turn sampler that that pi mc provides this takes nine
minutes ten minutes uh but produces much better r hat values that are close to
one indicating no problems with convergence there and therefore much more trustworthy
uh posterior inferences so the top is the using the metropolis step that falls
prey to the curse of dimensionality you can see that these samples are wild all over the place i have no reason to
expect a true posterior distribution would have this wild form so this shows inference problems whereas the
hamiltonian monte carlo ones have this beautiful shape much more plausible
um so even though it took about 10 times as long to sample the sampling efficiency
is uh just so much bigger right so the sampling time is an order of magnitude
longer for the adaptive hamiltonian monte carlo nuts is hmc yes for daniel's uh question nuts is
a form of hmc but the sampling efficiency in terms of effective sample size per second is an
order of magnitude larger so to get the same effective sample size with your
metropolis step you'd actually have to sample that model for 25 hours so 25 hours versus 10 minutes i'll take
10 minutes any day of the week so we can start to answer some of our questions pretty easily using pi mc here
we can look at the posterior distribution of what we would expect darth vader's meditation chamber to cost based on the
fact that it's a star wars set released in 2021 uh that has however many pieces i think
it's about 700 pieces so our models uh posterior expected value was 79 we
see that the 69.99 lego price to that is just below the median so it's pretty reasonably priced we can assess the
pretty easily the effect of different set uh types on the price of legos right so creator
sets are a little less expensive star wars sets are a little more expensive etc etc
here i've included some uh two books that are available online
for free this one on the right is also for purchase so the left is a classic reference
middle is a great reference written in r with stan but we have posted notebooks
implementing it in python with pi m c for all of the examples and exercises
here really great textbook to help you think about bayesian inference and then on the right is a textbook about
bayesian inference actually written by osvaldo raven and jung peng who are three piemce core
contributors that just came out uh has an online version available also available for purchase in print
i thank you for your attention again i thank reishma and the data umbrella team
for their hard work putting this together and oriole and nina for me
excuse me for their coordination uh there and at that point i will hand it back to reishma to perhaps say a
little bit more about the sprints this has been intended to introduce to you
uh and then i can take any q a after after reshma uh fills that in so thank
you all for your time i really appreciate it so yes actually me now is going to be
speaking a little bit about the upcoming sprint so i'll wait um if you know if you're able
to share your camera that would be great
right no
yep we can hear you so i'll share my screen
okay
oh i think my screen is visible yes it's loading yep now we can see the slides yep yeah so
uh yep uh so we're going to be organizing a sprint with data umbrella like the
entire biomc team on 18th and 19th february like that over that weekend
uh we haven't finalized the exact time slots yet but we're hoping to do like two hours uh
to our slots over the weekend so we can accommodate more time so
[Music]
two of these have already happened and two more of these will be happening and i really think you should be
like uh if you can make the time either attend them or watch a recorded version if you want to contribute to yfc like
austin gave a wonderful introduction on how to use pyeomc and why you should be interested in probabilistic programming
next we have a talk that ricardo will give which is more about you know how can you contribute to ymc
like how can you help out with the source code or other things and then martina will be giving a talk on
how do you contribute to the documentation like say if you're not really interested in contributing to code but you know a bit of statistics or
maybe you just want to contribute to the technical part which is again important
so these talks would help you out with that and finally then out month from now we have
the sprint uh a couple of us in the pi you should always be to help you through polar
request surveys and i mean i i think it would be really fun and
if you're new to open source i would really ask you to join in and
yeah that's that and thanks to vishwa for putting together this whole thing it's been like so much work
yes um let me turn on my camera um yes i want to thank um the entire um
pi mc team because um they initiated this sprint and there's a series of
webinars you can see that we've had two of them already that are on our youtube and we'll have two more upcoming which
will be available on our youtube and the meetup group is the best place to sign up
because that's where you're going to be able to find out about the upcoming events um
so meanwhile i have a couple of questions for you like for instance for the sprint how much of a background do
people need to have to be able to participate in the sprint
like uh i think uh people of like the background can be really varied like you can contribute to various areas
actually you can if you know some statistics you can contribute to documentation if you've already
contributed to open source but you don't know stuff about probabilistic programming there are still housekeeping issues that you can always contribute to
you know there's a bug there's a type or anything so as long as you're like slightly comfortable with using github
you have the local setup you'll be able to make at least some meaningful contribution and all of us will be there
so we'll try to help you out like you know according to whatever you know what can you best help out with so i think uh
it won't be like that much of a problem like background wouldn't be that much
with any background as long as you can like you have your github setup and everything that's something that we want
you to do and yeah after that it's all good from there
great um if anybody has any questions on the upcoming sprint feel free to post in
the chat and it will also be helpful for us because it means that we'll be able to sort of
include that information in the in the event so other people
probably if you have questions other people have questions as well
oh by the way uh austin we were speaking before but the question that i asked you um which would be great to share with
the group is um you know if you want to talk just a little bit about how this um the new version of pymc which is a major
major release if you just want to talk about that for people who weren't here before sure sure so if if you go and find on
the internet even even on my website for example you'll see a lot of
materials that reference pi mc3 and it's been quite an evolution to get
from pi mc3 to uh what we're currently calling pi mc which which under the covers is the
fourth version of pi mc the uh kind of saga has been that um
i talked about a sarah here for a while right um
a previous version of of acera was supported by a research group i believe out of the university of montreal
it was called fianno one of the first kind of tenser libraries for deep learning you could think like an
intellectual precursor to your tensorflows and and your pie torches and your terrace and all that
um a couple years back that lab announced that fianna would no longer be
supported by mc you know was kind of casting around for a new tensor back end
dabbled in in pi torch and mxnet and uh tensorflow for a while eventually you
know some great pi mc folks decided they would rather just take over sarah continue to maintain or take over thiano
rename it as sarah to show that it's a new project continue to evolve that to not just meet the needs
of pi mc although that's a big part but make it an interesting uh tensor package
and modern tensor package in and of itself and we've taken that uh that opportunity to call this pi mc v4
introduce some modernizing changes around a focus on rvs
uh focus on x-ray that were not present you know 10 years ago or whatever when pi mc3 v3 were started so we kind of
took that back and changes an opportunity to make some lightly breaking changes
uh to make pi mc a little more modern and i do say lightly breaking because by and large most of the code that i have
on my website um that runs on pioneer c3 will run on pi
mc now if you just change uh thiano to acera in a few of the right
places so it was more of an opportunity to modernize when changing back ends than anything
else is what i would say and it's some really exciting stuff i think to to work with and the acera
folks are doing uh really great and interesting work not only to support pi mc but in kind of tensor computation in
general you can you can do things like use c as a back end you can use jacks as
a back end i think there are maybe it's a number back end for your acera code there's all sorts of interesting um
kind of lower level programming language focus things that they're doing there so it is
the foundation of pi mc v4 for sure but it's so much more so worth thinking
about in its own right so i just want to read a comment that oriole who is a um maintainer for pi mc
foot regarding the sprint which is as an example of how how wide the range is our docs have a glossary of statistical
terms to which you can contribute with no python or pi mc knowledge only stats
i think really what's going to be unique um what is unique about this pi mc sprint is that you know
people from all different backgrounds in terms of what knowledge they have whether it's
statistics or python or just very can can contribute to it you don't have to be a pi mc expert
to learn how to to contribute to pi mc i'm just going to turn my camera off and i'll let austin answer a few of the
questions that are in the chat
all right folks let me scroll up a little bit pi mc3 is not being continued i forget
to what extent it's going to get bug fixes i think that is addressed uh
either on the pi mc website or in uh the pi mc discourse
which is quite an active forum we have for answering questions but no most of the active development is happening on
pi mc v4 which like i said it is almost most models written in pi mc3
require some very light like five minutes of porting to get them to work on v4 so it's all you know designed to
be as seamless as possible but you know we can't promise it's 100 seamless
um [Music] arielle mean all shared to answer ariel's
question i believe then claudia does the definition of custom probabilities change substantially so
yes one of the things that does change under the covers i've talked a lot about um
the interface the the user-facing interface has not changed a ton a little bit with the advent of rvs and and the
emphasis on x-ray uh the implementation of pi mc distributions under the covers has
changed a fair bit now if you've done it before it's not that hard to learn the new way
but it is not exactly what it was like before in v3 so it's where you've maybe implemented some custom distribution
there's a new pattern to follow i would say it's a better pattern now that sarah has kind of taken what thiano did and
made it more uh more suitable for pymc so i would say there's a newer better pattern to follow there but there is a
little bit of work if you've done something like implement a custom distribution
and uh as you say hopefully more documented um that's something that can definitely be
helped in this sprint i think there's a lot of uh my experience contributing new
distributions is a lot of find a distribution that's similar look at the patterns there
uh adapt it to your situation and test but i think that's a great place that our our documentation could for sure use
some improvement is in adding new distributions so i think it'd be a great uh sprint activity to contribute to
um also a great discourse topic so benjamin has asked are there differences
between probabilistic programming noteworthy significant reason why would you why you would choose pi mc over stan
uh so i'll answer this on a couple of different levels mathematically they're all kind of striving towards the similar
ideal of adaptive hmc when you really get down to the nuts and
bolts of it there's going to be some algorithmic differences between how they implement it but by and large those
should not matter to 95 99.9 percent of people
um i certainly couldn't tell you what they are off the top of my head and i use pi mc quite a bit
um you know stan stan versus pymc depends do you you know
do you want to have an all python interface to your programming language is that important for your application if so pymc might be a better fit for you
stan has its own you know model definition language um
strengths and minuses of each as a like a software library are you know
the language you use to specify models whether that's pure python for pi mc or you know stan's domain specific language
that's kind of a a subset of c plus plus neither is better than the other stan is
great software we are actually great friends with the folks on the stand team get dinner with them all the time when
i'm in new york um it's just it depends on your application
where you need to be running this code what kind of tasks you're doing with it so you know i
tend to be living in jupiter notebooks like everything to be concentrated in python like to be able to do my
contributions in python and not in c or c plus plus so i've chosen pimc
uh v3 and pymc as it's now renamed but you know i don't fault anyone who chooses to go down the stand rabbit hole
either i think they both have their strengths and weaknesses both uh numb focused supported projects so
and there's a lot of cross-pollination of ideas uh particularly manifested in rvs right rvs is a visualization
diagnostic library intended to be shared between pi and c and stan and several other
inference engines so really you know gets down to the nitty gritties of how do you choose any software package
uh what what your environment is like what your needs are um
chandra asks uh simulating conditional
probability can you share resources about that there's no resource that comes to my mind uh it's more about
taking those lego building blocks and putting them together if you had a specific question in mind you're saying
like a high school conditional probability problems probably you know involving colored balls in urns or
something like that uh i'd say that the best way to get help there is take a stab at it yourself
uh maybe you solve it great maybe you don't no worries uh there's a learning curve
here bring your you know partially worked example to discourse and there's an entire group of really
friendly people on discourse uh that sometimes includes me when i have the entire in the time but there's a great
community there that are very helpful in getting your questions answered so um
i don't know that there's a definitive reference for those sorts of problems my my advice in general would be take a
stab at it and then turn to discourse with your your partial progress and folks they are extremely friendly and
will help you um [Music] help you drive that to to resolution
and daniel points out yes adam downey's book i think think babies is probably the one
you're referencing is an excellent uh reference for those sorts of problems
um austin there's a couple of questions that i just put in the q a chat one is from luke and he writes hi austin great
talk have you played around with the infinite monty hall python problem with pi mc
so infinite doors rather than just three of them um infinite doors rather than just three
well pi mc does not deal well with infinities right just like any they're right you can't
specify an infinitely long numpy vector and if you think of acera as like numpy
fancy numpy not that's not technically correct but it's spiritually correct
it's hard to um answer that question
computationally i think and mathematically when i put my mathematician hat on because i am trained as a mathematician you know it
depends what kind of limiting process you're using to get to infinitely many rooms what the right answer is there so
the answer is no i have not done much thinking of it and when you start to deal with things that are infinite in pi
mc or any probabilistic programming language this isn't a an inherent limitation of pi m c you run the same
problems with stan when you try to implement things like gaussian processes or dirichlet processes
where there are you know potentially infinitely many parameters uh it generally takes a lot of hard work
um to find good approximations or truncations there so i think that's a subtle question and the answer is not
really um and then uh
there's sorry there's another question in the q and a tab maybe you answered it but i'm not sure does the best yes i i i
think i did get get to that one so if i come back i probably have time for about one more chandra's final question maybe
from the chat so pomegranate mc pyro tf probability how is it different
from pimc or stan yeah so these are all different things that let you specify
basically likelihood functions right and some of them are just specifying likelihood functions some are
performing inference on all on likelihood functions um so
they are all adjacent right if you think about pi mc it's a way to specify a model
perform inference on that model and then rvs is a way to visualize and quantify the uh the
inference you've done on that model uh each of these hits some or all of those
things that pi mc does and has flexibility more or less flexibility
in some of those places right there's no one probabilistic programming package to rule them all right so there's a couple
different things you need to specify your priors you need to specify your observational likelihood you need to
perform inference you need to draw conclusions from that inference if you think of those things as kind of layers
in getting value out of any probability model uh each of these packages speaks
to one or more of those layers it does then it does each of those layers differently
that has strengths and weaknesses in terms of completeness and flexibility that vary by those layers and so
uh not really possible to give an exhaustive answer here but cover some of the same ground is the
answer does some things more or less flexibly does some things more or less user
friendly right one thing that i love to buy mc is when you look at i said m is equal to pm.normal you know m as a
string zero one that's quite close to the mathematical notation you would use to write that model down very user
friendly is what pi mc goes for things like uh mc make you write a log
likelihood function on your own tf.probability a little less user friendly
um so just you know depends which trade-off is right for you but they play in similar areas and you can assemble
some of those other tools together to cover the same use cases as you would imc here it all depends on where you
need flexibility and where you need need or want simplicity and ease of use
i think that that's probably a uh a good place to call it a day and thank you again reishma and data
umbrella team and meanwhile and oriole on the pi mc side for organizing things again it's been a a real pleasure to
speak to all of you here today
oh ray schwein i think you're muted i wanted to thank you austin for your
presentation
