## meta-api

meta-api is an API that I will be using for varying purposes, e.g. an endpoint that I can use for any Slack apps that I create, content for a website that I might build, etc. Because I'll be using it for perhaps many different things, it's sort of an API for other more single-purpose APIs. ~It is hosted on Heroku at https://raghav-meta-api.herokuapp.com !~

### Deployment

meta-api was deployed on Heroku (Free Tier) using the GitHub Deployment method, Automatic Deploys on push to `master` enabled. **NOTE: Starting November 28, 2022, free Heroku Dynos, free Heroku Postgres, and free Heroku Data for Redis® will no longer be available. As such the Heroku deployment has been removed.**

### Background

A little backstory: My friend circle uses Slack as our group chat (we love channels, threads, and customizations). I wanted to make a Slack app, but I needed to create and host REST endpoints for the the app to send requests to. The app itself is quite small (in theory), so I didn't exactly want to waste a whole server for just one app. I decided to make it abstract enough so that in the future, if I wanted to build more Slack apps, we could simply update this project, without having to host another server to have to query. Also I aim to use this server and expose more endpoints for other projects (perhaps as a CMS for a personal website).

### Current APIs

- Slack App:

    - Hello: 
        - Description: A dummy app that echoes the name of the command used in the POST request along with whatever args were passed with the request
        - Endpoints: 
            - `/slack/apps/hello/fakeCommand`

    - Groupy:
        - Description: Groupy manages user groups, a feature that doesn't exist on Slack's free tier! (Note: Didn't think this functionality should need to be able to access Slack, leaving the responsibility of providing the proper arguments to the app which hits this endpoint, i.e., the Slack app)
        - Endpoints:
            - `/slack/apps/groupy/create` : Needs "TeamId", "GroupName", and "Users" 
            - `/slack/apps/groupy/add-to`: Needs "TeamId", "GroupName", and "Users"
            - `/slack/apps/groupy/remove-from`: Needs "TeamId", "GroupName", and "Users"
            - `/slack/apps/groupy/list-members`: Needs "TeamId", "GroupName"
            - `/slack/apps/groupy/list`: Needs "TeamId"
            - `/slack/apps/groupy/delete`: Needs "TeamId", "GroupName"
            - `/slack/apps/groupy/tag-group`: Needs "TeamId", "GroupName"
        - Misc:
            - To store this information we use MongoDB's Atlas, and to run and test this feature locally one needs only to have a local Mongo instance running on the default port.

### Notes

- Ensure local Mongo instance is up and running on port 27017 (If I want to test groupy slack app features locally)

- Run with Makefile: `make run`
