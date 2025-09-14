---
hide: [navigation, footer]
---
# Pagination

Pagination is a group of buttons that allow the user to navigate between a set of related content.

[Link to DaisyUI documentation](https://daisyui.com/components/pagination/)


## Properties

| Property | Required | Type | Description |
|----------|----------|------|-------------|
|Any additional properties|No|any||

## Children

Accepts children of type:

| Component | Description |
|-----------|-------------|
| [PaginationPage](/components/daisyui/PaginationPage) |  |
| [PaginationPrev](/components/daisyui/PaginationPrev) |  |
| [PaginationNext](/components/daisyui/PaginationNext) |  |


## Examples

```
<{Pagination}>
  <{PaginationPrev href="/page1"}/>
  <{PaginationPage href="/page1"}>
    1
  </{PaginationPage}>
  <{PaginationPage href="/page2" active=True}>
    2
  </{PaginationPage}>
  <{PaginationPage href="/page3"}>
    3
  </{PaginationPage}>
  <{PaginationNext href="/page3"}/>
</{Pagination}>
```