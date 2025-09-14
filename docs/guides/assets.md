# Assets

Hyperflask integrates esbuild to bundle assets and tailwind for styles.

!!! info
    This feature is provided by [Flask-Assets-Pipeline](https://github.com/hyperflask/flask-assets-pipeline)

## Static assets

Static assets can be located in 2 different folders:

 - *app/assets*: files located here will be copied to the *public* folder when the app is built. A hash will be appended to the filename for cache busting. URLs for these files should be created using `asset_url(filename)`
 - *public*: files located here are left untouched and are directly accessible from the web. URLs for these files should be created using `static_url(filename)`

## Embedded scripts and styles

You can define scripts and styles directly in your templates. Their content will be extracted and bundled automatically.

Add the `bundle` attribute to your script and style tags to extract and bundle them.

Example *components/Datatable.html* template:

```html
<table class="datatable">
    <!-- ... -->
</table>

<script bundle>
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".datatable").forEach(table => {
        // ...
    });
});
</script>

<style bundle>
.datatable {
    /* ... */
}
</style>
```

When this component is used as part of your request, its associated assets will be automatically included.

You can import any javascript package from node_modules in the script tag as it will be bundled using esbuild.

> [!IMPORTANT]
> No jinja directives can be used inside the bundled script and style tags

> [!NOTE]
> Extracted assets will be stored in your assets folder.  
> You can customize the name of the extracted files using a value for the bundle attribute: `<script bundle="filename.js">`

## Styling

Hyperflask uses [Tailwind](https://tailwindcss.com/) for styling. It is fully integrated and you can use tailwind utility classes across pages and components.

## Bundles

You can create bundles compiled using esbuild. Bundles need to be declared in the configuration. Bundles can be js or css files.

Let's imagine a file located at *app/assets/app.js*. Create a bundle for it by adding the following in *config.yml*:

```yaml
assets_bundles:
  - app.js
```

The bundles will be automatically included on all pages. To prevent automatic inclusion, add `assets_include: false`.
You can then include your bundle manually using `app.assets.include("app.js")` in python code or `{{ include_asset("app.js") }}` in templates.

Esbuild will bundle css files included in js files. These files will be automatically included when their parent js file is.