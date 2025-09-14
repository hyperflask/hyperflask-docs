# Going to production

## Infrastucture

1. Purchase a domain and configure DNS
2. Deploy your app to a VPS or docker hosting using `hyperflask deploy`
3. Setup [smtp server](/recipes/sending-emails) and configure your app
4. Setup [error monitoring](/recipes/monitoring) (and optionnaly [analytics](/recipes/analytics))
5. Review checklist
6. Annoucement !

## Checklist

### Content

- [ ] Favicon
- [ ] Spelling & grammar
- [ ] Optimized images

### Testing

- [ ] Check website in all browsers
- [ ] Mobile tests
- [ ] Test emails
- [ ] Run Google Lighthouse audit

### Security

Hyperflask setups all needed security headers.

- [ ] Review OWASP Top 10 list
- [ ] Ensure HTTPS is mandatory

### Accessibility

Hyperflask UI components respect accessibility guidelines.

- [ ] Accessibility validation
- [ ] Color contrast
- [ ] WAI-ARIA Landmarks

### Legal

Mandatory as soon as you save user generated data.

- [ ] Terms and Conditions
- [ ] Privacy Policy
- [ ] GDPR compliance
- [ ] Ensure that a contact email is available

### SEO

- [ ] Google Rich Snippets
- [ ] Structured data
- [ ] robots.txt
- [ ] Sitemaps
- [ ] Social media headers