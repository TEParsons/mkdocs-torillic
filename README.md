# Torillic
> Magic is distilled laziness

This theme, named after the fantasy setting of [Dungeons & Dragons](https://www.dndbeyond.com/), is designed with tabletop RPG players in mind. The theme allows beautiful HTML exports designed to look like a professionally made tabletop resource, whilst remaining easy to edit in code view and in small windows, thanks to CSS media queries.

## Installing
The easiest way to install `mkdocs-torillic` is via PyPi - in a command line terminal with pip installed, just run:
```
pip install mkdocs-torillic
```

Alternatively, you can clone/download this repo and either store it in your Python path or use `pip install <path to your local folder>`. If you do so, just remember to use the `last-release` branch rather than `main` - the base theme is copied over from [here](https://github.com/TEParsons/torillic) when a release is built, so in the `main` (development) branch there's just a file called `torillic.stub` in its place.

## Theme configuration
Torillic accepts the following theme configuration options in the `mkdocs.yaml` file:

### `background_image`
Supply either a file path or a web link to an image to use for the site's background. If not supplied, will use the defaut Torillic background (wood planks).

### `favicon`
Supply either a file path or a web link to an image to use for this site's favicon (the image on the tab in your browser). By default, will use the Torillic logo (wireframe of a D20).

## Plugins
Installing mkdocs-torillic now adds optional plugins to mkdocs:

### torillic-statblock
Recognises any code blocks whose language is `statblock` as a statblock and styles it as an expandable panel. You can also add the name of the game system after the word `statblock` (separated by a `:`) to alter the label created (e.g. `statblock:5e` will create an expandable stat block labelled "Statblock (5e)"). As with other elements, you can use `{.full-width}` to create a full-width statblock with columns inside, rather than sitting in a column.

For example, here's a statblock for a Kobold in D&D 5e:
```
\```statblock:5e
### Kobold
*Small Humanoid (Kobold), Lawful Evil*

---

**Armor Class** 12
**Hit Points** 5 (2d6 - 2)
**Speed** 30 ft.

---

| STR  | DEX  | CON  | INT  | WIS  | CHA  |
|------|------|------|------|------|------|
| 7    | 15   | 9    | 8    | 7    | 8    |
| (-2) | (+2) | (-1) | (-1) | (-2) | (-1) |

---

**Senses** [Darkvision](https://www.dndbeyond.com/compendium/rules/basic-rules/monsters#Darkvision) 60 ft., Passive Perception 8
**Languages** Common, Draconic
**Challenge** 1/8 (25 XP)

---

***Sunlight Sensitivity.*** While in sunlight, the kobold has disadvantage on attack rolls, as well as on Wisdom ([Perception](https://www.dndbeyond.com/compendium/rules/basic-rules/using-ability-scores#Perception)) checks that rely on sight.

***Pack Tactics.*** The kobold has advantage on an attack roll against a creature if at least one of the kobold's allies is within 5 feet of the creature and the ally isn't [incapacitated](https://www.dndbeyond.com/compendium/rules/basic-rules/appendix-a-conditions#Incapacitated).

#### Actions

***Dagger.** Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 4 (1d4 + 2) piercing damage.

***Sling.** Ranged Weapon Attack:* +4 to hit, range 30/120 ft., one target. *Hit:* 4 (1d4 + 2) bludgeoning damage.
\```
```

### torillic-ipa
Recognises content inbetween two `/` as International Phonetic Alphabet (IPA) and adds a link to it in [IPA Reader](https://ipa-reader.xyz), making it super easy to add pronunciation guides in your notes. 

For example, if you wanted to add a pronunciation guide for the word Torillic, you would do:

```
/tɔrɪlɪk/
```

## Page configuration
Torillic accepts the following configuration options from an individual page's yaml frontmatter:
### `contents`
Whether to include a contents block and, if so, what kind. Options are:
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
- Ultimately, it's yours to play with, so feel free to completely ignore this advice and lay things out however works for your campaign!
