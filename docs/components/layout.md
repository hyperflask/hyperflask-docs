# Layout

Hyperflask includes a few utilties to help you design your app quickly.

## Common app UI

Use the following snippet to kick start a very common application UI with a sidebar:

```jinja
<{AppUI}>
    <{Viewport}>

    </{Viewport}>
    <{Sidebar}>

    </{Sidebar}>
</{AppUI}>
```

Use the [Menu](/components/daisyui/Menu) component to create menus in the sidebar.

Viewport is a vertical flexbox with overflow by default. Use `<{Viewport overflow=False}>` for no overflowing.

## Flex boxes

Use `<{HBox}>` and `<{VBox}>` for respectively row and column flexbox with a gap between each items.

Use `<{CenterBox}>` for a box which content is vertically and horizontally centered.

Use `<{Spacer}/>` to add a growing div that takes all the space between 2 items.