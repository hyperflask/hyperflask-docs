# Forms

Use the `Form` component with a form object to write the form tag. Use `HxForm` instead of `Form` for an HTMX powered form instead.

```jinja
<{Form form action="..."}>
    
</{Form}>
```

!!! tip
    The component will automatically wrap its inner components with a fieldset. Use `fieldset=False` in the component props to disable.

Use `FormField` components to style fields properly:

```jinja
<{Form form}>
    <{FieldsetLegend}>Login</{}>

    <{FormField form.email.email("Email") }/>
    <{FormField form.password.password("Password") }/>

    <{SubmitButton}>Login</{}>
</{Form}>
```

Use the `form-w-full` call on the form tag for full width forms.

## Styling forms without the Form component

Follow the DaisyUI pattern:

```jinja
<{Fieldset}>
    <{FieldsetLegend}>Login</{}>

    <{Label}>Email</{}>
    <{Input type="email" }/>

    <{Label}>Password</{}>
    <{Input type="password" }/>

    <{Button type="submit" color="neutral"}>Login</{}>
</{Fieldset}>
```