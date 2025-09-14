---
hide: [navigation, footer]
---
# Filter

Filter is a group of radio buttons. Choosing one of the options will hide the others and shows a reset button next to the chosen option.

[Link to DaisyUI documentation](https://daisyui.com/components/filter/)


## Properties

| Property | Required | Type | Description |
|----------|----------|------|-------------|
|name|**Yes**|str||
|reset-label|No|str||
|color|No|str (one of: primary, secondary, accent, neutral, success, warning, info, error)||
|size|No|str (one of: xs, sm, md, lg, xl)||
|Any additional properties|No|any||

## Children

Accepts children of type:

| Component | Description |
|-----------|-------------|
| [FilterItem](/components/daisyui/FilterItem) |  |


## Examples

```
<{Filter}>

</{Filter}>
```