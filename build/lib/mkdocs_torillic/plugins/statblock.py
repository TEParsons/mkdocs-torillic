import re
from markdown.extensions import attr_list
from mkdocs.structure import pages, files
from mkdocs import config
from mkdocs.plugins import BasePlugin


class TorillicStatblockPlugin(BasePlugin):
    def on_page_markdown(self, markdown: str, page: pages.Page, config: config.Config, files: files.File) -> str:
        """
        Convert codeblocks with language set to `statblock` into formatted stat blocks.

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
            system = match.group("system")
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
            # add system to label, if given
            if system:
                label = f"Statblock ({system})"
            else:
                label = f"Statblock"
            
            return (
                f"<details class='statblock {system} {' '.join(classes)}' {' '.join(attrs)} markdown>\n"
                f"<summary>\n"
                f"{label}\n"
                f"</summary>\n"
                f"{content}\n"
                f"</details>\n"
            )

        re_statblock = r"```statblock:?(?P<system>[\w\d]*)?\n(?P<content>.*?)```(?:\{(?P<attrs>.*)\})?"
        return re.sub(
            pattern=re_statblock,
            repl=format_codeblock,
            string=markdown,
            flags=re.DOTALL
        )