---
hide: [navigation, footer]
---
# Why Hyperflask ?

The goal of the Hyperflask stack is to provide a single unified web stack, built on top of Python and proven technologies, where all components have been designed to work together seamlessly.

It intends to provide solo devs and small teams a solution that allows them to build and operate a website/web app with minimal boilerplate and overhead. All the focus can go to work on the actual product.

## Key goals

 - Full stack experience, from dev environment to UI framework to deployment
 - Backend driven with static content generation when needed
 - Great developer experience and high productivity
 - All the tech choices have been made so you don't need to ask yourself tech stack questions
 - Fully Open-Source stack that is 100% self-hostable if desired (no dependencies on cloud services)
 - Use proven technologies and rely on standards as much as possible
 - Built for pragmatical but professional production apps
 - Limit "magic", things should be understandable, evolvable and maintanable
 - Beginner friendly but well engineered for advanced use cases
 - Optimized for solo developers and small teams
 - Can run on cheap machines or VMs from any server/cloud providers

## Features and technologies

 - Web framework built on top of [Flask](https://flask.palletsprojects.com) as a set of extensions
 - File-based and/or app-based routing
 - A new file format combining python code in frontmatter and html templates to define routes
 - SQL focused ORM with [sqlorm](https://github.com/hyperflask/sqlorm), optimized for [sqlite](https://www.sqlite.org/)
 - Modern asset pipeline using [esbuild](https://esbuild.github.io/) and [tailwindcss](https://tailwindcss.com/)
 - Deep integration with [htmx](https://htmx.org/)
 - Easily create reusable backend and frontend components
 - Build frontend components using Web Components, [Alpine.js](https://alpinejs.dev/), [React](https://react.dev) and more. Mix technologies at will.
 - Component library based on [daisyUI](https://daisyui.com/) with icons from [Bootstrap Icons](https://icons.getbootstrap.com/)
 - Authentication and user management with social logins and MFA
 - Static content collections to easily create blogs and manage static content
 - File management with built-in image manipulation and S3 integration
 - Template based emails with [mjml](https://mjml.io) support
 - Background tasks using [dramatiq](https://dramatiq.io/) with sqlite as the default broker
 - Push support for realtime pages using [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
 - I18n using [gettext](https://www.gnu.org/software/gettext/)
 - Static, hybrid or dynamic modes for content serving
 - Dev environment based on [Development Containers](https://containers.dev/)
 - Deep integration with VS Code with full support for interactive debugging
 - Deploy to VPS or docker-based hosting in one command
 - Easy setup analytics and observability

## The Hyperflask umbrella

Many of the features of the Hyperflask framework are provided through Flask extensions and other libraries. A good portion of them are being developed under the Hyperflask umbrella. They are kept independant so they can be re-used in other projects outside of Hyperflask.

[Checkout the Github organization](https://github.com/hyperflask) for the list of projects.

## Reasoning

There are so many choices to make nowadays: what backend framework, what build tools, what frontend framework, how to deploy, how to easily develop locally, etc...  
The development world, and especially the javascript world, moves at a very fast pace. There is a lot of good stuff happening but at the same time it often feels overwhelming.

On top of the difficulty of selecting technologies, it seems we favor complexity over simplicity. Frameworks and libraries should aim to improve the life of developers with better DX not the opposite. I like the idea of [conceptual compression championned by DHH](https://www.youtube.com/watch?v=zKyv-IGvgGE&t=1037s). It is of course harder to make complicated things simple. We should keep innovating and finding better ways to program, [not just let React win because LLMs are well trained on it](https://www.youtube.com/watch?v=P1FLEnKZTAE)!

Backend driven architectures and javascript-light approaches simplifiy web development greatly. HTMX is a key piece of this renaissance of pre-heavy-frontend development. I'm hopeful as it seems SPA-everything as reached its apogee and the trend is shifting back, with the rise of SSR in the javascript world.

I do not find the direction React Server Components are following appealing. Blurring the line between frontend and backend has been tried before and it often leads to spaghetti code bases that are hard to maintain. It may make sense in Backend For Fronted architectures but I feel it is too complicated for most projects. Furthermore, I feel the backend building experience in javascript has never been great, far from python, php or rails.

At the same time, I feel the developer experience is lacking in many areas. There's so many moving parts to learn and manage, it's daunting. It's especially hard for beginners.

In the end, I love Python and Flask and want to continue building modern websites with them. Unfortunately, I felt a lot of extensions have become outdated and Flask being minimalist, no large scale frameworks around it. Hyperflask is my attempt to a super-powered Flask-based stack.

Finally, in the age of AI driven development, we shouldn't (yet) let AI generate tech architecture and core technologies. At the moment, AI is the perfect companion for product building, generating individual components and pages. Hyperflask is built with this in mind: to allow AI generation to operate at a very high level, limiting impact on core architectural choices and security implications.

## Acknowledgments

Hyperflask is inspired by many:

 - [Ruby on Rails](https://rubyonrails.org/) because of their backend-first, one man framework philosophy
 - [Astro](https://astro.build) for their page format, component islands and static content-first approach
 - [Jekyll](https://jekyllrb.com) for their content collections
 - [htmx](https://htmx.org/) for allowing to build web sites with minimal custom js
 - [Laravel](https://laravel.com/) for the everything included approach
 - and many other open source projects