---
hide: [navigation, footer]
---
# Avatar

Avatars are used to show a thumbnail representation of an individual or business in the interface.

[Link to DaisyUI documentation](https://daisyui.com/components/avatar/)


## Properties

| Property | Required | Type | Description |
|----------|----------|------|-------------|
|src|No|str||
|placeholder|No|str||
|placeholder-text-size|No|str||
|alt|No|str||
|rounded|No|bool||
|size|No|int|float||
|mask|No|str (one of: squircle, heart, hexagon, hexagon-2, decagon, pentagon, diamond, square, circle, star, star-2, triangle, triangle-2, triangle-3, triangle-4, half-1, half-2)||
|presence|No|str (one of: online, offline)||
|indicator|No|str||
|indicator-color|No|str (one of: primary, secondary, accent, neutral, success, warning, info, error)||
|indicator-position-x|No|str (one of: start, center, end)||
|indicator-position-y|No|str (one of: top, middle, bottom)||
|Any additional properties|No|any||

## Examples

```
<{Avatar}/>
```