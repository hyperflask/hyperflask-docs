---
hide: [navigation, footer]
---
# Tabs

Tabs can be used to show a list of links in a tabbed format.

[Link to DaisyUI documentation](https://daisyui.com/components/tabs/)


## Properties

| Property | Required | Type | Description |
|----------|----------|------|-------------|
|style|No|str (one of: box, border, lift)||
|size|No|str (one of: xs, sm, md, lg, xl)||
|Any additional properties|No|any||

## Children

Accepts children of type:

| Component | Description |
|-----------|-------------|
| [Tab](/components/daisyui/Tab) |  |


## Examples

```
<{Tabs}>
  <{Tab label="Tab 1"}>
    Content for tab 1
  </{Tab}>
  <{Tab label="Tab 2"}>
    Content for tab 2
  </{Tab}>
</{Tabs}>
```