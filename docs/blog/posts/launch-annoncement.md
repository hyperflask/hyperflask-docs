---
date: 2025-10-14
pin: true
authors:
  - maximebf
---
# Launch annoncement

After 2 years of working on & off on Hyperflask, I'm happy to finally announce a working version that can be used to create actual production apps ! Although it is still in beta, all the desired features are present and working.

In reality, Hyperflask is more than 10 years in the making ! My previous attempt at a comprehensive framework went nowhere but some of its ideas survived. The rise of [htmx](https://htmx.org/) and the revival of backend driven apps led me to get excited again.

Backend-driven apps using something like htmx are not an answer to all type of web development. However, I'm convinced that they provide a solution for 80% of use cases (if not more) while simplying greatly the development experience, the cognitive load and the many footguns that frontend-heavy frameworks bring.

I love [Flask](https://flask.palletsprojects.com/) as a framework but unfortunately, a lot of Flask extensions are barely maintained. In the meantime, other frameworks have introduced amazing innovations that greatly simplify the developer experience. Hyperflask is my attempt at synthetizing all the parts I like across various technologies and frameworks in a coherent stack. Integration between each chosen technology should be completely seamless.

Among these innovations, notable ones are:

 - [File-based routing](/guides/pages/) with a [new file format](https://github.com/hyperflask/jinjapy) that combines some python code and a jinja template, inspired by [Astro pages](https://docs.astro.build/en/basics/astro-pages/#astro-pages)
 - [A component system](/guides/components/) inspired by frontend frameworks and [Astro islands](https://docs.astro.build/en/concepts/islands/). It can be used to create frontend or backend components. Components can have their own endpoints.
 - Using streaming content to [display loaders](/guides/suspense/), inspired by [React Suspense](https://react.dev/reference/react/Suspense)
 - [Static content](/guides/static/) generation with collections, inspired by [Jekyll](https://jekyllrb.com/)

More than just a framework, **Hyperflask is a truly full stack solution**. From dev environments, to UI framework to deployments.  
On top of the previously mentionned features, Hyperflask provides:

 - Deep integration with [htmx](https://htmx.org/)
 - An easy to use and [powerful ORM](https://github.com/hyperflask/sqlorm) that stays close to SQL
 - A large library of [UI components](/components/) powered by [Tailwind](https://tailwindcss.com/), [DaisyUI](https://daisyui.com/) and [Bootstrap Icons](https://icons.getbootstrap.com/)
 - A modern assets pipeline using [esbuild](https://esbuild.github.io/) with image optimizations
 - [Server push](/guides/push/) for realtime updates using SSE, based on the [Mercure protocol](https://mercure.rocks/)
 - [Template based emails](/guides/emails/) powered by [MJML](https://mjml.io/)
 - Background tasks
 - Translations
 - Dev environments based on [dev containers](https://containers.dev/)
 - Deployments using containers

All the technologies used by Hyperflask have been carefully selected for their quality, developer experience, ease of use, feature set and popularity.

The framework is optimized to limit "magic" features while ensuring ease of use. React Server Components or Phoenix LiveView are impressive but they hide too many things, often leading to many footguns and hacks around them. In Hyperflask, everything is just Python, standard Flask and Jinja with jinjapy files and htmx as the binding agent.

One of my side goals with Hyperflask is to revive and modernize the Flask ecosystem. As a result, **almost all of the features listed before have been developed as independent Flask extensions**. Hyperflask itself is mostly glue code to make them work together. [Pick and choose the extensions](https://github.com/hyperflask) you want for your own projects.

In the same spirit, there are some projects developed as part of Hyperflask that can be used indepently of Flask:

 - [sqlorm](https://github.com/hyperflask/sqlorm), a performant and straighforward ORM that does not attempt to hide SQL
 - [jinjapy](https://github.com/hyperflask/jinjapy), a new file format that combines python code and a jinja template
 - [jinja-super-macros](https://github.com/hyperflask/jinja-super-macros), a new syntax to call macros in jinja
 - [uilib-spec](https://github.com/hyperflask/uilib-spec), a specification to generate bindings for UI component libraries (see [uilib-spec-daisyui](https://github.com/hyperflask/uilib-spec-daisyui) for a use case)

All these projects are available on the [Hyperflask Github organization](https://github.com/hyperflask).

Check out the [Getting Started](/getting-started) tutorial, read more about the [goals, technologies and reasoning](/why) behind the project or [deep dive into the guides](/guides/setup).

PS: I've already used Hyperflask to build [SQLify](https://sqlify.me/) as part of my job at [Digicoop](https://digicoop.io) / [Kantree](https://kantree.io) and the experience was very satisfying.


