# Introduction

I have a problem.  Ok, I have several, but in this context, there is one major one.  

I've never had a problem I'm interested in solving that I can't solve faster in [Perl](http://www.perl.org) than in [Python](http://www.python.org), because I learned Perl back in 19 _cough_ _cough_ and haven't needed to learn Python.

Then came COVID.  Now I have a problem, and it's not time sensitive, so why not?

# Problem Statement

Ok, straight up, this is incredibly geeky.  Probably over the top.  I get that.  Just go with me.

Because of COVID all I wear, every day, is short-sleeved tshirts and shorts.  Yes, I live in Arizona, so it makes more sense.  

But:

1. I don't want to just wear the same color shirt day after day.
2. I don't want to wear the same "themed" shirt day after day.
3. When my lovely wife does the laundry, she has the audacity to wash colors, darks and lights separately.
  1. As a result the shirts get clumped together by colors
4. I want to avoid decision fatigue and make it so I can just grab the next shirt, without violating 1 and 2.

# Solution

Write a python program that gives me an ordered list of shirts where neither colors nor themes repeat themselves.  Then every 30 days or so I just follow the output and order them, and I'm good for a month.

Note, as I point out in the code, I suspect there is an optimized solution to this using set/matrix math.  So I think I have a math problem masquerading as a programming challenge.  My quick Google searches didn't provide me a simple answer, so away I went.

## A note on colors and themes

I ended up "clumping" both of these.  

### Themes

These breakdown into a few broad categories that made sense to me.

* Company:  Shirts from the company I work for.  Mostly blue and light grey.
* Running:  (non-tech) Shirts I have from running events.  Primarily [Ragnar Trails](http://www.runragnar.com) and [Aravaipa](https://www.aravaiparunning.com/).
* Ohack:  [Opportunity Hack](https://www.aravaiparunning.com/) volunteer/hacker shirts.  I also include my capstone shirt in that.  These are my most colorful.
* Fatty:  I have several standard shirts and several 100 Miles to Nowhere shirts from [Fat Cyclist](http://fatcyclist.com/).  I'm not sure where he's writing anymore, but they're comfortable and the designs are great.  Mostly black/dark grey.
* Other:  None of the above, but small numbers.  

### Colors

Breaking out each color separately didn't really do what I wanted.  I could have really dark grey next to black, and it would really look like back to back, black to black.  Or I could have light red and pink right next to each other, so I clumped these too.

* Dark grey/black
* Light grey
* Blue (my company's colors are blue and blue.  So a lot of my shirts end up that or light grey)
* ROP == Red, Orange, Pink
* Green
* Other

# Code

So, I decided to start with an IDE, and that was [PyCharm](https://www.jetbrains.com/pycharm/).  Works great. But.  It started up a venv with python 2.7.  Even I knew python 2 was EOLd, but I went with it for the first version.  Then I had to get pycharm to start a python3 venv and port my code, and that's what I did.  

If anyone is looking at this code trying to judge my software dev capabilities and needs a reason to not hire me, I will refer to these as:

* [Exhibit A](shirt3.py)
* [Exhibit B](sort.py)


