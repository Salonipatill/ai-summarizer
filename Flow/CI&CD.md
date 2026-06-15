## CI/CD

Continuous Integration/Continuous Delivery or deployment


# consists of two steps:-

when we automate BUild and test steps. it is  called continuous integration.

# And

When we automate deployment step . so it is called continuous deployments


Develop -> Build -> Test -> Release[Deploy]


## Three main environments

1. Dev environment[only for developers]

2. Staging environment[preproduction  environments]

3. prod  environment[only for end users]



# there is few difference between continuous delivery and continuous deployment.


in continuous delivery when we deployed our application on the staging environments and then we want to deploy on the prod environment so there is involved a  manual  step.


# continuous delivery:-
deploy staging->test->manual approval->deploy prod

# continuous deployment:-
deploy staging ->test->deploy prod

To solve  problem of integration hell we use CI/CD

## CI/CD Tools:-

Github Action->2019

Jenkins->2011

Travis CI

Gitlab CI CD

Bamboo ......


## Deployment Strategies:-

# 1. Blue Green

create two identical and saperate environments
            
            redirect all traffic
curr-----------------------------------> new 
v1                                        v2

if any problem comes so [traffic will be back]
curr<---------------------------------------------------new


# 2. Canary deployment:-

first few traffic redirect then if all good so then 50% traffic then 70% then  100% traffic redirect[progessively redirect]

curr-----------------------------------> new 
v1                                        v2


# 3. Rolling deployment:-














