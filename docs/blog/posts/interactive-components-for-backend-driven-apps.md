---
date: 2026-07-19
authors:
  - maximebf
---
# Interactive components for backend-driven apps.

Components are one of the best ideas popularized by frontend frameworks.

A component gives a name and a boundary to a piece of UI. It can receive properties, contain other components and hide its implementation behind a small interface. Once you get used to thinking this way, going back to large templates made of loosely related includes and macros can feel limiting.

Yet components are still mostly treated as a frontend concept.

In traditional backend applications, reusable HTML is usually passive. A template partial or macro can render a form, a table or a dialog, but once that piece of UI becomes interactive, its implementation often spreads across several places: markup in a template, request handling in a Python route, and JavaScript responsible for sending the request or updating the page.

Frontend frameworks solve this by moving the component, its state and its behavior into the browser. This creates a coherent development model, but it often means building a frontend application alongside the backend application.

Hyperflask explores another option: treating components as backend abstractions.

A backend component can receive properties, contain children and compose other components. It can also run Python code and expose HTTP endpoints.

When called through HTMX, the component handles the request and returns the HTML representing its new state. HTMX then replaces the relevant part of the page.

The component becomes both a reusable unit of rendering and an addressable unit of interaction. It does not need to maintain a second representation of the application state in the browser. It accepts a request, calls regular Python code and returns HTML.

Supporting this model required more than a few helpers around Flask. Hyperflask introduced two related projects to make backend components feel natural.

The first is **jinja-super-macros**, which adds a component-oriented syntax to Jinja.

Instead of calling a macro like a function and relying on conventions for passing blocks of content, a component can be invoked with syntax such as `<{Card}>...</{Card}>`. Properties are declared alongside the component name, while nested content becomes its children.

The result looks closer to HTML and to the component syntax used by frontend frameworks, while remaining based on Jinja macros.

The second is **JinjaPy**, a new file format created by the Hyperflask project to support this vision. A JinjaPy file combines Python frontmatter with a Jinja template, allowing the code responsible for preparing or handling a component to live next to its markup.

Putting Python and HTML in the same file may initially look like a violation of separation of concerns. But separation of concerns does not necessarily require separation by file type.

The endpoint that opens a dialog is closely related to the template for that dialog. When its fields change, both usually change. When the component disappears, both disappear. Co-locating them makes that relationship explicit.

That does not mean moving business logic into templates. Domain logic, authorization rules and reusable operations still belong in ordinary Python modules, models and services. The component handles the web-facing part of the feature: reading the request, calling the relevant application code and deciding which HTML to return.

This approach also changes the boundary between the backend and the browser.

SPAs commonly use JSON APIs because the frontend and backend are independent applications. In a backend-driven application, that separation is not always necessary. When the browser ultimately needs HTML, the server can return the updated representation directly.

The browser reports an interaction, the server processes it, and HTMX places the resulting HTML in the page. There is less need to reproduce rendering decisions and application state on both sides.

Backend-driven does not mean that every interaction must go through the server. Dropdowns, tabs and other local states are usually better handled in the browser. Hyperflask components can include Alpine.js, Web Components or framework-based components when they are useful.

This is partly inspired by Astro’s component islands: different parts of a page can use different levels of client-side interactivity rather than forcing the entire application into a single frontend architecture.

Hyperflask applies a similar idea to backend-driven applications. One component may be entirely server-rendered. Another may use HTMX for server interactions. A third may contain local JavaScript, while a particularly rich feature may be implemented as a frontend island.

The choice can be made at the level of the component rather than for the whole application.

Backend-driven apps will not suit every use cases. Applications with substantial offline behavior, complex local state or highly interactive editing tools may need more responsibility in the browser.

But for applications built largely around forms, tables, filters and server-side workflows, they offer an interesting way to combine component-based design with a Python-centered architecture.

Jinja-super-macros provides the composition model, JinjaPy brings Python and markup together, and HTMX connects components to the browser through regular HTTP and HTML.

Hyperflask is an attempt to see how far that combination can go.
