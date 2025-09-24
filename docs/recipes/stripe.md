# Stripe Checkout

Using [Flask-Stripe-Checkout](https://github.com/hyperflask/flask-stripe-checkout), you can quickly start charging people using [Stripe Checkout](https://stripe.com/payments/checkout), Stripe's hosted payment pages.

## Installation & setup

First, create a Stripe account:

1. Signup
2. Retrieve your API key
3. Register your webhook (`https://yourdomain/stripe-webhook`) and retrieve your endpoint secret

To use webhooks locally:

1. Download [stripe-cli](https://stripe.com/docs/stripe-cli)
2. Login with `stripe login`
3. Run `stripe listen --forward-to localhost:5000/stripe-webhook`

Now, install the extension:

    uv add flask-stripe-checkout

Configure your environment variables in *.env*:

    FLASK_STRIPE_API_KEY=sk_...
    FLASK_STRIPE_WEBHOOKS_ENDPOINT_SECRET=whsec_...

Activate the extension in your app in *config.yml*:

```yaml
flask_extensions:
    - "flask_stripe_checkout:StripeCheckout"
```

## Selling products using a cart

Add product to the cart using the following snippet:

```py
from flask_stripe_checkout import current_cart

def post():
    current_cart.add(price="stripe_price_id", quantity=1)
```

Create a checkout session for payment using:

```py
from flask_stripe_checkout import current_cart

def post():
    return current_cart.checkout()
```

See [Flask-Stripe-Checkout documentation](https://github.com/hyperflask/flask-stripe-checkout?tab=readme-ov-file#usage) for more info.

## Selling subscriptions

Subscription work in a similar way but you don't need to add item to the cart.

```py
from flask_stripe_checkout.subscription import subscription_checkout

def post():
    return subscription_checkout("subscription_price_id", optional_customer_reference)
```

See [Flask-Stripe-Checkout documentation](https://github.com/hyperflask/flask-stripe-checkout?tab=readme-ov-file#subscriptions) for more info.