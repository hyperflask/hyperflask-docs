---
hide: [navigation, footer]
---
# Why Hyperflask ?

The goal of the Hyperflask stack is to provide a single unified web stack, built on top of Python and proven technologies, where all components have been designed to work together seamlessly.

It intends to provide solo devs and small teams a solution that allows them to build and operate a website/web app with minimal boilerplate and overhead. All the focus can go to work on the actual product.

## Key goals

 - Full stack experience, from dev environment to UI framework to deployment
 - All the tech choices have been made so you don't need to ask yourself tech stack questions
 - Fully Open-Source stack that is 100% self-hostable if desired (no dependencies on cloud services)
 - Use proven technologies and rely on standards as much as possible
 - Backend driven with static content generation when needed
 - Built for pragmatical but professional production apps
 - Great developer experience and high productivity
 - Beginner friendly but well engineered for advanced use cases
 - Optimized for solo developers and small teams
 - Can run on cheap machines or VMs from any server/cloud providers
 - Respect privacy and limit data collection (GDPR compliant by default)

## Features and technologies

 - Web framework built on top of [Flask](https://flask.palletsprojects.com) as a set of extensions
 - File-based and/or app-based routing
 - A new file format combining python code in frontmatter and html templates to define routes
 - SQL focused ORM with [sqlorm](https://github.com/hyperflask/sqlorm), optimized for [sqlite](https://www.sqlite.org/)
 - Modern asset pipeline using [esbuild](https://esbuild.github.io/) and [tailwindcss](https://tailwindcss.com/)
 - Easily create reusable components for your templates, compatible with [Storybook](https://storybook.js.org)
 - Component library based on [daisyUI](https://daisyui.com/) with icons from [Bootstrap Icons](https://icons.getbootstrap.com/)
 - Deep integration with [htmx](https://htmx.org/)
 - Seamless reactivity between frontend and backend
 - Authentication and user management with social logins and MFA
 - Static content collections to easily create blogs and manage static content
 - File management with built-in image manipulation and S3 integration
 - Template based emails with [mjml](https://mjml.io) support
 - Background tasks using [dramatiq](https://dramatiq.io/)
 - Push support for realtime pages using [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
 - [PWA](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps) support (with web push support)
 - I18n using [gettext](https://www.gnu.org/software/gettext/)
 - Static, hybrid or dynamic modes for content serving
 - Good debugging experience with [debugpy](https://github.com/microsoft/debugpy) and [Flask-DebugToolbar](https://flask-debugtoolbar.readthedocs.io) dev tools
 - Observable with [OpenTelemetry](https://opentelemetry.io/)
 - Dev environment based on [Development Containers](https://containers.dev/)
 - Provisioning and containerized deployments using [OpenTofu](https://opentofu.org) and [Ansible](https://www.ansible.com)

## The Hyperflask umbrella

Many of the features of the Hyperflask framework are provided through Flask extensions and other libraries. A good portion of them are being developed under the Hyperflask umbrella. They are kept independant so they can be re-used in other projects outside of Hyperflask.

[Checkout the Github organization](https://github.com/hyperflask) for the list of projects.

## Reasoning

There are so many choices to make nowadays: what backend framework, what build tools, what frontend framework, how to deploy, how to easily develop locally, etc...  
The development world, and especially the javascript world, moves at a very fast pace which feels overwhelming and hard to keep track. There is a lot of good stuff happening but at the same time it often feels needlessly over engineered. The focus is mostly on frontend frameworks and the javascript stack.

I think the "SPA everything" trend has reach its apogee. I never understood why use frontend component frameworks to build blogs as SPA apps. It seems ridiculous. This trend is shifting, with the rise of SSR in the javascript world. But it feels like they are rediscovering water.

I do not find the direction React Server Components are taking appealing. Blurring the line between frontend and backend has been tried before and it often leads to spaghetti code bases that are hard to maintain. Furthermore, I feel the backend building experience in javascript has never been great, far from python, php or rails.

At the same time, I feel the developer experience is lacking in many areas. There's so many moving parts to learn and manage, it's daunting. It's especially hard for beginners.

In the end, I love Python and Flask and want to continue building modern websites with them. Unfortunately, I felt a lot of extensions have become outdated and Flask being minimalist, no large scale frameworks around it. Hyperflask is my attempt to a super-powered Flask-based stack.

Hyperflask aims to be the Laravel of the Python world.

## Acknowledgments

Hyperflask is inspired by many:

 - [Ruby on Rails](https://rubyonrails.org/) because of their backend-first, one man framework philosophy
 - [Astro](https://astro.build) for their page format and static content-first approach
 - [Jekyll](https://jekyllrb.com) for their content collections
 - [htmx](https://htmx.org/) for allowing to build web sites with minimal custom js
 - [Laravel](https://laravel.com/) for the everything included approach
 - and many other open source projects