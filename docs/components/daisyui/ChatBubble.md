---
hide: [navigation, footer]
---
# ChatBubble

Chat bubbles are used to show one line of conversation and all its data, including the author image, author name, time, etc.

[Link to DaisyUI documentation](https://daisyui.com/components/chat/)


## Properties

| Property | Required | Type | Description |
|----------|----------|------|-------------|
|reply|No|bool||
|avatar|No|str||
|avatar-alt|No|str||
|header|No|str||
|footer|No|str||
|color|No|str (one of: primary, secondary, accent, neutral, success, warning, info, error)||
|Any additional properties|No|any||

## Children

Accepts any HTML content

## Examples

```
<{ChatBubble}>

</{ChatBubble}>
```