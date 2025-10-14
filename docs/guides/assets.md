# Assets

Hyperflask integrates esbuild to bundle assets and tailwind for styles.

!!! info
    This feature is provided by [Flask-Assets-Pipeline](https://github.com/hyperflask/flask-assets-pipeline)

## Static assets

Static assets can be located in 2 different folders:

 - *app/assets*: files located here will be copied to the *public* folder when the app is built. A hash will be appended to the filename for cache busting. URLs for these files should be created using `asset_url(filename)`
 - *public*: files located here are left untouched and are directly accessible from the web. URLs for these files should be created using `static_url(filename)`

## Styling

Hyperflask uses [Tailwind](https://tailwindcss.com/) for styling. It is fully integrated and you can use tailwind utility classes across pages and components.

## Images

Use the `<{Image}/>` component instead of `asset_url()` to generate image tags.
Using the component also enables using image placeholders (with a blurry image), responsive images and more.

Place your images in the assets folder (eg. `app/assets/image.png`) then include them:

```
<{Image src="image.png" }/>
```

The following default attributes will be set:

- `width` and `height`
- `loading="lazy"` (default for all images can be changed in the configuration using `images_default_loading`)
- `decoding="async"` (default for all images can be changed in the configuration using `images_default_decoding`)
- `style` to define a background image using a base64 encoded data URI containing a tiny blurry version of the image (disable using `placeholder=False` on the Image component)

Override any of these attributes on the Image component.

Using `preload=True` on the Image component will add a preload meta in the page header and use eager loading instead. Use `priority=True` to set `preload=True` and fetchpriority to high.

Example:

```
<{Image src="image.png" preload=True placeholder=False }/>
```

### Convert to webp

It is possible to auto convert all images to webp by adding `assets_images_webp: true` in `config.yml`. Webp is a highly optimized image format for the web.

If enabled, continue using the original name as the src of the image.

### Responsive images

You can resize your images to multiple widths and generate a `srcset` attribute for [responsive images](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images).

In your config add the `assets_images_sizes` key with a list of widths. Example: `assets_images_sizes: [400, 1200]`.
The images will be resized to all smaller width than their own.

The Image component will auto set the srcset attribute based on those sizes.

It is recommended to have large images as default and auto resize them to smaller ones. Use `assets_images_default_size` to specify the default size to use as the src attribute.

## Using fonts

TODO

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