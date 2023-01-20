---
id: lock-n-key 
title: Lock-n-Key
sidebar_label: Lock-n-Key
---
This project came out of some brainstorming at work.  The idea was to build a physically randomized key that could be easily made, and then read, using light.  I spent part of a couple of weekends working on it, and it was really entertaining, with a number of really interesting learnings.  In the end, this was [granted a patent](https://patents.google.com/patent/US20210019387A1/en?oq=US2021019387A1)!

## Overview

This came about from an Innovation Lab discussion where at the end, for whatever reason, I was thinking about whether or not you the interference of light patterns could be read in such a way as to be a key that would be hard to duplicate.  Then I thought about actually actively disturbing the light in ways that couldn't be replicated.  Then I was off and running.

One of the fundamental challenges with security is randomness.  It is incredibly hard to get right in the digital world, but in the physical world, it's a bit easier.  (As an aside, one of my favorite ways is the [Lava Lamp Wall](https://www.cloudflare.com/learning/ssl/lava-lamp-encryption/) ).  There are a lot of things that happen in ways that aren't possible to deterministically predict.

## Resin "keys"

When you normally make resin projects, your goal is to limit the number of bubbles that form.  You do this through either heating it up, pressurizing it, or using vacuum.  But, if you're trying to make a randomized key, they could be awesome.  In fact, I think they could be virtually impossible to replicate.  I happened to have resin around from a prior project (I'm sure all of you have it at home as well, right?), so I created a quick form and poured a block of resin, and stirred it around.  I tried adding some food coloring to increase it even more, but that didn't work out very well.  Then I just let it sit for a a day or two, before cutting it into blocks and polishing it up to be clear.


*  3D printed "lock"
*  Arduino with LED or laser being read by photoresistors
  *  Code to do the various pulsing and reading

## External links
* [Multi-factor authentication utilizing non-centralized key creation with physical randomness](https://patents.google.com/patent/US20210019387A1/en?oq=US2021019387A1)
