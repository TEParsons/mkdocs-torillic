import re
from markdown.extensions import attr_list
from mkdocs.structure import pages, files
from mkdocs import config
from mkdocs.plugins import BasePlugin


class TorillicSpoilerPlugin(BasePlugin):
    def on_page_markdown(self, markdown: str, page: pages.Page, config: config.Config, files: files.File) -> str:
        """
        Convert codeblocks with language set to `spoiler` into a hidden spoiler tag

        Parameters
        ----------
        markdown : str
            Markdown text
        page : pages.Page
            MkDocs page object
        config : config.Config
            MkDocs configutation object
        files : files.File
            MkDocs file object

        Returns
        -------
        str
            Parsed markdown text
        """
        def format_codeblock(match):
            content = match.group("content")
            attrs_str = match.group("attrs")
            # parse attributes
            if attrs_str:
                all_attrs, _ = attr_list.get_attrs_and_remainder(attrs_str)
            else:
                all_attrs = []
            # saprate classes from other attributes
            classes = []
            attrs = []
            for attr_type, attr_val in all_attrs:
                if attr_type in (".", "class"):
                    classes.append(attr_val)
                else:
                    attrs.append(f"{attr_type}={attr_val}")
            
            return (
                f"<div class='spoiler hidden {' '.join(classes)}' {' '.join(attrs)} onclick='toggleSpoiler(this)' markdown>\n"
                f"{content}\n"
                f"</div>\n"
            )

        re_spoiler = r"```spoiler\n(?P<content>.*?)```(?:\{(?P<attrs>.*)\})?"
        return re.sub(
            pattern=re_spoiler,
            repl=format_codeblock,
            string=markdown,
            flags=re.DOTALL
        )