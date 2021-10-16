# Social Bot
## High Level Plan 
1. [ ] Build mock social media platform with 
    1. [ ] ui (to write posts and read responses)
    1. [ ] api (to read posts and respond to posts)
1. [ ] build chat bot that can
    1. [ ] scan platform for some keywords
    1. [ ] apply hate analysis 
    1. [ ] check for trigger, to release counter media, if so, respond with counter media 
1. [ ] counter media library


## Scoring mechanism 
build hate profile vector with a score per category detecting hate towards a given group such that the score is equal to the sum of weighted incidents 

h = vector of [h_0, h_1, ...., h_n ]

h_c = Sum_i gamma ^ {delta t} . h(i,c)
where:
* h_c is the hate category score
* gamma is a tuning parameter from 0 to 1 
* delta t is time since post
* h(i,c) is the hate score of a given incident i, can be collected from a lookup table, give it value 1 as a start 

## Countering mechanism
define threshold map T with n categories and m escalations
each post hate score (h) is measured against T map and corresponding escalation responses are picked and sent in random intervals 

### example

hate score h = [0.3, 0.9, 0.01] 
T = [
    [0.1, 0.5, 0.5]
    [0.2, 0.75, 0.8]
    [0.3, 1.0, 1.2]
    [0.5, 1.25, 1.5]
]

this will;  send out response -> r = [3, 2, 0] 


####  Example Vulnerable Groups
* Muslims 
* Women 
* Immigrants 

Type        | Escalation 1 | Escalation 2 
------------|--------------|----------
Muslims     | Contribution of Muslims in Canada | Notable Muslims in the community 
Women       | Myths about women | You couldn't exist without a mom 
Immigrants  | |
