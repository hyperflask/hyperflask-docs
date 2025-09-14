---
hide: [navigation, footer]
---
# Drawer

Drawer is a grid layout that can show/hide a sidebar on the left or right side of the page.

[Link to DaisyUI documentation](https://daisyui.com/components/drawer/)


## Properties

| Property | Required | Type | Description |
|----------|----------|------|-------------|
|id|No|str||
|open|No|bool||
|responsive|No|str (one of: xs, sm, md, lg, xl)||
|end|No|bool||
|Any additional properties|No|any||

## Children

Accepts children of type:

| Component | Description |
|-----------|-------------|
| [DrawerContent](/components/daisyui/DrawerContent) |  |
| [DrawerSide](/components/daisyui/DrawerSide) |  |


## Examples

Navbar menu for desktop + sidebar drawer for mobile

```
<{Drawer id="drawer1"}>
  <{DrawerContent}>
    <{Navbar sidebar_toggle="drawer1" sidebar_toggle_responsive="lg"}/>
  </{DrawerContent}>
  <{DrawerSide id="drawer1"}>
    <{Menu}/>
  </{DrawerSide}>
</{Drawer}>
```