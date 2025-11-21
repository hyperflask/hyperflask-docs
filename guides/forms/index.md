# Forms

Easily define forms that can be validated on the frontend and the backend.

!!! info
    This feature is provided by [Jinja-WTForms](https://github.com/hyperflask/jinja-wtforms)

## Creating forms in templates

Create forms in templates by calling fields on a `form` object as if they would be already declared. The syntax for calling fields is slightly different compared to raw wtforms as it also includes the field type.

```jinja
{# signup.html #}
<{Form form}>
    <{FormField form.firstname.text("First name") }/>
    <{FormField form.lastname.text("Last name") }/>
    <{FormField form.email.email("Email", required=True) }/>
    <{FormField form.password.password("Password", required=True) }/>
    <{SubmitButton}>Signup</{}>
</{Form}>
```

!!! info
    This example uses built-ins UI form components

Field declarations look like `form.field_name.field_type(label, **options)`. Available field types: checkbox, decimal, date, datetime, float, int, radio, select, selectmulti, text, textarea, password, hidden, datetimelocal, decimalrange, email, intrange, search, tel, url, file, files.

Field types map to their equivalent wtforms field definition.

The [`{% form %}` directive](https://github.com/hyperflask/jinja-wtforms?tab=readme-ov-file#the-form-directive) can also be used before a form declaration. When used, a form object will be automatically created if none are provided. This directive also allows to customize the class name and declare multiple forms per template.

## Validating data on the backend

The process is the same as [using Wtforms](https://wtforms.readthedocs.io/en/3.1.x/forms/#using-forms).

To make things easier, when using pages, forms declared inside pages are available through `page.form` and `page.forms`. (It also works for components)

Example page:

```jpy
---
form = page.form()
def post():
    if form.validate():
        # do something with form.data
---
<{Form form}>
    <{FormField form.name.text("Name", required=True) }/>
    <{SubmitButton}>Signup</{}>
</{Form}>
```

## Forms outside pages

Forms can be defined in any template. It is recommended to use the `{% form %}` directive as it will ensure a form object is always available.

Form classes can be accessed through `app.forms[template_filename]`.

## Form components

Hyperflask includes some [form related UI components](/components/forms) to build beautiful apps. Input widgets are also automatically styled.

`<{Form}/>` can be used as an alternative to the form tag. It takes the form object as the first positional argument.

Use `<{FormField }/>` with the field as first argument to display a field correctly.

## Posting forms using HTMX

`<{HxForm}/>` can be used to create htmx powered forms. Use `action=url` as usual to define the form target. The form will be automatically resetted on successful submit.