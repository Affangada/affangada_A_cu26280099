# Design Rationale — Green Spoon Cafe

## Colour palette
- Deep green `#244C3B`: primary headings, buttons and footer; communicates nature and stability.
- Soft sage `#E6E9DF`: section backgrounds; creates a calm atmosphere.
- Warm cream `#F7F5EE`: page background; reduces visual harshness.
- Peach `#E9B99D`: optional warm accent.
- Dark ink `#24332C`: body text for readability.

## Typography
Playfair Display is used for large headings to create a warm editorial feel. DM Sans is used for navigation, body copy and controls because it remains clear at small sizes. A consistent scale uses large responsive headings, regular body text and small uppercase eyebrow labels.

## Layout and whitespace
The design uses a mobile-first single-column layout, then expands into CSS Grid columns at 700px and 1000px. Flexbox aligns navigation and action groups. Consistent section spacing and card padding make the page easier to scan.

## Accessibility
The page includes semantic header, nav, main, section and footer landmarks; a skip link; descriptive image alternative text; labels associated with form controls; accessible button names; live status feedback; visible keyboard focus; and reduced-motion handling. Colours are selected for strong contrast, but a formal WCAG contrast audit should be run before production.

## Audience alignment
The natural palette, fresh-food imagery and friendly language are intended for local customers seeking a relaxed, quality cafe. Prominent menu and booking actions reduce the steps needed to make a visit.
