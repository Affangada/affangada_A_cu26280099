# Testing Report — Lab Sheet 8

## Test plan
Run the website locally by opening `index.html` in each target browser. Test at mobile (375px), tablet (768px) and desktop (1366px) viewport widths.

| Test | Procedure | Expected result |
|---|---|---|
| Semantic structure | Inspect page landmarks | Header, nav, main, sections and footer are present |
| Responsive layout | Resize viewport | Cards and sections reflow without horizontal scrolling |
| Navigation | Activate menu button on mobile | Menu opens and `aria-expanded` updates |
| Carousel | Use previous/next buttons | Image and slide count change |
| Form required fields | Submit empty form | Browser validation identifies missing fields |
| Email validation | Enter invalid email | Browser prevents submission |
| Booking success | Enter valid details | Confirmation message appears |
| Map | Load contact section | Embedded map appears and fits its container |
| Keyboard access | Tab through page | Interactive elements are reachable and focus is visible |
| SEO | Inspect page source | Title, description and Open Graph tags are present |

## Browser and device matrix
Target browsers: Chrome, Firefox, Edge and Safari. Target viewports: 375px mobile, 768px tablet and 1366px desktop. Actual compatibility should be confirmed on available devices; this report describes the planned checks, not claimed test execution.

## Performance and final audit
Before production, compress and appropriately size images, serve minified CSS/JS, enable browser caching, and run Lighthouse. Check performance, accessibility, best practices and SEO. Fix all high-impact findings and manually verify keyboard and screen-reader use.

## Result
The supplied code implements the requested front-end features. Live reservation processing, real social feeds, and production deployment are outside this static prototype.
