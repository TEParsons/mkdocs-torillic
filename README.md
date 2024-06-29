# Torillic
> Magic is distilled laziness

This theme, named after the fantasy setting of [Dungeons & Dragons](https://www.dndbeyond.com/), is designed with tabletop RPG players in mind. The theme allows beautiful HTML exports designed to look like a professionally made tabletop resource, whilst remaining easy to edit in code view and in small windows, thanks to CSS media queries.

## Theme configuration
Torillic accepts the following theme configuration options in the `mkdocs.yaml` file:
### `background_image`
Supply either a file path or a web link to an image to use for the site's background. If not supplied, will use the defaut Torillic background (wood planks).

## Page configuration
Torillic accepts the following configuration options from an individual page's yaml frontmatter:
### `contents`
Whether to include a block and, if so, what kind. Options are:
- `global`: Include a "global" contents block, i.e. one which describes the entire site
- `local`: Include a local contents block, i.e. one which describes the current page's children / siblings
- `none`: Do not include a contents block

If not supplied, the site homepage will have global contents block and section home pages will have a local contents block, other pages will not include a contents block.

## Tips & Tricks

- Using `> blockquotes` will create a green box like the ones used in 5e stat blocks
- In full page view, content is arranged into two columns - however, `# heading 1` and `# heading 2` elements span both columns so can be used as separators. A blank top-level heading will still split the page.
- The heading with a yellow line underneath (you know the one) is `#### heading 4`
- Actions in 5e stat blocks are generally formatted like so:
```markdown
***Name.*** *Attack Type:* +[modifier] to hit, reach [reach] ft., [n targets] target(s). *Hit:* [approx damage] ([n dice]d[die size] + [additional]) [damage type] damage.
```
- For an example of a full stat sheet in Torillic, check out the markdown below the screenshots.
- Ultimately, it's yours to play with, so feel free to completely ignore this advice and lay things out however works for your capaign!