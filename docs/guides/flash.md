# Flash messages

Flask [provides a mechanism](https://flask.palletsprojects.com/en/stable/patterns/flashing/) for showing one time messages to the user.

Use `flash()` or `page.flash()` as described by Flask documentation.

Hyperflask will automatically print the messages as [alert messages in a toast](https://daisyui.com/components/toast/). This will also work when flashing messages during ajax requests.