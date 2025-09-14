---
hide: [navigation, footer]
---
# Menu

Menu is used to display a list of links vertically or horizontally.

[Link to DaisyUI documentation](https://daisyui.com/components/menu/)


## Properties

| Property | Required | Type | Description |
|----------|----------|------|-------------|
|horitzontal|No|bool||
|size|No|str (one of: xs, sm, md, lg, xl)||
|Any additional properties|No|any||

## Children

Accepts children of type:

| Component | Description |
|-----------|-------------|
| [MenuItem](/components/daisyui/MenuItem) | Use MenuItem to create a clickable item in the menu. |
| [MenuTitle](/components/daisyui/MenuTitle) | Use MenuTitle to create a title for a section in the menu. |
| [SubMenu](/components/daisyui/SubMenu) | Use SubMenu to create a nested menu with a title and items. |
| [CollapsibleSubMenu](/components/daisyui/CollapsibleSubMenu) | Use CollapsibleSubMenu to create a nested menu that can be expanded or collapsed. |


## Examples

Simple menu

```
<{Menu}>
  <{MenuItem}>
    Item 1
  </{MenuItem}>
  <{MenuItem}>
    Item 2
  </{MenuItem}>
</{Menu}>
```

Simple menu with title

```
<{Menu}>
  <{MenuTitle}>
    My menu
  </{MenuTitle}>
  <{MenuItem}>
    Item 1
  </{MenuItem}>
</{Menu}>
```

With submenu

```
<{Menu}>
  <{MenuItem}>
    Item 1
  </{MenuItem}>
  <{SubMenu label="Parent"}>
    <{MenuItem}>
      Child 1
    </{MenuItem}>
    <{MenuItem}>
      Child 2
    </{MenuItem}>
  </{SubMenu}>
</{Menu}>
```