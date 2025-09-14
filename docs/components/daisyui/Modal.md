---
hide: [navigation, footer]
---
# Modal

Modal is used to show a dialog or a box when you click a button.

[Link to DaisyUI documentation](https://daisyui.com/components/modal/)


## Properties

| Property | Required | Type | Description |
|----------|----------|------|-------------|
|close-btn|No|bool||
|open|No|bool||
|position-x|No|str (one of: start, end)||
|position-y|No|str (one of: top, middle, bottom)||
|responsive|No|bool||
|width|No|str||
|large|No|bool||
|no-blur|No|bool||
|Any additional properties|No|any||

## Children

Accepts children of type:

| Component | Description |
|-----------|-------------|
| [ModalAction](/components/daisyui/ModalAction) |  |
| [ModalTitle](/components/daisyui/ModalTitle) |  |


## Examples

```
<{Modal}>

</{Modal}>
```