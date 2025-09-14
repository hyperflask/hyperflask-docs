---
hide: [navigation, footer]
---
# Dropdown

Dropdown can open a menu or any other element when the button is clicked.

[Link to DaisyUI documentation](https://daisyui.com/components/dropdown/)


## Properties

| Property | Required | Type | Description |
|----------|----------|------|-------------|
|label|**Yes**|str||
|Any additional properties|No|any||

## Children

Accepts children of type:

| Component | Description |
|-----------|-------------|
| [DropdownItem](/components/daisyui/DropdownItem) | Use DropdownItem to create a clickable item in the dropdown. |


## Examples

Simple dropdown

```
<{Dropdown}>
  <{DropdownItem href="/page1"}>
    Item 1
  </{DropdownItem}>
  <{DropdownItem href="/page2"}>
    Item 2
  </{DropdownItem}>
</{Dropdown}>
```